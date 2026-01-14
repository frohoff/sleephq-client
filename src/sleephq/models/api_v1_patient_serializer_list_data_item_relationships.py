from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_patient_serializer_list_data_item_relationships_machines import (
        ApiV1PatientSerializerListDataItemRelationshipsMachines,
    )


T = TypeVar("T", bound="ApiV1PatientSerializerListDataItemRelationships")


@_attrs_define
class ApiV1PatientSerializerListDataItemRelationships:
    """
    Attributes:
        machines (ApiV1PatientSerializerListDataItemRelationshipsMachines | Unset):
    """

    machines: ApiV1PatientSerializerListDataItemRelationshipsMachines | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        machines: dict[str, Any] | Unset = UNSET
        if not isinstance(self.machines, Unset):
            machines = self.machines.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if machines is not UNSET:
            field_dict["machines"] = machines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_patient_serializer_list_data_item_relationships_machines import (
            ApiV1PatientSerializerListDataItemRelationshipsMachines,
        )

        d = dict(src_dict)
        _machines = d.pop("machines", UNSET)
        machines: ApiV1PatientSerializerListDataItemRelationshipsMachines | Unset
        if isinstance(_machines, Unset):
            machines = UNSET
        else:
            machines = ApiV1PatientSerializerListDataItemRelationshipsMachines.from_dict(_machines)

        api_v1_patient_serializer_list_data_item_relationships = cls(
            machines=machines,
        )

        api_v1_patient_serializer_list_data_item_relationships.additional_properties = d
        return api_v1_patient_serializer_list_data_item_relationships

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
