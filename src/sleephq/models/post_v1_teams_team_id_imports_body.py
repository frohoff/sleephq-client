from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1TeamsTeamIdImportsBody")


@_attrs_define
class PostV1TeamsTeamIdImportsBody:
    """
    Attributes:
        programatic (bool | Unset): Deprecated.
        device_id (int | Unset): The device type that the data is from. Find a list of device ids using the /devices
            endpoint.
        name (str | Unset): The name of the import to show in the UI.
    """

    programatic: bool | Unset = UNSET
    device_id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        programatic = self.programatic

        device_id = self.device_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if programatic is not UNSET:
            field_dict["programatic"] = programatic
        if device_id is not UNSET:
            field_dict["device_id"] = device_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.programatic, Unset):
            files.append(("programatic", (None, str(self.programatic).encode(), "text/plain")))

        if not isinstance(self.device_id, Unset):
            files.append(("device_id", (None, str(self.device_id).encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        programatic = d.pop("programatic", UNSET)

        device_id = d.pop("device_id", UNSET)

        name = d.pop("name", UNSET)

        post_v1_teams_team_id_imports_body = cls(
            programatic=programatic,
            device_id=device_id,
            name=name,
        )

        post_v1_teams_team_id_imports_body.additional_properties = d
        return post_v1_teams_team_id_imports_body

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
