# BMI Calculator
# BMI = KG / height (meters) ** 2

import tkinter

root = tkinter.Tk() # Class declaration Tk
root.geometry("300x150") # Set the default size of the UI
root.title("BMI Calculator") # Give the GUI window a title

# Create functions
def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2), 1)
    label_result['text'] = f"BMI: {bmi}"


# Create the GUI
label_kg = tkinter.Label(root, text="KG: ")
label_kg.pack() # This line will ensure the above laber is visible in th GUI

entry_kg = tkinter.Entry(root)
entry_kg.pack() # get the weight entry field to appear on the GUI

label_height = tkinter.Label(root, text="HEIGHT: ")
label_height.pack()

entry_height = tkinter.Entry(root)
entry_height.pack() # get the height entry field to appear on the GUI

label_result = tkinter.Label(root, text="BMI: ")
label_result.pack()

button_calculate = tkinter.Button(root, text="Calculate", fg="black", command=calculate_bmi)
button_calculate.pack() # get the button to appear on the GUI


root.mainloop() # Keep the GUI window open whilst the program runs
