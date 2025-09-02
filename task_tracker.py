import argparse, json
from datetime import date

class Task:
    def __init__(self):
        self.description = "task"
        self.status = "TODO"
        self.created_at = date.today()
        self.updated_at = date.today()

    # tasks = []  # A list where the 

    def add(self, task_description):
        with open("tasks.json", "a") as file:
            self.tasks_list = json.load(file)
        self.tasks_list.append(task_description)
        print("Task added!")


def main():
    parser = argparse.ArgumentParser(
        description="A simple Task CLI Tracker"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcommand: add
    greet_parser = subparsers.add_parser("add", help="Add a task description")
    greet_parser.add_argument("description", type=str, help="task description")

    # Parse arguments
    args = parser.parse_args()

    # Dispatch commands
    if args.command == "add":
        Task.add(args.name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

    

    
