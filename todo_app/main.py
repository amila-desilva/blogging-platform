from todo_app.tasks import ToDoList

def main():
    todo_list = ToDoList()
    
    while True:
        todo_list.display_menu()
        choice = input("\nChoose an option (1-4): ")
        
        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            todo_list.add_task()
        elif choice == '3':
            todo_list.delete_task()
        elif choice == '4':
            print("\nExiting the To-Do List application. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
