from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_imports_file_serializer_data import ApiV1ImportsFileSerializerData


T = TypeVar("T", bound="ApiV1ImportsFileSerializer")


@_attrs_define
class ApiV1ImportsFileSerializer:
    """Api_V1_Imports_FileSerializer model

    Attributes:
        data (ApiV1ImportsFileSerializerData | Unset):  Example: {'id': 1, 'type': 'imports/file', 'attributes': {'id':
            3962487332, 'added_by_id': 5953729021, 'added_by_type': 'incidunt', 'content_hash': 'architecto', 'team_id':
            3036896523, 'name': 'et', 'path': 'consequatur', 'size': 1050657894, 'fingerprint_base64': 'officiis',
            'created_at': '2026-01-14 17:45:11 UTC', 'updated_at': '2026-01-14 17:45:11 UTC', 'download_url': 'ut'},
            'relationships': {}}.
    """

    data: ApiV1ImportsFileSerializerData | Unset = UNSET
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
        from ..models.api_v1_imports_file_serializer_data import ApiV1ImportsFileSerializerData

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: ApiV1ImportsFileSerializerData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ApiV1ImportsFileSerializerData.from_dict(_data)

        api_v1_imports_file_serializer = cls(
            data=data,
        )

        api_v1_imports_file_serializer.additional_properties = d
        return api_v1_imports_file_serializer

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
