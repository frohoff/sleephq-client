from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1TeamsTeamIdJournalsBody")


@_attrs_define
class PostV1TeamsTeamIdJournalsBody:
    """
    Attributes:
        date (datetime.date | Unset): Date
        step_count (str | Unset): Step Count
        weight_grams (int | Unset): Weight (Grams)
        feeling_score (str | Unset): Feeling Score
        active_energy_joules (int | Unset): Active Energy (Joules)
        notes (str | Unset): Notes
        sleep_stages (str | Unset): Sleep Stages
    """

    date: datetime.date | Unset = UNSET
    step_count: str | Unset = UNSET
    weight_grams: int | Unset = UNSET
    feeling_score: str | Unset = UNSET
    active_energy_joules: int | Unset = UNSET
    notes: str | Unset = UNSET
    sleep_stages: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        step_count = self.step_count

        weight_grams = self.weight_grams

        feeling_score = self.feeling_score

        active_energy_joules = self.active_energy_joules

        notes = self.notes

        sleep_stages = self.sleep_stages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if step_count is not UNSET:
            field_dict["step_count"] = step_count
        if weight_grams is not UNSET:
            field_dict["weight_grams"] = weight_grams
        if feeling_score is not UNSET:
            field_dict["feeling_score"] = feeling_score
        if active_energy_joules is not UNSET:
            field_dict["active_energy_joules"] = active_energy_joules
        if notes is not UNSET:
            field_dict["notes"] = notes
        if sleep_stages is not UNSET:
            field_dict["sleep_stages"] = sleep_stages

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.date, Unset):
            files.append(("date", (None, self.date.isoformat().encode(), "text/plain")))

        if not isinstance(self.step_count, Unset):
            files.append(("step_count", (None, str(self.step_count).encode(), "text/plain")))

        if not isinstance(self.weight_grams, Unset):
            files.append(("weight_grams", (None, str(self.weight_grams).encode(), "text/plain")))

        if not isinstance(self.feeling_score, Unset):
            files.append(("feeling_score", (None, str(self.feeling_score).encode(), "text/plain")))

        if not isinstance(self.active_energy_joules, Unset):
            files.append(("active_energy_joules", (None, str(self.active_energy_joules).encode(), "text/plain")))

        if not isinstance(self.notes, Unset):
            files.append(("notes", (None, str(self.notes).encode(), "text/plain")))

        if not isinstance(self.sleep_stages, Unset):
            files.append(("sleep_stages", (None, str(self.sleep_stages).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        step_count = d.pop("step_count", UNSET)

        weight_grams = d.pop("weight_grams", UNSET)

        feeling_score = d.pop("feeling_score", UNSET)

        active_energy_joules = d.pop("active_energy_joules", UNSET)

        notes = d.pop("notes", UNSET)

        sleep_stages = d.pop("sleep_stages", UNSET)

        post_v1_teams_team_id_journals_body = cls(
            date=date,
            step_count=step_count,
            weight_grams=weight_grams,
            feeling_score=feeling_score,
            active_energy_joules=active_energy_joules,
            notes=notes,
            sleep_stages=sleep_stages,
        )

        post_v1_teams_team_id_journals_body.additional_properties = d
        return post_v1_teams_team_id_journals_body

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
