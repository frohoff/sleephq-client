from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_import_serializer_list_data_item_attributes import ApiV1ImportSerializerListDataItemAttributes
    from ..models.api_v1_import_serializer_list_data_item_relationships import (
        ApiV1ImportSerializerListDataItemRelationships,
    )


T = TypeVar("T", bound="ApiV1ImportSerializerListDataItem")


@_attrs_define
class ApiV1ImportSerializerListDataItem:
    """
    Example:
        {'id': 1, 'type': 'import', 'attributes': {'id': 3105916631, 'team_id': 7164259566, 'name': 'quisquam',
            'status': 6568117209, 'file_size': 6441812089, 'progress': 1834086593, 'machine_id': 8907446003, 'device_id':
            6002934309, 'programatic': False, 'failed_reason': 'et', 'created_at': '2026-01-14 17:45:11 UTC', 'updated_at':
            '2026-01-14 17:45:11 UTC'}, 'relationships': {'files': {'data': [{'id': 1, 'type': 'files'}]}}}

    Attributes:
        id (str | Unset):
        type_ (str | Unset):
        attributes (ApiV1ImportSerializerListDataItemAttributes | Unset):
        relationships (ApiV1ImportSerializerListDataItemRelationships | Unset):
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    attributes: ApiV1ImportSerializerListDataItemAttributes | Unset = UNSET
    relationships: ApiV1ImportSerializerListDataItemRelationships | Unset = UNSET
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
        from ..models.api_v1_import_serializer_list_data_item_attributes import (
            ApiV1ImportSerializerListDataItemAttributes,
        )
        from ..models.api_v1_import_serializer_list_data_item_relationships import (
            ApiV1ImportSerializerListDataItemRelationships,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: ApiV1ImportSerializerListDataItemAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ApiV1ImportSerializerListDataItemAttributes.from_dict(_attributes)

        _relationships = d.pop("relationships", UNSET)
        relationships: ApiV1ImportSerializerListDataItemRelationships | Unset
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = ApiV1ImportSerializerListDataItemRelationships.from_dict(_relationships)

        api_v1_import_serializer_list_data_item = cls(
            id=id,
            type_=type_,
            attributes=attributes,
            relationships=relationships,
        )

        api_v1_import_serializer_list_data_item.additional_properties = d
        return api_v1_import_serializer_list_data_item

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
