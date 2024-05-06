"""Bosch RBSH-RTH0-ZB-EU (room thermostat II 230 V)."""

from zigpy import types
from zigpy.quirks.v2 import CustomDeviceV2, add_to_registry_v2
from zigpy.zcl.clusters.hvac import ControlSequenceOfOperation, Thermostat

from zhaquirks.bosch import BOSCH

DEVICE_MODEL = "RBSH-RTH0-ZB-EU"

CTRL_SEQUENCE_OF_OPERATION_ID = 0x001B


class BoschControlSequenceOfOperation(types.enum8):
    "supported ControlSequenceOfOperation modes."

    Cooling_Only = ControlSequenceOfOperation.Cooling_Only
    Heating_Only = ControlSequenceOfOperation.Heating_Only


class BoschRoomThermostat(CustomDeviceV2):
    "bosch theromstat device."


(
    add_to_registry_v2(BOSCH, DEVICE_MODEL)
    .device_class(BoschRoomThermostat)
    .enum(
        Thermostat.AttributeDefs.ctrl_sequence_of_oper.name,
        BoschControlSequenceOfOperation,
        Thermostat.cluster_id,
        # TODO: where to define?
        translation_key="ctrl_sequence_of_oper",
    )
)
