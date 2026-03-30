from datetime import datetime
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    title = validate_task_title(title)
    description = validate_task_description(description)
    due_date = validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")

def mark_task_as_complete(index, tasks=tasks):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as complete!")
    else:
        print("Invalid task index.")

def view_pending_tasks(tasks=tasks):
    for i, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{i}. {task['title']} - Due: {task['due_date']}")

def calculate_progress(tasks=tasks):
    if not tasks:
        return 0

    completed = 0
    for task in tasks:
        if task["completed"]:
            completed += 1

    progress = (completed / len(tasks)) * 100
    return progress