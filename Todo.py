#so the todo is the literal task and the day i make it, not the due date, and a check box
class todo:
    def __init__(self, task, date, completed=False):
        self.task = task
        self.date = date
        self.completed = completed
    def mark_complete(self):
        self.completed = True

# todo_list is a list of todo objects
class todo_list:
    def __init__(self):
        self.todos = []

    def import_todos(self, todo_data):
        for task, date, completed in todo_data:
            new_todo = todo(task, date, completed)
            self.todos.append(new_todo)
    def add_todo(self, task, date):
        new_todo = todo(task, date)
        self.todos.append(new_todo)

    def export_todos(self):
        return [(t.task, t.date, t.completed) for t in self.todos]