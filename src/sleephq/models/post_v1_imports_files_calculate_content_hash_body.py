from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

T = TypeVar("T", bound="PostV1ImportsFilesCalculateContentHashBody")


@_attrs_define
class PostV1ImportsFilesCalculateContentHashBody:
    """
    Attributes:
        name (str): The name of the file
        file (File): The file to calculate the content hash for
    """

    name: str
    file: File
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "file": file,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        file = File(payload=BytesIO(d.pop("file")))

        post_v1_imports_files_calculate_content_hash_body = cls(
            name=name,
            file=file,
        )

        post_v1_imports_files_calculate_content_hash_body.additional_properties = d
        return post_v1_imports_files_calculate_content_hash_body

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
