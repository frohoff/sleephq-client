from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_import_serializer_data import ApiV1ImportSerializerData


T = TypeVar("T", bound="ApiV1ImportSerializer")


@_attrs_define
class ApiV1ImportSerializer:
    """Api_V1_ImportSerializer model

    Attributes:
        data (ApiV1ImportSerializerData | Unset):  Example: {'id': 1, 'type': 'import', 'attributes': {'id': 3105916631,
            'team_id': 7164259566, 'name': 'quisquam', 'status': 6568117209, 'file_size': 6441812089, 'progress':
            1834086593, 'machine_id': 8907446003, 'device_id': 6002934309, 'programatic': False, 'failed_reason': 'et',
            'created_at': '2026-01-14 17:45:11 UTC', 'updated_at': '2026-01-14 17:45:11 UTC'}, 'relationships': {'files':
            {'data': [{'id': 1, 'type': 'files'}]}}}.
    """

    data: ApiV1ImportSerializerData | Unset = UNSET
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
        from ..models.api_v1_import_serializer_data import ApiV1ImportSerializerData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ApiV1ImportSerializerData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ApiV1ImportSerializerData.from_dict(_data)

        api_v1_import_serializer = cls(
            data=data,
        )

        api_v1_import_serializer.additional_properties = d
        return api_v1_import_serializer

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
