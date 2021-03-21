#main-page of the system
import functions

#Menu
def printMenu():
  print (30 * "-" , "MENU" , 30 * "-"),
  print ("1. Input Project Details"),
  print("2. View Projects"),
  print("3. Schedule Projects"),
  print("4. Get a Project"),
  print("5. Exit")
# -------------------------------------------------------------------------
#.initFile() will create .csv files
functions.initFile()
#MENU
while True:
  try:     
    printMenu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
      functions.inputProject();
    elif choice == 2:
      print("\ta. One Project"),
      print("\tb. Completed Project"),
      print("\tc. All Project")
      choice1 = input("Enter your subchoice: ")
      if choice1 == 'a':
        functions.view_one()
      elif choice1 == 'b':
        functions.viewCompleted()  
      elif choice1 == 'c':
        print ("Active Projects")
        functions.view_all()
        print ("Completed Projects")
        functions.viewCompleted()
      else:
        print("Choice is not in the scope")
    elif choice == 3:
      print("\t a. Create Schedule"),
      print("\t b. View Schedule")
      choice3 = input("Enter your subchoice: ")
      if choice3 == 'a':
        functions.createSchedule()
        madeSchedule = True
      elif choice3 == 'b':
        functions.viewSchedule()
      else:
        print("Choice is not in the scope")
    elif choice == 4:
      functions.popList()
    elif choice == 5:
      break;
    else:
      print("Invalid input for user's choice. Please try again.")
  except ValueError:
    print ("Invalid input for user's choice. Please try again.")    