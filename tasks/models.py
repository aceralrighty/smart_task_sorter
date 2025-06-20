from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Optional


class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


@dataclass
class Task:
    id: str
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    category: Optional[str] = None
    priority: Priority = Priority.MEDIUM
    complete: bool = False
