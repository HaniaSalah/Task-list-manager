import os

FILE_PATH="tasks.txt"
lst=[]

def add_tasks():
    task=input("input tasks: ")
    lst.append(task)

def save_tasks():
    try:
        file=open(FILE_PATH,"w")
        for i in lst:
            file.write(i)
    
    except Exception as e:
        exception_handling(e)

def load_tasks():
    try:
        file=open(FILE_PATH)
        lst=file.read()
    
    except Exception as e:
        exception_handling(e)

def delete_task():
    try:
        task_del=int(input("Enter task line to delete: "))
        lst.pop(task_del-1)

    except Exception as e:
        exception_handling(e)

def display_list():
    try:
        for i in lst:
            print(i)
        
    except Exception as e:
        exception_handling(e)

def exception_handling():
    if Exception==(FileNotFoundError):
        print("please make sure you have a file to save")         
    elif  Exception==(PermissionError):
        print("please make sure you have a permission to open and write in this file")         
    elif  Exception==(IndexError):
        print("please make sure you choised a correct line index")         
    elif  Exception==(ValueError):
        print("please make sure you enter a integar number as a choice")

try:
    while True:
        print("Enter your choice:\n")
        print("1. Add task\n2. save task to file\n3. Load task\n4. Delete finished task\n5. Display list\n6. Terminate the program")  
        choice=int(input("Your choice: "))
        if choice==1:
            add_tasks()
        elif choice==2:
            save_tasks()
        elif choice==3:
            load_tasks()
        elif choice==4:
            delete_task()
        elif choice==5:
            display_list()
        elif choice==6:
            break
        else:
            print("Please enter a valid choice ")
except Exception as e:
    exception_handling(e)
