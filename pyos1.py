from queue import Queue


class Task:
    task_id = 0

    def __init__(self, target):
        self.tid = Task.taskid  # Task ID
        self.target = target  # Target coroutine
        self.sendval = None  # value to send

    def run(self):
        return self.target.send(self.sendval)


class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.task_map = {}

    def new(self, target):
        newTask = Task(target)
        self.task_map[newTask.tid] = newTask
