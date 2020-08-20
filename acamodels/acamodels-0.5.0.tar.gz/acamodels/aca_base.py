# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from pathlib import Path

from pydantic import BaseModel

# -----------------------------------------------------------------------------
# ACA Base model
# -----------------------------------------------------------------------------


class ACABase(BaseModel):
    """Base model with reusable methods & settings"""

    def dump(self, to_file: Path) -> None:
        data = super().json(indent=2, ensure_ascii=False)
        to_file.write_text(data, encoding="utf-8")
