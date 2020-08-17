from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union, cast

from .archive_record import ArchiveRecord
from .schema_field import SchemaField
from .type12 import Type12


@dataclass
class RequestSchema:
    """  """

    id: Optional[str] = None
    name: Optional[str] = None
    archive_record: Optional[Union[Optional[ArchiveRecord]]] = None
    field_definitions: Optional[List[SchemaField]] = None
    type: Optional[Type12] = None
    system_name: Optional[str] = None
    organization: Optional[Dict[Any, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        if self.archive_record is None:
            archive_record = None
        else:
            archive_record = self.archive_record.to_dict() if self.archive_record else None

        if self.field_definitions is None:
            field_definitions = None
        else:
            field_definitions = []
            for field_definitions_item_data in self.field_definitions:
                field_definitions_item = field_definitions_item_data.to_dict()

                field_definitions.append(field_definitions_item)

        type = self.type.value if self.type else None

        system_name = self.system_name
        organization = self.organization

        return {
            "id": id,
            "name": name,
            "archiveRecord": archive_record,
            "fieldDefinitions": field_definitions,
            "type": type,
            "systemName": system_name,
            "organization": organization,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> RequestSchema:
        id = d.get("id")

        name = d.get("name")

        def _parse_archive_record(data: Dict[str, Any]) -> Optional[Union[Optional[ArchiveRecord]]]:
            archive_record: Optional[Union[Optional[ArchiveRecord]]]
            archive_record = None
            if d.get("archiveRecord") is not None:
                archive_record = ArchiveRecord.from_dict(cast(Dict[str, Any], d.get("archiveRecord")))

            return archive_record

        archive_record = _parse_archive_record(d.get("archiveRecord"))

        field_definitions = []
        for field_definitions_item_data in d.get("fieldDefinitions") or []:
            field_definitions_item = SchemaField.from_dict(field_definitions_item_data)

            field_definitions.append(field_definitions_item)

        type = None
        if d.get("type") is not None:
            type = Type12(d.get("type"))

        system_name = d.get("systemName")

        organization = d.get("organization")

        return RequestSchema(
            id=id,
            name=name,
            archive_record=archive_record,
            field_definitions=field_definitions,
            type=type,
            system_name=system_name,
            organization=organization,
        )
