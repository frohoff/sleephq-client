from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_v1_machine_date_serializer_data_attributes_ahi_summary import (
        ApiV1MachineDateSerializerDataAttributesAhiSummary,
    )
    from ..models.api_v1_machine_date_serializer_data_attributes_epap_summary import (
        ApiV1MachineDateSerializerDataAttributesEpapSummary,
    )
    from ..models.api_v1_machine_date_serializer_data_attributes_flow_limit_summary import (
        ApiV1MachineDateSerializerDataAttributesFlowLimitSummary,
    )
    from ..models.api_v1_machine_date_serializer_data_attributes_leak_rate_summary import (
        ApiV1MachineDateSerializerDataAttributesLeakRateSummary,
    )
    from ..models.api_v1_machine_date_serializer_data_attributes_machine_settings import (
        ApiV1MachineDateSerializerDataAttributesMachineSettings,
    )
    from ..models.api_v1_machine_date_serializer_data_attributes_movement_summary import (
        ApiV1MachineDateSerializerDataAttributesMovementSummary,
    )
    from ..models.api_v1_machine_date_serializer_data_attributes_pressure_summary import (
        ApiV1MachineDateSerializerDataAttributesPressureSummary,
    )
    from ..models.api_v1_machine_date_serializer_data_attributes_pulse_rate_summary import (
        ApiV1MachineDateSerializerDataAttributesPulseRateSummary,
    )
    from ..models.api_v1_machine_date_serializer_data_attributes_resp_rate_summary import (
        ApiV1MachineDateSerializerDataAttributesRespRateSummary,
    )
    from ..models.api_v1_machine_date_serializer_data_attributes_spo_2_summary import (
        ApiV1MachineDateSerializerDataAttributesSpo2Summary,
    )


T = TypeVar("T", bound="ApiV1MachineDateSerializerDataAttributes")


