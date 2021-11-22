to_do_list = {
    "all_tasks": ["1. water lawn", "3. mow lawn", "2. feed dog"]

}

def to_do_list_program():
    while (True):
        menu = input('''
Press 1 to add task 
Press 2 to delete task 
Press 3 to view all tasks 
Press q to quit 
: ''')
        if menu == "1":
            task_list = input("Add priority number.task you want to complete: ")
            to_do_list["all_tasks"].append(task_list)
            print(to_do_list)
        elif menu == "2":
            delete_task = input("What task do you want to delete? ")
            if delete_task in to_do_list:
                del to_do_list[delete_task]
        elif menu == "3":
            print(sorted(to_do_list["all_tasks"]))
        elif menu == "q":
            break
to_do_list_program()