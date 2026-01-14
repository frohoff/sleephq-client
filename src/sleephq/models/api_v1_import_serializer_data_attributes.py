from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiV1ImportSerializerDataAttributes")


@_attrs_define
class ApiV1ImportSerializerDataAttributes:
    """
    Attributes:
        id (int | Unset):
        team_id (int | Unset):
        name (str | Unset):
        status (str | Unset):
        file_size (int | Unset):
        progress (int | Unset):
        machine_id (int | Unset):
        device_id (int | Unset):
        programatic (bool | Unset):
        failed_reason (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    team_id: int | Unset = UNSET
    name: str | Unset = UNSET
    status: str | Unset = UNSET
    file_size: int | Unset = UNSET
    progress: int | Unset = UNSET
    machine_id: int | Unset = UNSET
    device_id: int | Unset = UNSET
    programatic: bool | Unset = UNSET
    failed_reason: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        name = self.name

        status = self.status

        file_size = self.file_size

        progress = self.progress

        machine_id = self.machine_id

        device_id = self.device_id

        programatic = self.programatic

        failed_reason = self.failed_reason

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if progress is not UNSET:
            field_dict["progress"] = progress
        if machine_id is not UNSET:
            field_dict["machine_id"] = machine_id
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if programatic is not UNSET:
            field_dict["programatic"] = programatic
        if failed_reason is not UNSET:
            field_dict["failed_reason"] = failed_reason
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        team_id = d.pop("team_id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        file_size = d.pop("file_size", UNSET)

        progress = d.pop("progress", UNSET)

        machine_id = d.pop("machine_id", UNSET)

        device_id = d.pop("device_id", UNSET)

        programatic = d.pop("programatic", UNSET)

        failed_reason = d.pop("failed_reason", UNSET)

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

        api_v1_import_serializer_data_attributes = cls(
            id=id,
            team_id=team_id,
            name=name,
            status=status,
            file_size=file_size,
            progress=progress,
            machine_id=machine_id,
            device_id=device_id,
            programatic=programatic,
            failed_reason=failed_reason,
            created_at=created_at,
            updated_at=updated_at,
        )

        api_v1_import_serializer_data_attributes.additional_properties = d
        return api_v1_import_serializer_data_attributes

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
