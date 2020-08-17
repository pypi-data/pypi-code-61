from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class User:
    """  """

    handle: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        handle = self.handle
        id = self.id
        name = self.name

        return {
            "handle": handle,
            "id": id,
            "name": name,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> User:
        handle = d.get("handle")

        id = d.get("id")

        name = d.get("name")

        return User(handle=handle, id=id, name=name,)
