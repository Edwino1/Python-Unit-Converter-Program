# Unit Converter Program
#By Edwin Odiakosa, July 11, 2023
from tkinter import *
#creates the GUI complete with a title and label
mainWindow = Tk()
mainWindow.title("Unit Converter")
mainWindow.geometry("600x300")
mainWindow.config(background="#0377fc")
mainLabel = Label(mainWindow, text="Unit Converter",
      font=("Arial", 20, "bold"),
      fg="black",
      bg="White",
      relief=RAISED,
      bd=10, ).pack()

#allows the program to figure out which quantity of measurement was picked
def pick(unitOptions):
    startLabel.get()
    if startLabel.get() == "Length":
        length()
    elif startLabel.get() == "Temperture":
        temperture()
    elif startLabel.get() == "Weight":
        weight()

#The three different functions below
#takes the user input and the different options the user can
#pick and runs the calculations
def length_calculate():
    data = float(userEntry.get())
    if fromMenu.get() == toMenu.get():
        answer = data
    elif fromMenu.get() == "Millimeters" and toMenu.get() == "Centimeters":
        answer = data / 10
    elif fromMenu.get() == "Centimeters" and toMenu.get() == "Millimeters":
        answer = data * 10
    elif fromMenu.get() == "Millimeters" and toMenu.get() == "Inches":
        answer = data * 0.0393701
    elif fromMenu.get() == "Inches" and toMenu.get() == "Millimeters":
        answer = data / 0.0393701
    elif fromMenu.get() == "Millimeters" and toMenu.get() == "Meters":
        answer = data * 0.001
    elif fromMenu.get() == "Meters" and toMenu.get() == "Millimeters":
        answer = data * 1000
    elif fromMenu.get() == "Millimeters" and toMenu.get() == "Feet":
        answer = data / 304.8
    elif fromMenu.get() == "Feet" and toMenu.get() == "Millimeters":
        answer = data * 304.8
    elif fromMenu.get() == "Millimeters" and toMenu.get() == "Yards":
        answer = data / 914.4
    elif fromMenu.get() == "Yards" and toMenu.get() == "Millimeters":
        answer = data * 914.4
    elif fromMenu.get() == "Millimeters" and toMenu.get() == "Kilometers":
        answer = data / 1000000
    elif fromMenu.get() == "Kilometers" and toMenu.get() == "Millimeters":
        answer = data * 1000000
    elif fromMenu.get() == "Millimeters" and toMenu.get() == "Miles":
        answer = data / 1609000
    elif fromMenu.get() == "Miles" and toMenu.get() == "Millimeters":
        answer = data * 1609000
    elif fromMenu.get() == "Centimeters" and toMenu.get() == "Inches":
        answer = data / 2.54
    elif fromMenu.get() == "Inches" and toMenu.get() == "Centimeters":
        answer = data * 2.54
    elif fromMenu.get() == "Centimeters" and toMenu.get() == "Meters":
        answer = data / 100
    elif fromMenu.get() == "Meters" and toMenu.get() == "Centimeters":
        answer = data * 100
    elif fromMenu.get() == "Centimeters" and toMenu.get() == "Feet":
        answer = data / 30.48
    elif fromMenu.get() == "Feet" and toMenu.get() == "Centimeters":
        answer = data * 30.48
    elif fromMenu.get() == "Centimeters" and toMenu.get() == "Yards":
        answer = data / 91.44
    elif fromMenu.get() == "Yards" and toMenu.get() == "Centimeters":
        answer = data * 91.44
    elif fromMenu.get() == "Centimeters" and toMenu.get() == "Kilometers":
        answer = data / 100000
    elif fromMenu.get() == "Kilometers" and toMenu.get() == "Centimeters":
        answer = data * 100000
    elif fromMenu.get() == "Centimeters" and toMenu.get() == "Miles":
        answer = data / 160900
    elif fromMenu.get() == "Miles" and toMenu.get() == "Centimeters":
        answer = data * 160900
    elif fromMenu.get() == "Inches" and toMenu.get() == "Meters":
        answer = data / 39.37
    elif fromMenu.get() == "Meters" and toMenu.get() == "Inches":
        answer = data * 39.37
    elif fromMenu.get() == "Inches" and toMenu.get() == "Feet":
        answer = data / 12
    elif fromMenu.get() == "Feet" and toMenu.get() == "Inches":
        answer = data * 12
    elif fromMenu.get() == "Inches" and toMenu.get() == "Yards":
        answer = data / 36
    elif fromMenu.get() == "Yards" and toMenu.get() == "Inches":
        answer = data * 36
    elif fromMenu.get() == "Inches" and toMenu.get() == "Kilometers":
        answer = data / 39370
    elif fromMenu.get() == "Kilometers" and toMenu.get() == "Inches":
        answer = data * 39370
    elif fromMenu.get() == "Inches" and toMenu.get() == "Miles":
        answer = data / 63360
    elif fromMenu.get() == "Miles" and toMenu.get() == "Inches":
        answer = data * 63360
    elif fromMenu.get() == "Meters" and toMenu.get() == "Feet":
        answer = data * 3.281
    elif fromMenu.get() == "Feet" and toMenu.get() == "Meters":
        answer = data / 3.281
    elif fromMenu.get() == "Meters" and toMenu.get() == "Yards":
        answer = data * 1.094
    elif fromMenu.get() == "Yards" and toMenu.get() == "Meters":
        answer = data / 1.094
    elif fromMenu.get() == "Meters" and toMenu.get() == "Kilometers":
        answer = data / 1000
    elif fromMenu.get() == "Kilometers" and toMenu.get() == "Meters":
        answer = data * 1000
    elif fromMenu.get() == "Meters" and toMenu.get() == "Miles":
        answer = data / 1609
    elif fromMenu.get() == "Miles" and toMenu.get() == "Meters":
        answer = data * 1609
    elif fromMenu.get() == "Feet" and toMenu.get() == "Yards":
        answer = data / 3
    elif fromMenu.get() == "Yards" and toMenu.get() == "Feet":
        answer = data * 3
    elif fromMenu.get() == "Feet" and toMenu.get() == "Kilometers":
        answer = data / 3281
    elif fromMenu.get() == "Kilometers" and toMenu.get() == "Feet":
        answer = data * 3281
    elif fromMenu.get() == "Feet" and toMenu.get() == "Miles":
        answer = data / 5280
    elif fromMenu.get() == "Miles" and toMenu.get() == "Feet":
        answer = data * 5280
    elif fromMenu.get() == "Yards" and toMenu.get() == "Kilometers":
        answer = data / 1094
    elif fromMenu.get() == "Kilometers" and toMenu.get() == "Yards":
        answer = data * 1094
    elif fromMenu.get() == "Yards" and toMenu.get() == "Miles":
        answer = data / 1760
    elif fromMenu.get() == "Miles" and toMenu.get() == "Yards":
        answer = data * 1760
    elif fromMenu.get() == "Kilometers" and toMenu.get() == "Miles":
        answer = data / 1.609
    elif fromMenu.get() == "Miles" and toMenu.get() == "Kilometers":
        answer = data * 1.609
    resultLabelVar.set(answer)

