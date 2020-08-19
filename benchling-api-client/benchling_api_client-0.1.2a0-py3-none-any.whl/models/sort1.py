from enum import Enum


class Sort1(str, Enum):
    BARCODE = "barcode"
    MODIFIED_AT = "modifiedAt"
    NAME = "name"
    BARCODE_ASC = "barcode:asc"
    MODIFIED_AT_ASC = "modifiedAt:asc"
    NAME_ASC = "name:asc"
    BARCODE_DESC = "barcode:desc"
    MODIFIED_AT_DESC = "modifiedAt:desc"
    NAME_DESC = "name:desc"
