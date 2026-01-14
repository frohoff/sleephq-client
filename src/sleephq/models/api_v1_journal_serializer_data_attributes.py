from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiV1JournalSerializerDataAttributes")


@_attrs_define
class ApiV1JournalSerializerDataAttributes:
    """
    Attributes:
        id (int | Unset):
        team_id (int | Unset):
        date (datetime.date | Unset):
        step_count (int | Unset):
        weight_grams (int | Unset):
        feeling_score (int | Unset):
        sleep_stages (str | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        notes (str | Unset):
    """

    id: int | Unset = UNSET
    team_id: int | Unset = UNSET
    date: datetime.date | Unset = UNSET
    step_count: int | Unset = UNSET
    weight_grams: int | Unset = UNSET
    feeling_score: int | Unset = UNSET
    sleep_stages: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        team_id = self.team_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        step_count = self.step_count

        weight_grams = self.weight_grams

        feeling_score = self.feeling_score

        sleep_stages = self.sleep_stages

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if date is not UNSET:
            field_dict["date"] = date
        if step_count is not UNSET:
            field_dict["step_count"] = step_count
        if weight_grams is not UNSET:
            field_dict["weight_grams"] = weight_grams
        if feeling_score is not UNSET:
            field_dict["feeling_score"] = feeling_score
        if sleep_stages is not UNSET:
            field_dict["sleep_stages"] = sleep_stages
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        team_id = d.pop("team_id", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        step_count = d.pop("step_count", UNSET)

        weight_grams = d.pop("weight_grams", UNSET)

        feeling_score = d.pop("feeling_score", UNSET)

        sleep_stages = d.pop("sleep_stages", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        notes = d.pop("notes", UNSET)

        api_v1_journal_serializer_data_attributes = cls(
            id=id,
            team_id=team_id,
            date=date,
            step_count=step_count,
            weight_grams=weight_grams,
            feeling_score=feeling_score,
            sleep_stages=sleep_stages,
            created_at=created_at,
            updated_at=updated_at,
            notes=notes,
        )

        api_v1_journal_serializer_data_attributes.additional_properties = d
        return api_v1_journal_serializer_data_attributes

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
