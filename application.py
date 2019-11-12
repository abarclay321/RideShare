import os
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Custom filter
app.jinja_env.filters["usd"] = usd


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///travelers.db")


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    if not request.form.get("name") or not request.form.get("email") or not request.form.get("phonenumber") or not request.form.get("airport") or not request.form.get("time") or not (request.form.get("Departing") or request.form.get("Arriving")) or not (request.form.get("Yes") or request.form.get("No")):
        return render_template("error.html", message ="Please submit all fields")

    #define variables
    name=request.form.get("name")
    email=request.form.get("email")
    phonenumber=request.form.get("phonenumber")
    airport=request.form.get("airport")
    time=request.form.get("time")
    direction=(request.form.get("Departing") or request.form.get("Arriving"))
    driver=(request.form.get("Yes") or request.form.get("No"))
    block=request.form.get("block")
    date=request.form.get("date")

    # insert traveler information into table
    result = db.execute("INSERT INTO Travelers ('name', 'email', 'phonenumber', 'direction', 'driver', 'airport', 'block', 'date', 'time') VALUES(:name, :email, :phonenumber, :direction, :driver, :airport, :block, :date, :time)",
                            name=name, email=email, phonenumber=phonenumber, direction=direction, driver=driver, airport=airport, block=block, date=date, time=time)
    travelers = db.execute(
       "SELECT name, email, phonenumber, time, driver FROM Travelers WHERE airport = :airport AND direction = :direction AND date = :date AND block = :block", airport=airport, direction=direction, date=date, block=block)
    # Create information to pass through to html page - number of travelrs, Ridesharecost, Cheaproute costs, adn Cheapprice, all pulled from sql tables
    Number = len(travelers)
    index1 = db.execute("SELECT Rideshare FROM :airport WHERE Number_of_Travelers = :number", airport=airport, number=Number)
    Ridesharecost = index1[0]["Rideshare"]
    index2 = db.execute("SELECT Least_Expensive_Mode FROM :airport WHERE Number_of_Travelers = :number", airport=airport, number=Number)
    Cheaproute = index2[0]["Least_Expensive_Mode"]
    index3 = db.execute("SELECT Approximate_Cost_per_Traveler FROM :airport WHERE Number_of_Travelers = :number", airport=airport, number=Number)
    Cheapprice = index3[0]["Approximate_Cost_per_Traveler"]
    index4 = db.execute("SELECT Airport_Parking_Rate FROM :airport WHERE Number_of_Travelers = :number", airport=airport, number=Number)
    Parking = index4[0]["Airport_Parking_Rate"]
    prices = db.execute("SELECT Number_of_Travelers, Gas_and_Tolls, Rental_Car, Public_Transport, Public_Transport_Rideshare, Rideshare, Shared_Shuttle FROM :airport", airport=airport)

    # create html page
    return render_template("travelers.html", travelers=travelers, Ridesharecost=Ridesharecost, Cheaproute=Cheaproute, Cheapprice=Cheapprice, Number=Number, airport=airport, Parking=Parking, date=date, direction=direction, prices=prices)

