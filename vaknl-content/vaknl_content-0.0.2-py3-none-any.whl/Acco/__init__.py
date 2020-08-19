__author__ = "Wytze Bruinsma"

from dataclasses import dataclass, field

from vaknl_content import Content


@dataclass
class Acco(Content):
    street: str = None
    zip_code: str = None
    city: str = None
    country: str = None
    phone: str = None
    email: str = None
    website: str = None
    lat: str = None
    long: str = None
    airports: list = field(default_factory=list)
