import csv, os, operator, projclass

fieldnames=['id_number','title','size','priority']
projects = []

#initialization - OOP for schedule
def initFile():
  mode = 'a' if os.path.exists('projects.csv') else 'w+'
  files = ['projects.csv','schedules.csv', 'completed.csv']
  if mode == 'w+':
    for file in files:
      with open(file, mode, newline='') as csvfile:
        if mode == 'w+':
          writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
          writer.writeheader()
          
  filename = 'projects.csv' if scheduleEmpty() else 'schedules.csv'
  with open(filename, 'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
      projects.append(projclass.Projects(row['id_number'],row['title'],row['size'],row['priority']))

#function for inputting projects
def inputProject():
  with open('projects.csv', 'a', newline='') as csvfile:
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames) 
    project_idnumber=eval(input("Enter ID number of project: "))
    project_title=input("Enter title of project: ")
    project_size=eval(input("Enter the number of pages: "))
    project_priority=eval(input("Enter project priority [lower number-higher priority]: "))
    writer.writerow({'id_number':project_idnumber,'title':project_title,'size':project_size,'priority':project_priority})
    projects.append(projclass.Projects(project_idnumber,project_title,project_size,str(project_priority)))
    print("Input Project Successful")

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

#check if csvfiles are empty, 31 = length of headers
def projectEmpty():
  return os.stat('projects.csv').st_size <= 31

def scheduleEmpty():
  return os.stat('schedules.csv').st_size <= 31

#sort the available schedules on the class
def createSchedule():
  projects.sort(key = operator.attrgetter('priority','size'))
  inputSchedule()
  print ("Schedule Created!")
  
  

#view all schedules
def viewSchedule(madeSchedule):
  if(scheduleEmpty() and not madeSchedule):
    print("Create a Schedule First!")
  else:
    for project in projects:
      print("ID Number:",project.id_number,"| Title:", project.title, 
            "| Project size:", project.size, "| Priority:", project.priority)
      
def inputSchedule():
  with open('schedules.csv', 'w+', newline='') as csvfile:
    writer=csv.DictWriter(csvfile, fieldnames=fieldnames) 
    writer.writeheader()
    for project in projects:
      writer.writerow({'id_number':project.id_number,'title':project.title,'size':project.size,'priority':project.priority})
      
def popList():
  temp = []
  if(scheduleEmpty()):
    print("Create a Schedule First!")
  else:
    mode = 'a' if os.path.exists('completed.csv') else 'w+'
    with open("schedules.csv",'r') as sched:
      val = sched.readlines()
      pull = val[1]
      temp.append(val[0])
      temp.append(val[2:])
      with open("completed.csv",mode) as completed:
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
            
    
      
    

      
      

        
        
        