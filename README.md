Project Title
4039 Ride Share

Project Overview
This project helps SOM students to coordinate rides to and from the area airports, and recommends the most affordable modes of transport for the given group size.

The current method of coordination is to post a message on a Facebook wall with date of travel and airport, but there are many flaws with it.
It is underutilized, is hard to read and scan, and promotes last-minute posting behavior that makes it difficult to plan in advance.
This project seeks to address these issues by gathering all information in one spot and then automatically returning matches and associated travel information.

Compilation
I wrote all of the code in the CS50 IDE under "code" subfolder in "project".

The main file is application.py, and it is supported by 2 html pages - form.html (input for all travel information), and travelers.html (output for other travelers going the same way).
There is also error.html and layout.html that are available for behind the scenes support to help format the form and also ensure there are no errors with data entry.

The form automatically updates a sequel lite table called "Travelers". "Travelers", and 6 other sql tables named after each area airport contain the information necessary to populate travelers.html.
Application.py performs all of the sql querying and passes the information to travelers.html as variables.

Use
Run application.py in the CS50 IDE using flask and open the generated link.
The link will take you to a form modeled after a "google form" that will allow you to enter all flight information and submit.
Once you submit, you will be taken to an output page with information about other travelers going to the airport the same time.

Features
The database travelers.db contains 7 data tables.
As mentioned above, the Travelers table stores information from the form.
The other 6 tables include static price quotes for getting to each airport.
The tables include gas & tolls, rideshare expenses, public transport expenses, and combinations of those.
The travelers.html page will submit all of the travel information for the airport selected in the form so that the user can make the decision that works best for them depending on factors such as car ownership or desire for convenience.