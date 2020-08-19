__author__ = "Wytze Bruinsma"

from dataclasses import dataclass, field

from vaknl_content import Content


@dataclass
class Acco(Content):
    room_code: str = None
