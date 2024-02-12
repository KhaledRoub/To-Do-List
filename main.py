def main () :
    message="""
1- add tasks to a list 
2- mark task as compete
3- view tasks
4- Quit
"""
    global tasks
    tasks=[]


    while True:
        print(message)
        choice =input("Enter your choice ")
        if choice == '1':
            add_task()
        elif choice =='2':
            complete_tasks(tasks)
        elif choice=='3':
            view_tasks(tasks)
        elif choice =='4' :
            break
        else:
            print("Invalid choice , please enter a number between 1 and 4 ")




def add_task ():
    # get task from user 
    print("Enter the task you want to add: ")
    task = input()
    #define task status
    # status = "incomplete"
    task_info = {"task" : task , "completed": False}
    # append task to list of tasks
    tasks.append(task_info)
    print("Task added")

def complete_tasks(task_list):
    if not task_list:
        print ("No incomplete tasks!")
        return
    incomplete_tasks = [task for task in task_list if task["completed"] == False]
    # print ("Tasks that are not completed yet", incomplete_tasks)
    for i , task in enumerate(incomplete_tasks):
        print(f"{i+1} - {task['task']}")
        print("="*30)

    try:
        task_number= int (input(" choose the task to complete : "))
        if task_list < 1 or task_list > len(incomplete_tasks):
            raise IndexError("ــــــــ--ـــــــــ :(  ! ")
        incomplete_tasks[task_number-1]["completed"]=True
        print(tasks)
    except ValueError:
        print("INVALID input ")
    except IndexError : 
        print("choose from available tasks")
    

def view_tasks(task_list):
    if not task_list : print("no tasks to view");return

    for i , task in enumerate(task_list):
        status = "✔️" if task["completed"] else "❌"
        
        print(f"{i+1} - {task['task']} {status}")
        

if __name__ == "__main__":
    main()