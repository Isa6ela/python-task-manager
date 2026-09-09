from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1


    def add_task(self, task):
        new_task = Task(self.next_id, task)
        self.tasks.append(new_task)
        self.next_id = self.next_id + 1

    def find_task(self,id):
        for task in self.tasks:
            if task.id == id:
                return task

    def complete_task(self, id):
        task = self.find_task(id)
        task.completed = True

    def delete_task(self,id):
        task = self.find_task(id)
        self.tasks.remove(task)