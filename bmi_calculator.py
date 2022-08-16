# This is a simple BMI calculator

# First of all, lets get the user to provide some data
print('Welcome to the BMI calculator!')
height = input('Please enter your height in m: ')
weight = input('Please enter your weight in kg: ')
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)

# print the user's BMI
print('Your BMI is ' + str(bmi_as_int))

# Conditionals
if bmi_as_int <= 18:
    print("Under the government health guidelines, you are considered to be underweight.\nConsider looking into your diet to increase your weight.")
elif bmi_as_int <= 25:
    print("Under the government guidelines, your bmi is in good order.\nMaintain a healthy lifestyle!")
elif bmi_as_int <= 30:
    print("Under the government health guidelines, you are considered to be overweight.\nExercise and a healthy diet could help in bringing your weight to within the guideline.")
elif bmi_as_int <= 35:
    print("Under the government health guidelines, you are considered to be obese.\nExercise and a healthy diet could help in bringing your weight to within the guideline.")
elif bmi_as_int <= 40:
    print("Under the government health guidelines, you are considered to be overly obese.\nExercise and a healthy diet could help in bringing your weight to within the guideline.")
else:
    print("Under the government health guidelines, you are considered to be morbildy obese.\nPlease consider visting your GP for general advice!")

