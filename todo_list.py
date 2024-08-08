class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            del self.tasks[task_number]

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]['completed'] = True

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{idx + 1}. {task['task']} - {status}")
