import os, argparse, json
from datetime import date

class Task:
    def __init__(self):
        self.description = "task"
        self.status = "TODO"
        self.created_at = date.today
        self.updated_at = date.today
        self.tasks_list = []
        self.filename = "tasks.json"

                # Initialize parser
        self.parser = argparse.ArgumentParser(
            description="Class-based TASK-CLI TRACKER"
        )
        self.subparsers = self.parser.add_subparsers(dest="command", help="Available commands")

        # Register commands
        self._register_commands()

    def _register_commands(self):
        """Define CLI subcommands and arguments"""
        
        add_task_parser = self.subparsers.add_parser("add_task", help="Add a task ")
        add_task_parser.add_argument("description", type=str, help="Task description")


    # Internal function to Load the json data from file if it exists
    def get_json_from_file(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            with open(self.filename, "r") as json_data:
                self.tasks_list = json.load(json_data)
        return self.tasks_list


    # Internal function to save the json

    # Add a task
    def add_task(self, task_description): 
        pass