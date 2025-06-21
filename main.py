import uuid
from datetime import datetime

from tasks.models import Task, Priority
from tasks.repository import TaskRepository
from tasks.services import TaskService

repo = TaskRepository()

service = TaskService(repo)
title_input = input("")
category_input = input("")
task = Task(
    id=str(uuid.uuid4()),
    title=input(title_input),
    due_date=datetime.now(),
    priority=Priority.MEDIUM,
    category=input(category_input),

)

service.create_task(task)
for t in service.list_due_today():
    print(t)
