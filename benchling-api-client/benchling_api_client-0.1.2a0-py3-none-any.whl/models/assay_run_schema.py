from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union, cast

from .archive_record import ArchiveRecord
from .schema_field import SchemaField
from .type import Type


@dataclass
class AssayRunSchema:
    """  """

    id: Optional[str] = None
    name: Optional[str] = None
    archive_record: Optional[Union[Optional[ArchiveRecord]]] = None
    field_definitions: Optional[List[SchemaField]] = None
    type: Optional[Type] = None
    system_name: Optional[str] = None
    derived_from: Optional[str] = None
    automation_input_file_configs: Optional[List[Dict[Any, Any]]] = None
    automation_output_file_configs: Optional[List[Dict[Any, Any]]] = None
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
        derived_from = self.derived_from
        if self.automation_input_file_configs is None:
            automation_input_file_configs = None
        else:
            automation_input_file_configs = self.automation_input_file_configs

        if self.automation_output_file_configs is None:
            automation_output_file_configs = None
        else:
            automation_output_file_configs = self.automation_output_file_configs

        organization = self.organization

        return {
            "id": id,
            "name": name,
            "archiveRecord": archive_record,
            "fieldDefinitions": field_definitions,
            "type": type,
            "systemName": system_name,
            "derivedFrom": derived_from,
            "automationInputFileConfigs": automation_input_file_configs,
            "automationOutputFileConfigs": automation_output_file_configs,
            "organization": organization,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> AssayRunSchema:
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
            type = Type(d.get("type"))

        system_name = d.get("systemName")

        derived_from = d.get("derivedFrom")

        automation_input_file_configs = d.get("automationInputFileConfigs")

        automation_output_file_configs = d.get("automationOutputFileConfigs")

        organization = d.get("organization")

        return AssayRunSchema(
            id=id,
            name=name,
            archive_record=archive_record,
            field_definitions=field_definitions,
            type=type,
            system_name=system_name,
            derived_from=derived_from,
            automation_input_file_configs=automation_input_file_configs,
            automation_output_file_configs=automation_output_file_configs,
            organization=organization,
        )
