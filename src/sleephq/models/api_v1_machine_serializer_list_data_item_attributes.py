from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiV1MachineSerializerListDataItemAttributes")


@_attrs_define
class ApiV1MachineSerializerListDataItemAttributes:
    """
    Attributes:
        id (int | Unset):
        team_id (int | Unset):
        model (str | Unset):
        brand (str | Unset):
        serial_number (str | Unset):
        name (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
    """

    id: int | Unset = UNSET
    team_id: int | Unset = UNSET
    model: str | Unset = UNSET
    brand: str | Unset = UNSET
    serial_number: str | Unset = UNSET
    name: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        model = self.model

        brand = self.brand

        serial_number = self.serial_number

        name = self.name

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
        if model is not UNSET:
            field_dict["model"] = model
        if brand is not UNSET:
            field_dict["brand"] = brand
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if name is not UNSET:
            field_dict["name"] = name
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

        model = d.pop("model", UNSET)

        brand = d.pop("brand", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        name = d.pop("name", UNSET)

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

        api_v1_machine_serializer_list_data_item_attributes = cls(
            id=id,
            team_id=team_id,
            model=model,
            brand=brand,
            serial_number=serial_number,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
        )

        api_v1_machine_serializer_list_data_item_attributes.additional_properties = d
        return api_v1_machine_serializer_list_data_item_attributes

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
