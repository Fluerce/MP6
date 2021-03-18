import csv

#initial variables
csv_open=open("projects.csv",'r',encoding='utf-8-sig')
table_reader=csv.DictReader(csv_open)
csv_add=open("projects.csv",'a',newline='\n')
csv_dictwriter=csv.DictWriter(csv_add, fieldnames=['id_number','title','size','priority']) 
csv_dictreader=csv.DictReader(csv_open,fieldnames=['id_number','title','size','priority'])

#function for inputting projects
def input_project():
    project_idnumber=int(input("Enter ID number of project: "))
    project_title=input("Enter title of project: ")
    project_size=int(input("Enter the number of pages: "))
    project_priority=int(input("Enter project priority [lower number-higher priority]: "))
    csv_dictwriter.writerow({'id_number':project_idnumber,'title':project_title,'size':project_size,'priority':project_priority})
    print("Input Project Successful")
    csv_add.close()

#function for viewing all projects
def view_all():
    for row in table_reader:
        print(row)
    csv_open.close()

#view one project only
def view_one():
    search_id=int(input("Enter the id number of the project to view: "))
    for row in table_reader:
        if(row['id_number']==str(search_id)):
            print("ID Number:",row['id_number'],"| Title:",row['title'],
            "| Project size:",row['size'],"| Priority:",row['priority'])
