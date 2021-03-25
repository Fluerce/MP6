#functions.py - source code where all functions of the systems are written
import csv, os, operator, projclass

fieldnames=['id_number','title','size','priority']
projects = []

#initialization - OOP for schedule
def initFile():
  files = ['projects.csv','schedules.csv', 'completed.csv']
  for file in files:
    if not os.path.exists(file):
      with open(file, 'w+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

#function for inputting projects
def inputProject():
  while True:    
      try:
        with open('projects.csv', 'a', newline='') as csvfile:
          writer=csv.DictWriter(csvfile, fieldnames=fieldnames) 
          project_idnumber=eval(input("Enter ID number of project: "))
          if idNumberExists(project_idnumber):
              print("The ID Number already exists.")
              break
          project_title=input("Enter title of project: ")
          project_size=eval(input("Enter the number of pages: "))
          project_priority=eval(input("Enter project priority [lower number-higher priority]: "))
          writer.writerow({'id_number':project_idnumber,'title':project_title,'size':project_size,'priority':project_priority})
          print("Input Project Successful.")
          break
      except NameError:
        print("Characters are not allowed in this field.")
      except ValueError:
        print("Your input is invalid.")
      #except TypeError:
        #print("Invalid data type.")
      except FileNotFoundError:
        print("The file was not found.")
      except SyntaxError:
        print("Your input is in invalid syntax.")        

def idNumberExists(idNumber):
    with open('projects.csv','r') as idprojects:
      reader=csv.DictReader(idprojects)
      for ids in reader:
            if int(ids['id_number'])==(idNumber):
                  return True             
    with open('completed.csv','r') as idcompleted:
      reader=csv.DictReader(idcompleted)
      for ids in reader:
            if int(ids['id_number'])==(idNumber):
                  return True 
    return False              
              

#function for viewing all projects
def view_all():
  if projectEmpty():
    print("No Projects Available!")
  else:
    with open('projects.csv', 'r') as csvfile:
      reader=csv.DictReader(csvfile)
      for row in reader:
        print("ID Number:",row['id_number'],"| Title:",row['title'],
          "| Project size:",row['size'],"| Priority:",row['priority'])

#view one project only
def view_one():
  match = False
  try:
      with open('projects.csv', 'r') as csvfile:
        reader=csv.DictReader(csvfile)
        search_id=int(input("Enter the id number of the project to view: "))
        for row in reader:
          if(row['id_number']==str(search_id)):
            print("ID Number:",row['id_number'],"| Title:",row['title'],
            "| Project size:",row['size'],"| Priority:",row['priority'])
            match = True
        if not match:
          print("No Project With The Indicated ID!")
  except NameError:
    print("Characters are not allowed in this field.")
  except ValueError:
    print("Your input is invalid.")
  except TypeError:
    print("Invalid data type.")
  except FileNotFoundError:
    print("The file was not found.")
  except SyntaxError:
    print("Your input is in invalid syntax.")


#check if csvfiles are empty, 31 = length of headers
def projectEmpty():
  return os.stat('projects.csv').st_size <= 31

#check if the scedule file is empty
def scheduleEmpty():
  return os.stat('schedules.csv').st_size <= 31

#check if the completed projects file is empty
def completedEmpty():
  return os.stat('completed.csv').st_size <= 31

#this function will input the schedule of the projects
def inputSchedule():
  with open('schedules.csv', 'w+', newline='') as csvfile:
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames) 
    writer.writeheader()
    for project in projects:
      writer.writerow({'id_number':project.id_number,'title':project.title,'size':project.size,'priority':project.priority})    

#this function will create the schedule of the projects based on project-priority
def createSchedule():
  if projectEmpty():
    print("Create an Active Project first!")
  else:
    projects.clear();
    with open('projects.csv', 'r') as csvfile:
      reader=csv.DictReader(csvfile)
      for row in reader:
        projects.append(projclass.Projects(row['id_number'],row['title'],int(row['size']),int(row['priority'])))
    projects.sort(key = operator.attrgetter('priority','size'))
    inputSchedule()
    print ("Schedule Created!")

#this function will view the completed projects  
def viewCompleted():
  if(completedEmpty()):
    print("No Completed Projects Yet!")
  else:
    with open('completed.csv', 'r') as csvfile:
      reader=csv.DictReader(csvfile)
      for row in reader:
         print("ID Number:",row['id_number'],"| Title:",row['title'],
               "| Project size:",row['size'],"| Priority:",row['priority'])
          
#this function view the schedules in the system
def viewSchedule():
  if(scheduleEmpty()):
    print("Create a Schedule First!")
  else:
    with open('schedules.csv', 'r') as csvfile:
      reader=csv.DictReader(csvfile)
      for row in reader:
         print("ID Number:",row['id_number'],"| Title:",row['title'],
               "| Project size:",row['size'],"| Priority:",row['priority'])

#this will get the most prioritized project in the project schedule      
def popList():
  temp = []
  if(scheduleEmpty()):
    print("Create a Schedule First!")
  else:
    with open("schedules.csv",'r') as sched:
      val = sched.readlines()
      pull = val[1]
      pullers = pull.split(",")
      print("PROJECT DONE: ","ID - ",pullers[0],"| Title - ",pullers[1])
      temp.append(val[0])
      temp.append(val[2:])
      with open("completed.csv",'a') as completed:
        completed.write(pull)
      with open("schedules.csv",'w') as sched:
        for line in temp:
          sched.writelines(line)
      with open("projects.csv", 'r') as proj:
        temp.clear()
        for line in proj:
          if line != pull:
            temp.append(line)
      with open("projects.csv", 'w') as proj:
        for line in temp:
          proj.writelines(line)      
      
        
    
      
    

      
      
      

        
        
        