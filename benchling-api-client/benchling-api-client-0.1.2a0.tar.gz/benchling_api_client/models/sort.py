from enum import Enum


class Sort(str, Enum):
    MODIFIED_AT = "modifiedAt"
    MODIFIED_AT_ASC = "modifiedAt:asc"
    MODIFIED_AT_DESC = "modifiedAt:desc"
    NAME = "name"
    NAME_ASC = "name:asc"
    NAME_DESC = "name:desc"
