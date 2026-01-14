from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_import_serializer_data_relationships_files import ApiV1ImportSerializerDataRelationshipsFiles


T = TypeVar("T", bound="ApiV1ImportSerializerDataRelationships")


@_attrs_define
class ApiV1ImportSerializerDataRelationships:
    """
    Attributes:
        files (ApiV1ImportSerializerDataRelationshipsFiles | Unset):
    """

    files: ApiV1ImportSerializerDataRelationshipsFiles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_import_serializer_data_relationships_files import (
            ApiV1ImportSerializerDataRelationshipsFiles,
        )

        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: ApiV1ImportSerializerDataRelationshipsFiles | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = ApiV1ImportSerializerDataRelationshipsFiles.from_dict(_files)

        api_v1_import_serializer_data_relationships = cls(
            files=files,
        )

        api_v1_import_serializer_data_relationships.additional_properties = d
        return api_v1_import_serializer_data_relationships

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
