# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:19:47 2024
@author: harip
"""
# TO DO LIST APPLICATION
to_do_list = []

def add_tasks():
    task = input("Enter new task : ")
    to_do_list.append({'task':task , 'completed' : False})
    print ("Task has been added successfully !!!")
    ch = input("Do you want to add more tasks ? y/n 1")
    if ch.lower() ==  'y' :
        add_tasks()

    
def delete_tasks():
    if len(to_do_list) == 0:
        print("to do list is empty ! No tasks added ! Nothing to delete !\n")
    else :
        for i, task in enumerate(to_do_list, 1):
            print(f"{i}. {task['task']}")
        choice_task = int(input("\nEnter task number that you wish to delete : "))
        if choice_task >0 and choice_task <= len(to_do_list):
            del to_do_list[choice_task - 1]
            print("\nTask has been successfully deleted !!!")
        else :
            print("Invalid Choice !")
    
def all_tasks():
    if len(to_do_list) == 0:
        print("to do list is empty ! No tasks added !")
    else :
        print("All tasks:\n")
        for i, task in enumerate(to_do_list, 1):
            status = 'Completed' if task['completed'] else 'Pending'
            print(f"{i}. [{status}] {task['task']}")        
    
def completed_tasks():
    completed = [task for task in to_do_list if task['completed']]
    if not completed:
        print("No tasks completed yet.")
    else:
        print("Completed tasks:\n")
        for i, task in enumerate(completed, 1):
            print(f"{i}. {task['task']}")

def update_task():
    choice = input("Enter task number to mark as completed (or press Enter to go back): ")
    if choice.isdigit():
        choice = int(choice)
        if choice > 0 and choice <= len(to_do_list):
            to_do_list[choice - 1]['completed'] = True
            print("Task status updated to Completed!")
        else:
            print("Invalid task number!")
    
def main():
    while True:
        print("\n******** TO DO APPLICATION ********")
        print("\n1. Add task")
        print("\n2. Delete Task")
        print("\n3. View tasks")
        print("\n4. Update task")
        print("\n5. Quit")
        choice = int(input("\nEnter your choice : "))
        
        if choice == 1:
            add_tasks()
        elif choice == 2:
            delete_tasks()
        elif choice == 3:
            print("\na. view all tasks")
            print("\nb. view completed tasks")
            ch = input("\nEnter your choice : ")
            if ch.lower() == 'a':
                all_tasks()
            elif ch.lower() == 'b':
                completed_tasks()
        elif choice == 4:
            update_task()
        elif choice == 5:
            print("\nThank you for using TO DO APPLICATION !!!")
            break
        else:
            print("\nInvalid choice ! please enter appropriate choice")
            
        
if __name__ ==  '__main__':
    main()




