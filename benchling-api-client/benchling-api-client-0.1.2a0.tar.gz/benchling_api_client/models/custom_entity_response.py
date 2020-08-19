from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional, cast

from .schema_summary import SchemaSummary
from .user import User


@dataclass
class CustomEntityResponse:
    """  """

    aliases: Optional[List[str]] = None
    created_at: Optional[datetime] = None
    creator: Optional[User] = None
    authors: Optional[List[User]] = None
    custom_fields: Optional[Dict[Any, Any]] = None
    entity_registry_id: Optional[str] = None
    fields: Optional[Dict[Any, Any]] = None
    folder_id: Optional[str] = None
    id: Optional[str] = None
    modified_at: Optional[datetime] = None
    name: Optional[str] = None
    registry_id: Optional[str] = None
    schema: Optional[SchemaSummary] = None
    web_url: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        if self.aliases is None:
            aliases = None
        else:
            aliases = self.aliases

        created_at = self.created_at.isoformat() if self.created_at else None

        creator = self.creator.to_dict() if self.creator else None

        if self.authors is None:
            authors = None
        else:
            authors = []
            for authors_item_data in self.authors:
                authors_item = authors_item_data.to_dict()

                authors.append(authors_item)

        custom_fields = self.custom_fields
        entity_registry_id = self.entity_registry_id
        fields = self.fields
        folder_id = self.folder_id
        id = self.id
        modified_at = self.modified_at.isoformat() if self.modified_at else None

        name = self.name
        registry_id = self.registry_id
        schema = self.schema.to_dict() if self.schema else None

        web_url = self.web_url

        return {
            "aliases": aliases,
            "createdAt": created_at,
            "creator": creator,
            "authors": authors,
            "customFields": custom_fields,
            "entityRegistryId": entity_registry_id,
            "fields": fields,
            "folderId": folder_id,
            "id": id,
            "modifiedAt": modified_at,
            "name": name,
            "registryId": registry_id,
            "schema": schema,
            "webURL": web_url,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> CustomEntityResponse:
        aliases = d.get("aliases")

        created_at = None
        if d.get("createdAt") is not None:
            created_at = datetime.fromisoformat(cast(str, d.get("createdAt")))

        creator = None
        if d.get("creator") is not None:
            creator = User.from_dict(cast(Dict[str, Any], d.get("creator")))

        authors = []
        for authors_item_data in d.get("authors") or []:
            authors_item = User.from_dict(authors_item_data)

            authors.append(authors_item)

        custom_fields = d.get("customFields")

        entity_registry_id = d.get("entityRegistryId")

        fields = d.get("fields")

        folder_id = d.get("folderId")

        id = d.get("id")

        modified_at = None
        if d.get("modifiedAt") is not None:
            modified_at = datetime.fromisoformat(cast(str, d.get("modifiedAt")))

        name = d.get("name")

        registry_id = d.get("registryId")

        schema = None
        if d.get("schema") is not None:
            schema = SchemaSummary.from_dict(cast(Dict[str, Any], d.get("schema")))

        web_url = d.get("webURL")

        return CustomEntityResponse(
            aliases=aliases,
            created_at=created_at,
            creator=creator,
            authors=authors,
            custom_fields=custom_fields,
            entity_registry_id=entity_registry_id,
            fields=fields,
            folder_id=folder_id,
            id=id,
            modified_at=modified_at,
            name=name,
            registry_id=registry_id,
            schema=schema,
            web_url=web_url,
        )
