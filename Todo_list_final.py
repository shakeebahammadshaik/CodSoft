class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

    def remove_task(self, task_index):
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                removed_task = self.tasks.pop(task_index - 1)
                print(f'Task "{removed_task}" removed successfully.')
            else:
                print('Invalid task index.')
        except ValueError:
            print('Invalid task index.')

    def clear_tasks(self):
        self.tasks = []
        print('All tasks cleared.')

def main():
    to_do_list = ToDoList()

    while True:
        print('\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Clear All Tasks\n5. Exit')
        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            task = input('Enter the task: ')
            to_do_list.add_task(task)
        elif choice == '2':
            to_do_list.view_tasks()
        elif choice == '3':
            task_index = input('Enter the task index to remove: ')
            to_do_list.remove_task(task_index)
        elif choice == '4':
            to_do_list.clear_tasks()
        elif choice == '5':
            print('Exiting the to-do list application. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()
