from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from dapodik.base import BaseData


@dataclass
class JadwalPaud(BaseData):
    jadwal_id: str
    nama: str
    kesehatan: str
    pamts: str
    ddtk: str
    freq_parenting: str
    create_date: datetime
    last_update: datetime
    expired_date: Optional[datetime]
    last_sync: datetime
