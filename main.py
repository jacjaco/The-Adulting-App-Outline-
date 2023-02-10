import datetime
from datetime import timedelta
import pandas
from tabulate import tabulate


def welcome():
  print("Welcome to the Adulting App, the helpful assistant that makes sure you are never blindsided by the evasive to-do lists that come with adulting.")
  print()
  print("First off, let's learn about you, your life, and your goals.")
  print()
  print("Please fill in the following information")
  
  name = input("Name: ")
  # Check that age is an integer
  while True:
    age = input("Age: ")
    if age.isnumeric():
      age = int(age)
      break
    else:
      print("Invalid input. Please enter an integer.")
    
  location = input("State of residence: ")
  occupation = input("Occupation: ")
  
  print()
  print("Great start! Now take a chance to browse through the list of goals or responsibilities that you'd like to oragnize on this app.")
  print()
  print("You can add these items to your personal folder by entering the corresponding number (one number at a time) and then hitting enter.")
  print()
  
  responsibilities = ("(1) I want to buy a car.", "(2) I bought a car.", "(3) I'm looking for a new job.", "(4) I'm starting a new job.", "(5) I want to set up a monthly budget", "(6) I want to save for retirement.", "(7) I want to pay off student loans.", "(8) I want to do my taxes properly.", "(9) Continue.")
  print()
  
  user_folders = []
  
  while True:
    
    for responsibility in responsibilities:
      print(responsibility)
  
    print()
    user_selection = int(input("Which folder would you like to add? Or select 9 to continue: "))
    user_selection = user_selection - 1
    print()
    
    if user_selection < 8:
      user_folders.append(responsibilities[user_selection])
      print(f"You have added the following folder:'{responsibilities[user_selection]}'")
      print()
  
    if user_selection == 8:
      break

  return (name, age, location, occupation, user_folders)




def bought_car(car_maint_data):
  
  # regular car maintenance__________________________________________________
      ## Python program to print the data
      ## Format structure found from: https://www.educba.com/python-print-table/
      ## Maintenance chekclist from: https://www.travelers.com/iw-documents/tools-resources/car/maintenance/car-maintenance-checklist.pdf
  print("Excellent! Now that you have a car we can schedule regular maintenenace, so you can maximize the number of miles you get out of your vehicle. ")
  print()
  print("Here is your current schedule for car maintenance")
  print()
  print (tabulate(car_maint_data, headers=["Task", "Miles Frequency", "Month Frequency", "Last Checked", "Next Check", "Average Cost"]))
  print()

  while True:
    edit_maintenance = input("Would you like to continue to edit your car maintenance schedule? Y or N")
    edit_maintenance = edit_maintenance.upper()
  
    if edit_maintenance == "Y":
      maint_num = int(input("Which maintenance task would you like to edit? Please enter the corresponding number.  "))
      if maint_num in range(1,12):
        row = maint_num-1
        print("When was this last checked? Enter integers only YYYY, M, D. ")
        year1 = int(input("Year: "))
        month1 = int(input("Month (1-12): "))
        day1 = int(input("Day (1-31): "))
        lc = datetime.date(year1, month1, day1)
        car_maint_data[row][3] = lc
        month_value = (car_maint_data[row][2])*30
        delta1 = timedelta(days = month_value)
        nc = lc + delta1
        car_maint_data[row][4] = nc
      else:
        print("Invalid input.")
          
    elif edit_maintenance == "N":
      break

    else:
      print("Invalid input. Please enter Y or N.  ")

    print (tabulate(car_maint_data, headers=["Task", "Miles Frequency", "Month Frequency", "Last Checked", "Next Check", "Average Cost"]))

 
  print()
  print()
  print()
    
  # montly insurance budget__________________________________________________

  # DMV requirements__________________________________________________

  # Tickets, towing, and break downs__________________________________________________

  return car_maint_data # this overwrites the table every time the funciton is run, until you exit the program. 




  
  




# Initialize templates and tables for program
car_maint_data = [["1) Check Oil", 3000, 3, "-", "-", "-"],
["2) Check Transmission Fluid", 12000, 12, "-", "-", "-"],
["3) Check Lubrication System", 3000, 3, "-", "-", "-"],
["4) Check Spark Plugs",6000, 6, "-", "-", "-"],
["5) Check Tires",12000, 12, "-", "-", "-"],
["6) Check Battery",6000, 6, "-", "-", "-"],
["7) Check Air Filter",12000, 12, "-", "-", "-"],
["8) Check Fuel Filter",6000, 6, "-", "-", "-"],
["9) Check Brake Fluid",12000, 12, "-", "-", "-"],
["10) Check Radiator Coolant",12000, 12, "-", "-", "-"],
["11) Check Power Steering",6000, 6, "-", "-", "-"]]


def run_program():

  user_specs = welcome() # this is (name, age, location, occupation, user_folders)
  name = user_specs[0]
  age = user_specs[1]
  location = user_specs[2]
  occupation = user_specs[3]
  user_folders = user_specs[4]
  
  print()
  
  # https://realpython.com/python-return-statement/
  # name, age, location, occupation, user_folders = welcome()
  print(f"Thanks {name}, you have added the following folders:")
  print()

  for folder in user_folders:
    print(folder)

  print()


  # literally the only distinction between this if statement and the next while loop is saying what would you like to edit "first" instead of "next"
  folder_selection = int(input(f"Ok {name}, which folder would you like to edit first? Please enter the corresponding number."))
  print()
  print()
  if folder_selection == 2:
    bought_car(car_maint_data)
  # Below are placeholders for when more folders have written funcitons. 
  elif folder_selection == 1:
    print("This folder hasnt been written yet")
  elif folder_selection == 3:
    print("This folder hasnt been written yet")
  elif folder_selection == 4:
    print("This folder hasnt been written yet")
  elif folder_selection == 5:
    print("This folder hasnt been written yet")
  elif folder_selection == 6:
    print("This folder hasnt been written yet")
  elif folder_selection == 7:
    print("This folder hasnt been written yet")
  elif folder_selection == 8:
    print("This folder hasnt been written yet")
  elif folder_selection == 9:
    print("This folder hasnt been written yet")
  else:
    print("This is not a valid selection.")
    

  while True:

    print()
    print()
    print(f"{name}'s Folders:-----------")
    for folder in user_folders:
      print(folder)
    print()
    folder_selection = int(input(f"Ok {name}, which folder would you like to view next?"))
    print()
    print()

    
    if folder_selection == 2:
      bought_car(car_maint_data)
    # Below are placeholders for when more folders have written funcitons. 
    elif folder_selection == 1:
      print("This folder hasnt been written yet")
    elif folder_selection == 3:
      print("This folder hasnt been written yet")
    elif folder_selection == 4:
      print("This folder hasnt been written yet")
    elif folder_selection == 5:
      print("This folder hasnt been written yet")
    elif folder_selection == 6:
      print("This folder hasnt been written yet")
    elif folder_selection == 7:
      print("This folder hasnt been written yet")
    elif folder_selection == 8:
      print("This folder hasnt been written yet")
    elif folder_selection == 9:
      print("This folder hasnt been written yet")
    else:
      print("This is not a valid selection.")

  return

# Girl, dont forget to actually run the main function
run_program()
print("The end.")

