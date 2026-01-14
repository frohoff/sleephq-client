from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_user_serializer_data import ApiV1UserSerializerData


T = TypeVar("T", bound="ApiV1UserSerializer")


@_attrs_define
class ApiV1UserSerializer:
    """Api_V1_UserSerializer model

    Attributes:
        data (ApiV1UserSerializerData | Unset):  Example: {'id': 1, 'type': 'user', 'attributes': {'id': 6533609108,
            'email': 'assumenda', 'name': 'ipsam', 'first_name': 'sit', 'last_name': 'pariatur', 'time_zone': 'quo',
            'created_at': '2026-01-14 17:45:11 UTC', 'updated_at': '2026-01-14 17:45:11 UTC'}, 'relationships': {'teams':
            {'data': [{'id': 1, 'type': 'teams'}]}, 'memberships': {'data': [{'id': 1, 'type': 'memberships'}]}}}.
    """

    data: ApiV1UserSerializerData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_user_serializer_data import ApiV1UserSerializerData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ApiV1UserSerializerData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ApiV1UserSerializerData.from_dict(_data)

        api_v1_user_serializer = cls(
            data=data,
        )

        api_v1_user_serializer.additional_properties = d
        return api_v1_user_serializer

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
