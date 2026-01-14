from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiV1ImportsFileSerializerListDataItemAttributes")


@_attrs_define
class ApiV1ImportsFileSerializerListDataItemAttributes:
    """
    Attributes:
        id (int | Unset):
        added_by_id (int | Unset):
        added_by_type (str | Unset):
        content_hash (str | Unset):
        team_id (int | Unset):
        name (str | Unset):
        path (str | Unset):
        size (int | Unset):
        fingerprint_base64 (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        download_url (str | Unset):
    """

    id: int | Unset = UNSET
    added_by_id: int | Unset = UNSET
    added_by_type: str | Unset = UNSET
    content_hash: str | Unset = UNSET
    team_id: int | Unset = UNSET
    name: str | Unset = UNSET
    path: str | Unset = UNSET
    size: int | Unset = UNSET
    fingerprint_base64: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    download_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        added_by_id = self.added_by_id

        added_by_type = self.added_by_type

        content_hash = self.content_hash

        team_id = self.team_id

        name = self.name

        path = self.path

        size = self.size

        fingerprint_base64 = self.fingerprint_base64

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        download_url = self.download_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if added_by_id is not UNSET:
            field_dict["added_by_id"] = added_by_id
        if added_by_type is not UNSET:
            field_dict["added_by_type"] = added_by_type
        if content_hash is not UNSET:
            field_dict["content_hash"] = content_hash
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if size is not UNSET:
            field_dict["size"] = size
        if fingerprint_base64 is not UNSET:
            field_dict["fingerprint_base64"] = fingerprint_base64
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if download_url is not UNSET:
            field_dict["download_url"] = download_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        added_by_id = d.pop("added_by_id", UNSET)

        added_by_type = d.pop("added_by_type", UNSET)

        content_hash = d.pop("content_hash", UNSET)

        team_id = d.pop("team_id", UNSET)

        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        size = d.pop("size", UNSET)

        fingerprint_base64 = d.pop("fingerprint_base64", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        download_url = d.pop("download_url", UNSET)

        api_v1_imports_file_serializer_list_data_item_attributes = cls(
            id=id,
            added_by_id=added_by_id,
            added_by_type=added_by_type,
            content_hash=content_hash,
            team_id=team_id,
            name=name,
            path=path,
            size=size,
            fingerprint_base64=fingerprint_base64,
            created_at=created_at,
            updated_at=updated_at,
            download_url=download_url,
        )

        api_v1_imports_file_serializer_list_data_item_attributes.additional_properties = d
        return api_v1_imports_file_serializer_list_data_item_attributes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
