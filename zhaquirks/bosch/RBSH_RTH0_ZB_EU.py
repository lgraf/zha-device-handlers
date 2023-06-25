"""Device handler for Bosch RBSH_RTH0_ZB_EU (room thermostat II 230V) ."""

from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import Basic, Identify, Time, Ota
from zigpy.zcl.clusters.homeautomation import Diagnostic
from zigpy.zcl.clusters.measurement import RelativeHumidity
from zigpy.zcl.clusters.hvac import Thermostat, UserInterface

from zhaquirks.bosch import BOSCH
from zhaquirks.const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID
)


class RBSH_RTH0_ZB_EU(CustomDevice):
    signature = {
        # NodeDescriptor(
        #     logical_type= < LogicalType.Router: 1 >,
        #     complex_descriptor_available = 0,
        #     user_descriptor_available = 0,
        #     reserved = 0,
        #     aps_flags = 0,
        #     frequency_band = < FrequencyBand.Freq2400MHz: 8 >,
        #     mac_capability_flags = < MACCapabilityFlags.FullFunctionDevice | MainsPowered | RxOnWhenIdle | AllocateAddress: 142 >,
        #     manufacturer_code = 4617,
        #     maximum_buffer_size = 82,
        #     maximum_incoming_transfer_size = 255,
        #     server_mask = 11264,
        #     maximum_outgoing_transfer_size = 255,
        #     descriptor_capability_field = < DescriptorCapability.NONE: 0 >,
        #     *allocate_address = True,
        #     *is_alternate_pan_coordinator = False,
        #     *is_coordinator = False,
        #     *is_end_device = False,
        #     *is_full_function_device = True,
        #     *is_mains_powered = True,
        #     *is_receiver_on_when_idle = True,
        #     *is_router = True,
        #     *is_security_capable = False
        # )

        # SizePrefixedSimpleDescriptor(
        #     endpoint=1,
        #     profile=260,
        #     device_type=769,
        #     device_version=1,
        #     input_clusters=[0, 3, 513, 516, 1029, 2821],
        #     output_clusters=[10, 25]
        # )

        # <Endpoint
        #     id = 1
        #     in = [
        #         basic:0x0000,
        #         identify: 0x0003,
        #         thermostat: 0x0201,
        #         thermostat_ui: 0x0204,
        #         humidity: 0x0405,
        #         diagnostic: 0x0B05]
        #     out = [
        #         time:0x000A,
        #         ota: 0x0019
        #     ]
        #     status = < Status.ZDO_INIT: 1 >
        # >


        MODELS_INFO: [(BOSCH, "RBSH-RTH0-ZB-EU")],
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.THERMOSTAT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Thermostat.cluster_id,
                    UserInterface.cluster_id,
                    RelativeHumidity.cluster_id,
                    Diagnostic.cluster_id
                ],
                OUTPUT_CLUSTERS: [
                    Time.cluster_id,
                    Ota.cluster_id
                ]
            }
        }
    }

    replacement = {
        ENDPOINTS: {
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.THERMOSTAT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Thermostat.cluster_id,
                    UserInterface.cluster_id,
                    RelativeHumidity.cluster_id,
                    Diagnostic.cluster_id
                ],
                OUTPUT_CLUSTERS: [
                    Time.cluster_id,
                    Ota.cluster_id
                ]
            }
        }
    }

    """Custom device representing Bosch RBSH-RTH0-ZB-EU thermostat."""