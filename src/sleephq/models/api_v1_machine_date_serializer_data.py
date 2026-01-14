from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_machine_date_serializer_data_attributes import ApiV1MachineDateSerializerDataAttributes
    from ..models.api_v1_machine_date_serializer_data_relationships import ApiV1MachineDateSerializerDataRelationships


T = TypeVar("T", bound="ApiV1MachineDateSerializerData")


@_attrs_define
class ApiV1MachineDateSerializerData:
    """
    Example:
        {'id': 1, 'type': 'machine_date', 'attributes': {'id': 8476664143, 'usage': 'voluptatem', 'machine_id':
            5466645897, 'date': '2026-01-14', 'time_offset': 8164298296, 'created_at': '2026-01-14 17:45:11 UTC',
            'updated_at': '2026-01-14 17:45:11 UTC', 'large_leak': 1603233526, 'ahi_summary': 'autem', 'pressure_summary':
            'temporibus', 'leak_rate_summary': 'sed', 'flow_limit_summary': 'nulla', 'resp_rate_summary': 'sit',
            'epap_summary': 'sunt', 'machine_settings': 'modi', 'pulse_rate_summary': 'et', 'spo2_summary': 'accusamus',
            'movement_summary': 'quidem'}, 'relationships': {}}

    Attributes:
        id (str | Unset):
        type_ (str | Unset):
        attributes (ApiV1MachineDateSerializerDataAttributes | Unset):
        relationships (ApiV1MachineDateSerializerDataRelationships | Unset):
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    attributes: ApiV1MachineDateSerializerDataAttributes | Unset = UNSET
    relationships: ApiV1MachineDateSerializerDataRelationships | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_machine_date_serializer_data_attributes import ApiV1MachineDateSerializerDataAttributes
        from ..models.api_v1_machine_date_serializer_data_relationships import (
            ApiV1MachineDateSerializerDataRelationships,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: ApiV1MachineDateSerializerDataAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ApiV1MachineDateSerializerDataAttributes.from_dict(_attributes)

        _relationships = d.pop("relationships", UNSET)
        relationships: ApiV1MachineDateSerializerDataRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = ApiV1MachineDateSerializerDataRelationships.from_dict(_relationships)

        api_v1_machine_date_serializer_data = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )

        api_v1_machine_date_serializer_data.additional_properties = d
        return api_v1_machine_date_serializer_data

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