def temperture_calculate():
    data = float(userEntry.get())
    if fromMenu.get() == toMenu.get():
        answer = data
    elif fromMenu.get() == "Celsius" and toMenu.get() == "Fahrenheit":
        answer = (data * (9/5)) + 32
    elif fromMenu.get() == "Fahrenheit" and toMenu.get() == "Celsius":
        answer = (data - 32) * (5/9)
    elif fromMenu.get() == "Celsius" and toMenu.get() == "Kelvin":
        answer = data + 273.15
    elif fromMenu.get() == "Kelvin" and toMenu.get() == "Celsius":
        answer = data - 273.15
    elif fromMenu.get() == "Fahrenheit" and toMenu.get() == "Kelvin":
        answer = (data - 32) * (5/9) + 273.15
    elif fromMenu.get() == "Kelvin" and toMenu.get() == "Fahrenheit":
        answer = (data - 273.15) * (9/5) + 32
    resultLabelVar.set(answer)

#NOTE: tons here refer to metric tons, not imperial Tons
def weight_calculate():
    data = float(userEntry.get())
    if fromMenu.get() == toMenu.get():
        answer = data
    elif fromMenu.get() == "Pounds" and toMenu.get() == "Kilograms":
        answer = data / 2.205
    elif fromMenu.get() == "Kilograms" and toMenu.get() == "Pounds":
        answer = data * 2.205
    elif fromMenu.get() == "Pounds" and toMenu.get() == "Tons":
        answer = data / 2205
    elif fromMenu.get() == "Tons" and toMenu.get() == "Pounds":
        answer = data * 2205
    elif fromMenu.get() == "Pounds" and toMenu.get() == "Ounces":
        answer = data * 16
    elif fromMenu.get() == "Ounces" and toMenu.get() == "Pounds":
        answer = data / 16
    elif fromMenu.get() == "Kilograms" and toMenu.get() == "Tons":
        answer = data / 1000
    elif fromMenu.get() == "Tons" and toMenu.get() == "Kilograms":
        answer = data * 1000
    elif fromMenu.get() == "Kilograms" and toMenu.get() == "Ounces":
        answer = data * 35.274
    elif fromMenu.get() == "Ounces" and toMenu.get() == "Kilograms":
        answer = data / 35.274
    elif fromMenu.get() == "Tons" and toMenu.get() == "Ounces":
        answer = data * 35270
    elif fromMenu.get() == "Ounces" and toMenu.get() == "Tons":
        answer = data / 35270
    resultLabelVar.set(answer)

