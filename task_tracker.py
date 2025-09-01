import argparse, json
from datetime import date

class Task:
    def __init__(self, id, description, status):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = date.today()
        self.updated_at = date.today()

    # tasks = []  # A list where the 

    def add(self, task_description):
        with open("tasks.json", "a") as file:
            tasks_list = json.load(file)
        tasks_list.append(task_description)
        print("Task added!")



    

    
