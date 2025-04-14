option = 0
todo = {}
def add():
    while True:
        task = input("Enter/Update the task you want or type done to exit : ")
        if task == "done" or task == "Done":
            break
        detail = input("Enter the details you want : ")
        todo[task] = detail
    
def view():
    print("Your todo list that you entered :\n")
    for task in todo:
        print(f"{task} : {todo[task]}")

def delete():
    to_delete = input("Enter the task that you want to delete from here : ")
    if to_delete in todo:
        todo.pop(to_delete)
        print("Task deleted.")
    else:
        print("Task not found")
    view()



while option != 9:
    print("Select a option : ")
    print("Enter 1 to add/update task you want : ")
    print("Enter 2 to view task you want : ")
    print("Enter 3 to delete task you want : ")
    print("Enter 9 to exit if you want : ")

    option = int(input("Enter the choice you want : "))

    if option == 1:
        add()
    elif option == 2:
        view()
    elif option == 3:
        delete()