#This function takes whatever quantity the user wanted to convert units
#in and directs the program to the right function based on the choice
def select():
    if startLabel.get() == "Length":
        length_calculate()
    elif startLabel.get() == "Temperture":
        temperture_calculate()
    elif startLabel.get() == "Weight":
        weight_calculate()

#creates the first drop down menu
startLabel = StringVar(mainWindow)
startLabel.set("Select unit")
unitOptions = ["Length", "Temperture", "Weight"]
measurement = OptionMenu(mainWindow,startLabel,
                         *unitOptions,command=pick).pack(padx=20)

#creates the user entry, the "from" dropdown menu and the "to" dropdown menu
userEntry = Entry(mainWindow)
fromMenu = StringVar()
fromMenu.set("Select option")
toMenu = StringVar()
toMenu.set("Select Option")

#These three functions change what the units will be based on the
#quantity being measured
def length():
    lengthOptions = ["Millimeters", "Centimeters", "Inches", "Meters"
        , "Feet", "Yards", "Kilometers", "Miles"]
    lengthMeasurementsFrom = OptionMenu(mainWindow, fromMenu,
                                        *lengthOptions)
    lengthMeasurementsTo = OptionMenu(mainWindow, toMenu,
                                      *lengthOptions)
    userEntry.place(x=5,y=140)
    lengthMeasurementsFrom.place(x=5,y=175)
    equalLabel.place(x=220,y=140)
    resultLabel.place(x=270,y=140)
    lengthMeasurementsTo.place(x=270,y=175)
def temperture():
    tempOptions = ["Celsius", "Fahrenheit", "Kelvin"]
    tempMeasurementsFrom = OptionMenu(mainWindow, fromMenu,
                                      *tempOptions)
    tempMeasurementsTo = OptionMenu(mainWindow, toMenu,
                                    *tempOptions)
    userEntry.place(x=5,y=140)
    tempMeasurementsFrom.place(x=5,y=175)
    equalLabel.place(x=220,y=140)
    resultLabel.place(x=270,y=140)
    tempMeasurementsTo.place(x=270,y=175)

def weight():
    weightOptions = ["Pounds", "Kilograms", "Tons", "Ounces"]
    weightMeasurementsFrom = OptionMenu(mainWindow, fromMenu,
                                        *weightOptions)
    weightMeasurementsTo = OptionMenu(mainWindow, toMenu,
                                      *weightOptions)
    userEntry.place(x=5,y=140)
    weightMeasurementsFrom.place(x=5,y=175)
    equalLabel.place(x=220,y=140)
    resultLabel.place(x=270,y=140)
    weightMeasurementsTo.place(x=270,y=175)

#The convert button starts the entire process, running the functions
#that determine which quantity and units were picked, what the user entered
#and calculates the converson, as well as spitting out an answer
convert = Button(mainWindow,text="Convert",relief=RAISED,
                 command=select).pack(side=BOTTOM)

#the label where the answer is shown. The resultLabelVar variable
#allows the label to change based on what the answer is
resultLabelVar = StringVar(mainWindow)
resultLabelVar.set("Result")
resultLabel = Label(mainWindow,textvariable=resultLabelVar,
                    font=("Comic Sans", 20, "bold"),
                        bg="White",
                        fg="Black",
                         relief=RAISED)
equalLabel = Label(mainWindow,text="=",font=("Comic Sans",20,"bold"),
                   relief=RAISED)

#all the code is enclosed in the mainloop method so that the
#GUI runs continously
mainWindow.mainloop()