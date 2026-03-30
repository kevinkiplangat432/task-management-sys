from datetime import datetime

def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Task title cannot be empty.")
    return title

def validate_task_description(description):
    if len(description) == 0:
        raise ValueError("Task description cannot be empty.")
    if len(description) > 500:
        raise ValueError("Description too long.")
    return description

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return due_date
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format.")