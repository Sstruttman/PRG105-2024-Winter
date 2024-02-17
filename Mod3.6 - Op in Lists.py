# This program is meant to simulate ticket sales for an event

# Establish seats and welcome user
seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
          16, 17, 18, 19, 20]

print("Hello! Thank you for choosing our movie theater!")

# Establish wanted and use a loop. Print available seats each loop and .remove wanted
wanted = 1
while wanted != 0:
    print("Here are the seats that are available.")
    print(seats)
    wanted = int(input("Which seat would you like? If finished, enter 0 to exit. "))
    if wanted < 0 or wanted > 20:
        print("Sorry! That seat is not availabe. Please choose again")
    elif wanted == 0:
        print("Thank you for purchasing! Goodbye.")
    else:    
        seats.remove(wanted)
