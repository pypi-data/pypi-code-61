from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Measurement:
    """  """

    value: Optional[float] = None
    units: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        value = self.value
        units = self.units

        return {
            "value": value,
            "units": units,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Measurement:
        value = d.get("value")

        units = d.get("units")

        return Measurement(value=value, units=units,)
