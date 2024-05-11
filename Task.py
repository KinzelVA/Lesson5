class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        return f"{self.description} (Due: {self.due_date}) - {'Completed' if self.completed else 'Pending'}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print("Task added successfully.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def show_pending_tasks(self):
        print("Pending Tasks:")
        for task in self.tasks:
            if not task.completed:
                print(task)

# Пример использования:
task_manager = TaskManager()
task_manager.add_task("Complete the project report", "2023-04-10")
task_manager.add_task("Prepare for the meeting", "2023-04-12")

task_manager.mark_task_completed(0)

task_manager.show_pending_tasks()
