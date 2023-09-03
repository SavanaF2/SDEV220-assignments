'''
Savana Fallen
Deans list and honor role checker
Desc: This program accepts a students last and first name as well as their GPA and displays whether or not the student has made it to the Dean's list or the Honor Roll.
'''
last_name = input("Enter the student's last name or enter ZZZ to quit: ")

while last_name != "ZZZ":
    first_name = input("Enter the student's first name or enter ZZZ to quit: ")
    if first_name == "ZZZ":
        print("Program has successfully quit.")
        quit
    GPA = float(input("Enter the student's GPA: "))
    #Calculates and displays whether or not the student has made it to the Honor Roll or the Dean's list
    if GPA >= 3.5:
        print(f"The student has made it to the Dean's list.")
    elif GPA >= 3.25:
        print(f"The student has made it to the Honor Roll.")
    else:
        print("The student has not made it to the Dean's list nor the Honor Roll.")
    #Determines whether the while loop will restart or quit
    last_name = input("To continue, enter another student's last name or enter ZZZ to quit: ")

#Executes if the user enters ZZZ for the last_name
else:
    print("Program has successfully quit")