@_attrs_define
class ApiV1MachineDateSerializerDataAttributes:
    """
    Attributes:
        id (int | Unset):
        usage (int | Unset):
        machine_id (int | Unset):
        date (datetime.date | Unset):
        time_offset (int | Unset):
        created_at (datetime.datetime | Unset):
        updated_at (datetime.datetime | Unset):
        large_leak (int | Unset):
        ahi_summary (ApiV1MachineDateSerializerDataAttributesAhiSummary | Unset):
        pressure_summary (ApiV1MachineDateSerializerDataAttributesPressureSummary | Unset):
        leak_rate_summary (ApiV1MachineDateSerializerDataAttributesLeakRateSummary | Unset):
        flow_limit_summary (ApiV1MachineDateSerializerDataAttributesFlowLimitSummary | Unset):
        resp_rate_summary (ApiV1MachineDateSerializerDataAttributesRespRateSummary | Unset):
        epap_summary (ApiV1MachineDateSerializerDataAttributesEpapSummary | Unset):
        machine_settings (ApiV1MachineDateSerializerDataAttributesMachineSettings | Unset):
        pulse_rate_summary (ApiV1MachineDateSerializerDataAttributesPulseRateSummary | Unset):
        spo2_summary (ApiV1MachineDateSerializerDataAttributesSpo2Summary | Unset):
        movement_summary (ApiV1MachineDateSerializerDataAttributesMovementSummary | Unset):
    """

    id: int | Unset = UNSET
    usage: int | Unset = UNSET
    machine_id: int | Unset = UNSET
    date: datetime.date | Unset = UNSET
    time_offset: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    large_leak: int | Unset = UNSET
    ahi_summary: ApiV1MachineDateSerializerDataAttributesAhiSummary | Unset = UNSET
    pressure_summary: ApiV1MachineDateSerializerDataAttributesPressureSummary | Unset = UNSET
    leak_rate_summary: ApiV1MachineDateSerializerDataAttributesLeakRateSummary | Unset = UNSET
    flow_limit_summary: ApiV1MachineDateSerializerDataAttributesFlowLimitSummary | Unset = UNSET
    resp_rate_summary: ApiV1MachineDateSerializerDataAttributesRespRateSummary | Unset = UNSET
    epap_summary: ApiV1MachineDateSerializerDataAttributesEpapSummary | Unset = UNSET
    machine_settings: ApiV1MachineDateSerializerDataAttributesMachineSettings | Unset = UNSET
    pulse_rate_summary: ApiV1MachineDateSerializerDataAttributesPulseRateSummary | Unset = UNSET
    spo2_summary: ApiV1MachineDateSerializerDataAttributesSpo2Summary | Unset = UNSET
    movement_summary: ApiV1MachineDateSerializerDataAttributesMovementSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        usage = self.usage

        machine_id = self.machine_id

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        time_offset = self.time_offset

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        large_leak = self.large_leak

        ahi_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ahi_summary, Unset):
            ahi_summary = self.ahi_summary.to_dict()

        pressure_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pressure_summary, Unset):
            pressure_summary = self.pressure_summary.to_dict()

        leak_rate_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.leak_rate_summary, Unset):
            leak_rate_summary = self.leak_rate_summary.to_dict()

        flow_limit_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.flow_limit_summary, Unset):
            flow_limit_summary = self.flow_limit_summary.to_dict()

        resp_rate_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resp_rate_summary, Unset):
            resp_rate_summary = self.resp_rate_summary.to_dict()

        epap_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.epap_summary, Unset):
            epap_summary = self.epap_summary.to_dict()

        machine_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.machine_settings, Unset):
            machine_settings = self.machine_settings.to_dict()

        pulse_rate_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pulse_rate_summary, Unset):
            pulse_rate_summary = self.pulse_rate_summary.to_dict()

        spo2_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spo2_summary, Unset):
            spo2_summary = self.spo2_summary.to_dict()

        movement_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.movement_summary, Unset):
            movement_summary = self.movement_summary.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if usage is not UNSET:
            field_dict["usage"] = usage
        if machine_id is not UNSET:
            field_dict["machine_id"] = machine_id
        if date is not UNSET:
            field_dict["date"] = date
        if time_offset is not UNSET:
            field_dict["time_offset"] = time_offset
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if large_leak is not UNSET:
            field_dict["large_leak"] = large_leak
        if ahi_summary is not UNSET:
            field_dict["ahi_summary"] = ahi_summary
        if pressure_summary is not UNSET:
            field_dict["pressure_summary"] = pressure_summary
        if leak_rate_summary is not UNSET:
            field_dict["leak_rate_summary"] = leak_rate_summary
        if flow_limit_summary is not UNSET:
            field_dict["flow_limit_summary"] = flow_limit_summary
        if resp_rate_summary is not UNSET:
            field_dict["resp_rate_summary"] = resp_rate_summary
        if epap_summary is not UNSET:
            field_dict["epap_summary"] = epap_summary
        if machine_settings is not UNSET:
            field_dict["machine_settings"] = machine_settings
        if pulse_rate_summary is not UNSET:
            field_dict["pulse_rate_summary"] = pulse_rate_summary
        if spo2_summary is not UNSET:
            field_dict["spo2_summary"] = spo2_summary
        if movement_summary is not UNSET:
            field_dict["movement_summary"] = movement_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_machine_date_serializer_data_attributes_ahi_summary import (
            ApiV1MachineDateSerializerDataAttributesAhiSummary,
        )
        from ..models.api_v1_machine_date_serializer_data_attributes_epap_summary import (
            ApiV1MachineDateSerializerDataAttributesEpapSummary,
        )
        from ..models.api_v1_machine_date_serializer_data_attributes_flow_limit_summary import (
            ApiV1MachineDateSerializerDataAttributesFlowLimitSummary,
        )
        from ..models.api_v1_machine_date_serializer_data_attributes_leak_rate_summary import (
            ApiV1MachineDateSerializerDataAttributesLeakRateSummary,
        )
        from ..models.api_v1_machine_date_serializer_data_attributes_machine_settings import (
            ApiV1MachineDateSerializerDataAttributesMachineSettings,
        )
        from ..models.api_v1_machine_date_serializer_data_attributes_movement_summary import (
            ApiV1MachineDateSerializerDataAttributesMovementSummary,
        )
        from ..models.api_v1_machine_date_serializer_data_attributes_pressure_summary import (
            ApiV1MachineDateSerializerDataAttributesPressureSummary,
        )
        from ..models.api_v1_machine_date_serializer_data_attributes_pulse_rate_summary import (
            ApiV1MachineDateSerializerDataAttributesPulseRateSummary,
        )
        from ..models.api_v1_machine_date_serializer_data_attributes_resp_rate_summary import (
            ApiV1MachineDateSerializerDataAttributesRespRateSummary,
        )
        from ..models.api_v1_machine_date_serializer_data_attributes_spo_2_summary import (
            ApiV1MachineDateSerializerDataAttributesSpo2Summary,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        usage = d.pop("usage", UNSET)

        machine_id = d.pop("machine_id", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        time_offset = d.pop("time_offset", UNSET)

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

        large_leak = d.pop("large_leak", UNSET)

        _ahi_summary = d.pop("ahi_summary", UNSET)
        ahi_summary: ApiV1MachineDateSerializerDataAttributesAhiSummary | Unset
        if isinstance(_ahi_summary, Unset):
            ahi_summary = UNSET
        else:
            ahi_summary = ApiV1MachineDateSerializerDataAttributesAhiSummary.from_dict(_ahi_summary)

        _pressure_summary = d.pop("pressure_summary", UNSET)
        pressure_summary: ApiV1MachineDateSerializerDataAttributesPressureSummary | Unset
        if isinstance(_pressure_summary, Unset):
            pressure_summary = UNSET
        else:
            pressure_summary = ApiV1MachineDateSerializerDataAttributesPressureSummary.from_dict(_pressure_summary)

        _leak_rate_summary = d.pop("leak_rate_summary", UNSET)
        leak_rate_summary: ApiV1MachineDateSerializerDataAttributesLeakRateSummary | Unset
        if isinstance(_leak_rate_summary, Unset):
            leak_rate_summary = UNSET
        else:
            leak_rate_summary = ApiV1MachineDateSerializerDataAttributesLeakRateSummary.from_dict(_leak_rate_summary)

        _flow_limit_summary = d.pop("flow_limit_summary", UNSET)
        flow_limit_summary: ApiV1MachineDateSerializerDataAttributesFlowLimitSummary | Unset
        if isinstance(_flow_limit_summary, Unset):
            flow_limit_summary = UNSET
        else:
            flow_limit_summary = ApiV1MachineDateSerializerDataAttributesFlowLimitSummary.from_dict(_flow_limit_summary)

        _resp_rate_summary = d.pop("resp_rate_summary", UNSET)
        resp_rate_summary: ApiV1MachineDateSerializerDataAttributesRespRateSummary | Unset
        if isinstance(_resp_rate_summary, Unset):
            resp_rate_summary = UNSET
        else:
            resp_rate_summary = ApiV1MachineDateSerializerDataAttributesRespRateSummary.from_dict(_resp_rate_summary)

        _epap_summary = d.pop("epap_summary", UNSET)
        epap_summary: ApiV1MachineDateSerializerDataAttributesEpapSummary | Unset
        if isinstance(_epap_summary, Unset):
            epap_summary = UNSET
        else:
            epap_summary = ApiV1MachineDateSerializerDataAttributesEpapSummary.from_dict(_epap_summary)

        _machine_settings = d.pop("machine_settings", UNSET)
        machine_settings: ApiV1MachineDateSerializerDataAttributesMachineSettings | Unset
        if isinstance(_machine_settings, Unset):
            machine_settings = UNSET
        else:
            machine_settings = ApiV1MachineDateSerializerDataAttributesMachineSettings.from_dict(_machine_settings)

        _pulse_rate_summary = d.pop("pulse_rate_summary", UNSET)
        pulse_rate_summary: ApiV1MachineDateSerializerDataAttributesPulseRateSummary | Unset
        if isinstance(_pulse_rate_summary, Unset):
            pulse_rate_summary = UNSET
        else:
            pulse_rate_summary = ApiV1MachineDateSerializerDataAttributesPulseRateSummary.from_dict(_pulse_rate_summary)

        _spo2_summary = d.pop("spo2_summary", UNSET)
        spo2_summary: ApiV1MachineDateSerializerDataAttributesSpo2Summary | Unset
        if isinstance(_spo2_summary, Unset):
            spo2_summary = UNSET
        else:
            spo2_summary = ApiV1MachineDateSerializerDataAttributesSpo2Summary.from_dict(_spo2_summary)

        _movement_summary = d.pop("movement_summary", UNSET)
        movement_summary: ApiV1MachineDateSerializerDataAttributesMovementSummary | Unset
        if isinstance(_movement_summary, Unset):
            movement_summary = UNSET
        else:
            movement_summary = ApiV1MachineDateSerializerDataAttributesMovementSummary.from_dict(_movement_summary)

        api_v1_machine_date_serializer_data_attributes = cls(
            id=id,
            usage=usage,
            machine_id=machine_id,
            date=date,
            time_offset=time_offset,
            created_at=created_at,
            updated_at=updated_at,
            large_leak=large_leak,
            ahi_summary=ahi_summary,
            pressure_summary=pressure_summary,
            leak_rate_summary=leak_rate_summary,
            flow_limit_summary=flow_limit_summary,
            resp_rate_summary=resp_rate_summary,
            epap_summary=epap_summary,
            machine_settings=machine_settings,
            pulse_rate_summary=pulse_rate_summary,
            spo2_summary=spo2_summary,
            movement_summary=movement_summary,
        )

        api_v1_machine_date_serializer_data_attributes.additional_properties = d
        return api_v1_machine_date_serializer_data_attributes

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
