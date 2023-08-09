from tkinter import *
import calculate


window = Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=200)
window.config(pady=40)

labelWeight = Label(text="Enter Your Weight (kg)")
labelWeight.pack(side="top")

entryWeight = Entry(width=30)
entryWeight.pack(side="top")

labelHeight = Label(text="Enter Your Height (cm)")
labelHeight.pack(side="top")

entryHeight = Entry(width=30)
entryHeight.pack(side="top")

calculateBtn = Button(text="Calculate", command=lambda: calculate.calculate_BMI(entryWeight, entryHeight, labelResult))
calculateBtn.pack(side="top")


labelResult = Label()
labelResult.pack(side="top")


window.mainloop()