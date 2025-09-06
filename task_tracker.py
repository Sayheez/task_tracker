import os, argparse, json
from datetime import datetime

class Task:
    def __init__(self):
        self.status = "TODO"
        self.filename = ".\\tasks.json"
        self.tasks_list = self._get_json_from_file()

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

    def run(self):
        """Parse arguments and dispatch commands"""
        args = self.parser.parse_args()

        if args.command == "add_task":
            self.add_task(args.description)
        else:
            self.parser.print_help()


    # Internal function to Load the json data from file if it exists
    def _get_json_from_file(self):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                with open(self.filename, "r") as json_data:

                    self.tasks_list = json.load(json_data)
                    return self.tasks_list
            return []
        except ValueError:
            print("No such file exists")


    # Internal function to save the json
    def _save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks_list, file, indent=4)


    def start(self):
        self.status = "IN_PROGRESS"


    def complete(self):
        self.status = "DONE"


    # Add a task
    def add_task(self, task_description): 
        task_id = len(self.tasks_list) + 1
        new_task = {
            "id": task_id,
            "description": task_description,
            "status": self.status,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        } 
        self.tasks_list.append(new_task)
        self._save_tasks()
        print(f"✅ Task added successfully with the id being {task_id}")


    # List all tasks
    def list_tasks(self):
        """List all tasks with status"""
        if not self.tasks:
            print("📭 No tasks found.")
            return
        for task in self.tasks:
            status = "✅ Done" if task.get("completed") else "❌ Pending"
            print(f"{task['id']}: {task['description']} [{status}]")


    def delete_task(self, task_id):
        """Delete task by ID"""
        original_len = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]

        if len(self.tasks) < original_len:
            self._save_tasks()
            print(f"🗑 Task {task_id} deleted successfully.")
        else:
            print(f"⚠️ Task with id {task_id} not found.") 
    


if __name__ == "__main__":
   my_cli = Task()
   my_cli.run()
