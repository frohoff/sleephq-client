from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_user_serializer_data_relationships_memberships import (
        ApiV1UserSerializerDataRelationshipsMemberships,
    )
    from ..models.api_v1_user_serializer_data_relationships_teams import ApiV1UserSerializerDataRelationshipsTeams


T = TypeVar("T", bound="ApiV1UserSerializerDataRelationships")


@_attrs_define
class ApiV1UserSerializerDataRelationships:
    """
    Attributes:
        teams (ApiV1UserSerializerDataRelationshipsTeams | Unset):
        memberships (ApiV1UserSerializerDataRelationshipsMemberships | Unset):
    """

    teams: ApiV1UserSerializerDataRelationshipsTeams | Unset = UNSET
    memberships: ApiV1UserSerializerDataRelationshipsMemberships | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        teams: dict[str, Any] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams.to_dict()

        memberships: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = self.memberships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if teams is not UNSET:
            field_dict["teams"] = teams
        if memberships is not UNSET:
            field_dict["memberships"] = memberships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_user_serializer_data_relationships_memberships import (
            ApiV1UserSerializerDataRelationshipsMemberships,
        )
        from ..models.api_v1_user_serializer_data_relationships_teams import ApiV1UserSerializerDataRelationshipsTeams

        d = dict(src_dict)
        _teams = d.pop("teams", UNSET)
        teams: ApiV1UserSerializerDataRelationshipsTeams | Unset
        if isinstance(_teams, Unset):
            teams = UNSET
        else:
            teams = ApiV1UserSerializerDataRelationshipsTeams.from_dict(_teams)

        _memberships = d.pop("memberships", UNSET)
        memberships: ApiV1UserSerializerDataRelationshipsMemberships | Unset
        if isinstance(_memberships, Unset):
            memberships = UNSET
        else:
            memberships = ApiV1UserSerializerDataRelationshipsMemberships.from_dict(_memberships)

        api_v1_user_serializer_data_relationships = cls(
            teams=teams,
            memberships=memberships,
        )

        api_v1_user_serializer_data_relationships.additional_properties = d
        return api_v1_user_serializer_data_relationships

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
