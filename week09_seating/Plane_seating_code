#Collaborators:Elizabeth,                    ,           Patti, Jing
#Resource and Reference: https://github.com/ryanhoang15/Python/blob/master/9.22%20Lab%20Ch%209:%20Concert%20seating%20chart(2D).py


price_chart = [[4, 4, 4, 0, 4, 4, 4, 4, 4, 0, 4, 4, 4],
               [2, 2, 3, 0, 3, 2, 2, 2, 3, 0, 3, 2, 2],
               [2, 2, 3, 0, 3, 2, 2, 2, 3, 0, 3, 2, 2],
               [2, 2, 3, 0, 3, 2, 2, 2, 3, 0, 3, 2, 2],
               [2, 2, 3, 0, 3, 2, 2, 2, 3, 0, 3, 2, 2]]
# This is a small scale of airplane seating. The numbers represent the price. We picked single digit because double-digit numbers don't line-up. Number 4 are the front rows seats (discounts may be offered to certain groups by airlines); Number 3 are the seats by the corridor(the initial 0s); 1st column and last column are seats by the window.

print("Here are the available seats:\n")

for x, row in enumerate(price_chart):
    for col in price_chart[x]:
        print(col, end=" ")
    print()

user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:\n ").lower()

while user_input != "q":
    if user_input == "s":
        row = int(input("Enter the row:\n "))-1
        col = int(input("Enter the column:\n "))-1
        if price_chart[row][col] != 0:
            print("Sold, for $", price_chart[row][col], "!\n")
            price_chart[row][col] = 0
        else:
            print("Sorry, that seat is not available.\n")

    elif user_input == "p": #choose a seat by price
        money = int(input("How much do you want to spend?(2,3,4)\n "))
        found = False
        for y, col in enumerate(price_chart):
            for x, row in enumerate(col):
                if row == money and not found:
                    found = True
                    print("You can have seat (row, column): ", y+1, x+1) #give the first available seat number for the user to type in. We believe this may privide consective seats if needed.)
                    print()
        if not found:
            print("Sorry, no tickets available at that price.\n")
    else:
        print("That wasn't a valid option.\n")
      
    #print("Here are the available seats:\n")
    #for x, row in enumerate(price_chart):
      #for col in price_chart[x]:
        #print(col, end=" ")
        #print()
      # show the seating everytime a purchase is finished
    user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:\n ").lower()

for x, row in enumerate(price_chart):
    for col in price_chart[x]:
        print(col, end=" ")
    print()
