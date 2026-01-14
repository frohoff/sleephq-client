from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiV1DeviceSerializerListDataItemAttributes")


@_attrs_define
class ApiV1DeviceSerializerListDataItemAttributes:
    """
    Attributes:
        id (int | Unset):
        name (str | Unset):
        brand (str | Unset):
        device_type (str | Unset):
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    brand: str | Unset = UNSET
    device_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        brand = self.brand

        device_type = self.device_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if brand is not UNSET:
            field_dict["brand"] = brand
        if device_type is not UNSET:
            field_dict["device_type"] = device_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        brand = d.pop("brand", UNSET)

        device_type = d.pop("device_type", UNSET)

        api_v1_device_serializer_list_data_item_attributes = cls(
            id=id,
            name=name,
            brand=brand,
            device_type=device_type,
        )

        api_v1_device_serializer_list_data_item_attributes.additional_properties = d
        return api_v1_device_serializer_list_data_item_attributes

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
