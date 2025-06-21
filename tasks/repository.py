from typing import Protocol, Optional, List, Dict

from tasks.models import Task


class TaskRepository(Protocol):
    def __init__(self):
        self._tasks: Dict[str, Task] = {}

    def add(self, task: Task) -> None:
        self._tasks[task.id] = task

    def get(self, task_id: str) -> Optional[Task]:
        return self._tasks.get(task_id)

    def list(self) -> List[Task]:
        return list(self._tasks.values())

    def update(self, task: Task) -> None:
        if task.id in self._tasks:
            self._tasks[task.id] = task

    def delete(self, task_id: str) -> None:
        if task_id in self._tasks:
            del self._tasks[task_id]
