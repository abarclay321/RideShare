Design

I designed the web form to make it easier for users to find others going to the airport around the same time.
The form is an html form that stores all inputs into a sql data table.

The biggest value of the app are the airport datatables inluded in sql that contain static
information about the prices of each mode of transport to and from the airport. These add extra value to users
by not only helping them to find other people going their way, but to also quickly assess what
the best mode of transport is for their group and to understand the associated expenses.

One of the biggest challenges was to figure out how to group travelers using an algorithm in python based on their flight times.
Because of this, I ended up adding a feature to the form that allowed users to self-identify
a block for their travel time, and I used this input as my way of creating travel groups.

I initially built all of my travel expenses in an excel workbook that used a variable for # of travelers to calculate
the per person expense. However, I struggled to incorporate this once I decided to store this information to sequal, so I took
an extra step and created static sequal tables for each airport and layed out the number of travelers as a dimension on the table.
Although more time consuming, this made my code much simplier and easier to follow.

