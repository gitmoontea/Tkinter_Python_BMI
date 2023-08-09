import tkinter.messagebox
import tkinter as tk

resultText = ""
state = ""
def calculate_BMI(entryObject: tk.Entry, entryObject2: tk.Entry, resultLabel: tk.Label):
    global resultText, state
    weight = entryObject.get()
    height = entryObject2.get()
    if(str.isdigit(weight) and str.isdigit(height)):
        weight = float(weight)
        height = float(height) / 100
        result = weight / (height ** 2)
        result_str = str(round(result, 2))
        if(result < 18.5):
            state = "Under Weight"
        elif(result >= 18.5 and result < 25):
            state = "Normal Weight"
        elif (result >= 25 and result < 30):
            state = "Over Weight"
        elif (result >= 30 and result < 35):
            state = "Obesity Class 1"
        elif (result >= 35 and result < 40):
            state = "Obesity Class 2"
        else:
            state = "Extreme Obesity"

        resultText = f"Your BMI value is {result_str}. You are {state}"
        resultLabel.config(text=resultText)

    else:
        entryObject.delete(0, tk.END)
        entryObject2.delete(0, tk.END)
        tkinter.messagebox.showerror("Error!", "You can only enter numeric values")


