from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class BadRequestError:
    """  """

    error: Optional[Dict[Any, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        error = self.error

        return {
            "error": error,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> BadRequestError:
        error = d.get("error")

        return BadRequestError(error=error,)
