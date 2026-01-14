from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiV1TeamSerializerDataAttributes")


@_attrs_define
class ApiV1TeamSerializerDataAttributes:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        owner_id (int | Unset):
        time_zone (str | Unset):
        locale (str | Unset):
        energy_unit (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        teams_type (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    owner_id: int | Unset = UNSET
    time_zone: str | Unset = UNSET
    locale: str | Unset = UNSET
    energy_unit: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    teams_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        owner_id = self.owner_id

        time_zone = self.time_zone

        locale = self.locale

        energy_unit = self.energy_unit

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        teams_type = self.teams_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if locale is not UNSET:
            field_dict["locale"] = locale
        if energy_unit is not UNSET:
            field_dict["energy_unit"] = energy_unit
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if teams_type is not UNSET:
            field_dict["teams_type"] = teams_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        time_zone = d.pop("time_zone", UNSET)

        locale = d.pop("locale", UNSET)

        energy_unit = d.pop("energy_unit", UNSET)

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

        teams_type = d.pop("teams_type", UNSET)

        api_v1_team_serializer_data_attributes = cls(
            id=id,
            name=name,
            owner_id=owner_id,
            time_zone=time_zone,
            locale=locale,
            energy_unit=energy_unit,
            created_at=created_at,
            updated_at=updated_at,
            teams_type=teams_type,
        )

        api_v1_team_serializer_data_attributes.additional_properties = d
        return api_v1_team_serializer_data_attributes

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
