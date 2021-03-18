#Menu
import mp6
def printMenu():
  print (30 * "-" , "MENU" , 30 * "-"),
  print ("1. Input Project Details"),
  print("2. View Projects"),
  print("      a. One Project"),
  print("      b. Completed Project"),
  print("      c. All Project"),
  print("3. Schedule Projects"),
  print("      a. Create Schedule"),
  print("      b. View Schedule"),
  print("4. Get a Project"),
  print("5. Exit")
  
loop = True
while loop:
  printMenu()
  choice = int(input("Enter your choice: "))
  
  if choice == 1:
    print ("Menu 1 has been selected")
    mp6.input_project()
  elif choice == 2:
    print("\t a. One Project"),
    print("\t b. Completed Project"),
    print("\t c. All Project")
    while True:
      choice1 = input("Enter your subchoice: ")
      if choice1 == 'a':
        print ("Menu 2a has been selected")
        break
      if choice1 == 'b':
        print ("Menu 2b has been selected")
        break
      if choice1 == 'c':
        print ("Menu 2c has been selected")
        break
    break
  elif choice == 3:
    while True:
      choice3 = input("Enter your subchoice: ")
      print("\t a. Create Schedule"),
      print("\t b. View Schedule")
      if choice3 == 'a':
        print ("Menu 3a has been selected")
        break
      if choice3 == 'b':
        print ("Menu 3b has been selected")
        break
    break
  elif choice == 4:
    print ("Menu 4 has been selected")
    break
  elif choice == 5:
    break
  else:
    print("Not on the choices")
    break