class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n--- To-Do List Menu ---")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("\nYour to-do list is empty.")
        else:
            print("\nYour to-do list:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def add_task(self):
        task = input("\nEnter the task you want to add: ")
        self.tasks.append(task)
        print(f'"{task}" has been added to your to-do list.')

    def delete_task(self):
        if not self.tasks:
            print("\nYour to-do list is empty. Nothing to delete.")
            return

        self.view_tasks()
        try:
            task_num = int(input("\nEnter the task number you want to delete: "))
            if 1 <= task_num <= len(self.tasks):
                removed_task = self.tasks.pop(task_num - 1)
                print(f'"{removed_task}" has been removed from your to-do list.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")