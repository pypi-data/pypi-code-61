from threading import Thread
from time import time

class Task:
    """ 
    :param time: time (in seconds) after which the task will be triggered
    :type time: int
    
    :param repeating: repeating count. if True, the task will repeat indefinitely
    :type repeating: int
    
    :param name: Task name
    :type name: str
    
    :ivar target: func
    :ivar args: target args
    :ivar kwargs: target kwargs
    """
    time = None
    name = None
    repeating = 0
    target = None
    args = ()
    kwargs = {}
    utime = None 
    
    def __init__(self, time, repeating=0, name=None):
        self.time = time
        self.name = name
        self.repeating = repeating
       
    def run(self):
        if callable(self.target):
            self.target(*self.args, **self.kwargs)
        
class TaskManager(Thread):
    tasks = {}
    clones = {}
    completed = []
    bot = None
    
    def __init__(self, bot):
        Thread.__init__(self, name="TaskManager")
        self.bot = bot
        self.start()
       
    def run(self):
        while self.bot.RUNNING:
            tasks = self.tasks.copy()
            for key, task in tasks.items():
                if time() - task.utime >= task.time:
                    try:
                        thread = Thread(target=task.run)
                        thread.daemon = True
                        thread.start()
                        task.utime = time()
                        
                        if task.repeating is not True:
                            if task.repeating <= 0:
                                self.remove_task(task)
                                if bool(self.bot.get_settings("completed_tasks_list", False)):
                                    self.completed.append(task)
                            else:
                                task.repeating -= 1
                    except:
                        self.bot.logger.error(self.bot.get_messages("task_error", task=task.name))
                        self.bot.log_exception()
        
    def add_task(self, task):
        if isinstance(task, Task):
            if not task.name:
                task.name = task.__class__.__name__
            if task.name in self.tasks and task.name not in self.clones:
                self.clones[task.name] = 1
            if task.name in self.clones:
                task.name = "{}-#{}".format(task.name, self.clones[task.name])
                self.clones[task.name] += 1
            if task.name in self.tasks:
                return self.add_task(task)
            task.utime = time()
            self.tasks[task.name] = task
    
    def remove_task(self, task):
        if isinstance(task, Task):
            task = task.name
        self.tasks.pop(task, None)
        self.clones.pop(task, None)