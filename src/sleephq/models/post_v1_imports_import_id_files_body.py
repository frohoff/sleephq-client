from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostV1ImportsImportIdFilesBody")


@_attrs_define
class PostV1ImportsImportIdFilesBody:
    """
    Attributes:
        name (str): The name of the file Example: STR.edf.
        path (str): The path to the file relative to the SD card root. Example: "./" for a file that is at the root.
            "./DATALOG/20230924/" for a file in a DATALOG folder. Note do not include the quote marks (").
        content_hash (str): The calculated content_hash of the file. See the /v1/imports/files/calculate_content_hash
            endpoint for more information Example: d41d8cd98f00b204e9800998ecf8427e.
        file (File | Unset): The file object. Optional if the file has already been uploaded.
    """

    name: str
    path: str
    content_hash: str
    file: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        content_hash = self.content_hash

        file: FileTypes | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "path": path,
                "content_hash": content_hash,
            }
        )
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("path", (None, str(self.path).encode(), "text/plain")))

        files.append(("content_hash", (None, str(self.content_hash).encode(), "text/plain")))

        if not isinstance(self.file, Unset):
            files.append(("file", self.file.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        content_hash = d.pop("content_hash")

        _file = d.pop("file", UNSET)
        file: File | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = File(payload=BytesIO(_file))

        post_v1_imports_import_id_files_body = cls(
            name=name,
            path=path,
            content_hash=content_hash,
            file=file,
        )

        post_v1_imports_import_id_files_body.additional_properties = d
        return post_v1_imports_import_id_files_body

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
