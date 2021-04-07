# airline.py

from graphics import *
from button import Button
from textentry import textEntry_

def readSeats(filename):
    infile = open(str(filename), 'r')
    lst = list(map(int,infile.readlines()))
    infile.close()
    return lst

def writeSeats(filename,array):
    outfile = open(filename,'w')
    for i in array:
        outfile.write('%d \n' % i)
    outfile.close()

def main():

    win = GraphWin("Airline Reservation System",600, 400)
    win.setCoords(0, 0, 60, 45)

    #GUI

    r1 = Rectangle(Point(2,44),Point(58,2))
    r1.draw(win)

    title = Text(Point(24,42), "Airline Reservation System")
    title.setTextColor("Navy Blue")
    title.setSize(13)
    title.draw(win)

    #Define Entries

    textFirstName = textEntry_(win, Point(7,37), "First Name: ")
    textLastName = textEntry_(win, Point(7,32), "Last Name: ")
    textClass = textEntry_(win, Point(32,37), "Class: ")
    # textSeat = textEntry_(win, Point(7,27), "Seat #: ")
    textPrice = textEntry_(win, Point(32,32), "Price: ")

    # Set Inputs
    inputFN = textFirstName.input
    inputLN = textLastName.input
    inputC = textClass.input
    # inputS = textSeat.input
    inputP = textPrice.input

    #Draw Buttons
    reserveButton = Button(win, Point(17,20),12,4,"Reserve")
    quitButton = Button(win, Point(45,20),12,4,"Quit")

    #Program
    message1 = Text(Point(17,10), "Please enter your Name, \n Class: (F, B, E) and Seat Number")
    message1.draw(win)

    #read the records file to fill Seat_list array
    Seat_list = readSeats("pass.txt")

    print(Seat_list)

    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if reserveButton.clicked(pt):
            if inputC.getText() == "F":
                if Seat_list[0:29].count(0) >= 1:
                    s = Seat_list[0:29].index(0)
                    Seat_list[s] = 1            
                    inputP.setText("$3000")
                    message1.setText("Hello, {0} {1} , \n your seat will be number {2} in first class".format(inputFN.getText(),inputLN.getText(),s + 1))
                    lst = Seat_list
                    writeSeats("pass.txt", lst)
                    x = win.getMouse()
                    break
                else:
                    message1.setText("The first class is full would you like to downgrade to the next open class?")
                    yesButton = Button(win, Point(17,5),12,4, "Yes")
                    noButton = Button(win, Point(32,5),12,4, "No")
                    pt = win.getMouse()
                    while not noButton.clicked(pt):
                        if yesButton.clicked(pt):
                            if Seat_list[30:49].count(0) >= 1:
                                message1.setText("Downgrading you to business class")
                                s = Seat_list[30:49].index(0)
                                s = s + 30
                                Seat_list[s] = 1
                                inputP.setText("$2000")
                                message1.setText("Hello, {0} {1} your seat will be number {2} in business class".format(inputFN.getText(),inputLN.getText(),s+1))
                                lst = Seat_list
                                writeSeats("pass.txt",lst)
                                x = win.getMouse()
                                break
                            elif Seat_list[50:99].count(0) >= 1:
                                message1.setText("The business class was full so we are placing you in economy")
                                s = Seat_list[50:99].index(0)
                                s = s + 50
                                Seat_list[s] = 1
                                inputP.setText("1000")
                                message1.setText("Hello, {0} {1} your seat will be number {2} in economy class".format(inputFN.getText(),inputLN.getText(),s + 1))
                                lst = Seat_list
                                writeSeats("pass.txt",lst)
                                x = win.getMouse()
                                break
                            else:
                                message1.setText("The Plane is full")
                                x = win.getMouse()
                                break
                        elif noButton.clicked(pt):
                            win.close()
                            quit()
                    break
            elif inputC.getText() == "B":
                if Seat_list[30:49].count(0) >= 1:
                    s = Seat_list[30:49].index(0)
                    s = s + 30
                    Seat_list[s] = 1
                    inputP.setText("2000")
                    message1.setText("Hello, {0} {1}, \n your seat will be number {2} in business class".format(inputFN.getText(),inputLN.getText(),s + 1))
                    lst = Seat_list
                    print(lst)
                    writeSeats("pass.txt",lst)
                    x = win.getMouse()
                    break
                else:
                    message1.setText("The business class is full would you like to check for another seat?")
                    yesButton = Button(win, Point(17,5),12,4, "Yes")
                    noButton = Button(win, Point(32,5),12,4, "No")
                    pt = win.getMouse()
                    while not noButton.clicked(pt):
                        if yesButton.clicked(pt):
                            if Seat_list[50:99].count(0) >= 1:
                                s = Seat_list[50:99].index(0)
                                s = s + 50
                                Seat_list[s] = 1
                                inputP.setText("1000")
                                message1.setText("Hello, {0} {1} your seat will be number {2} in economy class".format(inputFN.getText(),inputLN.getText(),s + 1))
                                lst = Seat_list
                                writeSeats("pass.txt",lst)
                                x = win.getMouse()
                                break
                            elif Seat_list[0:29].count(0) >= 1:
                                s = Seat_list[0:29].index(0)
                                Seat_list[s] = 1
                                inputP.setText("3000")
                                message1.setText("Hello, {0} {1} your seat will be number {2} in first class".format(inputFN.getText(),inputLN.getText(),s + 1))
                                lst = Seat_list
                                writeSeats("pass.txt",lst)
                                x = win.getMouse()
                                break
                            else:
                                message1.setText("The Plane is full")
                                x = win.getMouse()
                                break
                        elif noButton.clicked(pt):
                            win.close()
                            quit()
            elif inputC.getText() == "E":
                if Seat_list[50:99].count(0) >= 1:
                    s = Seat_list[50:99].index(0)
                    s = s + 50
                    Seat_list[s] = 1
                    inputP.setText("$1000")
                    message1.setText("Hello, {0} {1}, \n your seat will be number {2} in economy class".format(inputFN.getText(),inputLN.getText(),s + 1))
                    lst = Seat_list
                    writeSeats("pass.txt",lst)
                    x = win.getMouse()
                    break
                else:
                    message1.setText("The economy class is full would you like to check for another seat?")
                    yesButton = Button(win, Point(17,5),12,4, "Yes")
                    noButton = Button(win, Point(32,5),12,4, "No")
                    pt = win.getMouse()
                    while not noButton.clicked(pt):
                        if yesButton.clicked(pt):
                            if Seat_list[30:49].count(0) >= 1:
                                s = Seat_list[30:49].index(0)
                                s = s + 30
                                Seat_list[s] = 1
                                inputP.setText("2000")
                                message1.setText("Hello, {0} {1} your seat will be number {2} in business class".format(inputFN.getText(),inputLN.getText(),s + 1))
                                lst = Seat_list
                                writeSeats("pass.txt",lst)
                                x = win.getMouse()
                                break
                            elif Seat_list[0:29].count(0) >= 1:
                                s = Seat_list[0:29].index(0)
                                Seat_list[s] = 1
                                inputP.setText("3000")
                                message1.setText("Hello, {0} {1} your seat will be number {2} in first class".format(inputFN.getText(),inputLN.getText(),s + 1))
                                lst = Seat_list
                                writeSeats("pass.txt",lst)
                                x = win.getMouse()
                                break
                            else:
                                message1.setText("The Plane is full")
                                x = win.getMouse()
                                break
                        elif noButton.clicked(pt):
                            win.close()
                            quit()
        elif quitButton.clicked(pt):
            win.close()
            quit()
    win.close()         #If the quit button is clicked from the start
main()
