Patti (Patricia) Elfers-Wygand
CSCI - 77800
Fall 2022
Plane Seating in Python

## Collaborators:  Elizabeth, Jing, Patti, Jenna 

 We found a file to model off of to help make the airplane seating algorithm more ethical. 
(https://github.com/ryanhoang15/Python/blob/master/9.22%20Lab%20Ch%209:%20Concert%20seating%20chart(2D).py )  It allows for choosing one seat or price at 
a time.  This is a small scale of airplane seating.  The numbers represent the price.  We picked single digits because double-digit numbers don’t line up 
well.  Number 4 are the front row seats (discounts may be offered to certain groups by airlines); Number 3 are the seats by the corridor (the initial 0’s);
1st column and last column are seats by the windows.

The algorithm will print the seats that are available to allow for choice.  It then asks for user input for Seat and Price.  It then prints what price 
the seat is and “Sold, for $” or it will print “Sorry, that seat is not available.”  You can also choose a seat by price as it asks for input on “how much
do you want to spend (2, 3, 4) if found = True then “you can have that seat ( row, column).  It gives the first available seat number for the user to type 
in.We believe this may provide consecutive seats if needed.  Otherwise if not  found it will print “Sorry no tickets available at that price’ or else, 
“That wasn’t a valid option.” 
