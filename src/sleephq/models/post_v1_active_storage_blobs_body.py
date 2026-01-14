from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostV1ActiveStorageBlobsBody")


@_attrs_define
class PostV1ActiveStorageBlobsBody:
    """
    Attributes:
        blobfilename (str): The name of the file including extension.
        blobcontent_type (str): The content type of the file.
        blobbyte_size (int): The size of the file in bytes.
        blobchecksum (str): The base64 encoded MD5 checksum of the file.
    """

    blobfilename: str
    blobcontent_type: str
    blobbyte_size: int
    blobchecksum: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blobfilename = self.blobfilename

        blobcontent_type = self.blobcontent_type

        blobbyte_size = self.blobbyte_size

        blobchecksum = self.blobchecksum

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blob[filename]": blobfilename,
                "blob[content_type]": blobcontent_type,
                "blob[byte_size]": blobbyte_size,
                "blob[checksum]": blobchecksum,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        blobfilename = d.pop("blob[filename]")

        blobcontent_type = d.pop("blob[content_type]")

        blobbyte_size = d.pop("blob[byte_size]")

        blobchecksum = d.pop("blob[checksum]")

        post_v1_active_storage_blobs_body = cls(
            blobfilename=blobfilename,
            blobcontent_type=blobcontent_type,
            blobbyte_size=blobbyte_size,
            blobchecksum=blobchecksum,
        )

        post_v1_active_storage_blobs_body.additional_properties = d
        return post_v1_active_storage_blobs_body

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
