from typing import List, Optional
from datetime import datetime
from tasks.models import Task, Priority
from tasks.repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def create_task(self, task: Task) -> None:
        self._repository.add(task)

    def get_task(self, task_id: str) -> Optional[Task]:
        return self._repository.get(task_id)

    def list_tasks(self) -> List[Task]:
        return self._repository.list()

    def update_task(self, task: Task) -> None:
        self._repository.update(task)

    def delete_task(self, task_id: str) -> None:
        self._repository.delete(task_id)

    def list_by_priority(self, priority: Priority) -> List[Task]:
        return [task for task in self._repository.list() if task.priority == priority]

    def list_by_category(self, category: str) -> List[Task]:
        return [task for task in self._repository.list() if task.category == category]

    def list_due_today(self) -> List[Task]:
        today = datetime.now().date()
        return [
            task for task in self._repository.list()
            if task.due_date is not None and task.due_date.date() == today
        ]

    def mark_complete(self, task_id: str) -> None:
        task = self._repository.get(task_id)
        if task:
            task.completed = True
            self._repository.update(task)
