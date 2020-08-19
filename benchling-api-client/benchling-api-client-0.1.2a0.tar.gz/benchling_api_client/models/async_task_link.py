from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class AsyncTaskLink:
    """  """

    task_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        task_id = self.task_id

        return {
            "taskId": task_id,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> AsyncTaskLink:
        task_id = d.get("taskId")

        return AsyncTaskLink(task_id=task_id,)
