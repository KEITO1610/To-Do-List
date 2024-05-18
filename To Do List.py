import os

class ToDoList:
    def __init__(self, filename='todolist.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]
            return tasks
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Added task: {task}")

    def remove_task(self, task_number):
        try:
            task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Removed task: {task}")
        except IndexError:
            print("Invalid task number")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            todo.list_tasks()
        elif choice == '2':
            task = input("Enter a new task: ")
            todo.add_task(task)
        elif choice == '3':
            todo.list_tasks()
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo.remove_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
