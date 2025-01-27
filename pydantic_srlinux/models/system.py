from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, RootModel
from typing_extensions import Annotated


class AsicLoopbackContainer(BaseModel):
    """
    ASIC loopback

    Use the ASIC loopback mode
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class DomainNameType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$'
        ),
    ]
    """
    The domain-name type represents a DNS domain name.  The
    name SHOULD be fully qualified whenever possible.

    Internet domain names are only loosely specified.  Section
    3.5 of RFC 1034 recommends a syntax (modified in Section
    2.1 of RFC 1123).  The pattern above is intended to allow
    for current practice in domain name use, and some possible
    future expansion.  It is designed to hold various types of
    domain names, including names used for A or AAAA records
    (host names) and other records, such as SRV records.  Note
    that Internet host names have a stricter syntax (described
    in RFC 952) than the DNS recommendations in RFCs 1034 and
    1123, and that systems that want to store host names in
    schema nodes using the domain-name type are recommended to
    adhere to this stricter standard to ensure interoperability.

    The encoding of DNS names in the DNS protocol is limited
    to 255 characters.  Since the encoding consists of labels
    prefixed by a length bytes and there is a trailing NULL
    byte, only 253 characters can appear in the textual dotted
    notation.

    The description clause of schema nodes using the domain-name
    type MUST describe when and how these names are resolved to
    IP addresses.  Note that the resolution of a domain-name value
    may require to query multiple DNS records (e.g., A for IPv4
    and AAAA for IPv6).  The order of the resolution process and
    which DNS record takes precedence can either be defined
    explicitly or may depend on the configuration of the
    resolver.

    Domain-name values use the US-ASCII encoding.  Their canonical
    format uses lowercase US-ASCII characters.  Internationalized
    domain names MUST be A-labels as per RFC 5890.
    """


class DscpValueType(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[int, Field(ge=0, le=63, title='Dscp-valueType')]
    """
    A DiffServ Code Point represented numerically.
    """


class GnssContainer(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class IndexLeaf3(RootModel[int]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[int, Field(ge=0, le=255, title='IndexLeaf3')]
    """
    Each key in a keychain requires a unique identifier, the index value specifies this identifier
    """


class InterfaceStandbySignalingOnNonDfContainer(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class Ipv4AddressWithZoneType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
            title='Ipv4-address-with-zoneType',
        ),
    ]
    """
    The ipv4-address-with-zone type represents an IPv4 address in dotted quad notation (added only for symmetry)
    """


class Ipv4Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]


class Ipv6AddressWithZoneType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%.+)?$)(?=^(([^:]+:){6}(([^:]+:[^:]+)|(.*\\..*)))|((([^:]+:)*[^:]+)?::(([^:]+:)*[^:]+)?)(%.+)?$)(?=^([^%]+)(%(mgmt0\\.0|system0\\.0|sync0\\.0|lo(0|1[0-9][0-9]|2([0-4][0-9]|5[0-5])|[1-9][0-9]|[1-9])\\.(0|[1-9](\\d){0,3})|lif-.*\\.(0|[1-9](\\d){0,3})|vhn-.*\\.(0|[1-9](\\d){0,3})|enp(0|1[0-9][0-9]|2([0-4][0-9]|5[0-5])|[1-9][0-9]|[1-9])s(0|[1-9]|[1-2][0-9]|3[0-1])f[0-7]\\.(0|[1-9](\\d){0,3})|ethernet-([1-9](\\d){0,1}(/[abcdef])?(/[1-9](\\d){0,1})?/(([1-9](\\d){0,1})|(1[0-1]\\d)|(12[0-8])))\\.([0]|[1-9](\\d){0,3})|irb(0|1[0-9][0-9]|2([0-4][0-9]|5[0-5])|[1-9][0-9]|[1-9])\\.(0|[1-9](\\d){0,3})|lag(([1-9](\\d){0,2})|(1000))\\.(0|[1-9](\\d){0,3})))?$).*$',
            title='Ipv6-address-with-zoneType',
        ),
    ]
    """
    The ipv6-address-with-zone type represents an IPv6 address in full, mixed, shortened, and
    shortened-mixed notation.  The IPv6 address may include a zone index, separated by
    a % sign. The zone index is used to disambiguate identical address values.  For link-local
    addresses, the zone index is expected to be the name of a subinterface. An example of
    a link-local address is:

    fe80::1234%ethernet-1/1.1
    """


class Ipv6Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$'
        ),
    ]


class LiHourlyStatusContainer(BaseModel):
    """
    An hourly notification to the LI monitoring system where li deployment status is success and in-use
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    allow_local_save: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-lawful-intercept:allow-local-save',
            title='Allow-local-saveLeaf',
        ),
    ] = None
    hourly_count: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lawful-intercept:hourly-count',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Hourly-countLeaf',
        ),
    ] = None
    """
    The date-and-time type is a profile of the ISO 8601
    standard for representation of dates and times using the
    Gregorian calendar.  The profile is defined by the
    date-time production in Section 5.6 of RFC 3339.

    The date-and-time type is compatible with the dateTime XML
    schema type with the following notable exceptions:

    (a) The date-and-time type does not allow negative years.

    (b) The date-and-time time-offset -00:00 indicates an unknown
        time zone (see RFC 3339) while -00:00 and +00:00 and Z
        all represent the same time zone in dateTime.

    (c) The canonical format (see below) of data-and-time values
        differs from the canonical format used by the dateTime XML
        schema type, which requires all times to be in UTC using
        the time-offset 'Z'.

    This type is not equivalent to the DateAndTime textual
    convention of the SMIv2 since RFC 3339 uses a different
    separator between full-date and full-time and provides
    higher resolution of time-secfrac.

    The canonical format for date-and-time values with a known time
    zone uses a numeric time zone offset that is calculated using
    the device's configured known offset to UTC time.  A change of
    the device's offset to UTC time will cause date-and-time values
    to change accordingly.  Such changes might happen periodically
    in case a server follows automatically daylight saving time
    (DST) time zone offset changes.  The canonical format for
    date-and-time values with an unknown time zone (usually
    referring to the notion of local time) uses the time-offset
    -00:00.
    """


class MtuContainer(BaseModel):
    """
    Top-level container for configuration and state data related to the system MTU
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    default_port_mtu: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mtu:default-port-mtu',
            ge=1500,
            le=9500,
            title='Default-port-mtuLeaf',
        ),
    ] = 9232
    """
    System default port MTU in bytes including ethernet overhead but excluding 4-bytes FCS

    The 7220 IXR-D1, 7220 IXR-D2, 7220 IXR-D3, 7220 IXR-D4, 7220 IXR-D5, 7220 IXR-H2, 7220 IXR-H3, and 7220 IXR-H4 systems support a maximum port MTU of 9412 bytes.

    The 7730 SXR systems support a maximum port MTU of 9408 bytes.
    """
    default_l2_mtu: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mtu:default-l2-mtu',
            ge=1500,
            le=9500,
            title='Default-l2-mtuLeaf',
        ),
    ] = 9232
    """
    System default Layer-2 MTU in bytes for bridged subinterfaces

    It includes the ethernet overhead and VLAN tags but excludes 4-bytes FCS. The default-l2-mtu
    is also used as the oper-mac-vrf-mtu and oper-vpws-mtu value if the network-instance does
    not have subinterfaces.

    The 7220 IXR-D1, 7220 IXR-D2, 7220 IXR-D3, 7220 IXR-D4, 7220 IXR-D5, 7220 IXR-H2, 7220 IXR-H3, and
    7220 IXR-H4 systems support a maximum L2 MTU of 9412 bytes.

    The 7730 SXR systems support a maximum L2 MTU of 9408 bytes.
    """
    default_ip_mtu: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mtu:default-ip-mtu',
            ge=1280,
            le=9486,
            title='Default-ip-mtuLeaf',
        ),
    ] = 1500
    """
    System default IP MTU in bytes including the IP header but excluding Ethernet overhead

    The 7220 IXR-D1, 7220 IXR-D2, 7220 IXR-D3, 7220 IXR-D4, 7220 IXR-D5, 7220 IXR-H2, 7220 IXR-H3, and 7220 IXR-H4 systems support a maximum IP MTU of 9398 bytes.

    The 7730 SXR systems support a maximum IP MTU of 9394 bytes.
    """
    default_mpls_mtu: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mtu:default-mpls-mtu',
            ge=1284,
            le=9496,
            title='Default-mpls-mtuLeaf',
        ),
    ] = 1508
    """
    System default MPLS MTU in bytes including the size of the transmitted label stack.

    The 7730 SXR systems support a maximum MPLS MTU of 9404 bytes.
    """
    min_path_mtu: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mtu:min-path-mtu',
            ge=552,
            le=9232,
            title='Min-path-mtuLeaf',
        ),
    ] = 552
    """
    Sets the minimum path MTU to use when receiving an ICMP fragmentation needed message

    The 7730 SXR systems support a maximum min path MTU of 9176 bytes.

    This is controlled via the kernel min_pmtu option. In the event an ICMP fragmentation needed message is received by the kernel, the system will drop the session to this MTU to allow packets to traverse the entire path.
    """


class MulticastContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    leave_sync_propagation: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-multicast:leave-sync-propagation',
            ge=0,
            le=300,
            title='Leave-sync-propagationLeaf',
        ),
    ] = 5
    """
    This value is the delta time applied by a node sending the leave synch route before removing the multicast state

    When EVPN multi-homing is used along with igmp/mld snooping, a node receiving a leave message from a receiver will
    advertise an EVPN Multicast Leave Sync route to synchronize the leave state across all nodes attached to the
    Ethernet Segment. This route encodes the maximum response time that the receiving node needs to apply for a given
    (S,G) or (*,G) state before removing it. The leave-sync-propagation time accounts for the BGP propagation
    time so that the local node minimizes the potential churn of removing the multicast state before the route made it
    to the node receiving a join for the multicast group to be removed. The value must be adjusted to the estimated
    BGP propagation time between the Ethernet Segment peers.
    """


class PtpContainer(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class RateLimitPerHostContainer(BaseModel):
    """
    Context for controller rate limiting behavior per host
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    peak_rate: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-datapath:peak-rate',
            ge=1,
            le=20,
            title='Peak-rateLeaf',
        ),
    ] = 10
    """
    The peak rate for generated ICMP messages sent towards each host

    A token bucket is maintained for each of the last 1000 IPv4 senders that generated traffic requiring ICMP messages to be sent back to them. Each token bucket has a maximum depth, counted in terms of ICMP messages, controlled by the max-burst parameter and a fill/drain rate controlled by this peak-rate parameter
    """
    max_burst: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-datapath:max-burst',
            ge=1,
            le=50,
            title='Max-burstLeaf',
        ),
    ] = 10
    """
    The maximum burst size for generated ICMP messages sent towards each host

    A token bucket is maintained for each of the last 1000 IPv4 senders that generated traffic requiring ICMP messages to be sent back to them. Each token bucket has a maximum depth, counted in terms of ICMP messages, controlled by this max-burst parameter and a fill/drain rate controlled by the peak-rate parameter
    """


class RateLimitPerHostContainer2(BaseModel):
    """
    Context for controller rate limiting behavior per host
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    peak_rate: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-datapath:peak-rate',
            ge=1,
            le=20,
            title='Peak-rateLeaf2',
        ),
    ] = 10
    """
    The peak rate for generated ICMP messages sent towards each host

    A token bucket is maintained for each of the last 1000 IPv6 senders that generated traffic requiring ICMPv6 messages to be sent back to them. Each token bucket has a maximum depth, counted in terms of ICMP messages, controlled by the max-burst parameter and a fill/drain rate controlled by this peak-rate parameter
    """
    max_burst: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-datapath:max-burst',
            ge=1,
            le=50,
            title='Max-burstLeaf2',
        ),
    ] = 10
    """
    The maximum burst size for generated ICMP messages sent towards each host

    A token bucket is maintained for each of the last 1000 IPv6 senders that generated traffic requiring ICMPv6 messages to be sent back to them. Each token bucket has a maximum depth, counted in terms of ICMP messages, controlled by this max-burst parameter and a fill/drain rate controlled by the peak-rate parameter
    """


class RouteDistinguisherType0Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9]):(429496729[0-5]|42949672[0-8][0-9]|4294967[0-1][0-9]{2}|429496[0-6][0-9]{3}|42949[0-5][0-9]{4}|4294[0-8][0-9]{5}|429[0-3][0-9]{6}|42[0-8][0-9]{7}|4[0-1][0-9]{8}|[1-3][0-9]{9}|[1-9][0-9]{1,8}|[0-9])$).*$',
            title='Route-distinguisher-type-0Type',
        ),
    ]


class RouteDistinguisherType1Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$).*$',
            title='Route-distinguisher-type-1Type',
        ),
    ]


class RouteDistinguisherType2Type(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(429496729[0-5]|42949672[0-8][0-9]|4294967[0-1][0-9]{2}|429496[0-6][0-9]{3}|42949[0-5][0-9]{4}|4294[0-8][0-9]{5}|429[0-3][0-9]{6}|42[0-8][0-9]{7}|4[0-1][0-9]{8}|[1-3][0-9]{9}|[1-9][0-9]{1,8}|[0-9]):(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$).*$',
            title='Route-distinguisher-type-2Type',
        ),
    ]


class RouteDistinguisherType2bType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9]).(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9]):(6553[0-5]|655[0-2][0-9]|654[0-9]{2}|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$).*$',
            title='Route-distinguisher-type-2bType',
        ),
    ]


class StringOrBinaryType1(RootModel[bytes]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[bytes, Field(max_length=18446744073709551615)]
    """
    Type definition for string or binary represenation
    """


class Sync0Container(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class Sync0Container2(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class SynchronizedLeaf1(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str, Field(pattern='^(?=^unsynchronized$).*$', title='SynchronizedLeaf')
    ]
    """
    Address of the NTP server that the local client is synchronized to
    This field is set to 'unsynchronized', if the local client is not
    synchronized
    """


class TacacsContainer(BaseModel):
    """
    Top-level container for configuration relating to TACACS+ interworking with roles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    priv_lvl: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:priv-lvl', ge=0, le=15, title='Priv-lvlLeaf2'),
    ] = None
    """
    The TACACS+ priv-lvl to map to this role

    All roles matching each specific priv-lvl, and their lessers are merged together to create the final ruleset applied to the user.
    """


class TimersContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    activation_timer: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:activation-timer',
            ge=0,
            le=100,
            title='Activation-timerLeaf2',
        ),
    ] = None
    """
    Remaining activation timer per Ethernet segment
    """


class TlsCase(BaseModel):
    pass
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )


class UnicastMsgRateContainer(BaseModel):
    """
    Aggregate unicast message rates for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:anno-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Anno-msg-rate-txLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of announce messages transmitted
    """
    anno_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:anno-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Anno-msg-rate-rxLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of announce messages received
    """
    sync_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:sync-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Sync-msg-rate-txLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of sync messages transmitted
    """
    sync_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:sync-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Sync-msg-rate-rxLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of sync messages received
    """
    del_req_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-req-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Del-req-msg-rate-txLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of delay-req messages transmitted
    """
    del_req_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-req-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Del-req-msg-rate-rxLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of delay-req messages received
    """
    del_resp_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Del-resp-msg-rate-txLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of delay-resp messages transmitted
    """
    del_resp_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Del-resp-msg-rate-rxLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of delay-resp messages received
    """
    follow_up_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Follow-up-msg-rate-txLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of follow-up messages transmitted
    """
    follow_up_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Follow-up-msg-rate-rxLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of follow-up messages received
    """
    signaling_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:signaling-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Signaling-msg-rate-txLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of signaling messages transmitted
    """
    signaling_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:signaling-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Signaling-msg-rate-rxLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of signaling messages received
    """
    other_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:other-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Other-rate-rxLeaf',
        ),
    ] = None
    """
    Specifies the rate of messages of other messages received
    """


class UnixSocketContainer2(BaseModel):
    """
    Create a new unix socket and bind the NETCONF service to it
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    socket_path: Annotated[
        Optional[str],
        Field(alias='srl_nokia-netconf-server:socket-path', title='Socket-pathLeaf2'),
    ] = None
    """
    Path to the unix socket used by NETCONF
    """


class UserListEntry2(BaseModel):
    """
    The list of protocols that are using this label block. If the block is not shared there will only be 1 user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    index: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mpls-label-management:index',
            ge=0,
            le=255,
            title='IndexLeaf',
        ),
    ] = None
    """
    Index number used to enumerate the clients
    """
    owner: Annotated[
        Optional[Any],
        Field(alias='srl_nokia-mpls-label-management:owner', title='OwnerLeaf'),
    ] = None
    """
    The protocol or service associated with the client
    """


class UserListEntry3(BaseModel):
    """
    The list of protocols that are using this label block. If the block is not shared there will only be 1 user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    index: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mpls-label-management:index',
            ge=0,
            le=255,
            title='IndexLeaf2',
        ),
    ] = None
    """
    Index number used to enumerate the clients
    """
    owner: Annotated[
        Optional[Any],
        Field(alias='srl_nokia-mpls-label-management:owner', title='OwnerLeaf2'),
    ] = None
    """
    The protocol or service associated with the client
    """


class YangContainer(BaseModel):
    """
    Top-level container for application state related to YANG
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    modules: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-app-mgmt:modules')
    ] = []
    """
    YANG module names used by this application instance
    """
    source_directories: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-app-mgmt:source-directories')
    ] = []
    """
    Source directories searched for YANG modules to load

    These directories are used to load modules indicated in the modules leaf, and any modules imported/included within them
    """


class EnumerationEnum(Enum):
    request = 'request'
    response = 'response'
    common = 'common'


class EnumerationEnum10(Enum):
    remote = 'remote'
    remote_and_console = 'remote-and-console'


class EnumerationEnum11(Enum):
    ar2 = 'ar2'
    sha2 = 'sha2'
    yescrypt = 'yescrypt'


class EnumerationEnum12(Enum):
    cli = 'cli'
    gnmi = 'gnmi'
    gnoi = 'gnoi'
    gnsi = 'gnsi'
    gribi = 'gribi'
    netconf = 'netconf'
    p4rt = 'p4rt'
    json_rpc = 'json-rpc'
    ftp = 'ftp'
    grpc_reflection = 'grpc-reflection'


class EnumerationEnum13(Enum):
    action = 'action'
    cancel_commit = 'cancel-commit'
    close_session = 'close-session'
    commit = 'commit'
    copy_config = 'copy-config'
    delete_config = 'delete-config'
    discard_changes = 'discard-changes'
    edit_config = 'edit-config'
    edit_data = 'edit-data'
    get = 'get'
    get_config = 'get-config'
    get_data = 'get-data'
    get_schema = 'get-schema'
    kill_session = 'kill-session'
    lock = 'lock'
    unlock = 'unlock'
    validate = 'validate'


class EnumerationEnum14(Enum):
    request = 'request'
    response = 'response'
    common = 'common'
    grpc = 'grpc'


class EnumerationEnum15(Enum):
    native = 'native'
    openconfig = 'openconfig'


class EnumerationEnum16(Enum):
    gnmi = 'gnmi'
    acctz = 'acctz'


class EnumerationEnum17(Enum):
    on_change = 'ON_CHANGE'
    sample = 'SAMPLE'
    target_defined = 'TARGET_DEFINED'
    poll = 'POLL'
    once = 'ONCE'


class EnumerationEnum18(Enum):
    preserve = 'preserve'
    delete = 'delete'


class EnumerationEnum19(Enum):
    ready = 'ready'
    not_ready = 'not-ready'
    delete_pending = 'delete-pending'
    updating = 'updating'


class EnumerationEnum2(Enum):
    enable = 'enable'
    disable = 'disable'


class EnumerationEnum20(Enum):
    ready = 'ready'
    not_ready = 'not-ready'
    delete_pending = 'delete-pending'
    updating = 'updating'


class EnumerationEnum21(Enum):
    tcp_md5 = 'tcp-md5'
    isis = 'isis'
    ospf = 'ospf'
    tcp_ao = 'tcp-ao'
    vrrp = 'vrrp'
    macsec = 'macsec'


class EnumerationEnum22(Enum):
    none = 'none'


class EnumerationEnum23(Enum):
    cleartext = 'cleartext'
    md5 = 'md5'
    hmac_md5 = 'hmac-md5'
    hmac_sha_1 = 'hmac-sha-1'
    hmac_sha_256 = 'hmac-sha-256'
    aes_128_cmac = 'aes-128-cmac'
    aes_256_cmac = 'aes-256-cmac'


class EnumerationEnum24(Enum):
    forever = 'forever'


class EnumerationEnum25(Enum):
    mirror_inst_admin_down = 'mirror-inst-admin-down'
    no_mirror_source = 'no-mirror-source'
    local_mirror_subif_down = 'local-mirror-subif-down'
    remote_mirror_dst_unreachable = 'remote-mirror-dst-unreachable'


class EnumerationEnum26(Enum):
    ingress_only = 'ingress-only'
    egress_only = 'egress-only'
    ingress_egress = 'ingress-egress'


class EnumerationEnum27(Enum):
    mirror_source_ingress_table_full = 'mirror-source-ingress-table-full'
    mirror_source_egress_table_full = 'mirror-source-egress-table-full'
    not_applicable = 'not-applicable'


class EnumerationEnum28(Enum):
    l2ogre = 'l2ogre'
    l3ogre = 'l3ogre'
    mpls_gre = 'mpls-gre'


class EnumerationEnum29(Enum):
    store_and_forward = 'store-and-forward'
    cut_through = 'cut-through'


class EnumerationEnum3(Enum):
    up = 'up'
    down = 'down'
    empty = 'empty'
    downloading = 'downloading'
    booting = 'booting'
    starting = 'starting'
    failed = 'failed'
    synchronizing = 'synchronizing'
    upgrading = 'upgrading'
    low_power = 'low-power'
    degraded = 'degraded'
    warm_reboot = 'warm-reboot'
    waiting = 'waiting'


class EnumerationEnum30(Enum):
    static = 'static'
    duplicate = 'duplicate'
    learnt = 'learnt'
    irb_interface = 'irb-interface'
    evpn = 'evpn'
    evpn_static = 'evpn-static'
    irb_interface_anycast = 'irb-interface-anycast'
    proxy_anti_spoof = 'proxy-anti-spoof'
    reserved = 'reserved'
    eth_cfm = 'eth-cfm'
    irb_interface_vrrp = 'irb-interface-vrrp'


class EnumerationEnum31(Enum):
    static = 'static'
    dynamic = 'dynamic'
    evpn = 'evpn'
    duplicate = 'duplicate'


class EnumerationEnum32(Enum):
    none = 'none'
    virtual = 'virtual'


class EnumerationEnum33(Enum):
    all_active = 'all-active'
    single_active = 'single-active'


class EnumerationEnum34(Enum):
    default = 'default'
    preference = 'preference'
    manual = 'manual'


class EnumerationEnum35(Enum):
    include = 'include'
    exclude = 'exclude'


class EnumerationEnum36(Enum):
    use_system_ipv4_address = 'use-system-ipv4-address'


class EnumerationEnum37(Enum):
    use_system_ipv4_address = 'use-system-ipv4-address'


class EnumerationEnum38(Enum):
    mpls_label = 'mpls-label'
    vni = 'vni'
    transposed_srv6_function = 'transposed-srv6-function'


class EnumerationEnum39(Enum):
    admin_disabled = 'admin-disabled'
    no_nexthop_address = 'no-nexthop-address'
    no_originating_address = 'no-originating-address'
    no_associated_interface = 'no-associated-interface'
    associated_interface_oper_down = 'associated-interface-oper-down'
    no_esi = 'no-esi'
    no_esi_label = 'no-esi-label'


class EnumerationEnum4(Enum):
    cs0 = 'CS0'
    le = 'LE'
    cs1 = 'CS1'
    af11 = 'AF11'
    af12 = 'AF12'
    af13 = 'AF13'
    cs2 = 'CS2'
    af21 = 'AF21'
    af22 = 'AF22'
    af23 = 'AF23'
    cs3 = 'CS3'
    af31 = 'AF31'
    af32 = 'AF32'
    af33 = 'AF33'
    cs4 = 'CS4'
    af41 = 'AF41'
    af42 = 'AF42'
    af43 = 'AF43'
    cs5 = 'CS5'
    ef = 'EF'
    cs6 = 'CS6'
    cs7 = 'CS7'


class EnumerationEnum40(Enum):
    auto_derived_from_system_ip_0 = 'auto-derived-from-system-ip:0'
    none = 'none'


class EnumerationEnum41(Enum):
    auto_derived_from_esi_bytes_1_6 = 'auto-derived-from-esi-bytes-1-6'
    none = 'none'


class EnumerationEnum42(Enum):
    auto_derived_from_esi_bytes_1_6 = 'auto-derived-from-esi-bytes-1-6'
    none = 'none'


class EnumerationEnum43(Enum):
    no_loopback_address = 'no-loopback-address'
    no_esi = 'no-esi'
    none = 'none'
    network_instance_oper_down = 'network-instance-oper-down'
    bad_rd_format = 'bad-rd-format'


class EnumerationEnum44(Enum):
    both = 'both'
    input = 'input'
    output = 'output'


class EnumerationEnum45(Enum):
    action = 'action'
    cancel_commit = 'cancel-commit'
    close_session = 'close-session'
    commit = 'commit'
    copy_config = 'copy-config'
    delete_config = 'delete-config'
    discard_changes = 'discard-changes'
    edit_config = 'edit-config'
    edit_data = 'edit-data'
    get_config = 'get-config'
    get_data = 'get-data'
    get_schema = 'get-schema'
    get = 'get'
    hello = 'hello'
    kill_session = 'kill-session'
    lock = 'lock'
    unknown = 'unknown'
    unlock = 'unlock'
    validate = 'validate'


class EnumerationEnum46(Enum):
    admin_disabled = 'admin-disabled'
    failed_to_compile = 'failed-to-compile'
    exception = 'exception'
    timeout = 'timeout'
    subscription_failed = 'subscription-failed'
    script_unavailable = 'script-unavailable'
    script_error = 'script-error'
    missing_function = 'missing-function'
    system_error = 'system-error'
    ephemeral_action_failed = 'ephemeral-action-failed'
    cfg_action_failed = 'cfg-action-failed'
    tools_action_failed = 'tools-action-failed'
    state_action_failed = 'state-action-failed'
    script_action_failed = 'script-action-failed'


class EnumerationEnum47(Enum):
    received = 'received'
    transmitted = 'transmitted'
    common = 'common'


class EnumerationEnum48(Enum):
    chassis_component = 'CHASSIS_COMPONENT'
    interface_alias = 'INTERFACE_ALIAS'
    port_component = 'PORT_COMPONENT'
    mac_address = 'MAC_ADDRESS'
    network_address = 'NETWORK_ADDRESS'
    interface_name = 'INTERFACE_NAME'
    local = 'LOCAL'


class EnumerationEnum49(Enum):
    i_pv4 = 'IPv4'
    i_pv6 = 'IPv6'


class EnumerationEnum5(Enum):
    ipv4 = 'ipv4'
    ipv6 = 'ipv6'
    mac = 'mac'


class EnumerationEnum50(Enum):
    interface_alias = 'INTERFACE_ALIAS'
    port_component = 'PORT_COMPONENT'
    mac_address = 'MAC_ADDRESS'
    network_address = 'NETWORK_ADDRESS'
    interface_name = 'INTERFACE_NAME'
    agent_circuit_id = 'AGENT_CIRCUIT_ID'
    local = 'LOCAL'


class EnumerationEnum51(Enum):
    unknown = 'unknown'


class EnumerationEnum52(Enum):
    serial = 'serial'


class EnumerationEnum53(Enum):
    shared = 'shared'
    private = 'private'


class EnumerationEnum54(Enum):
    validating = 'validating'
    publishing = 'publishing'
    unconfirmed = 'unconfirmed'
    checkpoint = 'checkpoint'
    save = 'save'
    complete = 'complete'
    reverting = 'reverting'
    failed = 'failed'


class EnumerationEnum55(Enum):
    active = 'ACTIVE'
    sandbox = 'SANDBOX'


class EnumerationEnum56(Enum):
    read = 'read'
    write = 'write'
    deny = 'deny'


class EnumerationEnum57(Enum):
    accept = 'accept'
    discard = 'discard'


class EnumerationEnum58(Enum):
    high = 'high'
    medium = 'medium'
    low = 'low'


class EnumerationEnum59(Enum):
    running = 'running'
    waiting_for_config = 'waiting-for-config'
    error = 'error'
    starting = 'starting'
    stopped = 'stopped'


class EnumerationEnum6(Enum):
    password = 'password'
    publickey = 'publickey'
    keyboard_interactive = 'keyboard-interactive'


class EnumerationEnum60(Enum):
    warm = 'warm'
    cold = 'cold'


class EnumerationEnum61(Enum):
    restart = 'restart'
    stop = 'stop'
    start = 'start'
    reload = 'reload'
    quit = 'quit'
    kill = 'kill'


class EnumerationEnum62(Enum):
    messages = 'messages'


class EnumerationEnum63(Enum):
    messages = 'messages'


class EnumerationEnum64(Enum):
    request = 'request'
    response = 'response'
    common = 'common'


class EnumerationEnum65(Enum):
    mac_vrf = 'mac-vrf'
    vxlan_interface = 'vxlan-interface'
    l2_proxy_arp_nd = 'l2-proxy-arp-nd'
    mfib = 'mfib'
    mac_vrf_bgp_evpn = 'mac-vrf-bgp-evpn'


class EnumerationEnum66(Enum):
    africa_abidjan = 'Africa/Abidjan'
    africa_accra = 'Africa/Accra'
    africa_addis_ababa = 'Africa/Addis_Ababa'
    africa_algiers = 'Africa/Algiers'
    africa_asmara = 'Africa/Asmara'
    africa_bamako = 'Africa/Bamako'
    africa_bangui = 'Africa/Bangui'
    africa_banjul = 'Africa/Banjul'
    africa_bissau = 'Africa/Bissau'
    africa_blantyre = 'Africa/Blantyre'
    africa_brazzaville = 'Africa/Brazzaville'
    africa_bujumbura = 'Africa/Bujumbura'
    africa_cairo = 'Africa/Cairo'
    africa_casablanca = 'Africa/Casablanca'
    africa_ceuta = 'Africa/Ceuta'
    africa_conakry = 'Africa/Conakry'
    africa_dakar = 'Africa/Dakar'
    africa_dar_es_salaam = 'Africa/Dar_es_Salaam'
    africa_djibouti = 'Africa/Djibouti'
    africa_douala = 'Africa/Douala'
    africa_el_aaiun = 'Africa/El_Aaiun'
    africa_freetown = 'Africa/Freetown'
    africa_gaborone = 'Africa/Gaborone'
    africa_harare = 'Africa/Harare'
    africa_johannesburg = 'Africa/Johannesburg'
    africa_juba = 'Africa/Juba'
    africa_kampala = 'Africa/Kampala'
    africa_khartoum = 'Africa/Khartoum'
    africa_kigali = 'Africa/Kigali'
    africa_kinshasa = 'Africa/Kinshasa'
    africa_lagos = 'Africa/Lagos'
    africa_libreville = 'Africa/Libreville'
    africa_lome = 'Africa/Lome'
    africa_luanda = 'Africa/Luanda'
    africa_lubumbashi = 'Africa/Lubumbashi'
    africa_lusaka = 'Africa/Lusaka'
    africa_malabo = 'Africa/Malabo'
    africa_maputo = 'Africa/Maputo'
    africa_maseru = 'Africa/Maseru'
    africa_mbabane = 'Africa/Mbabane'
    africa_mogadishu = 'Africa/Mogadishu'
    africa_monrovia = 'Africa/Monrovia'
    africa_nairobi = 'Africa/Nairobi'
    africa_ndjamena = 'Africa/Ndjamena'
    africa_niamey = 'Africa/Niamey'
    africa_nouakchott = 'Africa/Nouakchott'
    africa_ouagadougou = 'Africa/Ouagadougou'
    africa_porto_novo = 'Africa/Porto-Novo'
    africa_sao_tome = 'Africa/Sao_Tome'
    africa_tripoli = 'Africa/Tripoli'
    africa_tunis = 'Africa/Tunis'
    africa_windhoek = 'Africa/Windhoek'
    america_adak = 'America/Adak'
    america_anchorage = 'America/Anchorage'
    america_anguilla = 'America/Anguilla'
    america_antigua = 'America/Antigua'
    america_araguaina = 'America/Araguaina'
    america_argentina_buenos_aires = 'America/Argentina/Buenos_Aires'
    america_argentina_catamarca = 'America/Argentina/Catamarca'
    america_argentina_cordoba = 'America/Argentina/Cordoba'
    america_argentina_jujuy = 'America/Argentina/Jujuy'
    america_argentina_la_rioja = 'America/Argentina/La_Rioja'
    america_argentina_mendoza = 'America/Argentina/Mendoza'
    america_argentina_rio_gallegos = 'America/Argentina/Rio_Gallegos'
    america_argentina_salta = 'America/Argentina/Salta'
    america_argentina_san_juan = 'America/Argentina/San_Juan'
    america_argentina_san_luis = 'America/Argentina/San_Luis'
    america_argentina_tucuman = 'America/Argentina/Tucuman'
    america_argentina_ushuaia = 'America/Argentina/Ushuaia'
    america_aruba = 'America/Aruba'
    america_asuncion = 'America/Asuncion'
    america_atikokan = 'America/Atikokan'
    america_bahia = 'America/Bahia'
    america_bahia_banderas = 'America/Bahia_Banderas'
    america_barbados = 'America/Barbados'
    america_belem = 'America/Belem'
    america_belize = 'America/Belize'
    america_blanc_sablon = 'America/Blanc-Sablon'
    america_boa_vista = 'America/Boa_Vista'
    america_bogota = 'America/Bogota'
    america_boise = 'America/Boise'
    america_cambridge_bay = 'America/Cambridge_Bay'
    america_campo_grande = 'America/Campo_Grande'
    america_cancun = 'America/Cancun'
    america_caracas = 'America/Caracas'
    america_cayenne = 'America/Cayenne'
    america_cayman = 'America/Cayman'
    america_chicago = 'America/Chicago'
    america_chihuahua = 'America/Chihuahua'
    america_costa_rica = 'America/Costa_Rica'
    america_creston = 'America/Creston'
    america_cuiaba = 'America/Cuiaba'
    america_curacao = 'America/Curacao'
    america_danmarkshavn = 'America/Danmarkshavn'
    america_dawson = 'America/Dawson'
    america_dawson_creek = 'America/Dawson_Creek'
    america_denver = 'America/Denver'
    america_detroit = 'America/Detroit'
    america_dominica = 'America/Dominica'
    america_edmonton = 'America/Edmonton'
    america_eirunepe = 'America/Eirunepe'
    america_el_salvador = 'America/El_Salvador'
    america_fort_nelson = 'America/Fort_Nelson'
    america_fortaleza = 'America/Fortaleza'
    america_glace_bay = 'America/Glace_Bay'
    america_godthab = 'America/Godthab'
    america_goose_bay = 'America/Goose_Bay'
    america_grand_turk = 'America/Grand_Turk'
    america_grenada = 'America/Grenada'
    america_guadeloupe = 'America/Guadeloupe'
    america_guatemala = 'America/Guatemala'
    america_guayaquil = 'America/Guayaquil'
    america_guyana = 'America/Guyana'
    america_halifax = 'America/Halifax'
    america_havana = 'America/Havana'
    america_hermosillo = 'America/Hermosillo'
    america_indiana_indianapolis = 'America/Indiana/Indianapolis'
    america_indiana_knox = 'America/Indiana/Knox'
    america_indiana_marengo = 'America/Indiana/Marengo'
    america_indiana_petersburg = 'America/Indiana/Petersburg'
    america_indiana_tell_city = 'America/Indiana/Tell_City'
    america_indiana_vevay = 'America/Indiana/Vevay'
    america_indiana_vincennes = 'America/Indiana/Vincennes'
    america_indiana_winamac = 'America/Indiana/Winamac'
    america_inuvik = 'America/Inuvik'
    america_iqaluit = 'America/Iqaluit'
    america_jamaica = 'America/Jamaica'
    america_juneau = 'America/Juneau'
    america_kentucky_louisville = 'America/Kentucky/Louisville'
    america_kentucky_monticello = 'America/Kentucky/Monticello'
    america_kralendijk = 'America/Kralendijk'
    america_la_paz = 'America/La_Paz'
    america_lima = 'America/Lima'
    america_los_angeles = 'America/Los_Angeles'
    america_lower_princes = 'America/Lower_Princes'
    america_maceio = 'America/Maceio'
    america_managua = 'America/Managua'
    america_manaus = 'America/Manaus'
    america_marigot = 'America/Marigot'
    america_martinique = 'America/Martinique'
    america_matamoros = 'America/Matamoros'
    america_mazatlan = 'America/Mazatlan'
    america_menominee = 'America/Menominee'
    america_merida = 'America/Merida'
    america_metlakatla = 'America/Metlakatla'
    america_mexico_city = 'America/Mexico_City'
    america_miquelon = 'America/Miquelon'
    america_moncton = 'America/Moncton'
    america_monterrey = 'America/Monterrey'
    america_montevideo = 'America/Montevideo'
    america_montserrat = 'America/Montserrat'
    america_nassau = 'America/Nassau'
    america_new_york = 'America/New_York'
    america_nipigon = 'America/Nipigon'
    america_nome = 'America/Nome'
    america_noronha = 'America/Noronha'
    america_north_dakota_beulah = 'America/North_Dakota/Beulah'
    america_north_dakota_center = 'America/North_Dakota/Center'
    america_north_dakota_new_salem = 'America/North_Dakota/New_Salem'
    america_ojinaga = 'America/Ojinaga'
    america_panama = 'America/Panama'
    america_pangnirtung = 'America/Pangnirtung'
    america_paramaribo = 'America/Paramaribo'
    america_phoenix = 'America/Phoenix'
    america_port_au_prince = 'America/Port-au-Prince'
    america_port_of_spain = 'America/Port_of_Spain'
    america_porto_velho = 'America/Porto_Velho'
    america_puerto_rico = 'America/Puerto_Rico'
    america_punta_arenas = 'America/Punta_Arenas'
    america_rainy_river = 'America/Rainy_River'
    america_rankin_inlet = 'America/Rankin_Inlet'
    america_recife = 'America/Recife'
    america_regina = 'America/Regina'
    america_resolute = 'America/Resolute'
    america_rio_branco = 'America/Rio_Branco'
    america_santarem = 'America/Santarem'
    america_santiago = 'America/Santiago'
    america_santo_domingo = 'America/Santo_Domingo'
    america_sao_paulo = 'America/Sao_Paulo'
    america_scoresbysund = 'America/Scoresbysund'
    america_sitka = 'America/Sitka'
    america_st_barthelemy = 'America/St_Barthelemy'
    america_st_johns = 'America/St_Johns'
    america_st_kitts = 'America/St_Kitts'
    america_st_lucia = 'America/St_Lucia'
    america_st_thomas = 'America/St_Thomas'
    america_st_vincent = 'America/St_Vincent'
    america_swift_current = 'America/Swift_Current'
    america_tegucigalpa = 'America/Tegucigalpa'
    america_thule = 'America/Thule'
    america_thunder_bay = 'America/Thunder_Bay'
    america_tijuana = 'America/Tijuana'
    america_toronto = 'America/Toronto'
    america_tortola = 'America/Tortola'
    america_vancouver = 'America/Vancouver'
    america_whitehorse = 'America/Whitehorse'
    america_winnipeg = 'America/Winnipeg'
    america_yakutat = 'America/Yakutat'
    america_yellowknife = 'America/Yellowknife'
    antarctica_casey = 'Antarctica/Casey'
    antarctica_davis = 'Antarctica/Davis'
    antarctica_dumont_d_urville = 'Antarctica/DumontDUrville'
    antarctica_macquarie = 'Antarctica/Macquarie'
    antarctica_mawson = 'Antarctica/Mawson'
    antarctica_mc_murdo = 'Antarctica/McMurdo'
    antarctica_palmer = 'Antarctica/Palmer'
    antarctica_rothera = 'Antarctica/Rothera'
    antarctica_syowa = 'Antarctica/Syowa'
    antarctica_troll = 'Antarctica/Troll'
    antarctica_vostok = 'Antarctica/Vostok'
    arctic_longyearbyen = 'Arctic/Longyearbyen'
    asia_aden = 'Asia/Aden'
    asia_almaty = 'Asia/Almaty'
    asia_amman = 'Asia/Amman'
    asia_anadyr = 'Asia/Anadyr'
    asia_aqtau = 'Asia/Aqtau'
    asia_aqtobe = 'Asia/Aqtobe'
    asia_ashgabat = 'Asia/Ashgabat'
    asia_atyrau = 'Asia/Atyrau'
    asia_baghdad = 'Asia/Baghdad'
    asia_bahrain = 'Asia/Bahrain'
    asia_baku = 'Asia/Baku'
    asia_bangkok = 'Asia/Bangkok'
    asia_barnaul = 'Asia/Barnaul'
    asia_beirut = 'Asia/Beirut'
    asia_bishkek = 'Asia/Bishkek'
    asia_brunei = 'Asia/Brunei'
    asia_chita = 'Asia/Chita'
    asia_choibalsan = 'Asia/Choibalsan'
    asia_colombo = 'Asia/Colombo'
    asia_damascus = 'Asia/Damascus'
    asia_dhaka = 'Asia/Dhaka'
    asia_dili = 'Asia/Dili'
    asia_dubai = 'Asia/Dubai'
    asia_dushanbe = 'Asia/Dushanbe'
    asia_famagusta = 'Asia/Famagusta'
    asia_gaza = 'Asia/Gaza'
    asia_hebron = 'Asia/Hebron'
    asia_ho_chi_minh = 'Asia/Ho_Chi_Minh'
    asia_hong_kong = 'Asia/Hong_Kong'
    asia_hovd = 'Asia/Hovd'
    asia_irkutsk = 'Asia/Irkutsk'
    asia_jakarta = 'Asia/Jakarta'
    asia_jayapura = 'Asia/Jayapura'
    asia_jerusalem = 'Asia/Jerusalem'
    asia_kabul = 'Asia/Kabul'
    asia_kamchatka = 'Asia/Kamchatka'
    asia_karachi = 'Asia/Karachi'
    asia_kathmandu = 'Asia/Kathmandu'
    asia_khandyga = 'Asia/Khandyga'
    asia_kolkata = 'Asia/Kolkata'
    asia_krasnoyarsk = 'Asia/Krasnoyarsk'
    asia_kuala_lumpur = 'Asia/Kuala_Lumpur'
    asia_kuching = 'Asia/Kuching'
    asia_kuwait = 'Asia/Kuwait'
    asia_macau = 'Asia/Macau'
    asia_magadan = 'Asia/Magadan'
    asia_makassar = 'Asia/Makassar'
    asia_manila = 'Asia/Manila'
    asia_muscat = 'Asia/Muscat'
    asia_nicosia = 'Asia/Nicosia'
    asia_novokuznetsk = 'Asia/Novokuznetsk'
    asia_novosibirsk = 'Asia/Novosibirsk'
    asia_omsk = 'Asia/Omsk'
    asia_oral = 'Asia/Oral'
    asia_phnom_penh = 'Asia/Phnom_Penh'
    asia_pontianak = 'Asia/Pontianak'
    asia_pyongyang = 'Asia/Pyongyang'
    asia_qatar = 'Asia/Qatar'
    asia_qostanay = 'Asia/Qostanay'
    asia_qyzylorda = 'Asia/Qyzylorda'
    asia_riyadh = 'Asia/Riyadh'
    asia_sakhalin = 'Asia/Sakhalin'
    asia_samarkand = 'Asia/Samarkand'
    asia_seoul = 'Asia/Seoul'
    asia_shanghai = 'Asia/Shanghai'
    asia_singapore = 'Asia/Singapore'
    asia_srednekolymsk = 'Asia/Srednekolymsk'
    asia_taipei = 'Asia/Taipei'
    asia_tashkent = 'Asia/Tashkent'
    asia_tbilisi = 'Asia/Tbilisi'
    asia_tehran = 'Asia/Tehran'
    asia_thimphu = 'Asia/Thimphu'
    asia_tokyo = 'Asia/Tokyo'
    asia_tomsk = 'Asia/Tomsk'
    asia_ulaanbaatar = 'Asia/Ulaanbaatar'
    asia_urumqi = 'Asia/Urumqi'
    asia_ust_nera = 'Asia/Ust-Nera'
    asia_vientiane = 'Asia/Vientiane'
    asia_vladivostok = 'Asia/Vladivostok'
    asia_yakutsk = 'Asia/Yakutsk'
    asia_yangon = 'Asia/Yangon'
    asia_yekaterinburg = 'Asia/Yekaterinburg'
    asia_yerevan = 'Asia/Yerevan'
    atlantic_azores = 'Atlantic/Azores'
    atlantic_bermuda = 'Atlantic/Bermuda'
    atlantic_canary = 'Atlantic/Canary'
    atlantic_cape_verde = 'Atlantic/Cape_Verde'
    atlantic_faroe = 'Atlantic/Faroe'
    atlantic_madeira = 'Atlantic/Madeira'
    atlantic_reykjavik = 'Atlantic/Reykjavik'
    atlantic_south_georgia = 'Atlantic/South_Georgia'
    atlantic_st_helena = 'Atlantic/St_Helena'
    atlantic_stanley = 'Atlantic/Stanley'
    australia_adelaide = 'Australia/Adelaide'
    australia_brisbane = 'Australia/Brisbane'
    australia_broken_hill = 'Australia/Broken_Hill'
    australia_currie = 'Australia/Currie'
    australia_darwin = 'Australia/Darwin'
    australia_eucla = 'Australia/Eucla'
    australia_hobart = 'Australia/Hobart'
    australia_lindeman = 'Australia/Lindeman'
    australia_lord_howe = 'Australia/Lord_Howe'
    australia_melbourne = 'Australia/Melbourne'
    australia_perth = 'Australia/Perth'
    australia_sydney = 'Australia/Sydney'
    europe_amsterdam = 'Europe/Amsterdam'
    europe_andorra = 'Europe/Andorra'
    europe_astrakhan = 'Europe/Astrakhan'
    europe_athens = 'Europe/Athens'
    europe_belgrade = 'Europe/Belgrade'
    europe_berlin = 'Europe/Berlin'
    europe_bratislava = 'Europe/Bratislava'
    europe_brussels = 'Europe/Brussels'
    europe_bucharest = 'Europe/Bucharest'
    europe_budapest = 'Europe/Budapest'
    europe_busingen = 'Europe/Busingen'
    europe_chisinau = 'Europe/Chisinau'
    europe_copenhagen = 'Europe/Copenhagen'
    europe_dublin = 'Europe/Dublin'
    europe_gibraltar = 'Europe/Gibraltar'
    europe_guernsey = 'Europe/Guernsey'
    europe_helsinki = 'Europe/Helsinki'
    europe_isle_of_man = 'Europe/Isle_of_Man'
    europe_istanbul = 'Europe/Istanbul'
    europe_jersey = 'Europe/Jersey'
    europe_kaliningrad = 'Europe/Kaliningrad'
    europe_kiev = 'Europe/Kiev'
    europe_kirov = 'Europe/Kirov'
    europe_lisbon = 'Europe/Lisbon'
    europe_ljubljana = 'Europe/Ljubljana'
    europe_london = 'Europe/London'
    europe_luxembourg = 'Europe/Luxembourg'
    europe_madrid = 'Europe/Madrid'
    europe_malta = 'Europe/Malta'
    europe_mariehamn = 'Europe/Mariehamn'
    europe_minsk = 'Europe/Minsk'
    europe_monaco = 'Europe/Monaco'
    europe_moscow = 'Europe/Moscow'
    europe_oslo = 'Europe/Oslo'
    europe_paris = 'Europe/Paris'
    europe_podgorica = 'Europe/Podgorica'
    europe_prague = 'Europe/Prague'
    europe_riga = 'Europe/Riga'
    europe_rome = 'Europe/Rome'
    europe_samara = 'Europe/Samara'
    europe_san_marino = 'Europe/San_Marino'
    europe_sarajevo = 'Europe/Sarajevo'
    europe_saratov = 'Europe/Saratov'
    europe_simferopol = 'Europe/Simferopol'
    europe_skopje = 'Europe/Skopje'
    europe_sofia = 'Europe/Sofia'
    europe_stockholm = 'Europe/Stockholm'
    europe_tallinn = 'Europe/Tallinn'
    europe_tirane = 'Europe/Tirane'
    europe_ulyanovsk = 'Europe/Ulyanovsk'
    europe_uzhgorod = 'Europe/Uzhgorod'
    europe_vaduz = 'Europe/Vaduz'
    europe_vatican = 'Europe/Vatican'
    europe_vienna = 'Europe/Vienna'
    europe_vilnius = 'Europe/Vilnius'
    europe_volgograd = 'Europe/Volgograd'
    europe_warsaw = 'Europe/Warsaw'
    europe_zagreb = 'Europe/Zagreb'
    europe_zaporozhye = 'Europe/Zaporozhye'
    europe_zurich = 'Europe/Zurich'
    indian_antananarivo = 'Indian/Antananarivo'
    indian_chagos = 'Indian/Chagos'
    indian_christmas = 'Indian/Christmas'
    indian_cocos = 'Indian/Cocos'
    indian_comoro = 'Indian/Comoro'
    indian_kerguelen = 'Indian/Kerguelen'
    indian_mahe = 'Indian/Mahe'
    indian_maldives = 'Indian/Maldives'
    indian_mauritius = 'Indian/Mauritius'
    indian_mayotte = 'Indian/Mayotte'
    indian_reunion = 'Indian/Reunion'
    pacific_apia = 'Pacific/Apia'
    pacific_auckland = 'Pacific/Auckland'
    pacific_bougainville = 'Pacific/Bougainville'
    pacific_chatham = 'Pacific/Chatham'
    pacific_chuuk = 'Pacific/Chuuk'
    pacific_easter = 'Pacific/Easter'
    pacific_efate = 'Pacific/Efate'
    pacific_enderbury = 'Pacific/Enderbury'
    pacific_fakaofo = 'Pacific/Fakaofo'
    pacific_fiji = 'Pacific/Fiji'
    pacific_funafuti = 'Pacific/Funafuti'
    pacific_galapagos = 'Pacific/Galapagos'
    pacific_gambier = 'Pacific/Gambier'
    pacific_guadalcanal = 'Pacific/Guadalcanal'
    pacific_guam = 'Pacific/Guam'
    pacific_honolulu = 'Pacific/Honolulu'
    pacific_kiritimati = 'Pacific/Kiritimati'
    pacific_kosrae = 'Pacific/Kosrae'
    pacific_kwajalein = 'Pacific/Kwajalein'
    pacific_majuro = 'Pacific/Majuro'
    pacific_marquesas = 'Pacific/Marquesas'
    pacific_midway = 'Pacific/Midway'
    pacific_nauru = 'Pacific/Nauru'
    pacific_niue = 'Pacific/Niue'
    pacific_norfolk = 'Pacific/Norfolk'
    pacific_noumea = 'Pacific/Noumea'
    pacific_pago_pago = 'Pacific/Pago_Pago'
    pacific_palau = 'Pacific/Palau'
    pacific_pitcairn = 'Pacific/Pitcairn'
    pacific_pohnpei = 'Pacific/Pohnpei'
    pacific_port_moresby = 'Pacific/Port_Moresby'
    pacific_rarotonga = 'Pacific/Rarotonga'
    pacific_saipan = 'Pacific/Saipan'
    pacific_tahiti = 'Pacific/Tahiti'
    pacific_tarawa = 'Pacific/Tarawa'
    pacific_tongatapu = 'Pacific/Tongatapu'
    pacific_wake = 'Pacific/Wake'
    pacific_wallis = 'Pacific/Wallis'
    utc = 'UTC'


class EnumerationEnum67(Enum):
    ingress_only = 'ingress-only'
    egress_only = 'egress-only'
    ingress_egress = 'ingress-egress'


class EnumerationEnum68(Enum):
    unused = 'unused'
    prs = 'prs'
    stu = 'stu'
    st2 = 'st2'
    tnc = 'tnc'
    st3e = 'st3e'
    st3 = 'st3'
    prc = 'prc'
    ssua = 'ssua'
    ssub = 'ssub'
    sec = 'sec'
    eec1 = 'eec1'
    eec2 = 'eec2'


class EnumerationEnum69(Enum):
    unknown = 'unknown'
    prs = 'prs'
    stu = 'stu'
    st2 = 'st2'
    tnc = 'tnc'
    st3e = 'st3e'
    st3 = 'st3'
    smc = 'smc'
    st4 = 'st4'
    dus = 'dus'
    prc = 'prc'
    ssua = 'ssua'
    ssub = 'ssub'
    sec = 'sec'
    dnu = 'dnu'
    inv = 'inv'
    pno = 'pno'
    eec1 = 'eec1'
    eec2 = 'eec2'
    failed = 'failed'


class EnumerationEnum7(Enum):
    hiba_chk = 'hiba-chk'


class EnumerationEnum70(Enum):
    qualified = 'qualified'
    not_qualified = 'not-qualified'


class EnumerationEnum71(Enum):
    not_applicable = 'not-applicable'
    los = 'los'
    ssm_quality = 'ssm-quality'
    out_of_range = 'out-of-range'
    wtr = 'wtr'
    admin_disabled = 'admin-disabled'


class EnumerationEnum72(Enum):
    sdh = 'sdh'
    sonet = 'sonet'


class EnumerationEnum73(Enum):
    field_1 = '1'
    field_2 = '2'
    field_3 = '3'
    field_4 = '4'
    field_5 = '5'
    internal = 'internal'


class EnumerationEnum74(Enum):
    not_present = 'not-present'
    master_free_run = 'master-free-run'
    master_holdover = 'master-holdover'
    master_locked = 'master-locked'
    slave = 'slave'
    acquiring = 'acquiring'


class EnumerationEnum75(Enum):
    itug8275dot1 = 'itug8275dot1'
    itug8275dot2 = 'itug8275dot2'


class EnumerationEnum76(Enum):
    bc = 'bc'


class EnumerationEnum77(Enum):
    not_applicable = 'not-applicable'
    initial = 'initial'
    acquiring = 'acquiring'
    holdover = 'holdover'
    locked = 'locked'


class EnumerationEnum78(Enum):
    not_applicable = 'not-applicable'
    initial = 'initial'
    acquiring = 'acquiring'
    phase_tracking = 'phase-tracking'
    holdover = 'holdover'
    locked = 'locked'


class EnumerationEnum79(Enum):
    atomic_clock = 'atomic-clock'
    gps = 'gps'
    terrestrial_radio = 'terrestrial-radio'
    ptp = 'ptp'
    ntp = 'ntp'
    hand_set = 'hand-set'
    other = 'other'
    internal_oscillator = 'internal-oscillator'
    reserved = 'reserved'


class EnumerationEnum8(Enum):
    ssh_rsa_3076 = 'ssh-rsa-3076'
    ecdsa_sha2_nistp256 = 'ecdsa-sha2-nistp256'
    ecdsa_sha2_nistp521 = 'ecdsa-sha2-nistp521'
    ssh_ed25519 = 'ssh-ed25519'
    ssh_rsa_2048 = 'ssh-rsa-2048'
    ssh_rsa_4096 = 'ssh-rsa-4096'


class EnumerationEnum80(Enum):
    initializing = 'initializing'
    faulty = 'faulty'
    disabled = 'disabled'
    listening = 'listening'
    pre_master = 'pre-master'
    master = 'master'
    passive = 'passive'
    uncalibrated = 'uncalibrated'
    slave = 'slave'


class EnumerationEnum81(Enum):
    forwardable = 'forwardable'
    non_forwardable = 'non-forwardable'


class EnumerationEnum82(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum83(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum84(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum85(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum86(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum87(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum88(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum89(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum9(Enum):
    idevid = 'idevid'
    oidevid = 'oidevid'


class EnumerationEnum90(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum91(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum92(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum93(Enum):
    pending = 'pending'
    granted = 'granted'
    denied = 'denied'
    expired = 'expired'
    canceled = 'canceled'


class EnumerationEnum94(Enum):
    gnss_a = 'gnss-a'
    gnss_b = 'gnss-b'


class EnumerationEnum95(Enum):
    unknown = 'unknown'
    locked = 'locked'
    not_locked = 'not-locked'


class EnumerationEnum96(Enum):
    unknown = 'unknown'
    unsupported = 'unsupported'
    ok = 'ok'
    over_current = 'over-current'
    under_current = 'under-current'
    no_bias_voltage = 'no-bias-voltage'


class AcctzContainer(BaseModel):
    """
    Top-level container for acctz accounting
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    history_size: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:history-size',
            ge=1,
            le=100000,
            title='History-sizeLeaf',
        ),
    ] = 1000
    """
    Size of the kept accounting events history
    """


class AsicLoopbackCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    asic_loopback: Annotated[
        Optional[AsicLoopbackContainer],
        Field(alias='srl_nokia-packet-link-qual:asic-loopback'),
    ] = None


class BannerContainer(BaseModel):
    """
    Contains configuration and state related to system banners
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    login_banner: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-banner:login-banner', title='Login-bannerLeaf'),
    ] = None
    """
    Banner to display before a user has authenticated
    """
    motd_banner: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-banner:motd-banner', title='Motd-bannerLeaf'),
    ] = None
    """
    Banner to display after a user has authenticated
    """


class BgpAutoDiscoveryContainer3(BaseModel):
    """
    Enclosing container for BGP auto discovery
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bgp_peer_addresses: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-lldp:bgp-peer-addresses')
    ] = []
    """
    List of IP address learned from neighbor for BGP auto discovery
    """
    group_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:group-id', ge=0, le=4294967295, title='Group-idLeaf3'
        ),
    ] = None
    """
    A four byte integer to send on outgoing LLDPDUs, this value can be used on the remote
    end to do peer group association. This sub-TLV is not sent by default
    """


class BgpContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    restart_max_wait: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-bgp:restart-max-wait',
            ge=0,
            le=3600,
            title='Restart-max-waitLeaf',
        ),
    ] = 600
    """
    The maximum amount of time that BGP will wait to receive End of RIB markers from all peers and for all address families that were up prior to restart.

    After this time elapses BGP declares that convergence has occurred and sends its own EOR markers to its peers.
    """


class CapabilitiesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ac_df: Annotated[
        Optional[EnumerationEnum35],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ac-df',
            title='Ac-dfLeaf',
        ),
    ] = 'include'
    """
    Attachment Circuit influenced DF Election.
    """
    non_revertive: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:non-revertive',
            title='Non-revertiveLeaf',
        ),
    ] = False
    """
    Non Revertive mode. If set to true, the 'Don't Preempt Me' capability is advertised in the ES route.
    """


class CapabilityListEntry(BaseModel):
    """
    List of LLDP system capabilities advertised by the neighbor
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[Any], Field(alias='srl_nokia-lldp:name', title='NameLeaf27')
    ] = None
    """
    Name of the system capability advertised by the neighbor

    Capabilities are represented in a bitmap that defines the
    primary functions of the system. The capabilities are
    defined in IEEE 802.1AB.
    """
    enabled: Annotated[
        Optional[bool], Field(alias='srl_nokia-lldp:enabled', title='EnabledLeaf')
    ] = None
    """
    Indicates whether the corresponding system capability is enabled on the neighbor
    """


class CliContainer(BaseModel):
    """
    Top-level container for cli plugin configuration
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    load_global_plugins: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-aaa:load-global-plugins', title='Load-global-pluginsLeaf'
        ),
    ] = True
    """
    Specifies whether cli should load plugins from global plugin directory (from /etc/opt/srlinux/cli/plugins/).
    """
    load_user_plugins: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-aaa:load-user-plugins', title='Load-user-pluginsLeaf'),
    ] = True
    """
    Specifies whether cli should load plugins from user home directory (from ~/cli/plugins/).
    """
    deny_command_list: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:deny-command-list')
    ] = []
    """
    List of cli commands that are denied for this role

    Python style regular expressions are supported. Every item is left anchored (it matches from the beginning
    of line). Empty deny-command-list means anything that is not in allow-command-list is denied. If both lists
    are empty then everything is allowed.
    """
    allow_command_list: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:allow-command-list')
    ] = []
    """
    List of cli commands that are allowed for this role

    Python style regular expressions are supported. Every item is left anchored (it matches from the beginning
    of line). Empty allow-command-list means anything that is not in deny-command-list is allowed. If both
    lists are empty then everything is allowed.
    """


class ClockQualityContainer(BaseModel):
    """
    The clockQuality of the local clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_class: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:clock-class', ge=0, le=255, title='Clock-classLeaf'
        ),
    ] = None
    """
    The clockClass denotes the traceability of the time or frequency distributed by the clock
    """
    clock_accuracy: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:clock-accuracy',
            ge=0,
            le=255,
            title='Clock-accuracyLeaf',
        ),
    ] = None
    """
    The clockAccuracy indicates the expected accuracy of the clock
    """
    offset_scaled_log_variance: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:offset-scaled-log-variance',
            ge=0,
            le=65535,
            title='Offset-scaled-log-varianceLeaf',
        ),
    ] = None
    """
    The offsetScaledLogVariance provides an estimate of the variations of the clock
    """


class ComplexityRulesContainer(BaseModel):
    """
    Top-level container for password complexity rules
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    minimum_length: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:minimum-length',
            ge=1,
            le=12,
            title='Minimum-lengthLeaf',
        ),
    ] = 1
    """
    The minimum length of the password for local users, including admin and linuxadmin
    """
    maximum_length: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:maximum-length',
            ge=1,
            le=1023,
            title='Maximum-lengthLeaf',
        ),
    ] = 1023
    """
    The maximum length of the password for local users, including admin and linuxadmin
    """
    minimum_lowercase: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:minimum-lowercase',
            ge=0,
            le=10,
            title='Minimum-lowercaseLeaf',
        ),
    ] = 0
    """
    The minimum lowercase characters from (a-z) that the user password must include

    A value of 0 results in no minimum-lowercase being enforced.
    """
    minimum_uppercase: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:minimum-uppercase',
            ge=0,
            le=10,
            title='Minimum-uppercaseLeaf',
        ),
    ] = 0
    """
    The minimum uppercase characters from (A-Z) that the user password must include

    A value of 0 results in no minimum-uppercase being enforced.
    """
    minimum_numeric: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:minimum-numeric',
            ge=0,
            le=10,
            title='Minimum-numericLeaf',
        ),
    ] = 0
    """
    The minimum numeric digits that the user password must include

    A value of 0 results in no minimum-numeric being enforced.
    """
    minimum_special_character: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:minimum-special-character',
            ge=0,
            le=10,
            title='Minimum-special-characterLeaf',
        ),
    ] = 0
    """
    The minimum special characters that the user password must include

    A value of 0 results in no minimum-special-character being enforced.
    """
    allow_username: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-aaa:allow-username', title='Allow-usernameLeaf'),
    ] = True
    """
    Enable or disable using username as part of the user password
    """


class ConstellationContainer(BaseModel):
    """
    Selects which constellations to be used for GNSS
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    gps: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:gps', title='GpsLeaf')
    ] = True
    galileo: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:galileo', title='GalileoLeaf')
    ] = False


class CustomTlvListEntry(BaseModel):
    """
    List of custom LLDP TLVs from a neighbor
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:type',
            ge=-2147483648,
            le=2147483647,
            title='TypeLeaf12',
        ),
    ] = None
    """
    The integer value identifying the type of information
    contained in the value field.
    """
    oui: Annotated[
        Optional[str], Field(alias='srl_nokia-lldp:oui', title='OuiLeaf')
    ] = None
    """
    The organizationally unique identifier field from the custom TLV

    This field shall contain the organization's OUI as defined in
    Clause 9 of IEEE Std 802. The high-order octet is 0 and the
    low-order 3 octets are the SMI Network Management Private Enterprise
    Code of the Vendor in network byte order, as defined in the
    'Assigned Numbers' RFC [RFC3232].
    """
    oui_subtype: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:oui-subtype', title='Oui-subtypeLeaf'),
    ] = None
    """
    The subtype value defined by the OUI for this custom TLV

    The organizationally defined subtype field shall contain a
    unique subtype value assigned by the defining organization.
    """
    value: Annotated[
        Optional[bytes],
        Field(
            alias='srl_nokia-lldp:value',
            max_length=18446744073709551615,
            title='ValueLeaf3',
        ),
    ] = None
    """
    A variable-length octet-string containing the value for this TLV
    """


class DateAndTimeDeltaType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$'
        ),
    ]
    """
    When this type is used to store a date and time, show routines should display it as a delta
    with respect to the current date and time in the format 'dddd:hh:mm:ss ago' (for a past
    event) or 'in dddd:hh:mm:ss' (future event), where dddd is the number of days, hh is the
    number of  hours, mm is the number of  minutes and ss is the number of seconds.
    """


class DiscardsContainer(BaseModel):
    """
    Aggregate discard statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_domain: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:bad-domain',
            ge=0,
            le=4294967295,
            title='Bad-domainLeaf',
        ),
    ] = None
    """
    Specifies the number of bad domain messages that were discarded
    """
    alternate_master: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:alternate-master',
            ge=0,
            le=4294967295,
            title='Alternate-masterLeaf',
        ),
    ] = None
    """
    Specifies the number of alternate master messages that were discarded
    """
    out_of_sequence: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:out-of-sequence',
            ge=0,
            le=4294967295,
            title='Out-of-sequenceLeaf',
        ),
    ] = None
    """
    Specifies the number of out of sequence messages that were discarded
    """
    peer_disabled: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:peer-disabled',
            ge=0,
            le=4294967295,
            title='Peer-disabledLeaf',
        ),
    ] = None
    """
    Specifies the number of PTP messages that were discarded from disabled PTP peer

    Occurs when a PTP peer has been administratively disabled.
    This information is only available for configured and discovered peers.
    """
    other: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:other', ge=0, le=4294967295, title='OtherLeaf'),
    ] = None
    """
    Specifies the number of other messages that were discarded
    """


class DiscardsContainer2(BaseModel):
    """
    Aggregate discard statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_domain: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:bad-domain',
            ge=0,
            le=4294967295,
            title='Bad-domainLeaf2',
        ),
    ] = None
    """
    Specifies the number of bad domain messages that were discarded
    """
    alternate_master: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:alternate-master',
            ge=0,
            le=4294967295,
            title='Alternate-masterLeaf2',
        ),
    ] = None
    """
    Specifies the number of alternate master messages that were discarded
    """
    out_of_sequence: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:out-of-sequence',
            ge=0,
            le=4294967295,
            title='Out-of-sequenceLeaf2',
        ),
    ] = None
    """
    Specifies the number of out of sequence messages that were discarded
    """
    peer_disabled: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:peer-disabled',
            ge=0,
            le=4294967295,
            title='Peer-disabledLeaf2',
        ),
    ] = None
    """
    Specifies the number of PTP messages that were discarded from disabled PTP peer

    Occurs when a PTP peer has been administratively disabled.
    This information is only available for configured and discovered peers.
    """
    other: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:other', ge=0, le=4294967295, title='OtherLeaf2'),
    ] = None
    """
    Specifies the number of other messages that were discarded
    """


class DiscardsContainer3(BaseModel):
    """
    Aggregate discard statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_domain: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:bad-domain',
            ge=0,
            le=4294967295,
            title='Bad-domainLeaf3',
        ),
    ] = None
    """
    Specifies the number of bad domain messages that were discarded
    """
    alternate_master: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:alternate-master',
            ge=0,
            le=4294967295,
            title='Alternate-masterLeaf3',
        ),
    ] = None
    """
    Specifies the number of alternate master messages that were discarded
    """
    out_of_sequence: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:out-of-sequence',
            ge=0,
            le=4294967295,
            title='Out-of-sequenceLeaf3',
        ),
    ] = None
    """
    Specifies the number of out of sequence messages that were discarded
    """
    peer_disabled: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:peer-disabled',
            ge=0,
            le=4294967295,
            title='Peer-disabledLeaf3',
        ),
    ] = None
    """
    Specifies the number of PTP messages that were discarded from disabled PTP peer

    Occurs when a PTP peer has been administratively disabled.
    This information is only available for configured and discovered peers.
    """
    other: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:other', ge=0, le=4294967295, title='OtherLeaf3'),
    ] = None
    """
    Specifies the number of other messages that were discarded
    """


class DiscardsContainer4(BaseModel):
    """
    Aggregate discard statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bad_domain: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:bad-domain',
            ge=0,
            le=4294967295,
            title='Bad-domainLeaf4',
        ),
    ] = None
    """
    Specifies the number of bad domain messages that were discarded
    """
    alternate_master: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:alternate-master',
            ge=0,
            le=4294967295,
            title='Alternate-masterLeaf4',
        ),
    ] = None
    """
    Specifies the number of alternate master messages that were discarded
    """
    out_of_sequence: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:out-of-sequence',
            ge=0,
            le=4294967295,
            title='Out-of-sequenceLeaf4',
        ),
    ] = None
    """
    Specifies the number of out of sequence messages that were discarded
    """
    peer_disabled: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:peer-disabled',
            ge=0,
            le=4294967295,
            title='Peer-disabledLeaf4',
        ),
    ] = None
    """
    Specifies the number of PTP messages that were discarded from disabled PTP peer

    Occurs when a PTP peer has been administratively disabled.
    This information is only available for configured and discovered peers.
    """
    other: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:other', ge=0, le=4294967295, title='OtherLeaf4'),
    ] = None
    """
    Specifies the number of other messages that were discarded
    """


class EventListEntry(BaseModel):
    """
    List of events subject to accounting
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    event_type: Annotated[
        Optional[Any], Field(alias='srl_nokia-aaa:event-type', title='Event-typeLeaf')
    ] = None
    """
    The type of activity to record at the accounting server
    """
    record: Annotated[
        Optional[Any], Field(alias='srl_nokia-aaa:record', title='RecordLeaf')
    ] = None
    """
    Type of record to send to the accounting server for this activity type
    """


class EviListEntry(BaseModel):
    """
    evi range for this ethernet-segment association
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:start',
            ge=1,
            le=65535,
            title='StartLeaf3',
        ),
    ] = None
    """
    start of the evi-range for this ethernet-segment
    """


class ForwardingComplexContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[Optional[str], Field(alias='srl_nokia-grpc:id', title='IdLeaf4')] = (
        None
    )
    """
    The normalized ID for this forwarding-complex

    This is the slot number and complex number seperated by a '/', 0 indexed. For example '1/0', or '1/1' representing two forwarding complexes on slot 1.
    """
    device: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:device',
            ge=0,
            le=18446744073709551615,
            title='DeviceLeaf',
        ),
    ] = None
    """
    The P4Runtime ID of the forwarding complex for which this client has established itself

    This is the value configured at /platform/linecard/forwarding-complex/p4rt/id, or a system derived default.
    """
    slot: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:slot', ge=0, le=255, title='SlotLeaf'),
    ] = None
    """
    The linecard slot for which this forwarding complex resides on
    """


class GnmiContainer(BaseModel):
    """
    Container for gnmi configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    commit_confirmed_timeout: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:commit-confirmed-timeout',
            ge=0,
            le=86400,
            title='Commit-confirmed-timeoutLeaf',
        ),
    ] = 0
    """
    Number of seconds to wait for confirmation

    A value of 0 means commit confirmed is not used
    """
    commit_save: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-grpc:commit-save', title='Commit-saveLeaf'),
    ] = False
    """
    Specifies whether to save startup configuration after every successful commit
    """
    include_defaults_in_config_only_responses: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-grpc:include-defaults-in-config-only-responses',
            title='Include-defaults-in-config-only-responsesLeaf',
        ),
    ] = False
    """
    Specifies whether to include field default values in get/subscribe responses when
    using configuration only datastore (for example running/intended datastore)
    """


class GnssCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    gnss: Annotated[Optional[GnssContainer], Field(alias='srl_nokia-sync:gnss')] = None


class GrandmasterClockQualityContainer(BaseModel):
    """
    The clockQuality of the grandmaster clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_class: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:clock-class', ge=0, le=255, title='Clock-classLeaf2'
        ),
    ] = None
    """
    The clockClass denotes the traceability of the time or frequency distributed by the clock
    """
    clock_accuracy: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:clock-accuracy',
            ge=0,
            le=255,
            title='Clock-accuracyLeaf2',
        ),
    ] = None
    """
    The clockAccuracy indicates the expected accuracy of the clock
    """
    offset_scaled_log_variance: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:offset-scaled-log-variance',
            ge=0,
            le=65535,
            title='Offset-scaled-log-varianceLeaf2',
        ),
    ] = None
    """
    The offsetScaledLogVariance provides an estimate of the variations of the clock
    """


class GrandmasterClockQualityContainer2(BaseModel):
    """
    The clock quality of the grandmaster clock in the last Announce message received from this peer
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_class: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:clock-class', ge=0, le=255, title='Clock-classLeaf3'
        ),
    ] = None
    """
    The clockClass denotes the traceability of the time or frequency distributed by the clock
    """
    clock_accuracy: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:clock-accuracy',
            ge=0,
            le=255,
            title='Clock-accuracyLeaf3',
        ),
    ] = None
    """
    The clockAccuracy indicates the expected accuracy of the clock
    """
    offset_scaled_log_variance: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:offset-scaled-log-variance',
            ge=0,
            le=65535,
            title='Offset-scaled-log-varianceLeaf3',
        ),
    ] = None
    """
    The offsetScaledLogVariance provides an estimate of the variations of the clock
    """


class Icmp6Container(BaseModel):
    """
    Context for system-wide control of ICMPv6 message generation
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rate_limit_per_host: Annotated[
        Optional[RateLimitPerHostContainer2],
        Field(alias='srl_nokia-system-datapath:rate-limit-per-host'),
    ] = None


class IcmpContainer(BaseModel):
    """
    Context for system-wide control of ICMP message generation
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rate_limit_per_host: Annotated[
        Optional[RateLimitPerHostContainer],
        Field(alias='srl_nokia-system-datapath:rate-limit-per-host'),
    ] = None


class InstanceListEntry4(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:instance-number',
            ge=0,
            le=255,
            title='Instance-numberLeaf2',
        ),
    ] = None
    """
    Information regarding each SV (Space Vehicle)
    """
    constellation: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:constellation', title='ConstellationLeaf'),
    ] = None
    """
    Constellation of the SV (Space Vehicle)
    """
    prn: Annotated[
        Optional[int], Field(alias='srl_nokia-sync:prn', ge=0, le=255, title='PrnLeaf')
    ] = None
    """
    Pseudo Random Number (PRN) of the Space Vehicle

    This represents the satellite's unique pseudorandom noise code
    """
    band: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:band', title='BandLeaf')
    ] = None
    """
    SV's band
    """
    signal_strength: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:signal-strength',
            ge=0,
            le=255,
            title='Signal-strengthLeaf',
        ),
    ] = None
    """
    Carrier to noise ratio in dB-Hz
    """


class Ipv4AddressType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$'
        ),
    ]
    """
    An IPv4 address in dotted quad notation.
    """


class Ipv6AddressType(RootModel[str]):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    root: Annotated[
        str,
        Field(
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$'
        ),
    ]
    """
    An IPv6 address represented as either a full address; shortened
    or mixed-shortened formats.
    """


class LacpContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    system_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lacp:system-priority',
            ge=0,
            le=65535,
            title='System-priorityLeaf',
        ),
    ] = None
    """
    System priority used by the node on this LAG interface.
    Lower value is higher priority for determining which node
    is the controlling system.
    """
    system_id: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lacp:system-id',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
            title='System-idLeaf',
        ),
    ] = None
    """
    The MAC address portion of the node's System ID. This is
    combined with the system priority to construct the 8-octet
    system-id
    """


class LldpContainer2(BaseModel):
    """
    Container for LLDP.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='In-tunneled-packetsLeaf2',
        ),
    ] = 0
    """
    System level incoming Link Layer Discovery Protocol tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled LLDP frames. LLDP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0e and EtherType value
    of 0x88cc.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='In-trap-to-cpu-packetsLeaf2',
        ),
    ] = 0
    """
    System level incoming Link Layer Discovery Protocol frames copied to CPU.

    Cumulative of all Ethernet interfaces including all the copy-to-cpu LLDP frames. LLDP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0e and EtherType value
    of 0x88cc.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf5',
        ),
    ] = None
    """
    Timestamp of the last time the LACP counters were cleared.
    """


class LocalLinuxUsersContainer(BaseModel):
    """
    Enclosing container for local linux users
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    disable_login: Annotated[
        Optional[List[EnumerationEnum10]], Field(alias='srl_nokia-aaa:disable-login')
    ] = []
    """
    disable the loging for all local linux users via remote login or remote login and console
    """


class LockoutPolicyContainer(BaseModel):
    """
    Top-level container for lockout policy
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    attempts: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:attempts', ge=0, le=64, title='AttemptsLeaf'),
    ] = 0
    """
    The number of failed login attempts that will lock the account

    A value of 0 means unlimited number of failed login attempts is allowed
    """
    time: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:time', ge=0, le=1440, title='TimeLeaf'),
    ] = 1
    """
    The time period in minutes within which the failed login attempts occur
    """
    lockout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:lockout', ge=0, le=1440, title='LockoutLeaf'),
    ] = 15
    """
    The time duration in minutes the user account will be locked out

    A value of 0 means that the user account will be locked out/disabled indefinitely
    """


class MacLearningContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mac_relearn_only: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-system-bridge-table:mac-relearn-only',
            title='Mac-relearn-onlyLeaf',
        ),
    ] = None
    """
    The value of this leaf indicates that the system will not
    learn any new mac addresses, but will relearn any that are already
    programmed
    """


class MacLimitContainer(BaseModel):
    """
    Bridge Table size and thresholds.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    maximum_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:maximum-entries',
            ge=-2147483648,
            le=2147483647,
            title='Maximum-entriesLeaf',
        ),
    ] = None
    """
    Maximum number of mac addresses allowed in the system bridge-table.
    """
    warning_threshold_pct: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:warning-threshold-pct',
            ge=-2147483648,
            le=2147483647,
            title='Warning-threshold-pctLeaf',
        ),
    ] = None
    """
    Percentage of the configured max-number-macs over which a warning is triggered.
    The warning message is cleared when the percentage drops below the configured
    percentage minus 5%
    """


class MulticastMsgRateContainer(BaseModel):
    """
    Aggregate multicast message rates for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:anno-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Anno-msg-rate-txLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of announce messages transmitted
    """
    anno_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:anno-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Anno-msg-rate-rxLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of announce messages received
    """
    sync_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:sync-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Sync-msg-rate-txLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of sync messages transmitted
    """
    sync_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:sync-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Sync-msg-rate-rxLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of sync messages received
    """
    del_req_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-req-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Del-req-msg-rate-txLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of delay-req messages transmitted
    """
    del_req_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-req-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Del-req-msg-rate-rxLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of delay-req messages received
    """
    del_resp_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Del-resp-msg-rate-txLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of delay-resp messages transmitted
    """
    del_resp_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Del-resp-msg-rate-rxLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of delay-resp messages received
    """
    follow_up_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Follow-up-msg-rate-txLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of follow-up messages transmitted
    """
    follow_up_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Follow-up-msg-rate-rxLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of follow-up messages received
    """
    signaling_msg_rate_tx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:signaling-msg-rate-tx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Signaling-msg-rate-txLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of signaling messages transmitted
    """
    signaling_msg_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:signaling-msg-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Signaling-msg-rate-rxLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of signaling messages received
    """
    other_rate_rx: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:other-rate-rx',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Other-rate-rxLeaf2',
        ),
    ] = None
    """
    Specifies the rate of messages of other messages received
    """


class NameContainer(BaseModel):
    """
    Contains configuration and state related to system naming
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    domain_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-name:domain-name',
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$',
            title='Domain-nameLeaf',
        ),
    ] = None
    """
    The system domain name
    """
    host_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-name:host-name',
            pattern='^(?=^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\\-]*[A-Za-z0-9])$).*$',
            title='Host-nameLeaf',
        ),
    ] = None
    """
    The system host name
    """


class NeighborListListEntry(BaseModel):
    """
    List of MAC address of all the neighbors of this port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_identity: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:clock-identity',
            max_length=8,
            min_length=8,
            title='Clock-identityLeaf3',
        ),
    ] = None
    """
    The clockIdentity of this neighbor clock
    """
    port_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:port-number', ge=0, le=65535, title='Port-numberLeaf2'
        ),
    ] = None
    """
    The port number of this neighbor clock
    """
    mac_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:mac-address',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
            title='Mac-addressLeaf2',
        ),
    ] = None
    """
    Specifies the MAC address of this neighbor
    """
    rx_message_rate: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:rx-message-rate',
            ge=-9.223372036854776e17,
            le=9.223372036854776e17,
            title='Rx-message-rateLeaf',
        ),
    ] = None
    """
    The receive message rate from this neighbor clock
    """
    parent_clock: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:parent-clock', title='Parent-clockLeaf2'),
    ] = None
    """
    Indicates if this neighbor is the current parent clock of this PTP clock
    """
    no_port_timestamping: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-sync:no-port-timestamping',
            title='No-port-timestampingLeaf',
        ),
    ] = None
    """
    Indicates that the last PTP event message exchanged with this neighbor did not get timestamped at the port

    This is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping
    """


class NetconfContainer(BaseModel):
    """
    Top-level container for netconf plugin configuration
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    allowed_operations: Annotated[
        Optional[List[EnumerationEnum13]],
        Field(alias='srl_nokia-aaa:allowed-operations'),
    ] = []
    """
    List of netconf operation, that are allowed for this role. Rest of the operations are denied.
    """


class OverloadContainer(BaseModel):
    """
    Container for ISIS overload configurations.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    set_bit: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-maintenance-mode:set-bit', title='Set-bitLeaf'),
    ] = False
    """
    When set to true, the Overload bit is set
    """
    max_metric: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-maintenance-mode:max-metric', title='Max-metricLeaf'),
    ] = False
    """
    When set to true transit links are advertised with a wide metric of 0xffffffe and a narrow metric of 0x3f
    """


class P4rtContainer(BaseModel):
    """
    Container for P4RT related session info
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    primary: Annotated[
        Optional[bool], Field(alias='srl_nokia-grpc:primary', title='PrimaryLeaf')
    ] = None
    """
    Indicates if this client is the primary for the specified forwarding complex

    Only a single primary per forwarding complex is supported
    """
    forwarding_complex: Annotated[
        Optional[ForwardingComplexContainer],
        Field(alias='srl_nokia-grpc:forwarding-complex'),
    ] = None


class PacketGeneratorContainer(BaseModel):
    """
    Packet generator endpoint
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    packet_rate: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:packet-rate',
            ge=1,
            le=4294967295,
            title='Packet-rateLeaf',
        ),
    ]
    """
    Packet rate of the packet generator
    """
    packet_size: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:packet-size',
            ge=64,
            le=8184,
            title='Packet-sizeLeaf',
        ),
    ]
    """
    Packet size (in bytes) of the packet generator
    """


class ParentPortIdentityContainer(BaseModel):
    """
    The portIdentity of the port on the master
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    clock_identity: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:clock-identity',
            max_length=8,
            min_length=8,
            title='Clock-identityLeaf2',
        ),
    ] = None
    """
    Identity of the parent clock
    """
    port_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:port-number', ge=0, le=65535, title='Port-numberLeaf'
        ),
    ] = None
    """
    Port number of the parent clock
    """


class PasswordContainer4(BaseModel):
    """
    Top-level container for policies around user passwords
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    complexity_rules: Annotated[
        Optional[ComplexityRulesContainer],
        Field(alias='srl_nokia-aaa:complexity-rules'),
    ] = None
    lockout_policy: Annotated[
        Optional[LockoutPolicyContainer], Field(alias='srl_nokia-aaa:lockout-policy')
    ] = None
    hash_method: Annotated[
        Optional[EnumerationEnum11],
        Field(alias='srl_nokia-aaa:hash-method', title='Hash-methodLeaf'),
    ] = None
    """
    The hash algorithm for the passwords entered as plain text

    If no value is configured, then Yescrypt will be used as the hash algorithm unless overriden for specific leafs
    using the srl_nokia-extensions:hash-algorithm yang extension. The Argon2 (ar2) hash algorithm is not supported
    for the linuxadmin user and if selected then the linuxadmin password will be hashed using Yescrypt.
    """
    aging: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:aging', ge=0, le=500, title='AgingLeaf'),
    ] = 0
    """
    Expire user passwords after this period

    A value of 0 means that the user passwords do not expire
    """
    change_on_first_login: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-aaa:change-on-first-login',
            title='Change-on-first-loginLeaf',
        ),
    ] = False
    """
    Enable or disable a user being forced to change their password on first time login
    """
    history: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:history', ge=0, le=20, title='HistoryLeaf'),
    ] = 0
    """
    Defines how many previous passwords a new password is matched against, such that a new password can't be one of the previous n passwords
    """
    require_ntp_sync: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-aaa:require-ntp-sync', title='Require-ntp-syncLeaf'),
    ] = True
    """
    Enable or disable dependence of password aging and user lockout on NTP sync status
    """


class PathsListEntry(BaseModel):
    """
    List of paths being subscribed to
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        Optional[int], Field(alias='srl_nokia-grpc:id', ge=0, le=65535, title='IdLeaf3')
    ] = None
    """
    System generated ID for the subscribed path (within subscription)
    """
    path: Annotated[
        Optional[str], Field(alias='srl_nokia-grpc:path', title='PathLeaf')
    ] = None
    """
    Path being subscribed to
    """
    mode: Annotated[
        Optional[EnumerationEnum17],
        Field(alias='srl_nokia-grpc:mode', title='ModeLeaf'),
    ] = None
    """
    Subscription mode (on-change, sample, target-defined, poll, once)
    """
    sample_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:sample-interval',
            ge=0,
            le=18446744073709551615,
            title='Sample-intervalLeaf',
        ),
    ] = None
    """
    Time in seconds to provide updates to the remote host, set to 0 for all subscription modes except SAMPLE
    """


class PfcpContainer(BaseModel):
    """
    Configuration related to the PFCP interface between mag-c and upf
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    shared_secret: Annotated[
        str,
        Field(
            alias='srl_nokia-lawful-intercept:shared-secret', title='Shared-secretLeaf'
        ),
    ]
    """
    Shared secret between mag-c and upf
    """


class PreferenceAlgContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    preference_value: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:preference-value',
            ge=0,
            le=65535,
            title='Preference-valueLeaf',
        ),
    ] = 32767
    """
    Preference that is used to elect the designated forwarder
    """
    oper_preference_value: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-preference-value',
            ge=0,
            le=4294967295,
            title='Oper-preference-valueLeaf',
        ),
    ] = None
    """
    Operational Preference value
    """
    oper_do_not_prempt: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-do-not-prempt',
            title='Oper-do-not-premptLeaf',
        ),
    ] = None
    """
    Operational do-not-preempt value
    """
    capabilities: Annotated[
        Optional[CapabilitiesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:capabilities'
        ),
    ] = None


class PrimaryEviRangeListEntry(BaseModel):
    """
    evi range for this ethernet-segment
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start_evi: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:start-evi',
            ge=1,
            le=65535,
            title='Start-eviLeaf',
        ),
    ] = None
    """
    start of the evi-range for this ethernet-segment
    """
    end_evi: Annotated[
        int,
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:end-evi',
            ge=1,
            le=65535,
            title='End-eviLeaf',
        ),
    ]
    """
    end of the evi-range for this ethernet-segment
    """


class ProtocolsContainer(BaseModel):
    """
    The routing protocols that are supported by the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bgp: Annotated[Optional[BgpContainer], Field(alias='srl_nokia-bgp:bgp')] = None


class PtpCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ptp: Annotated[Optional[PtpContainer], Field(alias='srl_nokia-sync:ptp')] = None


class PtpContainer3(BaseModel):
    """
    Container for Precision Time Protocol Peer-Delay protocol.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='In-tunneled-packetsLeaf6',
        ),
    ] = 0
    """
    System level incoming Precision Time Protocol Peer-Delay tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled PTP frames. PTP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0e and Ethertype
    value of 0x88F7.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='In-trap-to-cpu-packetsLeaf6',
        ),
    ] = 0
    """
    System level incoming Precision Time Protocol Peer-Delay frames copied to CPU.

    Cumulative of all Ethernet interfaces including all the copy-to-cpu PTP frames. PTP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0e and Ethertype
    value of 0x88F7.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf9',
        ),
    ] = None
    """
    Timestamp of the last time the PTP counters were cleared.
    """


class QosContainer(BaseModel):
    """
    Parameters describing QoS handling of system generated traffic
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    management_protocols_dscp: Annotated[
        Optional[Union[DscpValueType, EnumerationEnum4]],
        Field(
            alias='srl_nokia-qos:management-protocols-dscp',
            title='Management-protocols-dscpLeaf',
        ),
    ] = '32'
    """
    Defines dscp value the system generated traffic by management-protocols should be marked with
    """


class ReadsContainer(BaseModel):
    """
    The counter were collected while performing a read operation on the schema path.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-pathz:access-rejects',
            ge=0,
            le=18446744073709551615,
            title='Access-rejectsLeaf5',
        ),
    ] = None
    """
    The total number of times the gNSI.pathz module denied access
    to a schema path.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-rejectLeaf5',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.pathz denied access to
    a schema path.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-pathz:access-accepts',
            ge=0,
            le=18446744073709551615,
            title='Access-acceptsLeaf5',
        ),
    ] = None
    """
    The total number of times the gNSI.pathz module allowed access
    to a schema path.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-acceptLeaf5',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.pathz allowed access to
    a schema path.
    """


class RouteDistinguisherContainer(BaseModel):
    """
    Route Distinguisher (RD) of the bgp-vpn instance.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rd: Annotated[
        Optional[
            Union[
                RouteDistinguisherType0Type,
                RouteDistinguisherType1Type,
                RouteDistinguisherType2Type,
                RouteDistinguisherType2bType,
            ]
        ],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:rd', title='RdLeaf'),
    ] = None
    """
    Route Distinguisher (RD) of the system bgp-vpn instance. The RD is auto-derived
    as <ip-address>:0 where 'ip-address' is the ipv4 address associated to the subinterface lo0.1.
    """
    route_distinguisher_origin: Annotated[
        Optional[EnumerationEnum40],
        Field(
            alias='srl_nokia-system-network-instance-bgp-vpn:route-distinguisher-origin',
            title='Route-distinguisher-originLeaf',
        ),
    ] = None
    """
    Origin of the operational Route Distinguisher (RD) of the bgp-vpn instance.

     'Auto-derived-from-system-ip:0' refers to the RD for the EVPN Ethernet Segment routes that is automatically allocated with the format <ip-address>:0
     where 'ip-address' is the ipv4 address associated to the subinterface lo0.1.
    """


class RouteTargetContainer(BaseModel):
    """
    Route Target (RT) of the system bgp-vpn instance.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    export_route_target_origin: Annotated[
        Optional[EnumerationEnum41],
        Field(
            alias='srl_nokia-system-network-instance-bgp-vpn:export-route-target-origin',
            title='Export-route-target-originLeaf',
        ),
    ] = None
    """
    Origin of the operational export Route Target (RT) of the bgp-vpn instance.

     'Auto-derived-from-esi-bytes-1-6' refers to the ES-import RT for the EVPN Ethernet Segment routes that is derived from bytes 1 to 6 of the Ethernet Segment
     Identifier of the route.
    """
    import_route_target_origin: Annotated[
        Optional[EnumerationEnum42],
        Field(
            alias='srl_nokia-system-network-instance-bgp-vpn:import-route-target-origin',
            title='Import-route-target-originLeaf',
        ),
    ] = None
    """
    Origin of the operational import Route Target (RT) of the bgp-vpn instance.

     'Auto-derived-from-esi-bytes-1-6' refers to the ES-import RT for the EVPN Ethernet Segment routes that is derived from bytes 1 to 6 of the Ethernet Segment
     Identifier of the route.
    """


class RpcContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    pre_sync_duration: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:pre-sync-duration',
            ge=0,
            le=4294967295,
            title='Pre-sync-durationLeaf',
        ),
    ]
    """
    Duration of the pre-sync phase
    """
    setup_duration: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:setup-duration',
            ge=20,
            le=4294967295,
            title='Setup-durationLeaf',
        ),
    ]
    """
    Duration of the setup phase
    """
    duration: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:duration',
            ge=1,
            le=4294967295,
            title='DurationLeaf',
        ),
    ]
    """
    Duration of the test
    """
    post_sync_duration: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:post-sync-duration',
            ge=0,
            le=4294967295,
            title='Post-sync-durationLeaf',
        ),
    ]
    """
    Duration of the post-sync phase
    """
    teardown_duration: Annotated[
        int,
        Field(
            alias='srl_nokia-packet-link-qual:teardown-duration',
            ge=15,
            le=4294967295,
            title='Teardown-durationLeaf',
        ),
    ]
    """
    Duration of the teardown phase
    """


class RpcListEntry(BaseModel):
    """
    A collection of counters collected by the gNSI.authz module
    for a RPC identified by the `name`.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-authz:name', title='NameLeaf6')
    ] = None
    """
    The name of the RPC the counters were collected
    for.
    """
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-authz:access-rejects',
            ge=0,
            le=18446744073709551615,
            title='Access-rejectsLeaf2',
        ),
    ] = None
    """
    The total number of times the gNSI.authz module denied access
    to a RPC.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-authz:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-rejectLeaf2',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.authz denied access to
    a RPC.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-authz:access-accepts',
            ge=0,
            le=18446744073709551615,
            title='Access-acceptsLeaf2',
        ),
    ] = None
    """
    The total number of times the gNSI.authz module allowed access
    to a RPC.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-authz:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-acceptLeaf2',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.authz allowed access to
    a RPC.
    """


class RpcListEntry2(BaseModel):
    """
    A collection of counters collected by the gNSI.authz module
    for a RPC identified by the `name`.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str], Field(alias='srl_nokia-grpc:name', title='NameLeaf9')
    ] = None
    """
    The name of the RPC the counters were collected
    for.
    """
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:access-rejects',
            ge=0,
            le=18446744073709551615,
            title='Access-rejectsLeaf4',
        ),
    ] = None
    """
    The total number of times the gNSI.authz module denied access
    to a RPC.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-rejectLeaf4',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.authz denied access to
    a RPC.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:access-accepts',
            ge=0,
            le=18446744073709551615,
            title='Access-acceptsLeaf4',
        ),
    ] = None
    """
    The total number of times the gNSI.authz module allowed access
    to a RPC.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-acceptLeaf4',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.authz allowed access to
    a RPC.
    """


class SatellitesInUseContainer(BaseModel):
    """
    The list of satellites currently in use
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    number_of_satellites_in_use: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:number-of-satellites-in-use',
            ge=0,
            le=255,
            title='Number-of-satellites-in-useLeaf',
        ),
    ] = None
    """
    The number of satellites currently in use
    """
    instance: Annotated[
        Optional[List[InstanceListEntry4]], Field(alias='srl_nokia-sync:instance')
    ] = None


class ServerListEntry2(BaseModel):
    """
    List of NTP servers to use for system clock synchronization
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    address: Annotated[
        Optional[Union[Ipv4Type, Ipv6Type, DomainNameType]],
        Field(alias='srl_nokia-ntp:address', title='AddressLeaf4'),
    ] = None
    """
    Domain or IP address of the NTP server

    IP address may be either IPv4 or IPv6.

    Domain resolution requires working DNS configuration in the same network-instance.
    """
    iburst: Annotated[
        Optional[bool], Field(alias='srl_nokia-ntp:iburst', title='IburstLeaf')
    ] = False
    """
    Indicates whether this server should enable burst synchronization or not
    iburst, or initial burst, improves the time taken for initial synchronization
    by sending a burst of eight packets instead of the usual one, these packets are
    spaced by a two second delay
    """
    prefer: Annotated[
        Optional[bool], Field(alias='srl_nokia-ntp:prefer', title='PreferLeaf')
    ] = False
    """
    Indicates whether this server should be preferred or not
    All other things being equal, this host will be chosen for synchronization among
    a set of correctly operating NTP servers
    """
    stratum: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ntp:stratum', ge=0, le=255, title='StratumLeaf'),
    ] = None
    """
    Indicates the level of the server in the NTP hierarchy
    as number increases, the accuracy is degraded.
    Primary servers are stratum 1 while a maximum value of 16
    indicates unsynchronized. The values have the following meanings:
    0 unspecified or invalid
    1 primary server (e.g., equipped with a GPS receiver)
    2-15 secondary server (via NTP)
    16 unsynchronized
    17-255 reserved
    """
    jitter: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ntp:jitter',
            ge=0,
            le=18446744073709551615,
            title='JitterLeaf',
        ),
    ] = None
    """
    Measurement of the variance in latency on the network
    """
    offset: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ntp:offset',
            ge=0,
            le=18446744073709551615,
            title='OffsetLeaf',
        ),
    ] = None
    """
    Estimate of the current time offset from the peer
    This is the time difference between the local and reference clock.
    """
    root_delay: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ntp:root-delay',
            ge=0,
            le=18446744073709551615,
            title='Root-delayLeaf',
        ),
    ] = None
    """
    The round-trip delay to the server
    """
    root_dispersion: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ntp:root-dispersion',
            ge=0,
            le=18446744073709551615,
            title='Root-dispersionLeaf',
        ),
    ] = None
    """
    Dispersion (epsilon) represents the maximum error inherent in the measurement
    """
    poll_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ntp:poll-interval',
            ge=0,
            le=4294967295,
            title='Poll-intervalLeaf',
        ),
    ] = None
    """
    Polling interval of the peer
    """


class SessionListEntry(BaseModel):
    """
    List of active sessions in the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    username: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:username', title='UsernameLeaf4')
    ] = None
    """
    Username linked to the session
    """
    id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:id', ge=0, le=4294967295, title='IdLeaf'),
    ] = None
    """
    System generated session ID
    """
    spiffe_id: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:spiffe-id', title='Spiffe-idLeaf')
    ] = None
    """
    SPIFFE ID linked to the session
    """
    service_name: Annotated[
        Optional[str],
        Field(alias='srl_nokia-aaa:service-name', title='Service-nameLeaf'),
    ] = None
    """
    Service name that called login for the session
    """
    authentication_method: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:authentication-method',
            title='Authentication-methodLeaf',
        ),
    ] = None
    """
    Authentication method that authorized the user (the server-group name or local)
    """
    priv_lvl: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:priv-lvl', ge=0, le=255, title='Priv-lvlLeaf'),
    ] = None
    """
    TACACS+ authorization priv-lvl (if TACACS+ authorization is enabled)
    """
    tty_name: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:tty-name', title='Tty-nameLeaf')
    ] = None
    """
    Terminal type
    """
    remote_host: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:remote-host', title='Remote-hostLeaf')
    ] = None
    """
    Remote host of the session
    """
    login_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:login-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Login-timeLeaf',
        ),
    ] = None
    """
    Time the user logged in
    """
    role: Annotated[Optional[List[str]], Field(alias='srl_nokia-aaa:role')] = []
    """
    List of roles assigned to this user
    """


class SignalingUniNegTlvContainer(BaseModel):
    """
    Counts of different unicast negotiation TLVs
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    request_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Request-anno-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of requests for announce messages have been received
    """
    grant_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Grant-anno-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of grants for announce messages have been received
    """
    reject_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Reject-anno-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been received
    """
    cancel_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-anno-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been received
    """
    ack_cancel_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-anno-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been received
    """
    request_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Request-sync-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of requests for sync messages have been received
    """
    grant_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Grant-sync-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of grants for sync messages have been received
    """
    reject_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Reject-sync-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been received
    """
    cancel_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-sync-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been received
    """
    ack_cancel_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-sync-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been received
    """
    request_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Request-delay-resp-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been received
    """
    grant_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Grant-delay-resp-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been received
    """
    reject_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Reject-delay-resp-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been received
    """
    cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-delay-resp-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been received
    """
    ack_cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-delay-resp-rxLeaf',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been received
    """
    request_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Request-anno-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of requests for announce messages have been transmitted
    """
    grant_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Grant-anno-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of grants for announce messages have been transmitted
    """
    reject_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Reject-anno-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been transmitted
    """
    cancel_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-anno-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been transmitted
    """
    ack_cancel_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-anno-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been transmitted
    """
    request_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Request-sync-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of requests for sync messages have been transmitted
    """
    grant_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Grant-sync-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of grants for sync messages have been transmitted
    """
    reject_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Reject-sync-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been transmitted
    """
    cancel_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-sync-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been transmitted
    """
    ack_cancel_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-sync-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been transmitted
    """
    request_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Request-delay-resp-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been transmitted
    """
    grant_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Grant-delay-resp-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been transmitted
    """
    reject_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Reject-delay-resp-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been transmitted
    """
    cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-delay-resp-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been transmitted
    """
    ack_cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-delay-resp-txLeaf',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been transmitted
    """
    other_tlv: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:other-tlv',
            ge=0,
            le=18446744073709551615,
            title='Other-tlvLeaf',
        ),
    ] = 0
    """
    The count of unsupported signaling message TLVs received.
    """


class SignalingUniNegTlvContainer2(BaseModel):
    """
    Counts of different unicast negotiation TLVs
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    request_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Request-anno-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of requests for announce messages have been received
    """
    grant_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Grant-anno-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of grants for announce messages have been received
    """
    reject_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Reject-anno-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been received
    """
    cancel_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-anno-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been received
    """
    ack_cancel_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-anno-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been received
    """
    request_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Request-sync-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of requests for sync messages have been received
    """
    grant_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Grant-sync-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of grants for sync messages have been received
    """
    reject_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Reject-sync-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been received
    """
    cancel_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-sync-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been received
    """
    ack_cancel_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-sync-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been received
    """
    request_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Request-delay-resp-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been received
    """
    grant_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Grant-delay-resp-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been received
    """
    reject_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Reject-delay-resp-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been received
    """
    cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-delay-resp-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been received
    """
    ack_cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-delay-resp-rxLeaf2',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been received
    """
    request_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Request-anno-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of requests for announce messages have been transmitted
    """
    grant_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Grant-anno-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of grants for announce messages have been transmitted
    """
    reject_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Reject-anno-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been transmitted
    """
    cancel_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-anno-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been transmitted
    """
    ack_cancel_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-anno-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been transmitted
    """
    request_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Request-sync-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of requests for sync messages have been transmitted
    """
    grant_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Grant-sync-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of grants for sync messages have been transmitted
    """
    reject_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Reject-sync-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been transmitted
    """
    cancel_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-sync-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been transmitted
    """
    ack_cancel_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-sync-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been transmitted
    """
    request_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Request-delay-resp-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been transmitted
    """
    grant_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Grant-delay-resp-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been transmitted
    """
    reject_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Reject-delay-resp-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been transmitted
    """
    cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-delay-resp-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been transmitted
    """
    ack_cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-delay-resp-txLeaf2',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been transmitted
    """
    other_tlv: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:other-tlv',
            ge=0,
            le=18446744073709551615,
            title='Other-tlvLeaf2',
        ),
    ] = 0
    """
    The count of unsupported signaling message TLVs received.
    """


class SignalingUniNegTlvContainer3(BaseModel):
    """
    Counts of different unicast negotiation TLVs
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    request_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Request-anno-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of requests for announce messages have been received
    """
    grant_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Grant-anno-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of grants for announce messages have been received
    """
    reject_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Reject-anno-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been received
    """
    cancel_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-anno-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been received
    """
    ack_cancel_anno_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-anno-rx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-anno-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been received
    """
    request_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Request-sync-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of requests for sync messages have been received
    """
    grant_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Grant-sync-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of grants for sync messages have been received
    """
    reject_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Reject-sync-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been received
    """
    cancel_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-sync-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been received
    """
    ack_cancel_sync_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-sync-rx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-sync-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been received
    """
    request_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Request-delay-resp-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been received
    """
    grant_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Grant-delay-resp-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been received
    """
    reject_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Reject-delay-resp-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been received
    """
    cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-delay-resp-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been received
    """
    ack_cancel_delay_resp_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-rx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-delay-resp-rxLeaf3',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been received
    """
    request_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Request-anno-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of requests for announce messages have been transmitted
    """
    grant_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Grant-anno-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of grants for announce messages have been transmitted
    """
    reject_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Reject-anno-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of rejections for announce messages have been transmitted
    """
    cancel_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-anno-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of cancels for announce messages have been transmitted
    """
    ack_cancel_anno_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-anno-tx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-anno-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for announce messages have been transmitted
    """
    request_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Request-sync-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of requests for sync messages have been transmitted
    """
    grant_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Grant-sync-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of grants for sync messages have been transmitted
    """
    reject_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Reject-sync-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of rejections for sync messages have been transmitted
    """
    cancel_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-sync-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of cancels for sync messages have been transmitted
    """
    ack_cancel_sync_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-sync-tx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-sync-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for sync messages have been transmitted
    """
    request_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:request-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Request-delay-resp-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of requests for delay-resp messages have been transmitted
    """
    grant_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grant-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Grant-delay-resp-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of grants for delay-resp messages have been transmitted
    """
    reject_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:reject-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Reject-delay-resp-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of rejections for delay-resp messages have been transmitted
    """
    cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:cancel-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Cancel-delay-resp-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of cancels for delay-resp messages have been transmitted
    """
    ack_cancel_delay_resp_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ack-cancel-delay-resp-tx',
            ge=0,
            le=18446744073709551615,
            title='Ack-cancel-delay-resp-txLeaf3',
        ),
    ] = 0
    """
    Specifies the number of acknowledgements of cancels for delay-resp messages have been transmitted
    """
    other_tlv: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:other-tlv',
            ge=0,
            le=18446744073709551615,
            title='Other-tlvLeaf3',
        ),
    ] = 0
    """
    The count of unsupported signaling message TLVs received.
    """


class SshCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ssh_server: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-netconf-server:ssh-server',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Ssh-serverLeaf',
        ),
    ] = None
    """
    The SSH server instance to bind the NETCONF server to
    """


class StatisticsContainer10(BaseModel):
    """
    Top-level container for event handler statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    upython_duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:upython-duration',
            ge=0,
            le=18446744073709551615,
            title='Upython-durationLeaf3',
        ),
    ] = None
    """
    Total time taken for all executions of this script to return output
    """
    execution_count: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:execution-count',
            ge=0,
            le=18446744073709551615,
            title='Execution-countLeaf',
        ),
    ] = 0
    """
    Indicates the total number of executions of this script
    """
    execution_successes: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:execution-successes',
            ge=0,
            le=18446744073709551615,
            title='Execution-successesLeaf',
        ),
    ] = 0
    """
    Indicates the total number of successful executions of this script
    """
    execution_timeouts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:execution-timeouts',
            ge=0,
            le=18446744073709551615,
            title='Execution-timeoutsLeaf',
        ),
    ] = 0
    """
    Indicates the total number of timeouts in executions of this script
    """
    execution_errors: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:execution-errors',
            ge=0,
            le=18446744073709551615,
            title='Execution-errorsLeaf',
        ),
    ] = 0
    """
    Indicates the total number of errors in executions of this script
    """


class StatisticsContainer13(BaseModel):
    """
    Top-level container for application statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    restart_count: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-app-mgmt:restart-count',
            ge=0,
            le=4294967295,
            title='Restart-countLeaf',
        ),
    ] = 0
    """
    The number of times this application instance has restarted
    """


class StatisticsContainer14(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    client_packets_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:client-packets-received',
            ge=0,
            le=18446744073709551615,
            title='Client-packets-receivedLeaf',
        ),
    ] = 0
    """
    Total received dhcp packets from dhcp client(s)
    """
    client_packets_discarded: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:client-packets-discarded',
            ge=0,
            le=18446744073709551615,
            title='Client-packets-discardedLeaf',
        ),
    ] = 0
    """
    Total discarded dhcp packets from dhcp client(s)
    """
    server_packets_sent: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:server-packets-sent',
            ge=0,
            le=18446744073709551615,
            title='Server-packets-sentLeaf',
        ),
    ] = 0
    """
    Total dhcp packets sent from DHCP server towards dhcp client(s)
    """


class StatisticsContainer15(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    client_packets_received: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:client-packets-received',
            ge=0,
            le=18446744073709551615,
            title='Client-packets-receivedLeaf2',
        ),
    ] = 0
    """
    Total received dhcp packets from dhcp client(s)
    """
    client_packets_discarded: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:client-packets-discarded',
            ge=0,
            le=18446744073709551615,
            title='Client-packets-discardedLeaf2',
        ),
    ] = 0
    """
    Total discarded dhcp packets from dhcp client(s)
    """
    server_packets_sent: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dhcp-server:server-packets-sent',
            ge=0,
            le=18446744073709551615,
            title='Server-packets-sentLeaf2',
        ),
    ] = 0
    """
    Total dhcp packets sent from DHCP server towards dhcp client(s)
    """


class StatisticsContainer2(BaseModel):
    """
    Enclosing container for server statistics
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    login_success: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:login-success',
            ge=0,
            le=4294967295,
            title='Login-successLeaf',
        ),
    ] = 0
    """
    Number of login successes
    """
    login_connection_failures: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:login-connection-failures',
            ge=0,
            le=4294967295,
            title='Login-connection-failuresLeaf',
        ),
    ] = 0
    """
    Number of login connection failures
    """
    login_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:login-rejects',
            ge=0,
            le=4294967295,
            title='Login-rejectsLeaf',
        ),
    ] = 0
    """
    Number of login rejections
    """
    accounting_success: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:accounting-success',
            ge=0,
            le=4294967295,
            title='Accounting-successLeaf',
        ),
    ] = 0
    """
    Number of accounting successes
    """
    accounting_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:accounting-rejects',
            ge=0,
            le=4294967295,
            title='Accounting-rejectsLeaf',
        ),
    ] = 0
    """
    Number of accounting rejections
    """
    accounting_connection_failures: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:accounting-connection-failures',
            ge=0,
            le=4294967295,
            title='Accounting-connection-failuresLeaf',
        ),
    ] = 0
    """
    Number of accounting connection failures
    """
    authorization_success: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:authorization-success',
            ge=0,
            le=4294967295,
            title='Authorization-successLeaf',
        ),
    ] = 0
    """
    Number of authorization successes
    """
    authorization_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:authorization-rejects',
            ge=0,
            le=4294967295,
            title='Authorization-rejectsLeaf',
        ),
    ] = 0
    """
    Number of authorization rejections
    """
    authorization_connection_failures: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:authorization-connection-failures',
            ge=0,
            le=4294967295,
            title='Authorization-connection-failuresLeaf',
        ),
    ] = 0
    """
    Number of authorization connection failures
    """


class StatisticsContainer21(BaseModel):
    """
    Total messages for a specific PTP port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:anno-msg-tx',
            ge=0,
            le=4294967295,
            title='Anno-msg-txLeaf2',
        ),
    ] = None
    """
    Specifies the number of announce messages transmitted
    """
    anno_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:anno-msg-rx',
            ge=0,
            le=4294967295,
            title='Anno-msg-rxLeaf2',
        ),
    ] = None
    """
    Specifies the number of announce messages received
    """
    sync_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-msg-tx',
            ge=0,
            le=4294967295,
            title='Sync-msg-txLeaf2',
        ),
    ] = None
    """
    Specifies the number of sync messages transmitted
    """
    sync_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-msg-rx',
            ge=0,
            le=4294967295,
            title='Sync-msg-rxLeaf2',
        ),
    ] = None
    """
    Specifies the number of sync messages received
    """
    del_req_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-req-msg-tx',
            ge=0,
            le=4294967295,
            title='Del-req-msg-txLeaf2',
        ),
    ] = None
    """
    Specifies the number of delay-req messages transmitted
    """
    del_req_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-req-msg-rx',
            ge=0,
            le=4294967295,
            title='Del-req-msg-rxLeaf2',
        ),
    ] = None
    """
    Specifies the number of delay-req messages received
    """
    del_resp_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-resp-msg-tx',
            ge=0,
            le=4294967295,
            title='Del-resp-msg-txLeaf2',
        ),
    ] = None
    """
    Specifies the number of delay-resp messages transmitted
    """
    del_resp_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rx',
            ge=0,
            le=4294967295,
            title='Del-resp-msg-rxLeaf2',
        ),
    ] = None
    """
    Specifies the number of delay-resp messages received
    """
    follow_up_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:follow-up-msg-tx',
            ge=0,
            le=4294967295,
            title='Follow-up-msg-txLeaf2',
        ),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    follow_up_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rx',
            ge=0,
            le=4294967295,
            title='Follow-up-msg-rxLeaf2',
        ),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    signaling_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:signaling-msg-tx',
            ge=0,
            le=4294967295,
            title='Signaling-msg-txLeaf2',
        ),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    signaling_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:signaling-msg-rx',
            ge=0,
            le=4294967295,
            title='Signaling-msg-rxLeaf2',
        ),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    other_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:other-rx', ge=0, le=4294967295, title='Other-rxLeaf2'
        ),
    ] = None
    """
    Specifies the number of other messages received
    """
    discards: Annotated[
        Optional[DiscardsContainer2], Field(alias='srl_nokia-sync:discards')
    ] = None


class StatisticsContainer22(BaseModel):
    """
    Total messages for a specific PTP port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:anno-msg-tx',
            ge=0,
            le=4294967295,
            title='Anno-msg-txLeaf3',
        ),
    ] = None
    """
    Specifies the number of announce messages transmitted
    """
    anno_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:anno-msg-rx',
            ge=0,
            le=4294967295,
            title='Anno-msg-rxLeaf3',
        ),
    ] = None
    """
    Specifies the number of announce messages received
    """
    sync_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-msg-tx',
            ge=0,
            le=4294967295,
            title='Sync-msg-txLeaf3',
        ),
    ] = None
    """
    Specifies the number of sync messages transmitted
    """
    sync_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-msg-rx',
            ge=0,
            le=4294967295,
            title='Sync-msg-rxLeaf3',
        ),
    ] = None
    """
    Specifies the number of sync messages received
    """
    del_req_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-req-msg-tx',
            ge=0,
            le=4294967295,
            title='Del-req-msg-txLeaf3',
        ),
    ] = None
    """
    Specifies the number of delay-req messages transmitted
    """
    del_req_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-req-msg-rx',
            ge=0,
            le=4294967295,
            title='Del-req-msg-rxLeaf3',
        ),
    ] = None
    """
    Specifies the number of delay-req messages received
    """
    del_resp_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-resp-msg-tx',
            ge=0,
            le=4294967295,
            title='Del-resp-msg-txLeaf3',
        ),
    ] = None
    """
    Specifies the number of delay-resp messages transmitted
    """
    del_resp_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rx',
            ge=0,
            le=4294967295,
            title='Del-resp-msg-rxLeaf3',
        ),
    ] = None
    """
    Specifies the number of delay-resp messages received
    """
    follow_up_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:follow-up-msg-tx',
            ge=0,
            le=4294967295,
            title='Follow-up-msg-txLeaf3',
        ),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    follow_up_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rx',
            ge=0,
            le=4294967295,
            title='Follow-up-msg-rxLeaf3',
        ),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    signaling_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:signaling-msg-tx',
            ge=0,
            le=4294967295,
            title='Signaling-msg-txLeaf3',
        ),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    signaling_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:signaling-msg-rx',
            ge=0,
            le=4294967295,
            title='Signaling-msg-rxLeaf3',
        ),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    other_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:other-rx', ge=0, le=4294967295, title='Other-rxLeaf3'
        ),
    ] = None
    """
    Specifies the number of other messages received
    """
    discards: Annotated[
        Optional[DiscardsContainer3], Field(alias='srl_nokia-sync:discards')
    ] = None
    signaling_uni_neg_tlv: Annotated[
        Optional[SignalingUniNegTlvContainer2],
        Field(alias='srl_nokia-sync:signaling-uni-neg-tlv'),
    ] = None


class StatisticsContainer23(BaseModel):
    """
    Total messages for a specific PTP port

    This container is not used with PTP special ports (gnss).
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:anno-msg-tx',
            ge=0,
            le=4294967295,
            title='Anno-msg-txLeaf4',
        ),
    ] = None
    """
    Specifies the number of announce messages transmitted
    """
    anno_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:anno-msg-rx',
            ge=0,
            le=4294967295,
            title='Anno-msg-rxLeaf4',
        ),
    ] = None
    """
    Specifies the number of announce messages received
    """
    sync_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-msg-tx',
            ge=0,
            le=4294967295,
            title='Sync-msg-txLeaf4',
        ),
    ] = None
    """
    Specifies the number of sync messages transmitted
    """
    sync_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-msg-rx',
            ge=0,
            le=4294967295,
            title='Sync-msg-rxLeaf4',
        ),
    ] = None
    """
    Specifies the number of sync messages received
    """
    del_req_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-req-msg-tx',
            ge=0,
            le=4294967295,
            title='Del-req-msg-txLeaf4',
        ),
    ] = None
    """
    Specifies the number of delay-req messages transmitted
    """
    del_req_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-req-msg-rx',
            ge=0,
            le=4294967295,
            title='Del-req-msg-rxLeaf4',
        ),
    ] = None
    """
    Specifies the number of delay-req messages received
    """
    del_resp_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-resp-msg-tx',
            ge=0,
            le=4294967295,
            title='Del-resp-msg-txLeaf4',
        ),
    ] = None
    """
    Specifies the number of delay-resp messages transmitted
    """
    del_resp_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rx',
            ge=0,
            le=4294967295,
            title='Del-resp-msg-rxLeaf4',
        ),
    ] = None
    """
    Specifies the number of delay-resp messages received
    """
    follow_up_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:follow-up-msg-tx',
            ge=0,
            le=4294967295,
            title='Follow-up-msg-txLeaf4',
        ),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    follow_up_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rx',
            ge=0,
            le=4294967295,
            title='Follow-up-msg-rxLeaf4',
        ),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    signaling_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:signaling-msg-tx',
            ge=0,
            le=4294967295,
            title='Signaling-msg-txLeaf4',
        ),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    signaling_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:signaling-msg-rx',
            ge=0,
            le=4294967295,
            title='Signaling-msg-rxLeaf4',
        ),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    other_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:other-rx', ge=0, le=4294967295, title='Other-rxLeaf4'
        ),
    ] = None
    """
    Specifies the number of other messages received
    """
    discards: Annotated[
        Optional[DiscardsContainer4], Field(alias='srl_nokia-sync:discards')
    ] = None
    signaling_uni_neg_tlv: Annotated[
        Optional[SignalingUniNegTlvContainer3],
        Field(alias='srl_nokia-sync:signaling-uni-neg-tlv'),
    ] = None


class StatisticsContainer3(BaseModel):
    """
    Statistics related to the gRPC server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:access-rejects',
            ge=0,
            le=18446744073709551615,
            title='Access-rejectsLeaf3',
        ),
    ] = None
    """
    The total number of times the gRPC server denied access to the server
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-rejectLeaf3',
        ),
    ] = None
    """
    A timestamp of the last time the gRPC server denied access to the server
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:access-accepts',
            ge=0,
            le=18446744073709551615,
            title='Access-acceptsLeaf3',
        ),
    ] = None
    """
    The total number of times the gPRC allowed access to the server
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-acceptLeaf3',
        ),
    ] = None
    """
    A timestamp of the last time the gRPC allowed access to the server
    """
    rpc: Annotated[Optional[List[RpcListEntry2]], Field(alias='srl_nokia-grpc:rpc')] = (
        None
    )


class StatisticsContainer4(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ingress_mirrored_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mirroring:ingress-mirrored-packets',
            ge=0,
            le=18446744073709551615,
            title='Ingress-mirrored-packetsLeaf',
        ),
    ] = 0
    """
    The number of ingress mirrored packets
    """
    egress_mirrored_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mirroring:egress-mirrored-packets',
            ge=0,
            le=18446744073709551615,
            title='Egress-mirrored-packetsLeaf',
        ),
    ] = 0
    """
    The number of egress mirrored packets
    """
    ingress_mirrored_octets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mirroring:ingress-mirrored-octets',
            ge=0,
            le=18446744073709551615,
            title='Ingress-mirrored-octetsLeaf',
        ),
    ] = 0
    """
    The number of ingress mirrored octets
    """
    egress_mirrored_octets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mirroring:egress-mirrored-octets',
            ge=0,
            le=18446744073709551615,
            title='Egress-mirrored-octetsLeaf',
        ),
    ] = 0
    """
    The number of egress mirrored octets
    """


class Sync0Case(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    sync0: Annotated[Optional[Sync0Container], Field(alias='srl_nokia-sync:sync0')] = (
        None
    )


class Sync0Case2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    sync0: Annotated[Optional[Sync0Container2], Field(alias='srl_nokia-sync:sync0')] = (
        None
    )


class TxAnnounceContainer(BaseModel):
    """
    Statistics for transmit announce sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum85],
        Field(alias='srl_nokia-sync:state', title='StateLeaf5'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf4',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf5'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf4',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxAnnounceContainer2(BaseModel):
    """
    Statistics for transmit announce sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum91],
        Field(alias='srl_nokia-sync:state', title='StateLeaf11'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf10',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf11'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf10',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxDelayRespContainer(BaseModel):
    """
    Statistics for transmit delay-resp sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum87],
        Field(alias='srl_nokia-sync:state', title='StateLeaf7'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf6',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf7'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf6',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxDelayRespContainer2(BaseModel):
    """
    Statistics for transmit delay-resp sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum93],
        Field(alias='srl_nokia-sync:state', title='StateLeaf13'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf12',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf13'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf12',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxSyncContainer(BaseModel):
    """
    Statistics for transmit sync sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum86],
        Field(alias='srl_nokia-sync:state', title='StateLeaf6'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf5',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf6'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf5',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TxSyncContainer2(BaseModel):
    """
    Statistics for transmit sync sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum92],
        Field(alias='srl_nokia-sync:state', title='StateLeaf12'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf11',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf12'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf11',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class TypeListEntry(BaseModel):
    """
    List of the SSH servers host private-keys and certificates
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[
        Optional[EnumerationEnum8], Field(alias='srl_nokia-ssh:type', title='TypeLeaf3')
    ] = None
    """
    Type of generated host key
    """
    private_key: Annotated[
        Optional[str], Field(alias='srl_nokia-ssh:private-key', title='Private-keyLeaf')
    ] = None
    """
    The value should be the host private key as read from the private key file.

    This sets the HostKey option within each SSH servers configuration file.
    """
    public_key: Annotated[
        Optional[str], Field(alias='srl_nokia-ssh:public-key', title='Public-keyLeaf')
    ] = None
    """
    The value is be the host public key as read from the public key file.
    """
    certificate: Annotated[
        Optional[str], Field(alias='srl_nokia-ssh:certificate', title='CertificateLeaf')
    ] = None
    """
    Each item value should be the host key certificate as read from the *-cert.pub file generated by the CA including the certificate type, e.g. 'ssh-rsa-cert-v01@openssh.com AAAA<...> comment'.

    This certificate is returned to clients during SSH init for the client to verify the host it is communicating with.

    This sets the HostCertificate option within each SSH servers configuration file. The certificate should be generated by first extracting the systems current public key and having this signed by a CA.
    """


class UnixSocketCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    unix_socket: Annotated[
        Optional[UnixSocketContainer2],
        Field(alias='srl_nokia-netconf-server:unix-socket'),
    ] = None


class ValueCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    value: Annotated[
        Optional[str], Field(alias='srl_nokia-event-handler:value', title='ValueLeaf2')
    ] = None
    """
    A single value to associate with this object
    """


class ValuesCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    values: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-event-handler:values')
    ] = []
    """
    List of values to associate with this object, these are serialized as a JSON array when provided as input to the script
    """


class WritesContainer(BaseModel):
    """
    The counter were collected while performing a write operation on the schema path.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-pathz:access-rejects',
            ge=0,
            le=18446744073709551615,
            title='Access-rejectsLeaf6',
        ),
    ] = None
    """
    The total number of times the gNSI.pathz module denied access
    to a schema path.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-rejectLeaf6',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.pathz denied access to
    a schema path.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-pathz:access-accepts',
            ge=0,
            le=18446744073709551615,
            title='Access-acceptsLeaf6',
        ),
    ] = None
    """
    The total number of times the gNSI.pathz module allowed access
    to a schema path.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-acceptLeaf6',
        ),
    ] = None
    """
    A timestamp of the last time the gNSI.pathz allowed access to
    a schema path.
    """


class XstpContainer(BaseModel):
    """
    Container for Spanning Tree Protocols.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='In-tunneled-packetsLeaf4',
        ),
    ] = 0
    """
    System level incoming Spanning Tree tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled Spanning Tree frames.
    xSTP frames are identified by a destination MAC value of 01:80:c2:00:00:00 and LLC value
    0x42.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='In-trap-to-cpu-packetsLeaf4',
        ),
    ] = 0
    """
    System level incoming Spanning Tree Protocol frames copied to CPU.

    Cumulative of all Ethernet interfaces including all the copy-to-cpu Spanning Tree frames.
    Spanning Tree frames are identified by a destination MAC value of 01:80:c2:00:00:00 and
    LLC value 0x42.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf7',
        ),
    ] = None
    """
    Timestamp of the last time the xSTP counters were cleared.
    """


class AccountingContainer(BaseModel):
    """
    Top-level container for accounting
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    accounting_method: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-aaa:accounting-method',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = []
    """
    Ordered list of server-groups to use for accounting in the system

    If accounting fails with one method, the next defined method is tried -- failure of all methods results in the accounting request failing.
    """
    event: Annotated[
        Optional[List[EventListEntry]], Field(alias='srl_nokia-aaa:event')
    ] = None
    acctz: Annotated[Optional[AcctzContainer], Field(alias='srl_nokia-aaa:acctz')] = (
        None
    )


class AdmfContainer(BaseModel):
    """
    Configuration related to ADMF IP address and port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    address: Annotated[
        str,
        Field(
            alias='srl_nokia-lawful-intercept:address',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
            title='AddressLeaf5',
        ),
    ]
    """
    Specify the IP address of ADMF server
    """
    port: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:port', ge=0, le=65535, title='PortLeaf6'
        ),
    ] = None
    """
    Specify the port number of ADMF server
    """


class BgpAutoDiscoveryContainer(BaseModel):
    """
    Top-level container for global LLDP BGP auto discovery
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-lldp:admin-state', title='Admin-stateLeaf14'),
    ] = 'disable'
    """
    Enable or disable LLDP BGP auto discovery at the system level

    Setting this to disable will override any per-interface LLDP
    BGP autodiscovery configuration
    """
    network_instance: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-lldp:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ] = []
    """
    List of network instances to enable LLDP BGP auto discovery in

    Default is to run LLDP BGP auto discovery in all network instances
    """
    group_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:group-id', ge=0, le=4294967295, title='Group-idLeaf'
        ),
    ] = None
    """
    A four byte integer to send on outgoing LLDPDUs

    This value can be used on the remote end to do peer group association.
    This sub-TLV is not sent by default
    """


class BgpInstanceListEntry3(BaseModel):
    """
    List of bgp-vpn instances configured in the system network-instance. Only one instance allowed in the current release.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:id', ge=1, le=2),
    ] = None
    """
    The index of the bgp-vpn instance
    """
    route_distinguisher: Annotated[
        Optional[RouteDistinguisherContainer],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:route-distinguisher'),
    ] = None
    route_target: Annotated[
        Optional[RouteTargetContainer],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:route-target'),
    ] = None
    oper_down_reason: Annotated[
        Optional[EnumerationEnum43],
        Field(
            alias='srl_nokia-system-network-instance-bgp-vpn:oper-down-reason',
            title='Oper-down-reasonLeaf4',
        ),
    ] = None
    """
    Reason for the system bgp-instance being down
    """


class BgpVpnContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bgp_instance: Annotated[
        Optional[List[BgpInstanceListEntry3]],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:bgp-instance'),
    ] = None


class CandidateListEntry(BaseModel):
    """
    List of configuration candidates currently active
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf30',
        ),
    ] = None
    """
    Name of the configuration candidate
    """
    type: Annotated[
        Optional[EnumerationEnum53],
        Field(alias='srl_nokia-configuration:type', title='TypeLeaf14'),
    ] = None
    """
    Type of configuration candidate
    """
    username: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='UsernameLeaf7',
        ),
    ] = None
    """
    User that started the configuration session
    """
    started: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:started',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='StartedLeaf2',
        ),
    ] = None
    """
    Start date and time of the configuration session
    """


class CommitListEntry(BaseModel):
    """
    List of configuration transactions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-configuration:id', ge=0, le=4294967295, title='IdLeaf11'
        ),
    ] = None
    """
    System identifier for the commit
    """
    type: Annotated[
        Optional[EnumerationEnum53],
        Field(alias='srl_nokia-configuration:type', title='TypeLeaf15'),
    ] = None
    """
    Type of configuration candidate the commit was triggered from
    """
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf31',
        ),
    ] = None
    """
    Name of the configuration candidate the commit was triggered from
    """
    status: Annotated[
        Optional[EnumerationEnum54],
        Field(alias='srl_nokia-configuration:status', title='StatusLeaf3'),
    ] = None
    """
    Current status of the commit
    """
    comment: Annotated[
        Optional[str],
        Field(alias='srl_nokia-configuration:comment', title='CommentLeaf2'),
    ] = None
    """
    Operator provided comment associated with this commit
    """
    username: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='UsernameLeaf8',
        ),
    ] = None
    """
    User that started the commit
    """
    started: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:started',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='StartedLeaf3',
        ),
    ] = None
    """
    Start date and time of the commit
    """
    ended: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:ended',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='EndedLeaf',
        ),
    ] = None
    """
    End date and time of the commit

    This field is not populated if the commit is in progress
    """
    persist_id: Annotated[
        Optional[str],
        Field(alias='srl_nokia-configuration:persist-id', title='Persist-idLeaf'),
    ] = None
    """
    Persistent confirmed commit identifier
    """


class CountersContainer(BaseModel):
    """
    A collection of counters that were collected by the SSH server during the SSH authentication process.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    access_rejects: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-credentialz:access-rejects',
            ge=0,
            le=18446744073709551615,
            title='Access-rejectsLeaf',
        ),
    ] = None
    """
    The total number of times the SSH server denied access to the server.
    """
    last_access_reject: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:last-access-reject',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-rejectLeaf',
        ),
    ] = None
    """
    A timestamp of the last time the SSH server denied access to the server.
    """
    access_accepts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-gnsi-credentialz:access-accepts',
            ge=0,
            le=18446744073709551615,
            title='Access-acceptsLeaf',
        ),
    ] = None
    """
    The total number of times the SSH allowed access to the server.
    """
    last_access_accept: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:last-access-accept',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-access-acceptLeaf',
        ),
    ] = None
    """
    A timestamp of the last time the SSH allowed access to the server.
    """


class CountersContainer2(BaseModel):
    """
    A collection of counters collected by the gNSI.authz module.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rpc: Annotated[
        Optional[List[RpcListEntry]], Field(alias='srl_nokia-gnsi-authz:rpc')
    ] = None


class CrlContainer(BaseModel):
    """
    State relating to the active certificate revocation list provided via Certz

    The list of certificates provided will not be used to validate mTLS or servers, even if those certificates exist within the trust anchor.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-certz:version', title='VersionLeaf6')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-certz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf6',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class CrlContainer2(BaseModel):
    """
    State relating to the active certificate revocation list provided via Certz

    The list of certificates provided will not be used to validate mTLS or servers, even if those certificates exist within the trust anchor.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-grpc:version', title='VersionLeaf19')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf19',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class CurrentDsContainer(BaseModel):
    """
    Provides current data from operation of the protocol
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    steps_removed: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:steps-removed',
            ge=0,
            le=65535,
            title='Steps-removedLeaf',
        ),
    ] = None
    """
    The number of PTP clock steps in the path between the this PTP instance and the GM
    """
    offset_from_master: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:offset-from-master',
            ge=-9223372036854775808,
            le=9223372036854775807,
            title='Offset-from-masterLeaf',
        ),
    ] = None
    """
    The time difference between this PTP instance and the master clock
    """
    mean_delay: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:mean-delay',
            ge=-9223372036854775808,
            le=9223372036854775807,
            title='Mean-delayLeaf',
        ),
    ] = None
    """
    The mean propagation time between this PTP instance and the master clock
    """


class CurrentTimeContainer(BaseModel):
    """
    The current time in the current data set
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    time_seconds: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-seconds',
            ge=0,
            le=18446744073709551615,
            title='Time-secondsLeaf',
        ),
    ] = None
    """
    Seconds of time
    """
    time_nano_seconds: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-nano-seconds',
            ge=0,
            le=4294967295,
            title='Time-nano-secondsLeaf',
        ),
    ] = None
    """
    Nano-seconds of time
    """
    date_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:date-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Date-timeLeaf',
        ),
    ] = None
    """
    PTP current time converted to UTC and presented as a date-time string
    """


class DatapathContainer(BaseModel):
    """
    Context for system wide forwarding options
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    forwarding_mode: Annotated[
        Optional[EnumerationEnum29],
        Field(
            alias='srl_nokia-system-datapath:forwarding-mode',
            title='Forwarding-modeLeaf',
        ),
    ] = 'store-and-forward'
    """
    The forwarding mode for Ethernet frames received on all eligible ports of the system

    In store-and-forward mode, the forwarding of an Ethernet frame received on a particular port must wait until the entire Ethernet frame has been received, including the trailing 4-byte CRC; if the CRC is valid the packet is forwarded to the egress port based on the L2/L3 lookup result but if the CRC is invalid the frame is discarded and the in-error-packets counter is incremented.

    In cut-through mode, the forwarding ASIC does the L2/L3 forwarding lookup as soon as it has read the necessary packet headers. If the target egress queue of the egress port is not congested the bytes of the received frame are transmitted across the switch fabric as they are received. The fully intact frame is transmitted from the egress port as soon as all the bytes have been received.
    """
    icmp: Annotated[
        Optional[IcmpContainer], Field(alias='srl_nokia-system-datapath:icmp')
    ] = None
    icmp6: Annotated[
        Optional[Icmp6Container], Field(alias='srl_nokia-system-datapath:icmp6')
    ] = None


class Dot1xContainer2(BaseModel):
    """
    Container for 802.1x protocols.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='In-tunneled-packetsLeaf5',
        ),
    ] = 0
    """
    System level incoming 802.1x tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled 802.1x frames. 802.1x
    frames are identified by a destination MAC value of 01:80:c2:00:00:03 and EtherType value
    of 0x888e.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='In-trap-to-cpu-packetsLeaf5',
        ),
    ] = 0
    """
    System level incoming 802.1x frames copied to CPU.

    Cumulative of all Ethernet interfaces including all the copy-to-cpu 802.1x frames. 802.1x
    frames are identified by a destination MAC value of 01:80:c2:00:00:03 and EtherType value
    of 0x888e.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf8',
        ),
    ] = None
    """
    Timestamp of the last time the LACP counters were cleared.
    """


class DynamicSpiffeContainer(BaseModel):
    """
    Dynamic SPIFFE settings
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    allow: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:allow', title='AllowLeaf')
    ] = False
    """
    Accept clients with SPIFFE ID values that are not configured under any local user

    With this behaviour enabled, when a client using a client certificate containing SPIFFE ID connects the system
    will accept the client. Otherwise the SPIFFE ID must be configured under some local user. Even if enabled, any
    client using local user's configured SPIFFE ID will use that user's identity in all operations
    """
    role: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-aaa:role',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = []
    """
    List of roles to assign to all dynamic SPIFFE clients

    Dynamic SPIFFE clients are clients authenticated using a client certificate containing SPIFFE ID value that
    is not configured under any local user. The most specific rule for a particular role takes precedence. Rules
    from all user roles are evaluated together, most permissive privilege taking precedence.
    """


class DynamicListEntry(BaseModel):
    """
    List of dynamic label blocks

    When a client application binds its operation to a dynamic label block that client application is expected to just ask for the next available label within the dynamic label block.

    At this time a dynamic label block cannot be shared by multiple different clients/protocols. Each protocol needing dynamic labels must have its own label block.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-mpls-label-management:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    The name of the dynamic label block
    """
    start_label: Annotated[
        int,
        Field(
            alias='srl_nokia-mpls-label-management:start-label',
            ge=16,
            le=1048575,
            title='Start-labelLeaf2',
        ),
    ]
    """
    The starting label value of the label block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    end_label: Annotated[
        int,
        Field(
            alias='srl_nokia-mpls-label-management:end-label',
            ge=16,
            le=1048575,
            title='End-labelLeaf2',
        ),
    ]
    """
    The ending label value of the label block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    allocated_labels: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mpls-label-management:allocated-labels',
            ge=0,
            le=4294967295,
            title='Allocated-labelsLeaf2',
        ),
    ] = None
    """
    The number of labels that are currently used in this block
    """
    free_labels: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mpls-label-management:free-labels',
            ge=0,
            le=4294967295,
            title='Free-labelsLeaf2',
        ),
    ] = None
    """
    The number of labels that are currently available and free in this block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    status: Annotated[
        Optional[EnumerationEnum20],
        Field(alias='srl_nokia-mpls-label-management:status', title='StatusLeaf2'),
    ] = None
    """
    The status of the MPLS label block
    """
    user: Annotated[
        Optional[List[UserListEntry3]],
        Field(alias='srl_nokia-mpls-label-management:user'),
    ] = None


class EfmOamContainer(BaseModel):
    """
    Container for Ethernet in the First Mile OAM frames

    EFM-OAM frames are identified by a Ethertype value 0x8809 and slow protocol subtype 0x03.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='In-tunneled-packetsLeaf9',
        ),
    ] = 0
    """
    System level incoming EFM-OAM tunneled frames

    Cumulative of all Ethernet interfaces including all the tunneled EFM-OAM frames. 
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='In-trap-to-cpu-packetsLeaf9',
        ),
    ] = 0
    """
    System level incoming EFM-OAM frames copied to CPU

    Cumulative of all Ethernet interfaces including all the copy-to-cpu EFM-OAM frames.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf12',
        ),
    ] = None
    """
    Timestamp of the last time the EFM-OAM counters were cleared.
    """


class ElmiContainer(BaseModel):
    """
    Container for Ethernet local management interface frames

    ELMI frames are identified by MAC DA 01-80-C2-00-00-07 and Ethertype 0x88ee.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='In-tunneled-packetsLeaf8',
        ),
    ] = 0
    """
    System level incoming ELMI tunneled frames

    Cumulative of all Ethernet interfaces including all the tunneled ELMI frames.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='In-trap-to-cpu-packetsLeaf8',
        ),
    ] = 0
    """
    System level incoming ELMI frames copied to CPU

    Cumulative of all Ethernet interfaces including all the copy-to-cpu ELMI frames.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf11',
        ),
    ] = None
    """
    Timestamp of the last time the ELMI counters were cleared
    """


class EntryListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    sequence_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mirroring:sequence-id',
            ge=0,
            le=65535,
            title='Sequence-idLeaf',
        ),
    ] = None
    """
    A number to indicate the relative evaluation order of the different entries; lower numbered entries are evaluated before higher numbered entries
    """


class EsmcContainer(BaseModel):
    """
    Container for Ethernet Synchronization Messaging Channel protocol

    ESMC frames are identified by a Ethertype 0x8809 and slow protocol subtype 0x0A.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='In-tunneled-packetsLeaf7',
        ),
    ] = 0
    """
    System level incoming ESMC tunneled frames

    Cumulative of all Ethernet interfaces including all the tunneled ESMC frames. 
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='In-trap-to-cpu-packetsLeaf7',
        ),
    ] = 0
    """
    System level incoming ESMC frames copied to CPU

    Cumulative of all Ethernet interfaces including all the copy-to-cpu ESMC frames.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf10',
        ),
    ] = None
    """
    Timestamp of the last time the ESMC counters were cleared
    """


class EthernetSegmentContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    originating_ip: Annotated[
        Optional[EnumerationEnum36],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:originating-ip',
            title='Originating-ipLeaf',
        ),
    ] = 'use-system-ipv4-address'
    """
    The originating ip-address that the inclusive multicast route will be advertised with in this evpn instance
    """


class EvpnContainer(BaseModel):
    """
    Container for system wide Services EVPN MPLS label management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    dynamic_label_block: Annotated[
        str,
        Field(
            alias='srl_nokia-mpls-services-evpn-label-management:dynamic-label-block',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Dynamic-label-blockLeaf',
        ),
    ]
    """
    Reference to a dynamic label block
    """


class GnmiContainer2(BaseModel):
    """
    Container for gNMI related session info
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    paths: Annotated[
        Optional[List[PathsListEntry]], Field(alias='srl_nokia-grpc:paths')
    ] = None


class GribiContainer(BaseModel):
    """
    Container for gRIBI related session info
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    persistence_mode: Annotated[
        Optional[EnumerationEnum18],
        Field(alias='srl_nokia-grpc:persistence-mode', title='Persistence-modeLeaf'),
    ] = None
    """
    The defined persistence mode as signaled by the client
    """


class HostCertificateContainer(BaseModel):
    """
    State relating to the Host Certificates provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str],
        Field(alias='srl_nokia-gnsi-credentialz:version', title='VersionLeaf2'),
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf2',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class HostKeyContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[
        Optional[List[TypeListEntry]], Field(alias='srl_nokia-ssh:type')
    ] = None
    preserve: Annotated[
        Optional[bool], Field(alias='srl_nokia-ssh:preserve', title='PreserveLeaf')
    ] = True
    """
    Indicates whether the autogenerated SSH server host keys should be preserved on reboots

    Setting this to true will result in host keys in /etc/sshd not being cleared on a reboot. Alternatively
    setting this to false will result in host keys being removed and regenerated on each reboot of the system.

    This is useful only when the host keys are not statically configured and not dynamically configured using
    gNSI Credentialz service (and therefore are suitable to be potentially regenerated on every reboot).

    Takes effect only if the value is set to false for every configured ssh server instance.
    """


class HostKeyContainer2(BaseModel):
    """
    State relating to the Host Keys provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str],
        Field(alias='srl_nokia-gnsi-credentialz:version', title='VersionLeaf3'),
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf3',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class InformationContainer(BaseModel):
    """
    Top-level container for system information configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    contact: Annotated[
        Optional[str], Field(alias='srl_nokia-system-info:contact', title='ContactLeaf')
    ] = None
    """
    The system contact

    This field represents contact information for the person or group that maintains the system. This field is exposed via SNMP at the sysContact OID.
    """
    location: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-info:location', title='LocationLeaf'),
    ] = None
    """
    The system location

    This field represents the location of the system, and is commonly used by inventory management systems to group elements together. This field is exposed via SNMP at the sysLocation OID.
    """
    description: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-info:description', title='DescriptionLeaf4'),
    ] = None
    """
    The system description

    This field is system generated, and is a combination of the system host name, software version, kernel version, and build date. The template for this field is: SRLinux-<version> <hostname> <kernel> <build date>. This field is exposed via SNMP at the sysDescr OID.
    """
    current_datetime: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-info:current-datetime',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Current-datetimeLeaf',
        ),
    ] = None
    """
    The current system date and time
    """
    last_booted: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-info:last-booted',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-bootedLeaf',
        ),
    ] = None
    """
    The date and time the system was last booted
    """
    version: Annotated[
        Optional[str],
        Field(alias='srl_nokia-system-info:version', title='VersionLeaf24'),
    ] = None
    """
    The system version

    This field represents the version of the management server
    """


class InterfaceListEntry(BaseModel):
    """
    List of interfaces used as mirror source
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str], Field(alias='srl_nokia-mirroring:name', title='NameLeaf16')
    ] = None
    """
    Reference type to a specific subinterface of the form <interface-name>
    """
    direction: Annotated[
        Optional[EnumerationEnum26],
        Field(alias='srl_nokia-mirroring:direction', title='DirectionLeaf'),
    ] = 'egress-only'
    """
    The direction of traffic to be mirrored
    """


class InterfaceListEntry2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ethernet_interface: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-interface',
            title='Ethernet-interfaceLeaf',
        ),
    ] = None
    """
    Interface associated with the ethernet segment.
    """


class IsisContainer(BaseModel):
    """
    Container for specifying the ISIS members of the maintenance group
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instances: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-maintenance-mode:network-instances',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
        ),
    ] = []
    """
    List of network instances that should be part of the maintenance group.
    """


class IsisContainer2(BaseModel):
    """
    Container for ISIS configurations.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    overload: Annotated[
        Optional[OverloadContainer], Field(alias='srl_nokia-maintenance-mode:overload')
    ] = None


class LabelContainer(BaseModel):
    """
    The encoded label value and type in the EVPN NLRI
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    value: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:value',
            ge=0,
            le=16777215,
            title='ValueLeaf',
        ),
    ] = None
    """
    The value of the label field

    If the route is an EVPN MPLS route, the mpls-label is read out of the 20-bit high order value.
    If the route is an EVPN VXLAN route, the vni is read out of the 24-bit value. If the route is
    an EVPN SRv6 route, this field is set to zero if no transposition is used and set to a non-zero
    value if transposition is used. For all the cases, if this is an Auto-Discovery per ES route,
    this leaf is set to zero.
    """
    value_type: Annotated[
        Optional[EnumerationEnum38],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:value-type',
            title='Value-typeLeaf',
        ),
    ] = None
    """
    Whether the encoded label value is an mpls-label, a vni or a transposed function or argument
    """


class LacpContainer2(BaseModel):
    """
    Container for LACP.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='In-tunneled-packetsLeaf3',
        ),
    ] = 0
    """
    System level incoming Link Aggregation Control Protocol tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled LACP frames. LACP
    frames are identified by a destination MAC value of 01:80:c2:00:00:02, EtherType value
    of 0x8809 and slow protocol subtype 0x1.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='In-trap-to-cpu-packetsLeaf3',
        ),
    ] = 0
    """
    System level incoming Link Aggregation Control Protocol frames copied to CPU.

    Cumulative of all Ethernet interfaces including all the copy-to-cpu LACP frames. LACP
    frames are identified by a destination MAC value of 01:80:c2:00:00:02, EtherType value
    of 0x8809 and slow protocol subtype 0x1.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf6',
        ),
    ] = None
    """
    Timestamp of the last time the LACP counters were cleared.
    """


class LastErroredExecutionContainer(BaseModel):
    """
    Operational state of the last errored execution of this instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    oper_down_reason: Annotated[
        Optional[EnumerationEnum46],
        Field(
            alias='srl_nokia-event-handler:oper-down-reason',
            title='Oper-down-reasonLeaf6',
        ),
    ] = None
    """
    The reason this instance is or was in its last operational state
    """
    oper_down_reason_detail: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:oper-down-reason-detail',
            title='Oper-down-reason-detailLeaf2',
        ),
    ] = None
    """
    Any additional detail event handler can provide around the last operational state of this instance
    """
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Start-timeLeaf5',
        ),
    ] = None
    """
    The time this instance last started execution
    """
    end_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:end-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='End-timeLeaf3',
        ),
    ] = None
    """
    The time this instance last finished execution

    This timestamp includes any actions provided as output from the execution
    """
    upython_duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:upython-duration',
            ge=0,
            le=18446744073709551615,
            title='Upython-durationLeaf2',
        ),
    ] = None
    """
    Time taken for the instance to return output
    """
    input: Annotated[
        Optional[str], Field(alias='srl_nokia-event-handler:input', title='InputLeaf2')
    ] = None
    """
    The input provided to the script
    """
    output: Annotated[
        Optional[str],
        Field(alias='srl_nokia-event-handler:output', title='OutputLeaf2'),
    ] = None
    """
    The output received from the script

    If empty, no response was received.
    """
    stdout_stderr: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:stdout-stderr', title='Stdout-stderrLeaf2'
        ),
    ] = None
    """
    The output printed on STDOUT or STDERR during this execution
    """


class LastExecutionContainer(BaseModel):
    """
    Operational state of the last execution of this instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    oper_down_reason: Annotated[
        Optional[EnumerationEnum46],
        Field(
            alias='srl_nokia-event-handler:oper-down-reason',
            title='Oper-down-reasonLeaf5',
        ),
    ] = None
    """
    The reason this instance is or was in its last operational state
    """
    oper_down_reason_detail: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:oper-down-reason-detail',
            title='Oper-down-reason-detailLeaf',
        ),
    ] = None
    """
    Any additional detail event handler can provide around the last operational state of this instance
    """
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Start-timeLeaf4',
        ),
    ] = None
    """
    The time this instance last started execution
    """
    end_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:end-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='End-timeLeaf2',
        ),
    ] = None
    """
    The time this instance last finished execution

    This timestamp includes any actions provided as output from the execution
    """
    upython_duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-event-handler:upython-duration',
            ge=0,
            le=18446744073709551615,
            title='Upython-durationLeaf',
        ),
    ] = None
    """
    Time taken for the instance to return output
    """
    input: Annotated[
        Optional[str], Field(alias='srl_nokia-event-handler:input', title='InputLeaf')
    ] = None
    """
    The input provided to the script
    """
    output: Annotated[
        Optional[str], Field(alias='srl_nokia-event-handler:output', title='OutputLeaf')
    ] = None
    """
    The output received from the script

    If empty, no response was received.
    """
    stdout_stderr: Annotated[
        Optional[str],
        Field(alias='srl_nokia-event-handler:stdout-stderr', title='Stdout-stderrLeaf'),
    ] = None
    """
    The output printed on STDOUT or STDERR during this execution
    """


class Layer2InterfaceCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[List[InterfaceListEntry2]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:interface'
        ),
    ] = None


class LicenseListEntry(BaseModel):
    """
    List of licenses configured on the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-license:id',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='IdLeaf5',
        ),
    ] = None
    """
    Unique identifier for this license
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-license:admin-state', title='Admin-stateLeaf9'),
    ] = 'disable'
    """
    Enable or disable the use of this license
    """
    preferred: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-license:preferred', title='PreferredLeaf'),
    ] = False
    """
    Set a license as being preferred

    Amongst all valid licenses, the preferred license will be chosen to become active. If no license is set as preferred or the preferred license is not valid, the valid license with the most distant expiry is chosen to become active.

    Only a single license can be set as preferred.
    """
    data: Annotated[
        Optional[str], Field(alias='srl_nokia-license:data', title='DataLeaf')
    ] = None
    """
    Content of the license

    This content includes a preceding UUID, followed by a space and the license data.

    For example:
    00000000-0000-0000-0000-000000000000 aACUAx...rYzNRPT0AAAAA
    """
    description: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-license:description',
            max_length=255,
            min_length=1,
            title='DescriptionLeaf3',
        ),
    ] = None
    """
    A user provided description for the license
    """
    issued_date: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-license:issued-date',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Issued-dateLeaf',
        ),
    ] = None
    """
    Date and time the license was issued
    """
    expiration_date: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-license:expiration-date',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Expiration-dateLeaf',
        ),
    ] = None
    """
    Date and time the license will expire
    """
    expired: Annotated[
        Optional[bool], Field(alias='srl_nokia-license:expired', title='ExpiredLeaf2')
    ] = None
    """
    Indicates if the license has expired
    """
    valid: Annotated[
        Optional[bool], Field(alias='srl_nokia-license:valid', title='ValidLeaf')
    ] = None
    """
    Indicates if the license is valid for use
    """
    in_use: Annotated[
        Optional[bool], Field(alias='srl_nokia-license:in-use', title='In-useLeaf')
    ] = None
    """
    Indicates if the license is actively in use
    """


class LockoutContainer(BaseModel):
    """
    Information relating to the lockout state of this user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    active: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:active', title='ActiveLeaf')
    ] = None
    """
    Indicates if a lockout is active for the user

    Lockouts can occur after successive failed logins, and can be cleared by 'tools system aaa authentication user <username> unlock'
    """
    start: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:start',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='StartLeaf',
        ),
    ] = None
    """
    Indicates the time at which the most recent lockout for this user started
    """
    end: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:end',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='EndLeaf',
        ),
    ] = None
    """
    Indicates the time at which the most recent lockout for this user ended or will end
    """


class LockoutContainer2(BaseModel):
    """
    Information relating to the lockout state of this user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    active: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:active', title='ActiveLeaf2')
    ] = None
    """
    Indicates if a lockout is active for the user

    Lockouts can occur after successive failed logins, and can be cleared by 'tools system aaa authentication user <username> unlock'
    """
    start: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:start',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='StartLeaf2',
        ),
    ] = None
    """
    Indicates the time at which the most recent lockout for this user started
    """
    end: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:end',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='EndLeaf2',
        ),
    ] = None
    """
    Indicates the time at which the most recent lockout for this user ended or will end
    """


class MacTypeListEntry(BaseModel):
    """
    the type of the mac in the system.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[
        Optional[EnumerationEnum30],
        Field(alias='srl_nokia-system-bridge-table:type', title='TypeLeaf8'),
    ] = None
    """
    type of mac addresses in the system
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:active-entries',
            ge=0,
            le=18446744073709551615,
            title='Active-entriesLeaf2',
        ),
    ] = 0
    """
    The total number of macs of this type on the system.
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:total-entries',
            ge=0,
            le=18446744073709551615,
            title='Total-entriesLeaf2',
        ),
    ] = 0
    """
    The total number of macs of this type , active and inactive, on the system.
    """
    failed_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:failed-entries',
            ge=0,
            le=18446744073709551615,
            title='Failed-entriesLeaf2',
        ),
    ] = 0
    """
    The total number of macs of this type, which have not been programmed on atleast one slot
    """


class MacsecContainer(BaseModel):
    """
    Container to configure macsec CAK and CAK Name.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    cak: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-keychains:cak',
            pattern='^(?=^[0-9a-fA-F]+$).*$',
            title='CakLeaf',
        ),
    ] = None
    """
    MACsec CAK, a hexadecimal name is only valid
    """
    key_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-keychains:key-name',
            pattern='^(?=^([0-9a-fA-F][0-9a-fA-F])+$).*$',
            title='Key-nameLeaf',
        ),
    ] = None
    """
    MACsec CKN, a hexadecimal name is onlynumber
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-keychains:admin-state', title='Admin-stateLeaf6'),
    ] = 'disable'
    """
    When set to disable, this key entry is inactive

    For macsec the cak and key-name can only be changed

    when the key entry id disabled
    """


class MaintenanceModeContainer(BaseModel):
    """
    Container with options for activating and deactivating maintenance mode for this group
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(
            alias='srl_nokia-maintenance-mode:admin-state', title='Admin-stateLeaf26'
        ),
    ] = 'disable'
    """
    Enable or disable maintenance mode for this group

    The enable setting is blocked if there is another maintenance group with at least one BGP session in its scope that overlaps with this maintenance group and that other maintenance group is currently in maintenance mode.

    While a maintenance group is in maintenance mode it is not possible to modify the BGP configuration of its members.
    """


class ManagementAddressListEntry(BaseModel):
    """
    List of subinterfaces to source management addresses from

    This list is sent in the management address TLV by LLDP.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subinterface: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:subinterface', title='SubinterfaceLeaf'),
    ] = None
    """
    Reference to the subinterface to source management addresses
    """
    type: Annotated[
        Optional[List[EnumerationEnum49]], Field(alias='srl_nokia-lldp:type')
    ] = []
    """
    Types of addresses sent in the management address TLV

    The enumerated value for the network address type
    identified in this TLV. This enumeration is defined in the
    'Assigned Numbers' RFC [RFC3232] and the
    ianaAddressFamilyNumbers object.
    """


class ManagementAddressListEntry2(BaseModel):
    """
    List of management addresses received from the remote LLDP neighbor
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    address: Annotated[
        Optional[str], Field(alias='srl_nokia-lldp:address', title='AddressLeaf3')
    ] = None
    """
    The management address received from the remote LLDP neighbor

    The Management Address is a mandatory TLV which identifies a
    network address associated with the LLDP agent, which
    can be used to reach the agent on the port identified in the
    Port ID TLV.
    """
    type: Annotated[
        Optional[EnumerationEnum49],
        Field(alias='srl_nokia-lldp:type', title='TypeLeaf11'),
    ] = None
    """
    The type of management address referenced in the address field

    The enumerated value for the network address type
    identified in this TLV. This enumeration is defined in the
    'Assigned Numbers' RFC [RFC3232] and the
    ianaAddressFamilyNumbers object.
    """


class ManualAlgContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    primary_evi_range: Annotated[
        Optional[List[PrimaryEviRangeListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:primary-evi-range'
        ),
    ] = None


class MulticastIdUserTypeListEntry(BaseModel):
    """
    the type of the user of multicast id in the system.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    user: Annotated[
        Optional[EnumerationEnum65],
        Field(alias='srl_nokia-system-multicast:user', title='UserLeaf2'),
    ] = None
    """
    type of multicast ids users in the system
    """
    current_usage: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:current-usage',
            ge=0,
            le=18446744073709551615,
            title='Current-usageLeaf2',
        ),
    ] = 0
    """
    The total number of multicast ids that are in use on the system.
    """
    total_pending: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:total-pending',
            ge=0,
            le=18446744073709551615,
            title='Total-pendingLeaf2',
        ),
    ] = 0
    """
    The total number of multicast ids pending allocation on the system.
    """


class NeighborOriginListEntry(BaseModel):
    """
    the origin of the proxy entry installed in the table.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    origin: Annotated[
        Optional[EnumerationEnum31],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:origin', title='OriginLeaf'
        ),
    ] = None
    """
    The origin of the neighbor entry.
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:total-entries',
            ge=0,
            le=18446744073709551615,
            title='Total-entriesLeaf5',
        ),
    ] = 0
    """
    The total number of proxy entries.
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:active-entries',
            ge=0,
            le=18446744073709551615,
            title='Active-entriesLeaf5',
        ),
    ] = 0
    """
    The total number of active proxy entries.
    """
    in_active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:in-active-entries',
            ge=0,
            le=18446744073709551615,
            title='In-active-entriesLeaf2',
        ),
    ] = 0
    """
    The total number of inactive proxy entries.
    """
    pending_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:pending-entries',
            ge=0,
            le=18446744073709551615,
            title='Pending-entriesLeaf2',
        ),
    ] = 0
    """
    The total number of pending proxy entries.
    """


class NeighborOriginListEntry2(BaseModel):
    """
    the origin of the proxy entry installed in the table.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    origin: Annotated[
        Optional[EnumerationEnum31],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:origin', title='OriginLeaf2'
        ),
    ] = None
    """
    The origin of the neighbor entry.
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:total-entries',
            ge=0,
            le=18446744073709551615,
            title='Total-entriesLeaf7',
        ),
    ] = 0
    """
    The total number of proxy entries.
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:active-entries',
            ge=0,
            le=18446744073709551615,
            title='Active-entriesLeaf7',
        ),
    ] = 0
    """
    The total number of active proxy entries.
    """
    in_active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:in-active-entries',
            ge=0,
            le=18446744073709551615,
            title='In-active-entriesLeaf4',
        ),
    ] = 0
    """
    The total number of inactive proxy entries.
    """
    pending_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:pending-entries',
            ge=0,
            le=18446744073709551615,
            title='Pending-entriesLeaf4',
        ),
    ] = 0
    """
    The total number of pending proxy entries.
    """


class NetworkInstanceContainer(BaseModel):
    """
    Container for system wide Service Network Instance MPLS label management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    dynamic_label_block: Annotated[
        str,
        Field(
            alias='srl_nokia-mpls-services-network-instance-label-management:dynamic-label-block',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Dynamic-label-blockLeaf2',
        ),
    ]
    """
    Reference to the dynamic label block used by network-instances

    The label block is used by all the applications that require MPLS label allocation
    in a network-instance. For example, EVPN-MPLS services, IP-VPN or Pseudowires.
    """
    dynamic_evpn_inclusive_multicast_label_block: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-mpls-services-network-instance-label-management:dynamic-evpn-inclusive-multicast-label-block',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Dynamic-evpn-inclusive-multicast-label-blockLeaf',
        ),
    ] = None
    """
    Reference to the dynamic evpn inclusive multicast label block used by EVPN MAC-VRFs

    The label block is used by EVPN-MPLS MAC-VRF services for the allocation of labels
    that are advertised in EVPN Inclusive Multicast Ethernet Tag routes and that identify
    incoming layer-2 Broadcast, Unknown unicast and Multicast traffic.
    """
    static_label_block: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-mpls-services-network-instance-label-management:static-label-block',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Static-label-blockLeaf',
        ),
    ] = None
    """
    Reference to the static label block used by network-instances

    The label block is used by all the applications that require static MPLS label allocation
    in a network-instance. For example, Pseudowires with static vc labels.
    """


class NetworkInstanceListEntry4(BaseModel):
    """
    List of network instances with one or more peers to be placed in maintenance mode
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-maintenance-mode:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='NameLeaf42',
        ),
    ] = None
    """
    A unique name identifying the network instance
    """
    peer_group: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-maintenance-mode:peer-group',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = []
    """
    List of BGP peer groups that belong to the network instance and that should be part of the maintenance group

    If this list is empty and so is the neighbor list, then the system interprets the meaning as ALL static and dynamic sessions belonging to the specified network-instance.
    """
    neighbor: Annotated[
        Optional[List[Union[Ipv4AddressWithZoneType, Ipv6AddressWithZoneType]]],
        Field(alias='srl_nokia-maintenance-mode:neighbor'),
    ] = []
    """
    List of BGP neighbors that belong to the network instance and that should be part of the maintenance group

    It is not necessary to list neighbors that are members of peer-groups that are already listed.

    If this list is empty and so is the group list, then the system interprets the meaning as ALL static and dynamic sessions belonging to the specified network-instance.
    """


class NextHopListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    l3_next_hop: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:l3-next-hop',
            title='L3-next-hopLeaf',
        ),
    ] = None
    """
    Layer-3 next-hop associated with the ethernet segment.
    """
    evi: Annotated[
        Optional[List[EviListEntry]],
        Field(alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:evi'),
    ] = None


class NtpContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start_time: Annotated[
        str,
        Field(
            alias='srl_nokia-packet-link-qual:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Start-timeLeaf6',
        ),
    ]
    """
    Start time of the test
    """
    end_time: Annotated[
        str,
        Field(
            alias='srl_nokia-packet-link-qual:end-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='End-timeLeaf4',
        ),
    ]
    """
    End time of the test
    """
    teardown_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-packet-link-qual:teardown-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Teardown-timeLeaf',
        ),
    ] = None
    """
    Time at which the test should be torn down
    """


class ObjectListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf25',
        ),
    ] = None
    """
    The name of this object
    """
    object: Annotated[
        Optional[Union[ValuesCase, ValueCase]],
        Field(alias='srl_nokia-event-handler:object'),
    ] = None


class OnePpsContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-sync:admin-state', title='Admin-stateLeaf33'),
    ] = 'disable'
    """
    Configure the administrative state of the 1PPS (50 ohm) output port

    When enabled, output is enabled. Otherwise, the output is disabled.
    """


class OptionsContainer(BaseModel):
    """
    Options to be passed on each execution of the script
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    object: Annotated[
        Optional[List[ObjectListEntry]], Field(alias='srl_nokia-event-handler:object')
    ] = None


class OptionsContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bootfile_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:bootfile-name',
            max_length=128,
            min_length=1,
            title='Bootfile-nameLeaf',
        ),
    ] = None
    """
    The name of the configuration file the client will use during booting - option 67
    """
    dns_server: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-dhcp-server:dns-server',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = []
    """
    An Ordered List of DNS servers to return to the dhcp client - option 6
    """
    domain_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:domain-name',
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$',
            title='Domain-nameLeaf2',
        ),
    ] = None
    """
    The domain name to return to the dhcp client that the client should use when resolving hostnames via the Domain Name System - option 15
    """
    hostname: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:hostname',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
            title='HostnameLeaf',
        ),
    ] = None
    """
    Host Name option of the dhcp client - option 12
    """
    ntp_server: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-dhcp-server:ntp-server',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = []
    """
    List of NTP Servers to return to the dhcp client - option 42
    """
    router: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:router',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
            title='RouterLeaf',
        ),
    ] = None
    """
    IPv4 address of the gateway for the dhcp client - option 3
    """
    server_id: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:server-id',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
            title='Server-idLeaf',
        ),
    ] = None
    """
    IP address the dhcp server must match any address within the network_instance e.g. sub-interface primary address, loopback address,
    anycast gateway address in case of multihoming - option 54
    """
    tftp_server_address: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-dhcp-server:tftp-server-address',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = []
    """
    List of IP address of the TFTP servers the client will use to download bootfile/configuration script - option 150
    """
    tftp_server_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:tftp-server-name',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
            title='Tftp-server-nameLeaf',
        ),
    ] = None
    """
    FQDN of the TFTP server the client will use to download bootfile/configuration script - option 66
    """


class OptionsContainer3(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bootfile_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:bootfile-name',
            max_length=128,
            min_length=1,
            title='Bootfile-nameLeaf2',
        ),
    ] = None
    """
    The name of the configuration file the client will use during booting - option 67
    """
    dns_server: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-dhcp-server:dns-server',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = []
    """
    An Ordered List of DNS servers to return to the dhcp client - option 6
    """
    domain_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:domain-name',
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$',
            title='Domain-nameLeaf3',
        ),
    ] = None
    """
    The domain name to return to the dhcp client that the client should use when resolving hostnames via the Domain Name System - option 15
    """
    hostname: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:hostname',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
            title='HostnameLeaf2',
        ),
    ] = None
    """
    Host Name option of the dhcp client - option 12
    """
    ntp_server: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-dhcp-server:ntp-server',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = []
    """
    List of NTP Servers to return to the dhcp client - option 42
    """
    router: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:router',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
            title='RouterLeaf2',
        ),
    ] = None
    """
    IPv4 address of the gateway for the dhcp client - option 3
    """
    server_id: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:server-id',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
            title='Server-idLeaf2',
        ),
    ] = None
    """
    IP address the dhcp server must match any address within the network_instance e.g. sub-interface primary address, loopback address,
    anycast gateway address in case of multihoming - option 54
    """
    tftp_server_address: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-dhcp-server:tftp-server-address',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
        ),
    ] = []
    """
    List of IP address of the TFTP servers the client will use to download bootfile/configuration script - option 150
    """
    tftp_server_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:tftp-server-name',
            pattern='^(?=^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9._-]*[a-zA-Z0-9]))*([A-Za-z]|[A-Za-z][A-Za-z0-9._-]*[A-Za-z0-9])$).*$',
            title='Tftp-server-nameLeaf2',
        ),
    ] = None
    """
    FQDN of the TFTP server the client will use to download bootfile/configuration script - option 66
    """


class OptionsContainer4(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    dns_server: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-dhcp-server:dns-server',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$',
        ),
    ] = []
    """
    An Ordered List of DNS servers to return to the dhcp client
    """


class OptionsContainer5(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    dns_server: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-dhcp-server:dns-server',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$',
        ),
    ] = []
    """
    An Ordered List of DNS servers to return to the dhcp client
    """


class OutputContainer(BaseModel):
    """
    Defines parameters determining the handling of system generated traffic.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    qos: Annotated[Optional[QosContainer], Field(alias='srl_nokia-qos:qos')] = None


class PacketGeneratorCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    packet_generator: Annotated[
        Optional[PacketGeneratorContainer],
        Field(alias='srl_nokia-packet-link-qual:packet-generator'),
    ] = None


class PasswordContainer(BaseModel):
    """
    State relating to the Password provided via Credentialz.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:version', title='VersionLeaf7')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf7',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class PasswordContainer2(BaseModel):
    """
    State relating to the Password provided via Credentialz.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:version', title='VersionLeaf10')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf10',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class PasswordContainer3(BaseModel):
    """
    State relating to the Password provided via Credentialz.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:version', title='VersionLeaf13')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf13',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class PathListEntry(BaseModel):
    """
    A collection of counters collected by the gNSI.pathz module for a schema path identified by the `name`.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-pathz:name', title='NameLeaf10')
    ] = None
    """
    A schema path the counters were collected for.

    Uses xpath format.
    """
    reads: Annotated[
        Optional[ReadsContainer], Field(alias='srl_nokia-gnsi-pathz:reads')
    ] = None
    writes: Annotated[
        Optional[WritesContainer], Field(alias='srl_nokia-gnsi-pathz:writes')
    ] = None


class RaGuardPolicyListEntry(BaseModel):
    """
    List containing RA Guard Policy and parameters
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ra_guard:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf33',
        ),
    ] = None
    """
    RA Guard Policy name
    """
    action: Annotated[
        Optional[EnumerationEnum57],
        Field(alias='srl_nokia-ra_guard:action', title='ActionLeaf2'),
    ] = 'discard'
    """
    Describes the RA Guard Policy action for RA Messages matching the specified attributes.
    RA Messages not matching the specified attributes will be handled in the opposite manner.
    """
    source_prefix_set: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ra_guard:source-prefix-set',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Source-prefix-setLeaf',
        ),
    ] = None
    """
    Reference to a prefix set to match RA source address.
    If not specified the verification is skipped.
    """
    hop_limit: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ra_guard:hop-limit', ge=1, le=255, title='Hop-limitLeaf'
        ),
    ] = None
    """
    Verifies the minimum advertised hop count limit, RA message value must e equal to or greater than hop-limit.
    If not specified the verification is skipped.
    """
    managed_config_flag: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-ra_guard:managed-config-flag',
            title='Managed-config-flagLeaf',
        ),
    ] = None
    """
    Causes the RA Guard policy to match IPv6 RA messages with the M (Managed address) flag set.
    If not specified the verification is skipped.
    """
    other_config_flag: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-ra_guard:other-config-flag', title='Other-config-flagLeaf'
        ),
    ] = None
    """
    Causes the RA Guard policy to match IPv6 RA messages with the O (Other config) flag set.
    If not specified the verification is skipped.
    """
    advertise_prefix_set: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ra_guard:advertise-prefix-set',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Advertise-prefix-setLeaf',
        ),
    ] = None
    """
    Reference to a prefix set to match advertised address within RA message
    """
    router_preference: Annotated[
        Optional[EnumerationEnum58],
        Field(
            alias='srl_nokia-ra_guard:router-preference', title='Router-preferenceLeaf'
        ),
    ] = None
    """
    Verifies that the advertised default router preference parameter value is
    equal to or less than the specified limit.
    If not specified the verification is skipped.
    """


class ReceiveLifetimeContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-keychains:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Start-timeLeaf3',
        ),
    ] = None
    """
    The time at which the key becomes valid for use in the receive direction

    If send-and-receive is true, this value is ignored. If send-and-receive is false the default is the Unix Epoch (Jan 1, 1970 00:00:00 UTC).

    If there are multiple keys in the keychain the one used for checking received authentication information is the key with the most recent receive-lifetime start-time that is earlier than the current date and time and that has not exceeded its receive-lifetime end-time by more than 'tolerance' seconds
    """
    end_time: Annotated[
        Optional[Union[EnumerationEnum24, DateAndTimeDeltaType]],
        Field(alias='srl_nokia-keychains:end-time', title='End-timeLeaf'),
    ] = None
    """
    The time at which the key becomes invalid for use in the receive direction

    The default is forever.
    """


class ReceiverListEntry(BaseModel):
    """
    Specific configuration and states of a specific receiver
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    gnss_id: Annotated[
        Optional[EnumerationEnum94],
        Field(alias='srl_nokia-sync:gnss-id', title='Gnss-idLeaf'),
    ] = None
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-sync:admin-state', title='Admin-stateLeaf32'),
    ] = 'disable'
    """
    Configure the administrative state of the GNSS port
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-sync:oper-state', title='Oper-stateLeaf24'),
    ] = None
    """
    Operational state of the GNSS port
    """
    antenna_cable_delay: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:antenna-cable-delay',
            ge=0,
            le=1000,
            title='Antenna-cable-delayLeaf',
        ),
    ] = 0
    """
    Sets the cable delay value (integer) in ns to the GNSS antenna
    """
    elevation_mask_angle: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:elevation-mask-angle',
            ge=0,
            le=89,
            title='Elevation-mask-angleLeaf',
        ),
    ] = 10
    """
    Sets the elevation mask angle

    This provides a method of filtering satellites low on the horizon to be
    used by the system.
    """
    gnss_receiver_status: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:gnss-receiver-status',
            title='Gnss-receiver-statusLeaf',
        ),
    ] = None
    """
    Specifies the current state of the GNSS receiver module
    """
    gnss_sync_status: Annotated[
        Optional[EnumerationEnum95],
        Field(alias='srl_nokia-sync:gnss-sync-status', title='Gnss-sync-statusLeaf'),
    ] = None
    """
    Specifies the current state of the sync recovery from GNSS
    """
    gnss_antenna_status: Annotated[
        Optional[EnumerationEnum96],
        Field(
            alias='srl_nokia-sync:gnss-antenna-status', title='Gnss-antenna-statusLeaf'
        ),
    ] = None
    """
    Specifies the current state of the GNSS antenna
    """
    latitude_position: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:latitude-position',
            ge=-92233720368547.77,
            le=92233720368547.77,
            title='Latitude-positionLeaf',
        ),
    ] = None
    """
    Specifies the current latitude of the GNSS antenna
    """
    longitude_position: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:longitude-position',
            ge=-92233720368547.77,
            le=92233720368547.77,
            title='Longitude-positionLeaf',
        ),
    ] = None
    """
    Specifies the current longitude of the GNSS antenna
    """
    altitude_position: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:altitude-position',
            ge=-92233720368547.77,
            le=92233720368547.77,
            title='Altitude-positionLeaf',
        ),
    ] = None
    """
    Specifies the current altitude of the GNSS antenna
    """
    position_valid: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:position-valid', title='Position-validLeaf'),
    ] = None
    """
    Specifies if the current position information is valid
    """
    gnss_date_and_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:gnss-date-and-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Gnss-date-and-timeLeaf',
        ),
    ] = None
    """
    Specifies the date and time as recovered from GNSS
    """
    gnss_utc_offset: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:gnss-utc-offset',
            ge=-32768,
            le=32767,
            title='Gnss-utc-offsetLeaf',
        ),
    ] = None
    """
    Specifies the UTC as recovered from GNSS
    """
    gnss_utc_offset_valid: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-sync:gnss-utc-offset-valid',
            title='Gnss-utc-offset-validLeaf',
        ),
    ] = None
    """
    Specifies the UTC offset is valid as recovered from GNSS
    """
    gnss_firmware: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:gnss-firmware', title='Gnss-firmwareLeaf'),
    ] = None
    """
    Specifies the current firmware used by the GNSS receiver
    """
    number_of_satellites_visible: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:number-of-satellites-visible',
            ge=0,
            le=255,
            title='Number-of-satellites-visibleLeaf',
        ),
    ] = None
    """
    The number of satellites currently visible
    """
    satellites_in_use: Annotated[
        Optional[SatellitesInUseContainer],
        Field(alias='srl_nokia-sync:satellites-in-use'),
    ] = None


class ResourceListEntry(BaseModel):
    """
    List of system-wide resources
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[Any],
        Field(alias='srl_nokia-system-utilization:name', title='NameLeaf39'),
    ] = None
    """
    The name of the resource
    """
    upper_threshold_set: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-utilization:upper-threshold-set',
            ge=0,
            le=100,
            title='Upper-threshold-setLeaf',
        ),
    ] = 90
    """
    Sets the threshold that triggers the generation of a WARNING log and the setting of 'used-upper-threshold-exceeded' to 'true' whenever the utilization of the resource reaches this value in a rising direction
    """
    upper_threshold_clear: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-utilization:upper-threshold-clear',
            ge=0,
            le=100,
            title='Upper-threshold-clearLeaf',
        ),
    ] = 70
    """
    Sets the threshold that triggers the generation of a NOTICE log and the setting of 'used-upper-threshold-exceeded' to 'false' whenever the utilization of the resource reaches this value in a falling direction
    """
    used_percent: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-utilization:used-percent',
            ge=0,
            le=100,
            title='Used-percentLeaf',
        ),
    ] = None
    """
    The percentage of the resource that is currently used
    """
    used_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-utilization:used-entries',
            ge=0,
            le=4294967295,
            title='Used-entriesLeaf',
        ),
    ] = None
    """
    The number of entries that are currently used
    """
    free_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-utilization:free-entries',
            ge=0,
            le=4294967295,
            title='Free-entriesLeaf',
        ),
    ] = None
    """
    The number of entries that are currently free
    """
    used_high_watermark: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-utilization:used-high-watermark',
            ge=0,
            le=4294967295,
            title='Used-high-watermarkLeaf',
        ),
    ] = None
    """
    A watermark of highest number of entries used for this resource
    """
    used_last_high_watermark_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-utilization:used-last-high-watermark-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Used-last-high-watermark-timeLeaf',
        ),
    ] = None
    """
    The timestamp when the high-watermark was last updated
    """
    used_upper_threshold_exceeded: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-system-utilization:used-upper-threshold-exceeded',
            title='Used-upper-threshold-exceededLeaf',
        ),
    ] = None
    """
    This value is set to true when the used percentage value (used / (used + free) * 100) has reached (in a rising direction) the configured upper-threshold-set for this resource and false when the used percentage value has reached (in a falling direction) the configured upper-threshold-clear for this resource
    """


class RoleListEntry(BaseModel):
    """
    List of local roles configured on the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rolename: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:rolename',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Assigned rolename for this role
    """
    services: Annotated[
        Optional[List[EnumerationEnum12]], Field(alias='srl_nokia-aaa:services')
    ] = []
    """
    Services that members of this role are authorized for

    Services are additive, if a user is a member of multiple roles, the available services are merged.
    """
    superuser: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:superuser', title='SuperuserLeaf3')
    ] = False
    """
    Indicates if users with this role are given superuser

    A superuser is granted implicit authorization to all YANG paths, has the ability to execute all CLI plugins, and by default is permitted to access the device through any interface.

    Additionally, users with the superuser attribute are able to execute 'sudo' in bash. A user may also be assigned a role or list of roles, but these are only evaluated for service authorization.
    """
    tacacs: Annotated[
        Optional[TacacsContainer], Field(alias='srl_nokia-aaa:tacacs')
    ] = None
    cli: Annotated[Optional[CliContainer], Field(alias='srl_nokia-aaa:cli')] = None
    netconf: Annotated[
        Optional[NetconfContainer], Field(alias='srl_nokia-aaa:netconf')
    ] = None


class RoutesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ethernet_segment: Annotated[
        Optional[EthernetSegmentContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-segment'
        ),
    ] = None
    next_hop: Annotated[
        Optional[EnumerationEnum37],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:next-hop',
            title='Next-hopLeaf',
        ),
    ] = 'use-system-ipv4-address'
    """
    The ip-address that will be used as the bgp-next hop for all ES and AD per-ES routes advertised for this Ethernet Segment.
    """


class RpcCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rpc: Annotated[
        Optional[RpcContainer], Field(alias='srl_nokia-packet-link-qual:rpc')
    ] = None


class RuleListEntry(BaseModel):
    """
    List of paths to perform access control against
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    path_reference: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration-role:path-reference',
            pattern='^(?=^[A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?\\-{}*\\\\\\\\"\\[\\]]+$).*$',
            title='Path-referenceLeaf',
        ),
    ] = None
    """
    Reference to a valid YANG path, in CLI notation

    This path may include keys, wildcards, ranges, and other management server supported constructs. Ranges will be expanded.
    The root path can be specified with '/'.

    E.g.
        /
        "/interface"
        "/acl ipv4-filter foo* description"
    """
    action: Annotated[
        EnumerationEnum56,
        Field(alias='srl_nokia-configuration-role:action', title='ActionLeaf'),
    ]
    """
    Action to allow for this path
    """


class RxAnnounceContainer(BaseModel):
    """
    Statistics for receive announce sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum82],
        Field(alias='srl_nokia-sync:state', title='StateLeaf2'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf2'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxAnnounceContainer2(BaseModel):
    """
    Statistics for receive announce sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum88],
        Field(alias='srl_nokia-sync:state', title='StateLeaf8'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf7',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf8'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf7',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxDelayRespContainer(BaseModel):
    """
    Statistics for receive delay-resp sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum84],
        Field(alias='srl_nokia-sync:state', title='StateLeaf4'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf3',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf4'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf3',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxDelayRespContainer2(BaseModel):
    """
    Statistics for receive delay-resp sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum90],
        Field(alias='srl_nokia-sync:state', title='StateLeaf10'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf9',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf10'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf9',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxSyncContainer(BaseModel):
    """
    Statistics for receive sync sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum83],
        Field(alias='srl_nokia-sync:state', title='StateLeaf3'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf2',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf3'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf2',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class RxSyncContainer2(BaseModel):
    """
    Statistics for receive sync sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    state: Annotated[
        Optional[EnumerationEnum89],
        Field(alias='srl_nokia-sync:state', title='StateLeaf9'),
    ] = None
    """
    Indicates the state of the negotiation
    """
    log_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-interval',
            ge=-128,
            le=127,
            title='Log-intervalLeaf8',
        ),
    ] = None
    """
    The packet rate requested or granted for unicast transmission between the PTP peers
    """
    duration: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:duration', ge=0, le=4294967295, title='DurationLeaf9'
        ),
    ] = None
    """
    The duration, in seconds, requested/granted for unicast transmission between the PTP peers
    """
    time_of_last_grant: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:time-of-last-grant',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Time-of-last-grantLeaf8',
        ),
    ] = None
    """
    The time when status last changed or the unicast session between the PTP clocks was renewed
    """


class SendLifetimeContainer(BaseModel):
    """
    Specifies the lifetime of the key for sending authentication information to the peer
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-keychains:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Start-timeLeaf2',
        ),
    ] = None
    """
    The time at which the key becomes valid for use in the send direction

    The default is the Unix Epoch (Jan 1, 1970 00:00:00 UTC).

    If there are multiple keys in the keychain the one used for sending authentication information is the key with the most recent send-lifetime start-time that is earlier than the current date and time
    """
    send_and_receive: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-keychains:send-and-receive', title='Send-and-receiveLeaf'
        ),
    ] = None
    """
    When this is set to true (the default value), the specified start-time also applies to the receive direction

    When set to false, router uses the specific start-time for the receive direction (asymmetric mode).
    """


class ServicesContainer(BaseModel):
    """
    Container for system wide Services MPLS label management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    evpn: Annotated[
        Optional[EvpnContainer],
        Field(alias='srl_nokia-mpls-services-evpn-label-management:evpn'),
    ] = None
    network_instance: Annotated[
        Optional[NetworkInstanceContainer],
        Field(
            alias='srl_nokia-mpls-services-network-instance-label-management:network-instance'
        ),
    ] = None


class SessionListEntry2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    session_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:session-id',
            ge=1,
            le=4294967295,
            title='Session-idLeaf',
        ),
    ] = None
    process_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:process-id',
            ge=0,
            le=4294967295,
            title='Process-idLeaf',
        ),
    ] = None
    """
    The process ID of the NETCONF session
    """
    in_bad_hellos: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:in-bad-hellos',
            ge=0,
            le=4294967295,
            title='In-bad-hellosLeaf',
        ),
    ] = 0
    """
    Inbound bad NETCONF hello messages

    Number of bad NETCONF hello messages that have been received by the NETCONF server
    """
    get_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:get-requests',
            ge=0,
            le=4294967295,
            title='Get-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <get> requests

    Number of <get> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    get_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:get-config-requests',
            ge=0,
            le=4294967295,
            title='Get-config-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <get-config> requests

    Number of <get-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    get_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:get-data-requests',
            ge=0,
            le=4294967295,
            title='Get-data-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <get-data> requests

    Number of <get-data> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    get_schema_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:get-schema-requests',
            ge=0,
            le=4294967295,
            title='Get-schema-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <get-schema> requests

    Number of <get-schema> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    edit_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:edit-config-requests',
            ge=0,
            le=4294967295,
            title='Edit-config-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <edit-config> requests

    Number of <edit-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    failed_edit_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:failed-edit-config-requests',
            ge=0,
            le=4294967295,
            title='Failed-edit-config-requestsLeaf',
        ),
    ] = 0
    """
    Failed NETCONF <edit-config> requests

    Number of <edit-config> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    edit_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:edit-data-requests',
            ge=0,
            le=4294967295,
            title='Edit-data-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <edit-data> requests

    Number of <edit-data> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    failed_edit_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:failed-edit-data-requests',
            ge=0,
            le=4294967295,
            title='Failed-edit-data-requestsLeaf',
        ),
    ] = 0
    """
    Failed NETCONF <edit-data> requests

    Number of <edit-data> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    kill_session_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:kill-session-requests',
            ge=0,
            le=4294967295,
            title='Kill-session-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <kill-session> requests

    Number of <kill-session> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    copy_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:copy-config-requests',
            ge=0,
            le=4294967295,
            title='Copy-config-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <copy-config> requests

    Number of copy-config NETCONF requests that have been accepted and processed by the NETCONF server
    """
    delete_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:delete-config-requests',
            ge=0,
            le=4294967295,
            title='Delete-config-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <delete-config> requests

    Number of <delete-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    validate_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:validate-requests',
            ge=0,
            le=4294967295,
            title='Validate-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <validate> requests

    Number of <validate> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    lock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:lock-requests',
            ge=0,
            le=4294967295,
            title='Lock-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <lock> requests

    Number of <lock> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    failed_lock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:failed-lock-requests',
            ge=0,
            le=4294967295,
            title='Failed-lock-requestsLeaf',
        ),
    ] = 0
    """
    Failed NETCONF <lock> requests

    Number of <lock> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    unlock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:unlock-requests',
            ge=0,
            le=4294967295,
            title='Unlock-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <unlock> requests

    Number of <unlock> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    commit_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:commit-requests',
            ge=0,
            le=4294967295,
            title='Commit-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <commit> requests

    Number of commit NETCONF requests that have been accepted and processed by the NETCONF server
    """
    discard_changes_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:discard-changes-requests',
            ge=0,
            le=4294967295,
            title='Discard-changes-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <discard-changes> requests

    Number of <discard-changes> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    action_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:action-requests',
            ge=0,
            le=4294967295,
            title='Action-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <action> requests

    Number of <action> NETCONF requests that have been accepted and processed by the NETCONF server
    """


class SessionListEntry3(BaseModel):
    """
    List of configuration sessions currently active
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-configuration:id', ge=0, le=4294967295, title='IdLeaf10'
        ),
    ] = None
    """
    System generated ID for the configuration session
    """
    type: Annotated[
        Optional[EnumerationEnum53],
        Field(alias='srl_nokia-configuration:type', title='TypeLeaf13'),
    ] = None
    """
    Type of configuration session
    """
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf29',
        ),
    ] = None
    """
    Name of the candidate the session is active on

    Set to 'default' if a non-named candidate is active
    """
    exclusive: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-configuration:exclusive', title='ExclusiveLeaf'),
    ] = None
    """
    Details if this session is running in exclusive mode
    """
    username: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='UsernameLeaf6',
        ),
    ] = None
    """
    User that started the configuration session
    """
    started: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:started',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='StartedLeaf',
        ),
    ] = None
    """
    Start date and time of the configuration session
    """


class StaticListEntry(BaseModel):
    """
    List of static label blocks

    When a client application binds its operation to a static label block that client application is expected to specify the exact label value it wants to use every time it requests a label within the static label block.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-mpls-label-management:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    The name of the static label block
    """
    shared: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-mpls-label-management:shared', title='SharedLeaf'),
    ] = True
    """
    When set to true, the label block can be shared by multiple protoccols. When set to false, the label block is dedicated to one protocol.
    """
    start_label: Annotated[
        int,
        Field(
            alias='srl_nokia-mpls-label-management:start-label',
            ge=16,
            le=1048575,
            title='Start-labelLeaf',
        ),
    ]
    """
    The starting label value of the label block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    end_label: Annotated[
        int,
        Field(
            alias='srl_nokia-mpls-label-management:end-label',
            ge=16,
            le=1048575,
            title='End-labelLeaf',
        ),
    ]
    """
    The ending label value of the label block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    allocated_labels: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mpls-label-management:allocated-labels',
            ge=0,
            le=4294967295,
            title='Allocated-labelsLeaf',
        ),
    ] = None
    """
    The number of labels that are currently used in this block
    """
    free_labels: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-mpls-label-management:free-labels',
            ge=0,
            le=4294967295,
            title='Free-labelsLeaf',
        ),
    ] = None
    """
    The number of labels that are currently available and free in this block.

    When the status is not-ready or updating, the state value may be different from the configured value
    """
    status: Annotated[
        Optional[EnumerationEnum19],
        Field(alias='srl_nokia-mpls-label-management:status', title='StatusLeaf'),
    ] = None
    """
    The status of the MPLS label block
    """
    user: Annotated[
        Optional[List[UserListEntry2]],
        Field(alias='srl_nokia-mpls-label-management:user'),
    ] = None


class StatisticsContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    total_in_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dot1x:total-in-packets',
            ge=0,
            le=18446744073709551615,
            title='Total-in-packetsLeaf',
        ),
    ] = 0
    """
    System or interface level total incoming dot1x frames

    Cumulative of all Ethernet interfaces or specific interface including the tunneled, discarded and copy-to-cpu dot1x frames.
    """
    total_in_discarded_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dot1x:total-in-discarded-packets',
            ge=0,
            le=18446744073709551615,
            title='Total-in-discarded-packetsLeaf',
        ),
    ] = 0
    """
    System or interface level incoming do1x discarded frames

    Cumulative of all Ethernet interfaces or specific interface including all the discarded dot1x frames.
    """
    in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dot1x:in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='In-tunneled-packetsLeaf',
        ),
    ] = 0
    """
    System or interface level incoming 802.1x tunneled frames

    Cumulative of all Ethernet interfaces including all the tunneled 802.1x frames.
    802.1x frames are identified by a destination MAC value of 01:80:c2:00:00:03 and EtherType value of 0x888e.
    """
    in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-dot1x:in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='In-trap-to-cpu-packetsLeaf',
        ),
    ] = 0
    """
    System or interface level incoming 802.1x frames copied to CPU

    Cumulative of all Ethernet interfaces including all the copy-to-cpu 802.1x frames.
    802.1x frames are identified by a destination MAC value of 01:80:c2:00:00:03 and EtherType value of 0x888e.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dot1x:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf',
        ),
    ] = None
    """
    Timestamp of the last time the 802.1x counters were cleared
    """


class StatisticsContainer11(BaseModel):
    """
    Global LLDP counters
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    frame_in: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:frame-in',
            ge=0,
            le=18446744073709551615,
            title='Frame-inLeaf',
        ),
    ] = 0
    """
    The number of LLDP frames received
    """
    frame_out: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:frame-out',
            ge=0,
            le=18446744073709551615,
            title='Frame-outLeaf',
        ),
    ] = 0
    """
    The number of LLDP frames transmitted
    """
    frame_error_in: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:frame-error-in',
            ge=0,
            le=18446744073709551615,
            title='Frame-error-inLeaf',
        ),
    ] = 0
    """
    The number of LLDP frames received with errors
    """
    frame_discard: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:frame-discard',
            ge=0,
            le=18446744073709551615,
            title='Frame-discardLeaf',
        ),
    ] = 0
    """
    The number of LLDP frames received and discarded
    """
    tlv_discard: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:tlv-discard',
            ge=0,
            le=18446744073709551615,
            title='Tlv-discardLeaf',
        ),
    ] = 0
    """
    The number of TLV frames received and discarded
    """
    tlv_unknown: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:tlv-unknown',
            ge=0,
            le=18446744073709551615,
            title='Tlv-unknownLeaf',
        ),
    ] = 0
    """
    The number of frames received with unknown TLV
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf2',
        ),
    ] = None
    """
    Indicates the last time the counters were cleared
    """
    tlv_accepted: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:tlv-accepted',
            ge=0,
            le=18446744073709551615,
            title='Tlv-acceptedLeaf',
        ),
    ] = 0
    """
    The number of valid TLVs received.
    """
    entries_aged_out: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:entries-aged-out',
            ge=0,
            le=18446744073709551615,
            title='Entries-aged-outLeaf',
        ),
    ] = 0
    """
    The number of entries aged out due to timeout.
    """


class StatisticsContainer12(BaseModel):
    """
    LLDP counters on each interface
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    frame_in: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:frame-in',
            ge=0,
            le=18446744073709551615,
            title='Frame-inLeaf2',
        ),
    ] = 0
    """
    The number of LLDP frames received
    """
    frame_out: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:frame-out',
            ge=0,
            le=18446744073709551615,
            title='Frame-outLeaf2',
        ),
    ] = 0
    """
    The number of LLDP frames transmitted
    """
    frame_error_in: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:frame-error-in',
            ge=0,
            le=18446744073709551615,
            title='Frame-error-inLeaf2',
        ),
    ] = 0
    """
    The number of LLDP frames received with errors
    """
    frame_discard: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:frame-discard',
            ge=0,
            le=18446744073709551615,
            title='Frame-discardLeaf2',
        ),
    ] = 0
    """
    The number of LLDP frames received and discarded
    """
    tlv_discard: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:tlv-discard',
            ge=0,
            le=18446744073709551615,
            title='Tlv-discardLeaf2',
        ),
    ] = 0
    """
    The number of TLV frames received and discarded
    """
    tlv_unknown: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:tlv-unknown',
            ge=0,
            le=18446744073709551615,
            title='Tlv-unknownLeaf2',
        ),
    ] = 0
    """
    The number of frames received with unknown TLV
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf3',
        ),
    ] = None
    """
    Indicates the last time the counters were cleared
    """
    frame_error_out: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:frame-error-out',
            ge=0,
            le=18446744073709551615,
            title='Frame-error-outLeaf',
        ),
    ] = 0
    """
    The number of frame transmit errors on the interface
    """


class StatisticsContainer16(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    maximum_ids: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:maximum-ids',
            ge=-2147483648,
            le=2147483647,
            title='Maximum-idsLeaf',
        ),
    ] = None
    """
    Maximum number of multicast ids available in the system.
    """
    current_usage: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:current-usage',
            ge=0,
            le=18446744073709551615,
            title='Current-usageLeaf',
        ),
    ] = 0
    """
    The total number of multicast ids that are in use on the system.
    """
    total_pending: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast:total-pending',
            ge=0,
            le=18446744073709551615,
            title='Total-pendingLeaf',
        ),
    ] = 0
    """
    The total number of multicast ids pending allocation on the system.
    """
    multicast_id_user_type: Annotated[
        Optional[List[MulticastIdUserTypeListEntry]],
        Field(alias='srl_nokia-system-multicast:multicast-id-user-type'),
    ] = None


class StatisticsContainer18(BaseModel):
    """
    Aggregate statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    anno_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:anno-msg-tx',
            ge=0,
            le=4294967295,
            title='Anno-msg-txLeaf',
        ),
    ] = None
    """
    Specifies the number of announce messages transmitted
    """
    anno_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:anno-msg-rx',
            ge=0,
            le=4294967295,
            title='Anno-msg-rxLeaf',
        ),
    ] = None
    """
    Specifies the number of announce messages received
    """
    sync_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-msg-tx',
            ge=0,
            le=4294967295,
            title='Sync-msg-txLeaf',
        ),
    ] = None
    """
    Specifies the number of sync messages transmitted
    """
    sync_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-msg-rx',
            ge=0,
            le=4294967295,
            title='Sync-msg-rxLeaf',
        ),
    ] = None
    """
    Specifies the number of sync messages received
    """
    del_req_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-req-msg-tx',
            ge=0,
            le=4294967295,
            title='Del-req-msg-txLeaf',
        ),
    ] = None
    """
    Specifies the number of delay-req messages transmitted
    """
    del_req_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-req-msg-rx',
            ge=0,
            le=4294967295,
            title='Del-req-msg-rxLeaf',
        ),
    ] = None
    """
    Specifies the number of delay-req messages received
    """
    del_resp_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-resp-msg-tx',
            ge=0,
            le=4294967295,
            title='Del-resp-msg-txLeaf',
        ),
    ] = None
    """
    Specifies the number of delay-resp messages transmitted
    """
    del_resp_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:del-resp-msg-rx',
            ge=0,
            le=4294967295,
            title='Del-resp-msg-rxLeaf',
        ),
    ] = None
    """
    Specifies the number of delay-resp messages received
    """
    follow_up_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:follow-up-msg-tx',
            ge=0,
            le=4294967295,
            title='Follow-up-msg-txLeaf',
        ),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    follow_up_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:follow-up-msg-rx',
            ge=0,
            le=4294967295,
            title='Follow-up-msg-rxLeaf',
        ),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    signaling_msg_tx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:signaling-msg-tx',
            ge=0,
            le=4294967295,
            title='Signaling-msg-txLeaf',
        ),
    ] = None
    """
    Specifies the number of follow-up messages transmitted
    """
    signaling_msg_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:signaling-msg-rx',
            ge=0,
            le=4294967295,
            title='Signaling-msg-rxLeaf',
        ),
    ] = None
    """
    Specifies the number of follow-up messages received
    """
    other_rx: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:other-rx', ge=0, le=4294967295, title='Other-rxLeaf'
        ),
    ] = None
    """
    Specifies the number of other messages received
    """
    discards: Annotated[
        Optional[DiscardsContainer], Field(alias='srl_nokia-sync:discards')
    ] = None
    signaling_uni_neg_tlv: Annotated[
        Optional[SignalingUniNegTlvContainer],
        Field(alias='srl_nokia-sync:signaling-uni-neg-tlv'),
    ] = None
    sync_packet_loss: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-packet-loss',
            ge=0,
            le=4294967295,
            title='Sync-packet-lossLeaf',
        ),
    ] = 0
    """
    The number of events with detected packet loss of sync packets from the master clock
    """
    sync_high_packet_loss: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-high-packet-loss',
            ge=0,
            le=4294967295,
            title='Sync-high-packet-lossLeaf',
        ),
    ] = 0
    """
    The number of events with high packet loss of sync packets
    """
    delay_packet_loss: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:delay-packet-loss',
            ge=0,
            le=4294967295,
            title='Delay-packet-lossLeaf',
        ),
    ] = 0
    """
    The number of events with detected packet loss for the delay request/response packets
    """
    delay_high_packet_loss: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:delay-high-packet-loss',
            ge=0,
            le=4294967295,
            title='Delay-high-packet-lossLeaf',
        ),
    ] = 0
    """
    The number of events with high packet loss for delay req packets
    """
    unicast_msg_rate: Annotated[
        Optional[UnicastMsgRateContainer],
        Field(alias='srl_nokia-sync:unicast-msg-rate'),
    ] = None
    multicast_msg_rate: Annotated[
        Optional[MulticastMsgRateContainer],
        Field(alias='srl_nokia-sync:multicast-msg-rate'),
    ] = None


class StatisticsContainer19(BaseModel):
    """
    Time recovery engine state statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    time_in_initial: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-in-initial',
            ge=0,
            le=4294967295,
            title='Time-in-initialLeaf',
        ),
    ] = None
    """
    Specifies the number of seconds while in Initializing state
    """
    time_in_acquiring: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-in-acquiring',
            ge=0,
            le=4294967295,
            title='Time-in-acquiringLeaf',
        ),
    ] = None
    """
    Specifies the number of seconds while in Acquiring state
    """
    time_in_holdover: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-in-holdover',
            ge=0,
            le=4294967295,
            title='Time-in-holdoverLeaf',
        ),
    ] = None
    """
    Specifies the number of seconds while in Holdover state
    """
    time_in_locked: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-in-locked',
            ge=0,
            le=4294967295,
            title='Time-in-lockedLeaf',
        ),
    ] = None
    """
    Specifies the number of seconds while in Locked state
    """
    sync_too_much_pdv: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-too-much-pdv',
            ge=0,
            le=4294967295,
            title='Sync-too-much-pdvLeaf',
        ),
    ] = 0
    """
    The number of events with high PDV for sync packets for time recovery
    """
    delay_too_much_pdv: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:delay-too-much-pdv',
            ge=0,
            le=4294967295,
            title='Delay-too-much-pdvLeaf',
        ),
    ] = 0
    """
    The number of events with high PDV for delay request/response packets for time recovery
    """


class StatisticsContainer20(BaseModel):
    """
    Freq recovery engine state statistics for the PTP clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    time_in_initial: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-in-initial',
            ge=0,
            le=4294967295,
            title='Time-in-initialLeaf2',
        ),
    ] = None
    """
    Specifies the number of seconds while in Initializing state
    """
    time_in_acquiring: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-in-acquiring',
            ge=0,
            le=4294967295,
            title='Time-in-acquiringLeaf2',
        ),
    ] = None
    """
    Specifies the number of seconds while in Acquiring state
    """
    time_in_phase_tracking: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-in-phase-tracking',
            ge=0,
            le=4294967295,
            title='Time-in-phase-trackingLeaf',
        ),
    ] = None
    """
    Specifies the number of seconds while in Phase Tracking state
    """
    time_in_holdover: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-in-holdover',
            ge=0,
            le=4294967295,
            title='Time-in-holdoverLeaf2',
        ),
    ] = None
    """
    Specifies the number of seconds while in Holdover state
    """
    time_in_locked: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:time-in-locked',
            ge=0,
            le=4294967295,
            title='Time-in-lockedLeaf2',
        ),
    ] = None
    """
    Specifies the number of seconds while in Locked state
    """
    sync_high_phase_shift: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-high-phase-shift',
            ge=0,
            le=4294967295,
            title='Sync-high-phase-shiftLeaf',
        ),
    ] = 0
    """
    The number of events with large clock shift from sync packets for frequency recovery
    """
    sync_too_much_pdv: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:sync-too-much-pdv',
            ge=0,
            le=4294967295,
            title='Sync-too-much-pdvLeaf2',
        ),
    ] = 0
    """
    The number of events with high PDV for sync packets for frequency recovery
    """
    delay_high_phase_shift: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:delay-high-phase-shift',
            ge=0,
            le=4294967295,
            title='Delay-high-phase-shiftLeaf',
        ),
    ] = 0
    """
    The number of events with large clock shift for delay req packets for frequency recovery
    """
    delay_too_much_pdv: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:delay-too-much-pdv',
            ge=0,
            le=4294967295,
            title='Delay-too-much-pdvLeaf2',
        ),
    ] = 0
    """
    The number of events with high PDV for delay req packets for frequency recovery
    """


class StatisticsContainer5(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:active-entries',
            ge=0,
            le=18446744073709551615,
            title='Active-entriesLeaf',
        ),
    ] = 0
    """
    The total number of macs that are active on the system.
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:total-entries',
            ge=0,
            le=18446744073709551615,
            title='Total-entriesLeaf',
        ),
    ] = 0
    """
    The total number of macs, active and inactive, on the system.
    """
    failed_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table:failed-entries',
            ge=0,
            le=18446744073709551615,
            title='Failed-entriesLeaf',
        ),
    ] = 0
    """
    The total number of macs, which have not been programmed on atleast one slot
    """
    mac_type: Annotated[
        Optional[List[MacTypeListEntry]],
        Field(alias='srl_nokia-system-bridge-table:mac-type'),
    ] = None


class StatisticsContainer6(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    max_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:max-entries',
            ge=0,
            le=18446744073709551615,
            title='Max-entriesLeaf',
        ),
    ] = 0
    """
    The maximum number of BGP-EVPN MPLS multicast Termination EndPoints (TEPs) allowed in the system
    """
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:total-entries',
            ge=0,
            le=18446744073709551615,
            title='Total-entriesLeaf3',
        ),
    ] = 0
    """
    The total number of BGP-EVPN MPLS multicast Termination EndPoints (TEPs)
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:active-entries',
            ge=0,
            le=18446744073709551615,
            title='Active-entriesLeaf3',
        ),
    ] = 0
    """
    The total number of active BGP-EVPN MPLS multicast Termination Endpoints (TEPs)
    """


class StatisticsContainer7(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:total-entries',
            ge=0,
            le=18446744073709551615,
            title='Total-entriesLeaf4',
        ),
    ] = 0
    """
    The total number of proxy entries.
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:active-entries',
            ge=0,
            le=18446744073709551615,
            title='Active-entriesLeaf4',
        ),
    ] = 0
    """
    The total number of active proxy entries.
    """
    in_active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:in-active-entries',
            ge=0,
            le=18446744073709551615,
            title='In-active-entriesLeaf',
        ),
    ] = 0
    """
    The total number of inactive proxy entries.
    """
    pending_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:pending-entries',
            ge=0,
            le=18446744073709551615,
            title='Pending-entriesLeaf',
        ),
    ] = 0
    """
    The total number of pending proxy entries.
    """
    neighbor_origin: Annotated[
        Optional[List[NeighborOriginListEntry]],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:neighbor-origin'),
    ] = None


class StatisticsContainer8(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    total_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:total-entries',
            ge=0,
            le=18446744073709551615,
            title='Total-entriesLeaf6',
        ),
    ] = 0
    """
    The total number of proxy entries.
    """
    active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:active-entries',
            ge=0,
            le=18446744073709551615,
            title='Active-entriesLeaf6',
        ),
    ] = 0
    """
    The total number of active proxy entries.
    """
    in_active_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:in-active-entries',
            ge=0,
            le=18446744073709551615,
            title='In-active-entriesLeaf3',
        ),
    ] = 0
    """
    The total number of inactive proxy entries.
    """
    pending_entries: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-proxy-arp:pending-entries',
            ge=0,
            le=18446744073709551615,
            title='Pending-entriesLeaf3',
        ),
    ] = 0
    """
    The total number of pending proxy entries.
    """
    neighbor_origin: Annotated[
        Optional[List[NeighborOriginListEntry2]],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:neighbor-origin'),
    ] = None


class StatisticsContainer9(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    active_sessions: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:active-sessions',
            ge=1,
            le=64,
            title='Active-sessionsLeaf',
        ),
    ] = None
    """
    Active NETCONF sessions

    The total number of active NETCONF sessions.  A session is defined as an individual client connection
    over which a NETCONF session has been started by providing bi-directional <hello> messages
    """
    total_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-requests',
            ge=0,
            le=4294967295,
            title='Total-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF total requests

    Total number of NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_responses: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-responses',
            ge=0,
            le=4294967295,
            title='Total-responsesLeaf',
        ),
    ] = 0
    """
    NETCONF total responses

    Total number of NETCONF responses that have been generated and sent by the NETCONF server
    """
    total_error_responses: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-error-responses',
            ge=0,
            le=4294967295,
            title='Total-error-responsesLeaf',
        ),
    ] = 0
    """
    NETCONF error responses

    Total number of NETCONF error responses that have been generated and sent by the NETCONF server
    """
    total_close_session_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-close-session-requests',
            ge=0,
            le=4294967295,
            title='Total-close-session-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <close-session> requests

    Total number of <close-session> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_in_bad_hellos: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-in-bad-hellos',
            ge=0,
            le=4294967295,
            title='Total-in-bad-hellosLeaf',
        ),
    ] = 0
    """
    Inbound bad NETCONF hello messages

    Total number of bad NETCONF hello messages that have been received by the NETCONF server
    """
    total_dropped_sessions: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-dropped-sessions',
            ge=0,
            le=4294967295,
            title='Total-dropped-sessionsLeaf',
        ),
    ] = 0
    """
    NETCONF dropped sessions

    Total number of dropped NETCONF sessions
    """
    total_get_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-get-requests',
            ge=0,
            le=4294967295,
            title='Total-get-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <get> requests

    Total number of <get> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_get_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-get-config-requests',
            ge=0,
            le=4294967295,
            title='Total-get-config-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <get-config> requests

    Total number of <get-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_get_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-get-data-requests',
            ge=0,
            le=4294967295,
            title='Total-get-data-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <get-data> requests

    Total number of <get-data> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_get_schema_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-get-schema-requests',
            ge=0,
            le=4294967295,
            title='Total-get-schema-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <get-schema> requests

    Total number of <get-schema> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_edit_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-edit-config-requests',
            ge=0,
            le=4294967295,
            title='Total-edit-config-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <edit-config> requests

    Total number of <edit-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_failed_edit_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-failed-edit-config-requests',
            ge=0,
            le=4294967295,
            title='Total-failed-edit-config-requestsLeaf',
        ),
    ] = 0
    """
    Failed NETCONF <edit-config> requests

    Total number of <edit-config> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    total_edit_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-edit-data-requests',
            ge=0,
            le=4294967295,
            title='Total-edit-data-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <edit-data> requests

    Total number of <edit-data> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_failed_edit_data_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-failed-edit-data-requests',
            ge=0,
            le=4294967295,
            title='Total-failed-edit-data-requestsLeaf',
        ),
    ] = 0
    """
    Failed NETCONF <edit-data> requests

    Total number of <edit-data> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    total_kill_session_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-kill-session-requests',
            ge=0,
            le=4294967295,
            title='Total-kill-session-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <kill-session> requests

    Total number of <kill-session> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_copy_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-copy-config-requests',
            ge=0,
            le=4294967295,
            title='Total-copy-config-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <copy-config> requests

    Total number of copy-config NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_delete_config_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-delete-config-requests',
            ge=0,
            le=4294967295,
            title='Total-delete-config-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <delete-config> requests

    Total number of <delete-config> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_validate_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-validate-requests',
            ge=0,
            le=4294967295,
            title='Total-validate-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <validate> requests

    Total number of <validate> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_lock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-lock-requests',
            ge=0,
            le=4294967295,
            title='Total-lock-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <lock> requests

    Total number of <lock> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_failed_lock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-failed-lock-requests',
            ge=0,
            le=4294967295,
            title='Total-failed-lock-requestsLeaf',
        ),
    ] = 0
    """
    Failed NETCONF <lock> requests

    Total number of <lock> NETCONF requests that have failed because of locks taken by other NETCONF sessions
    """
    total_unlock_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-unlock-requests',
            ge=0,
            le=4294967295,
            title='Total-unlock-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <unlock> requests

    Total number of <unlock> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_commit_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-commit-requests',
            ge=0,
            le=4294967295,
            title='Total-commit-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <commit> requests

    Total number of commit NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_discard_changes_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-discard-changes-requests',
            ge=0,
            le=4294967295,
            title='Total-discard-changes-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <discard-changes> requests

    Total number of <discard-changes> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    total_action_requests: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:total-action-requests',
            ge=0,
            le=4294967295,
            title='Total-action-requestsLeaf',
        ),
    ] = 0
    """
    NETCONF <action> requests

    Total number of <action> NETCONF requests that have been accepted and processed by the NETCONF server
    """
    session: Annotated[
        Optional[List[SessionListEntry2]],
        Field(alias='srl_nokia-netconf-server:session'),
    ] = None


class SubinterfaceListEntry(BaseModel):
    """
    List of subinterfaces used as mirror source
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str], Field(alias='srl_nokia-mirroring:name', title='NameLeaf17')
    ] = None
    """
    Reference type to a specific subinterface of the form <interface-name>.<subinterface-index>
    """
    direction: Annotated[
        Optional[EnumerationEnum26],
        Field(alias='srl_nokia-mirroring:direction', title='DirectionLeaf2'),
    ] = 'egress-only'
    """
    The direction of traffic to be mirrored
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-mirroring:oper-state', title='Oper-stateLeaf7'),
    ] = None
    """
    This leaf contains the operational state of the mirror-source.
    """
    oper_down_reason: Annotated[
        Optional[EnumerationEnum27],
        Field(
            alias='srl_nokia-mirroring:oper-down-reason', title='Oper-down-reasonLeaf2'
        ),
    ] = None
    """
    The reason for the mirror source being operational down.  When the reason is not applicable, it is due to the mirror instance being shutdown or the mirror source is operational up.
    """


class SubscriberListEntry(BaseModel):
    """
    Indicates the LI target is a broadband subsriber
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subscriber_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lawful-intercept:subscriber-name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Subscriber-nameLeaf',
        ),
    ] = None
    """
    Specify the LI target is a wireline subscriber and is identified by the subscriber name/id
    """
    description: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lawful-intercept:description',
            max_length=255,
            min_length=1,
            title='DescriptionLeaf5',
        ),
    ] = None
    """
    A user-entered description of this LI target
    """
    intercept_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:intercept-id',
            ge=1,
            le=4294967295,
            title='Intercept-idLeaf',
        ),
    ] = None
    """
    Specifies the shim header intercept-id
    """
    session_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:session-id',
            ge=1,
            le=4294967295,
            title='Session-idLeaf2',
        ),
    ] = None
    """
    Specifies the shim header session-id
    """
    direction: Annotated[
        EnumerationEnum67,
        Field(alias='srl_nokia-lawful-intercept:direction', title='DirectionLeaf4'),
    ]
    """
    The direction of traffic to be mirrored
    """
    mirror_instance_name: Annotated[
        str,
        Field(
            alias='srl_nokia-lawful-intercept:mirror-instance-name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Mirror-instance-nameLeaf',
        ),
    ]
    """
    Specifies that the mirror instance name would be used to identify the mirror destination.  In the case of MAG-c the mirror-instance-name should match the mirror service name on the User Plane
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-lawful-intercept:oper-state', title='Oper-stateLeaf21'),
    ] = None
    """
    Indicates the lawful intercept operational state of the subscriber, true indicates that the subscriber is online and interception is active, false indicates the interception has not started
    """
    oper_down_reason: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lawful-intercept:oper-down-reason',
            title='Oper-down-reasonLeaf8',
        ),
    ] = None
    """
    Indicates the interception has not started because either the subscriber is not online or a problem occured
    """


class SubscribersContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    total_configured: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:total-configured',
            ge=0,
            le=18446744073709551615,
            title='Total-configuredLeaf',
        ),
    ] = 0
    """
    Total number of subscribers provisioned as LI target in the system
    """
    total_active: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:total-active',
            ge=0,
            le=18446744073709551615,
            title='Total-activeLeaf',
        ),
    ] = 0
    """
    Total number of subscribers that are currently in active LI session on the system
    """
    total_down: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:total-down',
            ge=0,
            le=18446744073709551615,
            title='Total-downLeaf',
        ),
    ] = 0
    """
    Total number of subscribers that are not currently in active LI session on the system
    """
    total_error: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lawful-intercept:total-error',
            ge=0,
            le=18446744073709551615,
            title='Total-errorLeaf',
        ),
    ] = 0
    """
    Total number of subscribers that have failed LI
    """


class TacacsContainer2(BaseModel):
    """
    Top-level container for TACACS+ server data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:port', ge=0, le=65535, title='PortLeaf2'),
    ] = 49
    """
    The port number on which to contact the TACACS+ server
    """
    secret_key: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:secret-key', title='Secret-keyLeaf')
    ] = None
    """
    The unencrypted shared key used between the system and server
    """
    source_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-aaa:source-address', title='Source-addressLeaf'),
    ] = None
    """
    Source address for TACACS to use for messages sent to a remote server
    """


class TepListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    tep: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:tep',
            title='TepLeaf',
        ),
    ] = None
    """
    The IP address that identifies the remote BGP-EVPN MPLS multicast Termination Endpoint (TEP)
    """
    index: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:index',
            ge=0,
            le=18446744073709551615,
            title='IndexLeaf5',
        ),
    ] = None
    """
    The hardware index (system allocated) for the BGP-EVPN MPLS multicast Termination Endpoint (TEP)

    If a non-zero hardware index is allocated, then there are available system resources and there is
    at least one BGP-EVPN MPLS multicast destination (using this TEP) ready to be programmed. If the
    hardware index is 0, there are not resources left and the TEP is not programmed, even if an Inclusive
    Multicast Ethernet Tag route was correctly imported from a peer.
    """
    last_changed: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:last-changed',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-changedLeaf',
        ),
    ] = None
    """
    The date and time of the last update of this BGP-EVPN MPLS multicast Termination Endpoint
    """


class TimePropertiesDsContainer(BaseModel):
    """
    The timeProperties data set of the clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    current_utc_offset_valid: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-sync:current-utc-offset-valid',
            title='Current-utc-offset-validLeaf',
        ),
    ] = None
    """
    When set to true, the current UTC offset is valid
    """
    current_utc_offset: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:current-utc-offset',
            ge=-32768,
            le=32767,
            title='Current-utc-offsetLeaf',
        ),
    ] = None
    """
    The offset between TAI and UTC

    Only applies when the epoch of the PTP system is the PTP epoch in units of seconds
    (i.e. when ptp-timescale is TRUE). Otherwise, the value has no meaning.
    """
    leap59: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:leap59', title='Leap59Leaf')
    ] = None
    """
    If true, the last minute of the current UTC day contains 59 seconds
    """
    leap61: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:leap61', title='Leap61Leaf')
    ] = None
    """
    If true, the last minute of the current UTC day contains 61 seconds
    """
    time_traceable: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:time-traceable', title='Time-traceableLeaf'),
    ] = None
    """
    If true, the timescale and the currentUtcOffset are traceable to a primary reference
    """
    frequency_traceable: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-sync:frequency-traceable', title='Frequency-traceableLeaf'
        ),
    ] = None
    """
    If true, the frequency determining the timescale is traceable to a primary reference
    """
    ptp_timescale: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:ptp-timescale', title='Ptp-timescaleLeaf'),
    ] = None
    """
    If true clock timescale of the grandmaster is PTP; false it is ARB (arbitrary)
    """
    time_source: Annotated[
        Optional[EnumerationEnum79],
        Field(alias='srl_nokia-sync:time-source', title='Time-sourceLeaf'),
    ] = None
    """
    The source of time used by the grandmaster clock

    If a value is received that does not map to one of the enumerations, then the reserved value is used
    """


class TimeRecoveryEngineContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    recovery_state: Annotated[
        Optional[EnumerationEnum77],
        Field(alias='srl_nokia-sync:recovery-state', title='Recovery-stateLeaf'),
    ] = None
    """
    Specifies the current state of the time recovery engine in the PTP clock
    """
    state_last_changed: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:state-last-changed',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='State-last-changedLeaf',
        ),
    ] = None
    """
    Specifies the last occurrence of a ptp state change for the time recovery engine
    """
    last_adjustment: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:last-adjustment',
            ge=-9223372036854775808,
            le=9223372036854775807,
            title='Last-adjustmentLeaf',
        ),
    ] = None
    """
    Specifies the last adjustment in nanoseconds to the local time of the PTP clock
    """
    last_adjustment_timestamp: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:last-adjustment-timestamp',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-adjustment-timestampLeaf',
        ),
    ] = None
    """
    The time when last-adjustment was last calculated
    """
    statistics: Annotated[
        Optional[StatisticsContainer19], Field(alias='srl_nokia-sync:statistics')
    ] = None


class TimersContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    boot_timer: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:boot-timer',
            ge=0,
            le=6000,
            title='Boot-timerLeaf',
        ),
    ] = 10
    """
    Remaining time before running BGP EVPN multi-homing DF election algorithm
    """
    activation_timer: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:activation-timer',
            ge=0,
            le=100,
            title='Activation-timerLeaf',
        ),
    ] = 3
    boot_remaining_time: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:boot-remaining-time',
            ge=0,
            le=4294967295,
            title='Boot-remaining-timeLeaf',
        ),
    ] = None
    """
    Indicates the number of seconds remaining for the boot timer to expire.
    """
    boot_start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:boot-start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Boot-start-timeLeaf',
        ),
    ] = None
    """
    Indicates the time at which the boot timer started.
    """


class TraceOptionsContainer(BaseModel):
    """
    Debug trace-options for NETCONF
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    direction: Annotated[
        Optional[EnumerationEnum44],
        Field(alias='srl_nokia-netconf-server:direction', title='DirectionLeaf3'),
    ] = 'both'
    """
    Direction to trace messages
    """
    rpc: Annotated[
        Optional[List[EnumerationEnum45]], Field(alias='srl_nokia-netconf-server:rpc')
    ] = []
    """
    RPC messages to trace
    """


class TraceOptionsContainer2(BaseModel):
    """
    Container for tracing DHCP server operations instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trace: Annotated[
        Optional[List[EnumerationEnum62]], Field(alias='srl_nokia-dhcp-server:trace')
    ] = []
    """
    List of events to trace
    """


class TraceOptionsContainer3(BaseModel):
    """
    Container for tracing DHCP server operations instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trace: Annotated[
        Optional[List[EnumerationEnum63]], Field(alias='srl_nokia-dhcp-server:trace')
    ] = []
    """
    List of events to trace
    """


class TrustAnchorContainer(BaseModel):
    """
    State relating to the active trust anchor provided via Certz

    This is equivalent to the certificate authority bundle, and is the list of certificates used to validate clients in mTLS, and to validate servers in outbound TLS.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-certz:version', title='VersionLeaf5')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-certz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf5',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class TrustAnchorContainer2(BaseModel):
    """
    State relating to the active trust anchor provided via Certz

    This is equivalent to the certificate authority bundle, and is the list of certificates used to validate clients in mTLS, and to validate servers in outbound TLS.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-grpc:version', title='VersionLeaf18')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf18',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class TrustedUserCaKeysContainer(BaseModel):
    """
    State relating to the Certificate Authorities provided via Credentialz.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str],
        Field(alias='srl_nokia-gnsi-credentialz:version', title='VersionLeaf'),
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-credentialz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class UnicastNegotiationContainer(BaseModel):
    """
    Details of each negotiation session
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rx_announce: Annotated[
        Optional[RxAnnounceContainer], Field(alias='srl_nokia-sync:rx-announce')
    ] = None
    rx_sync: Annotated[
        Optional[RxSyncContainer], Field(alias='srl_nokia-sync:rx-sync')
    ] = None
    rx_delay_resp: Annotated[
        Optional[RxDelayRespContainer], Field(alias='srl_nokia-sync:rx-delay-resp')
    ] = None
    tx_announce: Annotated[
        Optional[TxAnnounceContainer], Field(alias='srl_nokia-sync:tx-announce')
    ] = None
    tx_sync: Annotated[
        Optional[TxSyncContainer], Field(alias='srl_nokia-sync:tx-sync')
    ] = None
    tx_delay_resp: Annotated[
        Optional[TxDelayRespContainer], Field(alias='srl_nokia-sync:tx-delay-resp')
    ] = None


class UnicastNegotiationContainer2(BaseModel):
    """
    Details of each negotiation session
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    rx_announce: Annotated[
        Optional[RxAnnounceContainer2], Field(alias='srl_nokia-sync:rx-announce')
    ] = None
    rx_sync: Annotated[
        Optional[RxSyncContainer2], Field(alias='srl_nokia-sync:rx-sync')
    ] = None
    rx_delay_resp: Annotated[
        Optional[RxDelayRespContainer2], Field(alias='srl_nokia-sync:rx-delay-resp')
    ] = None
    tx_announce: Annotated[
        Optional[TxAnnounceContainer2], Field(alias='srl_nokia-sync:tx-announce')
    ] = None
    tx_sync: Annotated[
        Optional[TxSyncContainer2], Field(alias='srl_nokia-sync:tx-sync')
    ] = None
    tx_delay_resp: Annotated[
        Optional[TxDelayRespContainer2], Field(alias='srl_nokia-sync:tx-delay-resp')
    ] = None


class UnixSocketContainer(BaseModel):
    """
    Top-level container for configuration and state related to unix sockets
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-grpc:admin-state', title='Admin-stateLeaf4'),
    ] = 'disable'
    """
    Administratively enable or disable the gRPC server
    """
    socket_path: Annotated[
        Optional[str],
        Field(alias='srl_nokia-grpc:socket-path', title='Socket-pathLeaf'),
    ] = None
    """
    Path to the unix socket used by gRPC
    """


class UnixSocketContainer3(BaseModel):
    """
    Top-level container for configuration and state related to unix sockets
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-json-rpc:admin-state', title='Admin-stateLeaf25'),
    ] = 'disable'
    """
    Administratively enable or disable the JSON RPC server via unix socket
    This requires the JSON RPC server to be globally enabled
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-json-rpc:oper-state', title='Oper-stateLeaf19'),
    ] = None
    """
    Details if the JSON RPC server is operationally available
    """
    use_authentication: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-json-rpc:use-authentication',
            title='Use-authenticationLeaf3',
        ),
    ] = True
    """
    Enable or disable the use of username/password authentication for every JSON RPC request
    """
    socket_path: Annotated[
        Optional[str],
        Field(alias='srl_nokia-json-rpc:socket-path', title='Socket-pathLeaf3'),
    ] = None
    """
    Path to the unix socket used by JSON RPC
    """
    tls_profile: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-json-rpc:tls-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Tls-profileLeaf3',
        ),
    ] = None
    """
    Reference to the TLS profile to use on the JSON RPC unix socket server

    If none is specified, then TLS is not used.
    """


class UtilizationContainer(BaseModel):
    """
    Configuration and state for each system resource
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    resource: Annotated[
        Optional[List[ResourceListEntry]],
        Field(alias='srl_nokia-system-utilization:resource'),
    ] = None


class AclFilterListEntry(BaseModel):
    """
    List MAC, IPv4, IPv6 ACL filter(s) to be applied on this subinterface direction
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str], Field(alias='srl_nokia-acl:name', title='NameLeaf')
    ] = None
    """
    Referencence to the ACL Filter policy name
    """
    type: Annotated[
        Optional[EnumerationEnum5], Field(alias='srl_nokia-acl:type', title='TypeLeaf')
    ] = None
    """
    Referencence to the ACL Filter policy type
    """


class AclFilterListEntry2(BaseModel):
    """
    List  IPv4, IPv6 ACL filters
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str], Field(alias='srl_nokia-mirroring:name', title='NameLeaf18')
    ] = None
    """
    ACL Filter policy name
    """
    type: Annotated[
        Optional[EnumerationEnum5],
        Field(alias='srl_nokia-mirroring:type', title='TypeLeaf7'),
    ] = None
    """
    Reference to the ACL filter policy type
    """
    entry: Annotated[
        Optional[List[EntryListEntry]], Field(alias='srl_nokia-mirroring:entry')
    ] = None


class AclContainer(BaseModel):
    """
    Container for ACL.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    acl_filter: Annotated[
        Optional[List[AclFilterListEntry]], Field(alias='srl_nokia-acl:acl-filter')
    ] = None


class AclContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    acl_filter: Annotated[
        Optional[List[AclFilterListEntry2]],
        Field(alias='srl_nokia-mirroring:acl-filter'),
    ] = None


class AlgorithmContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    type: Annotated[
        Optional[EnumerationEnum34],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:type',
            title='TypeLeaf10',
        ),
    ] = 'default'
    """
    Designated Forwarder algorithm type for this ethernet-segment.
    """
    oper_type: Annotated[
        Optional[EnumerationEnum34],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-type',
            title='Oper-typeLeaf',
        ),
    ] = None
    """
    Operational Designated Forwarder algorithm type for this ethernet-segment.
    """
    preference_alg: Annotated[
        Optional[PreferenceAlgContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:preference-alg'
        ),
    ] = None
    manual_alg: Annotated[
        Optional[ManualAlgContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:manual-alg'
        ),
    ] = None


class ApplicationListEntry(BaseModel):
    """
    List of all applications managed by the application manager
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str], Field(alias='srl_nokia-app-mgmt:name', title='NameLeaf35')
    ] = None
    """
    Unique name of this application instance
    """
    pid: Annotated[
        Optional[int],
        Field(alias='srl_nokia-app-mgmt:pid', ge=0, le=4294967295, title='PidLeaf'),
    ] = None
    """
    Process ID of this application instance
    """
    state: Annotated[
        Optional[EnumerationEnum59],
        Field(alias='srl_nokia-app-mgmt:state', title='StateLeaf'),
    ] = None
    """
    Current state of this application instance
    """
    last_change: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-app-mgmt:last-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-changeLeaf2',
        ),
    ] = None
    """
    Date and time the application instance last changed state
    """
    last_start_type: Annotated[
        Optional[EnumerationEnum60],
        Field(alias='srl_nokia-app-mgmt:last-start-type', title='Last-start-typeLeaf'),
    ] = None
    """
    Indicates the type of the most recent start or restart of this application instance
    """
    supported_restart_types: Annotated[
        Optional[List[EnumerationEnum60]],
        Field(alias='srl_nokia-app-mgmt:supported-restart-types'),
    ] = []
    """
    Indicates the supported restart types for this application
    """
    author: Annotated[
        Optional[str], Field(alias='srl_nokia-app-mgmt:author', title='AuthorLeaf')
    ] = None
    """
    The author of the application
    """
    failure_threshold: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-app-mgmt:failure-threshold',
            ge=0,
            le=255,
            title='Failure-thresholdLeaf',
        ),
    ] = None
    """
    How many restarts within 'failure-window' are required to trigger the failure action

    Setting this value to 0 will result in no action taking place on application restarts
    """
    failure_window: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-app-mgmt:failure-window',
            ge=300,
            le=86400,
            title='Failure-windowLeaf',
        ),
    ] = None
    """
    Sliding window in seconds, over which to count restarts towards failure-threshold
    """
    failure_action: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-app-mgmt:failure-action',
            pattern='^(?=^(reboot|wait=(forever|\\d*))$).*$',
            title='Failure-actionLeaf',
        ),
    ] = None
    """
    The action taken after 'failure-threshold' failures within 'failure-window'

    This action can be to reboot the system, wait forever, or wait for a predefined number of seconds
    """
    path: Annotated[
        Optional[str], Field(alias='srl_nokia-app-mgmt:path', title='PathLeaf2')
    ] = None
    """
    The directory where the application can be found
    """
    launch_command: Annotated[
        Optional[str],
        Field(alias='srl_nokia-app-mgmt:launch-command', title='Launch-commandLeaf'),
    ] = None
    """
    The command used to launch the application
    """
    search_command: Annotated[
        Optional[str],
        Field(alias='srl_nokia-app-mgmt:search-command', title='Search-commandLeaf'),
    ] = None
    """
    The command used to search for the applications liveness
    """
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-app-mgmt:version', title='VersionLeaf23')
    ] = None
    """
    The version of the application
    """
    restricted_operations: Annotated[
        Optional[List[EnumerationEnum61]],
        Field(alias='srl_nokia-app-mgmt:restricted-operations'),
    ] = []
    """
    The operations that may not be manually performed on this application
    """
    oom_score_adj: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-app-mgmt:oom-score-adj',
            ge=-2147483648,
            le=2147483647,
            title='Oom-score-adjLeaf',
        ),
    ] = None
    """
    OOM score adj value set for this application
    """
    cgroup: Annotated[
        Optional[str], Field(alias='srl_nokia-app-mgmt:cgroup', title='CgroupLeaf')
    ] = None
    """
    Cgroup in with this application is started
    """
    statistics: Annotated[
        Optional[StatisticsContainer13], Field(alias='srl_nokia-app-mgmt:statistics')
    ] = None
    yang: Annotated[Optional[YangContainer], Field(alias='srl_nokia-app-mgmt:yang')] = (
        None
    )


class AuthorizedKeysContainer(BaseModel):
    """
    State relating to the Authorized Keys provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:version', title='VersionLeaf8')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf8',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedKeysContainer2(BaseModel):
    """
    State relating to the Authorized Keys provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:version', title='VersionLeaf11')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf11',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedKeysContainer3(BaseModel):
    """
    State relating to the Authorized Keys provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:version', title='VersionLeaf14')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf14',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedPrincipalsContainer(BaseModel):
    """
    State relating to the Authorized Principals provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:version', title='VersionLeaf9')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf9',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedPrincipalsContainer2(BaseModel):
    """
    State relating to the Authorized Principals provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:version', title='VersionLeaf12')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf12',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthorizedPrincipalsContainer3(BaseModel):
    """
    State relating to the Authorized Principals provided via Credentialz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:version', title='VersionLeaf15')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the artifact

    The maps to the version field within a Entity message in the Credentialz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf15',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the artifact

    The maps to the created_on field within a Entity message in the Credentialz protobuf.
    """


class AuthzPolicyContainer(BaseModel):
    """
    Information relating to the active gRPC authorization policy

    This policy is provided by the gNSI gRPC service, and can be changed using the gNSI.Authz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str],
        Field(alias='srl_nokia-gnsi-authz:version', title='VersionLeaf16'),
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the policy

    The maps to the version field within a UploadRequest message in the Authz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-authz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf16',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    This maps to the created_on field within a UploadRequest message in the Authz protobuf.
    """
    policy: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-authz:policy', title='PolicyLeaf')
    ] = None
    """
    The policy definition

    This JSON string contains the full gRPC authorization rules conforming to the gRPC authorization policy schema.

    This maps to the policy field within a UploadRequest message in the Authz protobuf.
    """
    counters: Annotated[
        Optional[CountersContainer2], Field(alias='srl_nokia-gnsi-authz:counters')
    ] = None


class AutobootContainer(BaseModel):
    """
    Top-level container for configuration and state data related to autobooting the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-boot:admin-state', title='Admin-stateLeaf18'),
    ] = None
    """
    Administratively enable or disable autoboot functionality
    """
    oper_state: Annotated[
        Optional[str],
        Field(alias='srl_nokia-boot:oper-state', title='Oper-stateLeaf14'),
    ] = None
    """
    The current operational status of the autoboot process
    """
    timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-boot:timeout', ge=200, le=3600, title='TimeoutLeaf4'),
    ] = None
    """
    Sets the timeout for each attempt to autoboot
    """
    attempts: Annotated[
        Optional[int],
        Field(alias='srl_nokia-boot:attempts', ge=1, le=10, title='AttemptsLeaf2'),
    ] = None
    """
    Sets the amount of executions to try autoboot, before rebooting the system
    """
    interface: Annotated[
        Optional[str], Field(alias='srl_nokia-boot:interface', title='InterfaceLeaf')
    ] = 'mgmt0'
    """
    Sets the interface to use for autoboot functionality
    """
    client_id: Annotated[
        Optional[EnumerationEnum52],
        Field(alias='srl_nokia-boot:client-id', title='Client-idLeaf'),
    ] = None
    """
    The client ID to use on outgoing DHCP requests
    """
    mode: Annotated[Optional[List[str]], Field(alias='srl_nokia-boot:mode')] = []
    """
    Ztp operation modes. One or more modes can passed
    """


class AutodiscoveryPerEthernetSegmentRoutesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    route_distinguisher: Annotated[
        Optional[
            Union[
                RouteDistinguisherType0Type,
                RouteDistinguisherType1Type,
                RouteDistinguisherType2Type,
                RouteDistinguisherType2bType,
            ]
        ],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:route-distinguisher',
            title='Route-distinguisherLeaf',
        ),
    ] = None
    """
    The route distinguisher encoded in the NLRI
    """
    esi: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:esi',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){9}$).*$',
            title='EsiLeaf2',
        ),
    ] = None
    """
    The Ethernet Segment Identifier encoded in the NLRI
    """
    ethernet_tag_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-tag-id',
            ge=0,
            le=4294967295,
            title='Ethernet-tag-idLeaf',
        ),
    ] = None
    """
    The 32-bit Ethernet Tag ID encoded in the NLRI. The Ethernet Tag ID identifies a broadcast domain
    """
    neighbor: Annotated[
        Optional[Union[Ipv4AddressWithZoneType, Ipv6AddressWithZoneType]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:neighbor',
            title='NeighborLeaf',
        ),
    ] = None
    """
    If the route was learned from a BGP neighbor, this is the IPv4 or IPv6 address of that neighbor
    """
    path_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:path-id',
            ge=0,
            le=4294967295,
            title='Path-idLeaf',
        ),
    ] = None
    """
    Path identifier of the BGP route
    """
    label: Annotated[
        Optional[LabelContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:label'
        ),
    ] = None
    attr_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:attr-id',
            ge=0,
            le=18446744073709551615,
            title='Attr-idLeaf',
        ),
    ] = None
    """
    Leaf reference to networkinstance/protocols/bgp/rib/attr-sets/attr-set/index.
    """


class BgpAutoDiscoveryContainer2(BaseModel):
    """
    Configuration and state related to LLDP BGP auto discovery on the interface
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-lldp:admin-state', title='Admin-stateLeaf16'),
    ] = 'enable'
    """
    Enable or disable LLDP BGP auto discovery on this interface
    """
    peering_address: Annotated[
        Optional[List[Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(alias='srl_nokia-lldp:peering-address'),
    ] = []
    """
    List of IP addresses to be sent for BGP auto discovery

    Default values for this sub-TLV is to populate the addresses
    of the first subinterface of the interface the LLDPDU is being
    generated from, along with a unicast AFI/SAFI for IPv4 if an IPv4
    address exists, and/or IPv6 if an IPv6 address exists.

    If neither of these exist in the system, LLDP will not add the TLV
    to outgoing LLDPDUs, unless the peering-address is manually configured
    on a per-LLDP-port basis.
    """
    group_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:group-id', ge=0, le=4294967295, title='Group-idLeaf2'
        ),
    ] = None
    """
    A four byte integer to send on outgoing LLDPDUs

    This value can be used on the remote end to do peer group association.
    This sub-TLV is not sent by default.
    """


class BgpContainer2(BaseModel):
    """
    Container for specifying the BGP members of the maintenance group
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[List[NetworkInstanceListEntry4]],
        Field(alias='srl_nokia-maintenance-mode:network-instance'),
    ] = None


class BgpContainer3(BaseModel):
    """
    Container for BGP policies used to achieve traffic draining
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    import_policy: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-maintenance-mode:import-policy',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Import-policyLeaf',
        ),
    ] = None
    """
    A reference to the pre-configured routing policy to apply as an additional/final import policy on BGP sessions in the maintenance group
    """
    export_policy: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-maintenance-mode:export-policy',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Export-policyLeaf',
        ),
    ] = None
    """
    A reference to the pre-configured routing policy to apply as an additional/final export policy on BGP sessions in the maintenance group
    """


class CertificateContainer(BaseModel):
    """
    State relating to the active certificate provided via Certz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-certz:version', title='VersionLeaf4')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-certz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf4',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class CertificateContainer2(BaseModel):
    """
    State relating to the active certificate provided via Certz
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str], Field(alias='srl_nokia-grpc:version', title='VersionLeaf17')
    ] = None
    """
    The version string as provided by the gNSI client at the time of uploading the certificate or bundle/s

    The maps to the version field within a Entity message in the Certz protobuf.
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf17',
        ),
    ] = None
    """
    The created on timestamp as provided by the gNSI client at the time of uploading the policy

    The maps to the created_on field within a Entity message in the Certz protobuf.
    """


class CertzContainer(BaseModel):
    """
    Information relating to the active certificate and bundle/s as provided via Certz

    State is provided by the gNSI Certz service, and can be changed using the gNSI.Certz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ssl_profile_id: Annotated[
        Optional[str],
        Field(alias='srl_nokia-gnsi-certz:ssl-profile-id', title='Ssl-profile-idLeaf'),
    ] = None
    """
    The ID of this gRPC server's SSL profile as used by the gNSI Certz service
    """
    certificate: Annotated[
        Optional[CertificateContainer], Field(alias='srl_nokia-gnsi-certz:certificate')
    ] = None
    trust_anchor: Annotated[
        Optional[TrustAnchorContainer], Field(alias='srl_nokia-gnsi-certz:trust-anchor')
    ] = None
    crl: Annotated[Optional[CrlContainer], Field(alias='srl_nokia-gnsi-certz:crl')] = (
        None
    )


class CertzContainer2(BaseModel):
    """
    Information relating to the active certificate and bundle/s as provided via Certz

    State is provided by the gNSI Certz service, and can be changed using the gNSI.Certz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ssl_profile_id: Annotated[
        Optional[str],
        Field(alias='srl_nokia-grpc:ssl-profile-id', title='Ssl-profile-idLeaf2'),
    ] = None
    """
    The ID of this gRPC server's SSL profile as used by the gNSI Certz service
    """
    certificate: Annotated[
        Optional[CertificateContainer2], Field(alias='srl_nokia-grpc:certificate')
    ] = None
    trust_anchor: Annotated[
        Optional[TrustAnchorContainer2], Field(alias='srl_nokia-grpc:trust-anchor')
    ] = None
    crl: Annotated[Optional[CrlContainer2], Field(alias='srl_nokia-grpc:crl')] = None


class CheckpointListEntry(BaseModel):
    """
    List of current checkpoints present in the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-configuration:id', ge=0, le=255, title='IdLeaf9'),
    ] = None
    """
    System generated ID for the checkpoint
    """
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:name',
            pattern='^(?=^[^0-9].*$).*$',
            title='NameLeaf28',
        ),
    ] = None
    """
    User provided name of the checkpoint
    """
    comment: Annotated[
        Optional[str],
        Field(alias='srl_nokia-configuration:comment', title='CommentLeaf'),
    ] = None
    """
    User provided annotations associated with the checkpoint
    """
    created: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:created',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='CreatedLeaf',
        ),
    ] = None
    """
    Date and time this checkpoint was created
    """
    version: Annotated[
        Optional[str],
        Field(alias='srl_nokia-configuration:version', title='VersionLeaf21'),
    ] = None
    """
    System version that the checkpoint was generated on
    """
    tag: Annotated[
        Optional[str], Field(alias='srl_nokia-configuration:tag', title='TagLeaf')
    ] = None
    """
    Full system version that the checkpoint was generated on
    """
    username: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='UsernameLeaf5',
        ),
    ] = None
    """
    Username that created this checkpoint
    """
    size: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-configuration:size',
            ge=0,
            le=18446744073709551615,
            title='SizeLeaf',
        ),
    ] = None
    """
    Size of the checkpoint configuration file
    """


class ClientListEntry(BaseModel):
    """
    List of active gRPC client sessions
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:id', ge=0, le=4294967295, title='IdLeaf2'),
    ] = None
    """
    System generated ID for for the client
    """
    type: Annotated[
        Optional[EnumerationEnum16],
        Field(alias='srl_nokia-grpc:type', title='TypeLeaf5'),
    ] = None
    user: Annotated[
        Optional[str], Field(alias='srl_nokia-grpc:user', title='UserLeaf')
    ] = None
    """
    Authenticated username for the client
    """
    user_agent: Annotated[
        Optional[str], Field(alias='srl_nokia-grpc:user-agent', title='User-agentLeaf')
    ] = None
    """
    User agent used for the client
    """
    remote_host: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-grpc:remote-host', title='Remote-hostLeaf2'),
    ] = None
    """
    Remote host of the client
    """
    remote_port: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:remote-port', ge=0, le=65535, title='Remote-portLeaf'
        ),
    ] = None
    """
    Remote port of the client
    """
    election_id: Annotated[
        Optional[str],
        Field(alias='srl_nokia-grpc:election-id', title='Election-idLeaf'),
    ] = None
    """
    Election ID of this client

    Provided only for services supporting an election ID
    """
    acctz_starting_point: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:acctz-starting-point',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Acctz-starting-pointLeaf',
        ),
    ] = None
    """
    Time of the acctz accounting subscription starting point
    """
    rpc: Annotated[
        Optional[str], Field(alias='srl_nokia-grpc:rpc', title='RpcLeaf')
    ] = None
    """
    The called package, service, and RPC

    For example gnmi.gNMI.Subscribe
    """
    start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Start-timeLeaf',
        ),
    ] = None
    """
    Time of the subscription creation
    """
    gnmi: Annotated[Optional[GnmiContainer2], Field(alias='srl_nokia-grpc:gnmi')] = None
    gribi: Annotated[Optional[GribiContainer], Field(alias='srl_nokia-grpc:gribi')] = (
        None
    )
    p4rt: Annotated[Optional[P4rtContainer], Field(alias='srl_nokia-grpc:p4rt')] = None


class ClockContainer(BaseModel):
    """
    Top-level container for system clock configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    timezone: Annotated[
        Optional[EnumerationEnum66],
        Field(alias='srl_nokia-ntp:timezone', title='TimezoneLeaf'),
    ] = None
    """
    The timezone to use for the system
    Based on IANAs Time Zone database
    """


class CountersContainer3(BaseModel):
    """
    A collection of per-schema path counters collected by the gNSI.pathz module.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    path: Annotated[
        Optional[List[PathListEntry]], Field(alias='srl_nokia-gnsi-pathz:path')
    ] = None


class CredentialzContainer(BaseModel):
    """
    Information relating to the active host keys and certificates as provided via Credentialz

    State is provided by the gNSI Credentialz service, and can be changed using the gNSI.Credentialz.RotateHostParameters RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trusted_user_ca_keys: Annotated[
        Optional[TrustedUserCaKeysContainer],
        Field(alias='srl_nokia-gnsi-credentialz:trusted-user-ca-keys'),
    ] = None
    host_certificate: Annotated[
        Optional[HostCertificateContainer],
        Field(alias='srl_nokia-gnsi-credentialz:host-certificate'),
    ] = None
    host_key: Annotated[
        Optional[HostKeyContainer2], Field(alias='srl_nokia-gnsi-credentialz:host-key')
    ] = None


class CredentialzContainer2(BaseModel):
    """
    Information relating to the active user credentials as provided via Credentialz

    State is provided by the gNSI Credentialz service, and can be changed using the gNSI.Credentialz.RotateAccountCredentials RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    password: Annotated[
        Optional[PasswordContainer], Field(alias='srl_nokia-aaa:password')
    ] = None
    authorized_keys: Annotated[
        Optional[AuthorizedKeysContainer], Field(alias='srl_nokia-aaa:authorized-keys')
    ] = None
    authorized_principals: Annotated[
        Optional[AuthorizedPrincipalsContainer],
        Field(alias='srl_nokia-aaa:authorized-principals'),
    ] = None


class CredentialzContainer3(BaseModel):
    """
    Information relating to the active user credentials as provided via Credentialz

    State is provided by the gNSI Credentialz service, and can be changed using the gNSI.Credentialz.RotateAccountCredentials RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    password: Annotated[
        Optional[PasswordContainer2], Field(alias='srl_nokia-aaa:password')
    ] = None
    authorized_keys: Annotated[
        Optional[AuthorizedKeysContainer2], Field(alias='srl_nokia-aaa:authorized-keys')
    ] = None
    authorized_principals: Annotated[
        Optional[AuthorizedPrincipalsContainer2],
        Field(alias='srl_nokia-aaa:authorized-principals'),
    ] = None


class CredentialzContainer4(BaseModel):
    """
    Information relating to the active user credentials as provided via Credentialz

    State is provided by the gNSI Credentialz service, and can be changed using the gNSI.Credentialz.RotateAccountCredentials RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    password: Annotated[
        Optional[PasswordContainer3], Field(alias='srl_nokia-aaa:password')
    ] = None
    authorized_keys: Annotated[
        Optional[AuthorizedKeysContainer3], Field(alias='srl_nokia-aaa:authorized-keys')
    ] = None
    authorized_principals: Annotated[
        Optional[AuthorizedPrincipalsContainer3],
        Field(alias='srl_nokia-aaa:authorized-principals'),
    ] = None


class DesignatedForwarderCandidateListEntry(BaseModel):
    """
    designated forwarder candidates for this evi
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:address',
            title='AddressLeaf2',
        ),
    ] = None
    """
    An IPv4 or IPv6 address with no prefix specified.
    """
    add_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:add-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Add-timeLeaf',
        ),
    ] = None
    """
    The date and time when the designated-forwarder-candidate was added to the designated forwarder candidate list for this evi
    """
    designated_forwarder: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder',
            title='Designated-forwarderLeaf',
        ),
    ] = False
    """
    Indicates if this designated-forwarder-candidate is the designated-forwarder.
    """


class DfElectionContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    timers: Annotated[
        Optional[TimersContainer2],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:timers'
        ),
    ] = None
    interface_standby_signaling_on_non_df: Annotated[
        Optional[InterfaceStandbySignalingOnNonDfContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:interface-standby-signaling-on-non-df'
        ),
    ] = None
    algorithm: Annotated[
        Optional[AlgorithmContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:algorithm'
        ),
    ] = None


class Dot1xContainer(BaseModel):
    """
    Enclosing container for system level dot1x
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer], Field(alias='srl_nokia-dot1x:statistics')
    ] = None


class EthernetSegmentRoutesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    route_distinguisher: Annotated[
        Optional[
            Union[
                RouteDistinguisherType0Type,
                RouteDistinguisherType1Type,
                RouteDistinguisherType2Type,
                RouteDistinguisherType2bType,
            ]
        ],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:route-distinguisher',
            title='Route-distinguisherLeaf2',
        ),
    ] = None
    """
    The route distinguisher encoded in the NLRI
    """
    esi: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:esi',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){9}$).*$',
            title='EsiLeaf3',
        ),
    ] = None
    """
    The Ethernet Segment Identifier
    """
    originating_router: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:originating-router',
            title='Originating-routerLeaf',
        ),
    ] = None
    """
    The IPv4 or IPv6 address of the originating router
    """
    neighbor: Annotated[
        Optional[Union[Ipv4AddressWithZoneType, Ipv6AddressWithZoneType]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:neighbor',
            title='NeighborLeaf2',
        ),
    ] = None
    """
    If the route was learned from a BGP neighbor, this is the IPv4 or IPv6 address of that neighbor
    """
    path_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:path-id',
            ge=0,
            le=4294967295,
            title='Path-idLeaf2',
        ),
    ] = None
    """
    Path identifier of the BGP route
    """
    attr_id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:attr-id',
            ge=0,
            le=18446744073709551615,
            title='Attr-idLeaf2',
        ),
    ] = None
    """
    Leaf reference to networkinstance/protocols/bgp/rib/attr-sets/attr-set/index
    """


class Fips140Container(BaseModel):
    """
    Boot up the router in fips-provider mode

    In fips-provider mode only fips approved algorithms are allowed.
    In addition for fip-provider mode to take effect a reboot is of the router is needed.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-boot:admin-state', title='Admin-stateLeaf17'),
    ] = 'disable'
    """
    This leaf contains the configured, desired state of the fips-provider.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-boot:oper-state', title='Oper-stateLeaf13'),
    ] = None
    """
    This leaf contains the operational state of fips-provider.
    """
    oper_down_reason: Annotated[
        Optional[EnumerationEnum51],
        Field(alias='srl_nokia-boot:oper-down-reason', title='Oper-down-reasonLeaf7'),
    ] = None
    """
    The reason for not enabling fips operational down
    """


class FreqClockContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ql_input_threshold: Annotated[
        Optional[EnumerationEnum68],
        Field(
            alias='srl_nokia-sync:ql-input-threshold', title='Ql-input-thresholdLeaf'
        ),
    ] = 'unused'
    """
    This command configures the minimum acceptable QL value
    Frequency references with lower QL will not be considered for selection
    by the system timing module.
    Options: unused, prs, stu, st2, tnc, st3e, st3, prc, ssua, ssub, sec, eec1, eec2
    """
    network_type: Annotated[
        Optional[EnumerationEnum72],
        Field(alias='srl_nokia-sync:network-type', title='Network-typeLeaf'),
    ] = 'sonet'
    """
    Configures SyncE for SSM code-type as SONET or SDH mode
    sdh specifies the values corresponding to ITU-T G.781 Option 1 compliant networks.
    sonet specifies the values corresponding to ITU-T G.781 Option 2 compliant networks.
    """
    ql_selection: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:ql-selection', title='Ql-selectionLeaf'),
    ] = False
    """
    Configures if frequency reference selection takes the QL (Quality Level) into account
    When enabled, the selection of system timing reference and BITS output timing reference
    takes into account quality level. Quality level is conveyed via the SSM or forced using
    the ql-override command..
    """
    wait_to_restore: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:wait-to-restore',
            ge=0,
            le=12,
            title='Wait-to-restoreLeaf',
        ),
    ] = 5
    """
    This command configures the time for the Wait to Restore timer
    A previously failed input reference must be valid for the time specified before it is
    used for the clock input reference.
    """
    revert: Annotated[
        Optional[bool], Field(alias='srl_nokia-sync:revert', title='RevertLeaf')
    ] = False
    """
    This command configures if the frequency clock is in revertive mode
    In revertive mode, when a failed reference becomes operational, the system will
    automatically switch to the recovered reference if it is of higher priority and/or QL.
    When the mode is non-revertive, a failed clock source is not automatically selected.
    """
    active_reference: Annotated[
        Optional[EnumerationEnum73],
        Field(alias='srl_nokia-sync:active-reference', title='Active-referenceLeaf'),
    ] = None
    """
    Indicates the current selected reference

    This will be an instance-number; or internal for the case of holdover or freerun.
    """
    freq_offset: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:freq-offset',
            ge=-9223372036854776.0,
            le=9223372036854776.0,
            title='Freq-offsetLeaf',
        ),
    ] = None
    """
    The frequency offset between the central frequency clock and the selected reference in ppb
    """
    freq_clock_state: Annotated[
        Optional[EnumerationEnum74],
        Field(alias='srl_nokia-sync:freq-clock-state', title='Freq-clock-stateLeaf'),
    ] = None
    """
    Shows the frequency clock mode state
    """
    system_ql_value: Annotated[
        Optional[EnumerationEnum69],
        Field(alias='srl_nokia-sync:system-ql-value', title='System-ql-valueLeaf'),
    ] = None
    """
    System QL value based on the reference selected
    """


class FreqRecoveryEngineContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    recovery_state: Annotated[
        Optional[EnumerationEnum78],
        Field(alias='srl_nokia-sync:recovery-state', title='Recovery-stateLeaf2'),
    ] = None
    """
    Specifies the current state of the time recovery engine in the PTP clock
    """
    state_last_changed: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:state-last-changed',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='State-last-changedLeaf2',
        ),
    ] = None
    """
    Specifies the last occurrence of a ptp state change for the time recovery engine
    """
    frequency_offset: Annotated[
        Optional[float],
        Field(
            alias='srl_nokia-sync:frequency-offset',
            ge=-9223372036854776.0,
            le=9223372036854776.0,
            title='Frequency-offsetLeaf',
        ),
    ] = None
    """
    The frequency offset of the recovered PTP clock

     Positive values indicate that the recovered clock is faster than nominal,
     negative values indicate that the recovered clock is slower than nominal.
    """
    last_adjustment_timestamp: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:last-adjustment-timestamp',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-adjustment-timestampLeaf2',
        ),
    ] = None
    """
    The time when last-adjustment was last calculated
    """
    statistics: Annotated[
        Optional[StatisticsContainer20], Field(alias='srl_nokia-sync:statistics')
    ] = None


class GnssContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    constellation: Annotated[
        Optional[ConstellationContainer], Field(alias='srl_nokia-sync:constellation')
    ] = None
    receiver: Annotated[
        Optional[List[ReceiverListEntry]], Field(alias='srl_nokia-sync:receiver')
    ] = None


class HostEntryListEntry(BaseModel):
    """
    List of static host entries
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dns:name',
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$',
            title='NameLeaf14',
        ),
    ] = None
    """
    Name of host entry
    """
    ipv4_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dns:ipv4-address',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$).*$',
            title='Ipv4-addressLeaf',
        ),
    ] = None
    """
    IPv4 address for the host entry
    """
    ipv6_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dns:ipv6-address',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))$).*$',
            title='Ipv6-addressLeaf',
        ),
    ] = None
    """
    IPv6 address for the host entry
    """


class HostListEntry(BaseModel):
    """
    host name for static ip allocations
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mac: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:mac',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
            title='MacLeaf',
        ),
    ] = None
    """
    The mac-address type represents an IEEE 802 MAC address.
    The canonical representation uses lowercase characters.

    In the value set and its semantics, this type is equivalent
    to the MacAddress textual convention of the SMIv2.
    """
    ip_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:ip-address',
            pattern='^(?=^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))$).*$',
            title='Ip-addressLeaf',
        ),
    ] = None
    """
    An IPv4 prefix with host bits.
    """
    options: Annotated[
        Optional[OptionsContainer3], Field(alias='srl_nokia-dhcp-server:options')
    ] = None


class HostListEntry2(BaseModel):
    """
    host name for static ip allocations
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mac: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:mac',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
            title='MacLeaf2',
        ),
    ] = None
    """
    The mac-address type represents an IEEE 802 MAC address.
    The canonical representation uses lowercase characters.

    In the value set and its semantics, this type is equivalent
    to the MacAddress textual convention of the SMIv2.
    """
    ip_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:ip-address',
            pattern='^(?=^((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))$).*$',
            title='Ip-addressLeaf2',
        ),
    ] = None
    """
    An IPv6 prefix with host bits.
    """
    options: Annotated[
        Optional[OptionsContainer5], Field(alias='srl_nokia-dhcp-server:options')
    ] = None


class HttpContainer(BaseModel):
    """
    Top-level container for the JSON RPC HTTP server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-json-rpc:admin-state', title='Admin-stateLeaf23'),
    ] = 'disable'
    """
    Administratively enable or disable the HTTP JSON RPC server
    This requires the JSON RPC server to be globally enabled
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-json-rpc:oper-state', title='Oper-stateLeaf17'),
    ] = None
    """
    Details if the JSON RPC server is operationally available
    """
    source_address: Annotated[
        Optional[List[Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(alias='srl_nokia-json-rpc:source-address'),
    ] = ['::']
    """
    List of IP addresses the JSON RPC server will listen on within the network instance
    """
    use_authentication: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-json-rpc:use-authentication',
            title='Use-authenticationLeaf',
        ),
    ] = True
    """
    Enable or disable the use of username/password authentication for every JSON RPC request
    """
    session_limit: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-json-rpc:session-limit',
            ge=1,
            le=100,
            title='Session-limitLeaf3',
        ),
    ] = None
    """
    The number of concurrent requests the server will allow
    If a request comes in while this limit is reached, the request will block until another request is finished.
    """
    port: Annotated[
        Optional[int],
        Field(alias='srl_nokia-json-rpc:port', ge=0, le=65535, title='PortLeaf4'),
    ] = 80
    """
    The port the HTTP JSON RPC server will listen on for incoming connections
    """


class HttpsContainer(BaseModel):
    """
    Top-level container for the JSON-RPC HTTPS server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-json-rpc:admin-state', title='Admin-stateLeaf24'),
    ] = 'disable'
    """
    Administratively enable or disable the HTTPS JSON RPC server
    This requires the JSON RPC server to be globally enabled
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-json-rpc:oper-state', title='Oper-stateLeaf18'),
    ] = None
    """
    Details if the JSON RPC server is operationally available
    """
    source_address: Annotated[
        Optional[List[Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(alias='srl_nokia-json-rpc:source-address'),
    ] = ['::']
    """
    List of IP addresses the JSON RPC server will listen on within the network instance
    """
    use_authentication: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-json-rpc:use-authentication',
            title='Use-authenticationLeaf2',
        ),
    ] = True
    """
    Enable or disable the use of username/password authentication for every JSON RPC request
    """
    session_limit: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-json-rpc:session-limit',
            ge=1,
            le=100,
            title='Session-limitLeaf4',
        ),
    ] = None
    """
    The number of concurrent requests the server will allow
    If a request comes in while this limit is reached, the request will block until another request is finished.
    """
    port: Annotated[
        Optional[int],
        Field(alias='srl_nokia-json-rpc:port', ge=0, le=65535, title='PortLeaf5'),
    ] = 443
    """
    Port the HTTPS JSON RPC server will listen on for incoming connections
    """
    tls_profile: Annotated[
        str,
        Field(
            alias='srl_nokia-json-rpc:tls-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Tls-profileLeaf2',
        ),
    ]
    """
    Reference to the TLS profile to use on the HTTP JSON RPC server
    """


class InputContainer(BaseModel):
    """
    Defines parameters determining the handling of system generated traffic.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    acl: Annotated[Optional[AclContainer], Field(alias='srl_nokia-acl:acl')] = None


class InstanceListEntry(BaseModel):
    """
    List of all event handler instances

    An event handler instance consists of a set of paths to be monitored for changes, and a Python script to execute if changes occur.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf24',
        ),
    ] = None
    """
    A user-defined name for this event handler instance
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-event-handler:admin-state', title='Admin-stateLeaf12'),
    ] = 'disable'
    """
    Administratively enable or disable this event handler instance
    """
    paths: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-event-handler:paths',
            pattern='^(?=^[A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?\\-{}*\\\\\\\\"\\[\\]]+$).*$',
        ),
    ] = []
    """
    List of valid YANG paths in CLI notation to monitor for changes

    If any events are received on any of the provided paths, the configured script will be executed.

    This path may include keys, wildcards, ranges, and other management server supported constructs.

    E.g.
        "interface * oper-state"
        "acl ipv4-filter foo* description"
    """
    options: Annotated[
        Optional[OptionsContainer], Field(alias='srl_nokia-event-handler:options')
    ] = None
    upython_script: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:upython-script',
            pattern='^(?=^([^./][^/]*)|(\\.[^\\./]+)|(\\.\\.[^/])+$).*$',
            title='Upython-scriptLeaf',
        ),
    ] = None
    """
    File name of a MicroPython script, including .py suffix

    This script should exist in /etc/opt/srlinux/eventmgr or /opt/srlinux/eventmgr already.
    Explicit paths outside of these two directories are not permitted.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-event-handler:oper-state', title='Oper-stateLeaf11'),
    ] = None
    """
    Details if this event handler instance is operationally available
    """
    last_execution: Annotated[
        Optional[LastExecutionContainer],
        Field(alias='srl_nokia-event-handler:last-execution'),
    ] = None
    last_errored_execution: Annotated[
        Optional[LastErroredExecutionContainer],
        Field(alias='srl_nokia-event-handler:last-errored-execution'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer10],
        Field(alias='srl_nokia-event-handler:statistics'),
    ] = None


class InterfaceCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:interface', title='InterfaceLeaf2')
    ] = None
    """
    The name of the interface

    Valid options are:
    irb<N>, N=0..255
    lif-<lif_name>
    enp<bus>s<dev>f<fn>, bus=0..255, dev=0..31, fn=0..7
    vhn-<vhn_name>
    lag<N>, N=1..1000 [note1]
    lo<N>, N=0..255
    mgmt0
    mgmt0-standby
    ethernet-<slot>/<port>
    ethernet-<slot>/<mda>/<port>
    system0
    sync0

    <lif_name>=Linux interface name
    <vhn_name>=vhost interface name
    <slot>=slot number {1,2,3,..}
    <mda>=mda id {a,b,c,d,e,f}
    <port>=port id {1,2,3,..}

    [note1] The maximum number of LAGs per platform is as follows:
     D1: 32 (N must be 1..32)
     D2-D3: 128 (N must be 1..1000)
     D4-D5: 64 (N must be 1..64)
     H2-H3: 127 (N must be 1..127)
     H4: 255 (N must be 1..255)
     IXR: 128 (N must be 1..128)
     SXR-1d-32D: 128 (N must be 1..128)
     SXR-1x-44S: 128 (N must be 1..128)
     A1: 10 (N must be 1..10)
     IXR-X1b: 512 (N must be 1..512)
     IXR-X3b: 512 (N must be 1..512)
    """


class InterfaceCase2(BaseModel):
    """
    Local interface used for ptp over ethernet communication
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[str], Field(alias='srl_nokia-sync:interface', title='InterfaceLeaf3')
    ] = None
    """
    The name of the interface

    Valid options are:
    irb<N>, N=0..255
    lif-<lif_name>
    enp<bus>s<dev>f<fn>, bus=0..255, dev=0..31, fn=0..7
    vhn-<vhn_name>
    lag<N>, N=1..1000 [note1]
    lo<N>, N=0..255
    mgmt0
    mgmt0-standby
    ethernet-<slot>/<port>
    ethernet-<slot>/<mda>/<port>
    system0
    sync0

    <lif_name>=Linux interface name
    <vhn_name>=vhost interface name
    <slot>=slot number {1,2,3,..}
    <mda>=mda id {a,b,c,d,e,f}
    <port>=port id {1,2,3,..}

    [note1] The maximum number of LAGs per platform is as follows:
     D1: 32 (N must be 1..32)
     D2-D3: 128 (N must be 1..1000)
     D4-D5: 64 (N must be 1..64)
     H2-H3: 127 (N must be 1..127)
     H4: 255 (N must be 1..255)
     IXR: 128 (N must be 1..128)
     SXR-1d-32D: 128 (N must be 1..128)
     SXR-1x-44S: 128 (N must be 1..128)
     A1: 10 (N must be 1..10)
     IXR-X1b: 512 (N must be 1..512)
     IXR-X3b: 512 (N must be 1..512)
    """


class IpContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='Network-instanceLeaf3',
        ),
    ] = None
    """
    Network instance containing the IP address
    """
    ip_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-sync:ip-address', title='Ip-addressLeaf3'),
    ] = None
    """
    IP address for the PTP peer
    """


class KeyListEntry(BaseModel):
    """
    List of keys in the keychain
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    index: Annotated[
        Optional[int],
        Field(alias='srl_nokia-keychains:index', ge=0, le=255, title='IndexLeaf4'),
    ] = None
    """
    Each key in a keychain requires a unique identifier, the index value specifies this identifier
    """
    algorithm: Annotated[
        Optional[EnumerationEnum23],
        Field(alias='srl_nokia-keychains:algorithm', title='AlgorithmLeaf'),
    ] = None
    """
    The cryptographic algorithm used with the keying material to secure the messages
    """
    authentication_key: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-keychains:authentication-key',
            title='Authentication-keyLeaf',
        ),
    ] = None
    """
    The secret key to use for authentication
    """
    macsec: Annotated[
        Optional[MacsecContainer], Field(alias='srl_nokia-keychains:macsec')
    ] = None
    send_lifetime: Annotated[
        Optional[SendLifetimeContainer],
        Field(alias='srl_nokia-keychains:send-lifetime'),
    ] = None
    receive_lifetime: Annotated[
        Optional[ReceiveLifetimeContainer],
        Field(alias='srl_nokia-keychains:receive-lifetime'),
    ] = None


class KeychainListEntry(BaseModel):
    """
    List of system keychains
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-keychains:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf13',
        ),
    ] = None
    """
    The user configured name for the keychain
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-keychains:admin-state', title='Admin-stateLeaf5'),
    ] = 'disable'
    """
    When set to disable, the keychain is inactive

    When a protocol refers to a keychain that is inactive, no authentication data is added to the outbound messages and/or all inbound messages with authentication data are dropped, depending on the context.

    A keychain is operationally disabled in a particular direction (send/receive) if:
    - the keychain is administratively disabled
    - no keys are configured
    - all of the keys are administratively disabled
    - all of the  keys are inactive because their start-times are in the future
    - all of the keys are inactive because their end-times (plus tolerance) are in the past (applies only to receive direction)
    """
    description: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-keychains:description',
            max_length=255,
            min_length=1,
            title='DescriptionLeaf',
        ),
    ] = None
    """
    The user configured description for the keychain
    """
    tolerance: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-keychains:tolerance',
            ge=0,
            le=4294967295,
            title='ToleranceLeaf',
        ),
    ] = 0
    """
    Tolerance for receive keys

    If tolerance is Z then all receive keys remain valid up to the configured/applicable end-time plus an additional Z seconds.
    """
    type: Annotated[
        Optional[EnumerationEnum21],
        Field(alias='srl_nokia-keychains:type', title='TypeLeaf6'),
    ] = None
    """
    Specifies the intended use of the keychain

    The type constrains the set of crypto algorithms that are available to use with each key in the keychain. It is also used to ensure that this keychain is only used by protocols for which it is intended.
    """
    usable: Annotated[
        Optional[bool], Field(alias='srl_nokia-keychains:usable', title='UsableLeaf')
    ] = None
    """
    The value of this object indicates if the keychain is usable for authentication
    """
    expired: Annotated[
        Optional[bool], Field(alias='srl_nokia-keychains:expired', title='ExpiredLeaf')
    ] = None
    """
    The value of this object indicates whether the keychain is expired

    Expired can mean past end-time or prior to start-time.
    """
    active_key_for_send: Annotated[
        Optional[Union[EnumerationEnum22, IndexLeaf3]],
        Field(
            alias='srl_nokia-keychains:active-key-for-send',
            title='Active-key-for-sendLeaf',
        ),
    ] = None
    """
    Provides the key index of the currently active Keychain key
    """
    key: Annotated[
        Optional[List[KeyListEntry]], Field(alias='srl_nokia-keychains:key')
    ] = None


class L2cpStatisticsContainer(BaseModel):
    """
    Container for Layer-2 Control Plane protocol statistics.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    total_in_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:total-in-packets',
            ge=0,
            le=18446744073709551615,
            title='Total-in-packetsLeaf2',
        ),
    ] = 0
    """
    System level total incoming L2CP frames.

    Cumulative of all Ethernet interfaces including the tunneled, discarded and copy-to-cpu
    L2CP frames. L2CP frames are identified by a destination MAC value of 01:80:c2:00:00:0X
    or 01:80:c2:00:00:2X, being X any value in the 0..F range.
    """
    total_in_discarded_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:total-in-discarded-packets',
            ge=0,
            le=18446744073709551615,
            title='Total-in-discarded-packetsLeaf2',
        ),
    ] = 0
    """
    System level incoming L2CP discarded frames.

    Cumulative of all Ethernet interfaces including all the discarded L2CP frames. L2CP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0X or
    01:80:c2:00:00:2X, being X any value in the 0..F range.
    """
    total_in_tunneled_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:total-in-tunneled-packets',
            ge=0,
            le=18446744073709551615,
            title='Total-in-tunneled-packetsLeaf',
        ),
    ] = 0
    """
    System level incoming L2CP tunneled frames.

    Cumulative of all Ethernet interfaces including all the tunneled L2CP frames. L2CP
    frames are identified by a destination MAC value of 01:80:c2:00:00:0X or
    01:80:c2:00:00:2X, being X any value in the 0..F range.
    """
    total_in_trap_to_cpu_packets: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-interfaces-l2cp:total-in-trap-to-cpu-packets',
            ge=0,
            le=18446744073709551615,
            title='Total-in-trap-to-cpu-packetsLeaf',
        ),
    ] = 0
    """
    System level incoming L2CP copy-to-cpu frames.

    Cumulative of all Ethernet interfaces including all the L2CP frames that are copied
    to CPU. L2CP frames are identified by a destination MAC value of 01:80:c2:00:00:0X or
    01:80:c2:00:00:2X, being X any value in the 0..F range.
    """
    last_clear: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-interfaces-l2cp:last-clear',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-clearLeaf4',
        ),
    ] = None
    """
    Timestamp of the last time the L2CP counters were cleared.
    """
    lldp: Annotated[
        Optional[LldpContainer2], Field(alias='srl_nokia-interfaces-l2cp:lldp')
    ] = None
    lacp: Annotated[
        Optional[LacpContainer2], Field(alias='srl_nokia-interfaces-l2cp:lacp')
    ] = None
    xstp: Annotated[
        Optional[XstpContainer], Field(alias='srl_nokia-interfaces-l2cp:xstp')
    ] = None
    dot1x: Annotated[
        Optional[Dot1xContainer2], Field(alias='srl_nokia-interfaces-l2cp:dot1x')
    ] = None
    ptp: Annotated[
        Optional[PtpContainer3], Field(alias='srl_nokia-interfaces-l2cp:ptp')
    ] = None
    esmc: Annotated[
        Optional[EsmcContainer], Field(alias='srl_nokia-interfaces-l2cp:esmc')
    ] = None
    elmi: Annotated[
        Optional[ElmiContainer], Field(alias='srl_nokia-interfaces-l2cp:elmi')
    ] = None
    efm_oam: Annotated[
        Optional[EfmOamContainer], Field(alias='srl_nokia-interfaces-l2cp:efm-oam')
    ] = None


class L2cpTransparencyContainer(BaseModel):
    """
    Enclosing container for system level Layer-2 Control Protocol transparency.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    l2cp_statistics: Annotated[
        Optional[L2cpStatisticsContainer],
        Field(alias='srl_nokia-interfaces-l2cp:l2cp-statistics'),
    ] = None


class LabelRangesContainer(BaseModel):
    """
    Container for managing MPLS label blocks
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    static: Annotated[
        Optional[List[StaticListEntry]],
        Field(alias='srl_nokia-mpls-label-management:static'),
    ] = None
    dynamic: Annotated[
        Optional[List[DynamicListEntry]],
        Field(alias='srl_nokia-mpls-label-management:dynamic'),
    ] = None


class Layer3NextHopCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    next_hop: Annotated[
        Optional[List[NextHopListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:next-hop'
        ),
    ] = None


class LinuxadminUserContainer(BaseModel):
    """
    Enclosing container for linuxadmin user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    username: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:username', title='UsernameLeaf2')
    ] = 'linuxadmin'
    """
    Assigned username for linuxadmin user
    """
    password: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:password', title='PasswordLeaf2')
    ] = '$y$j9T$l/vKPXdvWQKKPH8qPzbLs0$Hz98mmTg.j87QMZlTqY2ieGWa3Ed7kzHkp5z6kROEy4'
    """
    The linuxadmin password, supplied either as cleartext or as a hashed value

    If provided as cleartext, the system will hash the value on input, storing only the hashed value.
    If provided as a hashed value, the value should include any '$' characters, for example '$6$c66a15569d3f5952$kA2WPt9iqR5uMbaCUBNxsjKyXROQFdJtV1HX0CFY9wk7F326/yB3h.dERX9cH7YpeJ1N872hjzTb2tlaZFwwg0'.
    """
    ssh_principals: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-principals')
    ] = []
    """
    List of principals to associate with this user

    If any of the principals in the list are matched in a SSH client's certificate, and that clients username matches this user, and the certificate is verified, the client will authenticate.
    """
    ssh_key: Annotated[Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-key')] = []
    """
    SSH public key(s) for the user

    If defined, the user may login to the system over SSH with this key. This should use the SSH public authorized key format.
    """
    credentialz: Annotated[
        Optional[CredentialzContainer3], Field(alias='srl_nokia-aaa:credentialz')
    ] = None


class MembersContainer(BaseModel):
    """
    Container for specifying the members of the maintenance group - i.e. the components that will eventually be taken out of service for repair or replacement.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    bgp: Annotated[
        Optional[BgpContainer2], Field(alias='srl_nokia-maintenance-mode:bgp')
    ] = None
    isis: Annotated[
        Optional[IsisContainer], Field(alias='srl_nokia-maintenance-mode:isis')
    ] = None


class MirrorSourceContainer(BaseModel):
    """
    Configure mirror source(s)
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface: Annotated[
        Optional[List[InterfaceListEntry]], Field(alias='srl_nokia-mirroring:interface')
    ] = None
    subinterface: Annotated[
        Optional[List[SubinterfaceListEntry]],
        Field(alias='srl_nokia-mirroring:subinterface'),
    ] = None
    acl: Annotated[Optional[AclContainer2], Field(alias='srl_nokia-mirroring:acl')] = (
        None
    )


class MplsMulticastTepContainer(BaseModel):
    """
    System bridge-table BGP-EVPN MPLS multicast Termination Endpoint information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer6],
        Field(alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:statistics'),
    ] = None
    tep: Annotated[
        Optional[List[TepListEntry]],
        Field(alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:tep'),
    ] = None


class MplsContainer(BaseModel):
    """
    Container for system wide MPLS label management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    label_ranges: Annotated[
        Optional[LabelRangesContainer],
        Field(alias='srl_nokia-mpls-label-management:label-ranges'),
    ] = None
    services: Annotated[
        Optional[ServicesContainer],
        Field(alias='srl_nokia-mpls-label-management:services'),
    ] = None


class MulticastIdsContainer(BaseModel):
    """
    system multicast id information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer16],
        Field(alias='srl_nokia-system-multicast:statistics'),
    ] = None


class MulticastRouteListEntry(BaseModel):
    """
    List of all the MFIB entries in the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-multicast-mfib-table:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='Network-instanceLeaf2',
        ),
    ] = None
    """
    Indicates that the MFIB entry is associated to this network instance
    """
    source: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-system-multicast-mfib-table:source', title='SourceLeaf'),
    ] = None
    """
    Source IP address of the MFIB entry
    """
    group: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-system-multicast-mfib-table:group', title='GroupLeaf'),
    ] = None
    """
    Multicast group address of the MFIB entry
    """
    line_card_replication_index: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-multicast-mfib-table:line-card-replication-index',
            ge=0,
            le=18446744073709551615,
            title='Line-card-replication-indexLeaf',
        ),
    ] = 0
    """
    Line card Replication Index (LRID) allocated by mfib_mgr

    Upon programming an MFIB entry, mfib_mgr requests a Multicast Identifier (MCID) to mcid_mgr
    and based on the response with an allocated MCID, mfib_mgr allocates a LRID for the entry.
    A value 0 indicates that no MCID was received for the entry, and therefore the MFIB entry
    cannot forward multicast traffic.
    """
    last_update: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-multicast-mfib-table:last-update',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-updateLeaf2',
        ),
    ] = None
    """
    Last update of this MFIB entry
    """


class MulticastContainer2(BaseModel):
    """
    system multicast information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    multicast_ids: Annotated[
        Optional[MulticastIdsContainer],
        Field(alias='srl_nokia-system-multicast:multicast-ids'),
    ] = None


class NeighborListEntry(BaseModel):
    """
    List of LLDP neighbors on this interface
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[Optional[str], Field(alias='srl_nokia-lldp:id', title='IdLeaf8')] = (
        None
    )
    """
    System generated identifier for the remote neighbor
    """
    first_message: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:first-message',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='First-messageLeaf',
        ),
    ] = None
    """
    Date and time of the first message from neighbor
    """
    last_update: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:last-update',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-updateLeaf',
        ),
    ] = None
    """
    Date and time of the last update from neighbor
    """
    system_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:system-name',
            max_length=255,
            min_length=0,
            title='System-nameLeaf2',
        ),
    ] = None
    """
    The administratively assigned name of the remote neighbor

    The system name field shall contain an alpha-numeric string
    that indicates the system's administratively assigned name.
    The system name should be the system's fully qualified domain
    name. If implementations support IETF RFC 3418, the sysName
    object should be used for this field.
    """
    system_description: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:system-description',
            max_length=255,
            min_length=0,
            title='System-descriptionLeaf2',
        ),
    ] = None
    """
    The system description of the remote neighbor

    The system description field shall contain an alpha-numeric
    string that is the textual description of the network entity.
    The system description should include the full name and
    version identification of the system's hardware type,
    software operating system, and networking software. If
    implementations support IETF RFC 3418, the sysDescr object
    should be used for this field.
    """
    chassis_id: Annotated[
        Optional[str], Field(alias='srl_nokia-lldp:chassis-id', title='Chassis-idLeaf2')
    ] = None
    """
    The chassis ID of the remote neighbor

    The Chassis ID is a mandatory TLV which identifies the
    chassis component of the endpoint identifier associated with
    the transmitting LLDP agent
    """
    chassis_id_type: Annotated[
        Optional[EnumerationEnum48],
        Field(alias='srl_nokia-lldp:chassis-id-type', title='Chassis-id-typeLeaf2'),
    ] = 'MAC_ADDRESS'
    """
    The type of identifier used in the chassis-id field

    This field identifies the format and source of the chassis
    identifier string. It is an enumerator defined by the
    LldpChassisIdSubtype object from IEEE 802.1AB MIB.
    """
    port_id: Annotated[
        Optional[Union[str, StringOrBinaryType1]],
        Field(alias='srl_nokia-lldp:port-id', title='Port-idLeaf'),
    ] = None
    """
    The Port ID of the remote neighbor

    The Port ID is a mandatory TLV which identifies the port
    component of the endpoint identifier associated with the
    transmitting LLDP agent. If the specified port is an IEEE
    802.3 Repeater port, then this TLV is optional.
    """
    port_id_type: Annotated[
        Optional[EnumerationEnum50],
        Field(alias='srl_nokia-lldp:port-id-type', title='Port-id-typeLeaf'),
    ] = None
    """
    The type of identifier used in the port-id field

    This field identifies the format and source of the port
    identifier string. It is an enumerator defined by the
    PtopoPortIdType object from RFC2922.
    """
    port_description: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lldp:port-description', title='Port-descriptionLeaf'),
    ] = None
    """
    The description of the port referenced in the port-id field

    The binary string containing the actual port identifier for
    the port which this LLDP PDU was transmitted. The source and
    format of this field is defined by PtopoPortId from
    RFC2922.
    """
    management_address: Annotated[
        Optional[List[ManagementAddressListEntry2]],
        Field(alias='srl_nokia-lldp:management-address'),
    ] = None
    bgp_auto_discovery: Annotated[
        Optional[BgpAutoDiscoveryContainer3],
        Field(alias='srl_nokia-lldp:bgp-auto-discovery'),
    ] = None
    custom_tlv: Annotated[
        Optional[List[CustomTlvListEntry]], Field(alias='srl_nokia-lldp:custom-tlv')
    ] = None
    capability: Annotated[
        Optional[List[CapabilityListEntry]], Field(alias='srl_nokia-lldp:capability')
    ] = None


class NetconfServerListEntry(BaseModel):
    """
    Configures the NETCONF server instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-netconf-server:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='NameLeaf23',
        ),
    ] = None
    """
    NETCONF service instance name
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-netconf-server:admin-state', title='Admin-stateLeaf11'),
    ] = 'disable'
    """
    Administratively enable or disable the NETCONF server instance
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-netconf-server:oper-state', title='Oper-stateLeaf10'),
    ] = None
    """
    Details if the NETCONF server instance is operationally available
    """
    last_oper_change: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-netconf-server:last-oper-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-oper-changeLeaf',
        ),
    ] = None
    """
    NETCONF last operational state change

     Time of last change of operational state of NETCONF server instance
    """
    trace_options: Annotated[
        Optional[TraceOptionsContainer],
        Field(alias='srl_nokia-netconf-server:trace-options'),
    ] = None
    transport: Annotated[
        Optional[Union[SshCase, TlsCase, UnixSocketCase]],
        Field(alias='srl_nokia-netconf-server:transport'),
    ] = None
    session_limit: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-netconf-server:session-limit',
            ge=1,
            le=64,
            title='Session-limitLeaf2',
        ),
    ] = 64
    """
    Set a limit on the number of simultaneous active NETCONF sessions

     A session is defined as an individual client connection over which a NETCONF session has been started
     by providing bi-directional <hello> messages
    """
    statistics: Annotated[
        Optional[StatisticsContainer9],
        Field(alias='srl_nokia-netconf-server:statistics'),
    ] = None


class NetworkInstanceListEntry3(BaseModel):
    """
    List of network instances to run the JSON RPC server in
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-json-rpc:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='NameLeaf38',
        ),
    ] = None
    """
    Reference to a configured network-instance
    """
    http: Annotated[Optional[HttpContainer], Field(alias='srl_nokia-json-rpc:http')] = (
        None
    )
    https: Annotated[
        Optional[HttpsContainer], Field(alias='srl_nokia-json-rpc:https')
    ] = None


class NtpCase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ntp: Annotated[
        Optional[NtpContainer], Field(alias='srl_nokia-packet-link-qual:ntp')
    ] = None


class OpenconfigContainer(BaseModel):
    """
    Top-level container for options relating to OpenConfig
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-openconfig:admin-state', title='Admin-stateLeaf'),
    ] = None
    """
    Enable or disable the OpenConfig management server

    This will disable OpenConfig throughout the system, and bring any gRPC servers that use it operationally down.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-openconfig:oper-state', title='Oper-stateLeaf'),
    ] = None
    """
    Indicates the operational state of the OpenConfig management server
    """


class PathzContainer(BaseModel):
    """
    Information relating to the active Pathz authorization policy instances

    This policies is provided by the gNSI gRPC service, and can be changed using the gNSI.Pathz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    version: Annotated[
        Optional[str],
        Field(alias='srl_nokia-gnsi-pathz:version', title='VersionLeaf20'),
    ] = None
    """
    The version of the Pathz authorization policy (sent by the gNSI client).
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-gnsi-pathz:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf20',
        ),
    ] = None
    """
    The timestamp of the moment when the Pathz policy was created (sent by the gNSI client).
    """
    policy: Annotated[
        Optional[str], Field(alias='srl_nokia-gnsi-pathz:policy', title='PolicyLeaf2')
    ] = None
    """
    The policy definition

    This JSON string contains the full gRPC authorization policy conforming to the gRPC Path-based authorization
    policy schema.

    This maps to the policy field within a UploadRequest message in the Pathz protobuf.
    """
    counters: Annotated[
        Optional[CountersContainer3], Field(alias='srl_nokia-gnsi-pathz:counters')
    ] = None


class PeerContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='Network-instanceLeaf4',
        ),
    ] = None
    """
    Network instance used by this peer

    All configured peers use the same network-instance.   It can be configured at the top level of the ptp tree.
    """
    ip_address: Annotated[
        Union[Ipv4AddressType, Ipv6AddressType],
        Field(alias='srl_nokia-sync:ip-address', title='Ip-addressLeaf4'),
    ]
    """
    IP address for the PTP peer

    Only Unicast addresses are supported
    """


class PeerContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='Network-instanceLeaf5',
        ),
    ] = None
    """
    Network instance that owns the PTP peer
    """
    ip_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-sync:ip-address', title='Ip-addressLeaf5'),
    ] = None
    """
    IP address for the PTP peer

    Only Unicast addresses are supported
    """


class PolicyListEntry(BaseModel):
    """
    Information about freshness of an schema-path-based Pathz authorization policy that have been installed
    on the device using the gNSI schema-path-based Pathz authorization policy management service.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance: Annotated[
        Optional[EnumerationEnum55],
        Field(alias='srl_nokia-configuration:instance', title='InstanceLeaf2'),
    ] = None
    version: Annotated[
        Optional[str],
        Field(alias='srl_nokia-configuration:version', title='VersionLeaf22'),
    ] = None
    """
    The version of the Pathz authorization policy (sent by the gNSI client).
    """
    created_on: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:created-on',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Created-onLeaf21',
        ),
    ] = None
    """
    The timestamp of the moment when the Pathz policy was created (sent by the gNSI client).
    """
    policy: Annotated[
        Optional[str],
        Field(alias='srl_nokia-configuration:policy', title='PolicyLeaf3'),
    ] = None
    """
    The policy definition

    This JSON string contains the full gRPC authorization policy conforming to the gRPC Path-based authorization
    policy schema.

    This maps to the policy field within a UploadRequest message in the Pathz protobuf.
    """


class PortDsCfgIpListListEntry(BaseModel):
    """
    List of port data sets for configured IP peers
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port_index: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:port-index', ge=1, le=999, title='Port-indexLeaf2'),
    ] = None
    """
    Index into the port-ds list

    This is not the PTP port number.
    Configurable ports use port indices 1 through 999 but there is a limit on the overall number of these configured ports based on the platform and software release.

    The data sets (i.e., information model) of IEEE Std
    1588-2008 specify a member portDS.portIdentity, which
    uses a typed struct with members clockIdentity and
    portNumber.

    In this YANG data model, portIdentity is not modeled
    in the port-ds.  However, its members are provided
    as follows:
    portIdentity.portNumber is provided as this
    ptp-port-number leaf in port-ds, and
    portIdentity.clockIdentity is provided as the
    clock-identity leaf in default-ds of the instance
    (i.e., ../../default-ds/clock-identity).
    """
    ptp_port_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ptp-port-number',
            ge=0,
            le=65535,
            title='Ptp-port-numberLeaf2',
        ),
    ] = None
    """
    IEEE Std 1588 portNumber

    This is the port-number that will appear in messages sent for this port-index.
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-sync:admin-state', title='Admin-stateLeaf31'),
    ] = 'disable'
    """
    The administrative state of the ptp port
    """
    port_state: Annotated[
        Optional[EnumerationEnum80],
        Field(alias='srl_nokia-sync:port-state', title='Port-stateLeaf2'),
    ] = None
    """
    Current state associated with the port
    """
    peer: Annotated[Optional[PeerContainer], Field(alias='srl_nokia-sync:peer')] = None
    best_master: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:best-master', title='Best-masterLeaf2'),
    ] = None
    """
    Indicates if this peer was selected by the BMCA to be the best master
    """
    parent_clock: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:parent-clock', title='Parent-clockLeaf3'),
    ] = None
    """
    Indicates if this peer is the current parent clock of this PTP clock

    May differ from best-master due to use of local GNSS as time source.
    """
    log_min_delay_req_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-min-delay-req-interval',
            ge=-6,
            le=0,
            title='Log-min-delay-req-intervalLeaf2',
        ),
    ] = None
    """
    The base-2 logarithm of the minDelayReqInterval

    The minimum permitted mean time interval between successive Delay_Req messages.
    The value is not configurable.  The delay messages use the same interval as for Sync messages (log-sync-interval)
    """
    log_announce_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-announce-interval',
            ge=-3,
            le=4,
            title='Log-announce-intervalLeaf3',
        ),
    ] = None
    """
    The base-2 logarithm of the mean announceInterval

    Mean time interval between successive Announce messages. To change this setting,
    refer to log-announce-interval in the Default data set.
    """
    announce_receipt_timeout: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:announce-receipt-timeout',
            ge=2,
            le=10,
            title='Announce-receipt-timeoutLeaf3',
        ),
    ] = None
    """
    Sets the time limit for missed Announce packets before the master clock is deemed down

    This command configures the announceReceiptTimeout value for all peer associations.
    This defines the number of Announce message intervals that must expire with no received
    Announce messages before declaring an ANNOUNCE_RECEIPT_TIMEOUT event. To change this
    setting, refer to announce-receipt-timeout in the Default data set.
    """
    log_sync_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-sync-interval',
            ge=-6,
            le=0,
            title='Log-sync-intervalLeaf2',
        ),
    ] = None
    """
    The base-2 logarithm of the mean SyncInterval for multicast messages

    The default log sync interval is defined by the profile.
       itug8275dot1: -4 (16 messages per second)
       itug8275dot2: -6 (64 messages per second)
    The rates for unicast transmissions are negotiated separately on a per-port
    basis and are not constrained by this attribute.
    """
    major_version_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:major-version-number',
            ge=0,
            le=255,
            title='Major-version-numberLeaf2',
        ),
    ] = None
    """
    The PTP major version number in use on the port
    """
    minor_version_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:minor-version-number',
            ge=0,
            le=255,
            title='Minor-version-numberLeaf2',
        ),
    ] = None
    """
    The PTP minor version number in use on the port
    """
    local_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:local-priority',
            ge=1,
            le=255,
            title='Local-priorityLeaf3',
        ),
    ] = 128
    """
    Specifies the local priority of the ptp port
    """
    clock_identity: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:clock-identity',
            max_length=8,
            min_length=8,
            title='Clock-identityLeaf4',
        ),
    ] = None
    """
    Identity of the peer clock
    """
    port_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:port-number', ge=0, le=65535, title='Port-numberLeaf3'
        ),
    ] = None
    """
    Port number of the peer clock
    """
    grandmaster_identity: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:grandmaster-identity',
            max_length=8,
            min_length=8,
            title='Grandmaster-identityLeaf2',
        ),
    ] = None
    """
    The clockIdentity of the grandmaster clock in the last Announce message received from this peer
    """
    grandmaster_clock_quality: Annotated[
        Optional[GrandmasterClockQualityContainer2],
        Field(alias='srl_nokia-sync:grandmaster-clock-quality'),
    ] = None
    grandmaster_priority1: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grandmaster-priority1',
            ge=0,
            le=255,
            title='Grandmaster-priority1Leaf2',
        ),
    ] = None
    """
    The priority1 of the grandmaster clock in the last Announce message received from this peer
    """
    grandmaster_priority2: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grandmaster-priority2',
            ge=0,
            le=255,
            title='Grandmaster-priority2Leaf2',
        ),
    ] = None
    """
    The priority2 of the grandmaster clock in the last Announce message received from this peer
    """
    steps_removed: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:steps-removed',
            ge=0,
            le=65535,
            title='Steps-removedLeaf2',
        ),
    ] = None
    """
    The stepsRemoved in the last Announce message received from this peer
    """
    last_rx_interface: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:last-rx-interface', title='Last-rx-interfaceLeaf'),
    ] = None
    """
    Interface used for the last PTP message received from this peer
    """
    last_tx_interface: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:last-tx-interface', title='Last-tx-interfaceLeaf'),
    ] = None
    """
    Interface used for the last PTP message transmitted to this peer
    """
    no_rx_port_timestamping: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-sync:no-rx-port-timestamping',
            title='No-rx-port-timestampingLeaf',
        ),
    ] = None
    """
    Indicates that the last PTP event message received from the peer did not get timestamped at the port

    This is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping
    """
    no_tx_port_timestamping: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-sync:no-tx-port-timestamping',
            title='No-tx-port-timestampingLeaf',
        ),
    ] = None
    """
    Indicates that the last PTP event message transmitted toward the peer did not get timestamped at the port

    This is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping and ptp-ip-timestamping is not disabled
    """
    statistics: Annotated[
        Optional[StatisticsContainer22], Field(alias='srl_nokia-sync:statistics')
    ] = None
    unicast_negotiation: Annotated[
        Optional[UnicastNegotiationContainer],
        Field(alias='srl_nokia-sync:unicast-negotiation'),
    ] = None


class PortDsDscIpListListEntry(BaseModel):
    """
    List of port data sets for discovered IP peers
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port_index: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:port-index', ge=0, le=65535, title='Port-indexLeaf3'
        ),
    ] = None
    """
    Index into the port-ds list

    This is not the PTP port number.
    Discovered IP peer ports are created based on Unicast negotiation.

    If an IP peer is a discovered IP peer and later that IP address is entered as a configured peer, then
    port DS information will move from this list to teh port-ds-cfg-ip-list to cover both aspects of communication with this peer.

    The data sets (i.e., information model) of IEEE Std
    1588-2008 specify a member portDS.portIdentity, which
    uses a typed struct with members clockIdentity and
    portNumber.

    In this YANG data model, portIdentity is not modeled
    in the port-ds.  However, its members are provided
    as follows:
    portIdentity.portNumber is provided as this
    ptp-port-number leaf in port-ds, and
    portIdentity.clockIdentity is provided as the
    clock-identity leaf in default-ds of the instance
    (i.e., ../../default-ds/clock-identity).
    """
    ptp_port_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ptp-port-number',
            ge=0,
            le=65535,
            title='Ptp-port-numberLeaf3',
        ),
    ] = None
    """
    IEEE Std 1588 portNumber

    This is the port-number that will appear in messages sent for this port-index.
    """
    port_state: Annotated[
        Optional[EnumerationEnum80],
        Field(alias='srl_nokia-sync:port-state', title='Port-stateLeaf3'),
    ] = None
    """
    Current state associated with the port
    """
    peer: Annotated[Optional[PeerContainer2], Field(alias='srl_nokia-sync:peer')] = None
    log_min_delay_req_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-min-delay-req-interval',
            ge=-6,
            le=0,
            title='Log-min-delay-req-intervalLeaf3',
        ),
    ] = None
    """
    The base-2 logarithm of the minDelayReqInterval

    This reports the value that was established during the unicast negotiation.
    """
    log_announce_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-announce-interval',
            ge=-3,
            le=4,
            title='Log-announce-intervalLeaf4',
        ),
    ] = None
    """
    The base-2 logarithm of the mean announceInterval

    Mean time interval between successive Announce messages.
    This reports the value that was established during the unicast negotiation.
    """
    log_sync_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-sync-interval',
            ge=-6,
            le=0,
            title='Log-sync-intervalLeaf3',
        ),
    ] = None
    """
    The base-2 logarithm of the mean SyncInterval for multicast messages

    This reports the value that was established during the unicast negotiation.
    """
    major_version_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:major-version-number',
            ge=0,
            le=255,
            title='Major-version-numberLeaf3',
        ),
    ] = None
    """
    The PTP major version number in use on the port
    """
    minor_version_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:minor-version-number',
            ge=0,
            le=255,
            title='Minor-version-numberLeaf3',
        ),
    ] = None
    """
    The PTP minor version number in use on the port
    """
    last_rx_interface: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:last-rx-interface', title='Last-rx-interfaceLeaf2'),
    ] = None
    """
    Interface used for the last PTP message received from this peer
    """
    last_tx_interface: Annotated[
        Optional[str],
        Field(alias='srl_nokia-sync:last-tx-interface', title='Last-tx-interfaceLeaf2'),
    ] = None
    """
    Interface used for the last PTP message transmitted to this peer
    """
    no_rx_port_timestamping: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-sync:no-rx-port-timestamping',
            title='No-rx-port-timestampingLeaf2',
        ),
    ] = None
    """
    Indicates that the last PTP event message received from the peer did not get timestamped at the port

    This is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping
    """
    no_tx_port_timestamping: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-sync:no-tx-port-timestamping',
            title='No-tx-port-timestampingLeaf2',
        ),
    ] = None
    """
    Indicates that the last PTP event message transmitted toward the peer did not get timestamped at the port

    This is an invalid setup for PTP.  All event messages must be timestamped at the port level.  Check that the IMM or MDA supports PTP message timestamping and ptp-ip-timestamping is not disabled
    """
    statistics: Annotated[
        Optional[StatisticsContainer23], Field(alias='srl_nokia-sync:statistics')
    ] = None
    unicast_negotiation: Annotated[
        Optional[UnicastNegotiationContainer2],
        Field(alias='srl_nokia-sync:unicast-negotiation'),
    ] = None


class PortDsGnssContainer(BaseModel):
    """
    List of port data sets for the GNSS special PTP port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ptp_port_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ptp-port-number',
            ge=0,
            le=65535,
            title='Ptp-port-numberLeaf4',
        ),
    ] = None
    """
    IEEE Std 1588 portNumber
    """
    port_state: Annotated[
        Optional[EnumerationEnum80],
        Field(alias='srl_nokia-sync:port-state', title='Port-stateLeaf4'),
    ] = None
    """
    Current state associated with the port
    """
    best_master: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:best-master', title='Best-masterLeaf3'),
    ] = None
    """
    Indicates if this peer was selected by the BMCA to be the best master
    """
    parent_clock: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:parent-clock', title='Parent-clockLeaf4'),
    ] = None
    """
    Indicates if this peer is the current parent clock of this PTP clock

    May differ from best-master due to use of local GNSS as time source.
    """
    major_version_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:major-version-number',
            ge=0,
            le=255,
            title='Major-version-numberLeaf4',
        ),
    ] = None
    """
    The PTP major version number in use on the port
    """
    minor_version_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:minor-version-number',
            ge=0,
            le=255,
            title='Minor-version-numberLeaf4',
        ),
    ] = None
    """
    The PTP minor version number in use on the port
    """


class ProfileListEntry(BaseModel):
    """
    List of configured Packet Link Qualification profiles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-packet-link-qual:name',
            pattern="^(?=^[<>A-Za-z0-9!@#$%^&()|+=`~.,'/_:;?-][<>A-Za-z0-9 !@#$%^&()|+=`~.,'/_:;?-]*$).*$",
            title='NameLeaf37',
        ),
    ] = None
    """
    Name of the Packet Link Qualification profile
    """
    timing: Annotated[
        Union[NtpCase, RpcCase], Field(alias='srl_nokia-packet-link-qual:timing')
    ]
    endpoint_type: Annotated[
        Union[PacketGeneratorCase, AsicLoopbackCase],
        Field(alias='srl_nokia-packet-link-qual:endpoint-type'),
    ]


class ProfileListEntry2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-maintenance-mode:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Name of the maintenance profile
    """
    bgp: Annotated[
        Optional[BgpContainer3], Field(alias='srl_nokia-maintenance-mode:bgp')
    ] = None
    isis: Annotated[
        Optional[IsisContainer2], Field(alias='srl_nokia-maintenance-mode:isis')
    ] = None


class ProtocolAddressContainer(BaseModel):
    """
    The protocol address of the PTP Port that issues the Sync messages
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_protocol: Annotated[
        Optional[Any],
        Field(alias='srl_nokia-sync:network-protocol', title='Network-protocolLeaf'),
    ] = None
    """
    Protocol used by a PTP instance to transport PTP messages
    """
    mac_address: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:mac-address',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}$).*$',
            title='Mac-addressLeaf',
        ),
    ] = None
    """
    The MAC address of the PTP port

    This is only valid for PTP over ethernet encapsulation.
    """
    ip: Annotated[Optional[IpContainer], Field(alias='srl_nokia-sync:ip')] = None


class ProxyArpContainer(BaseModel):
    """
    system bridge-table proxy ARP entry information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer7],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:statistics'),
    ] = None


class ProxyNdContainer(BaseModel):
    """
    system bridge-table proxy ND entry information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    statistics: Annotated[
        Optional[StatisticsContainer8],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:statistics'),
    ] = None


class RadiusContainer(BaseModel):
    """
    Top-level container for RADIUS server data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    auth_port: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:auth-port', ge=0, le=65535, title='Auth-portLeaf'),
    ] = 1812
    """
    Port number for authentication requests
    """
    acct_port: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:acct-port', ge=0, le=65535, title='Acct-portLeaf'),
    ] = 1813
    """
    Port number for accounting requests
    """
    secret_key: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:secret-key', title='Secret-keyLeaf2')
    ] = None
    """
    The unencrypted shared key used between the system and server, up to 64 characters cleartext
    """
    source_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-aaa:source-address', title='Source-addressLeaf2'),
    ] = None
    """
    Source IP address to use in messages to the RADIUS server
    """
    retransmit_attempts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:retransmit-attempts',
            ge=0,
            le=255,
            title='Retransmit-attemptsLeaf',
        ),
    ] = 3
    """
    Number of times the system may send a request to the unresponsive server
    """


class RoleListEntry2(BaseModel):
    """
    List of roles configured in the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration-role:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf32',
        ),
    ] = None
    """
    Assigned rolename for this role
    """
    rule: Annotated[
        Optional[List[RuleListEntry]], Field(alias='srl_nokia-configuration-role:rule')
    ] = None


class ServerProfileListEntry(BaseModel):
    """
    List of configured TLS server profiles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-tls:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Name of the TLS server-profile
    """
    key: Annotated[Optional[str], Field(alias='srl_nokia-tls:key', title='KeyLeaf')] = (
        None
    )
    """
    Base64 encoded key to use with the server certificate

    This includes the '-----BEGIN PRIVATE KEY-----', and '-----END PRIVATE KEY-----' header and footer
    The value is hashed, and only the hashed value is kept
    """
    certificate: Annotated[
        Optional[str],
        Field(alias='srl_nokia-tls:certificate', title='CertificateLeaf2'),
    ] = None
    """
    Base64 encoded certificate to use with the private key

    This includes the '-----BEGIN CERTIFICATE-----' and '-----END CERTIFICATE-----' header and footer
    """
    use_tpm_devid: Annotated[
        Optional[EnumerationEnum9],
        Field(alias='srl_nokia-tls:use-tpm-devid', title='Use-tpm-devidLeaf'),
    ] = None
    """
    Defines if the server profile key and certificate uses the TPM idevid or oidevid
    """
    authenticate_client: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-tls:authenticate-client', title='Authenticate-clientLeaf'
        ),
    ] = False
    """
    Defines if the server should authenticate the identity of connecting clients using the trust anchor
    """
    trust_anchor: Annotated[
        Optional[str],
        Field(alias='srl_nokia-tls:trust-anchor', title='Trust-anchorLeaf'),
    ] = None
    """
    Base64 encoded certificate to use as a trust anchor

    This includes the '-----BEGIN CERTIFICATE-----' and '-----END CERTIFICATE-----' header and footer
    """
    certificate_revocation_list: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-tls:certificate-revocation-list',
            title='Certificate-revocation-listLeaf',
        ),
    ] = None
    """
    Base64 encoded certificate revocation list

    This includes the '-----BEGIN X509 CRL' and '-----END X509 CRL' header and footer
    """
    cipher_list: Annotated[
        Optional[List[Any]], Field(alias='srl_nokia-tls:cipher-list')
    ] = None
    """
    List of ciphers to use when negotiating TLS 1.2 with clients

    TLS 1.3 cipher suites are always enabled:
        tls_aes_256_gcm_sha384, tls_aes_128_gcm_sha256, tls_chacha20_poly1305_sha256
    """
    dynamic: Annotated[
        Optional[bool], Field(alias='srl_nokia-tls:dynamic', title='DynamicLeaf')
    ] = None
    """
    Defines if the profile was dynamically created by service (for example gNSI Authz/Certz)
    """
    certz: Annotated[
        Optional[CertzContainer], Field(alias='srl_nokia-gnsi-certz:certz')
    ] = None


class ServerListEntry(BaseModel):
    """
    List of AAA servers to use within this server-group

    Servers are tried in a round-robin fashion, with the first server always being tried if it is operationally available
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf7',
        ),
    ] = None
    """
    User defined name assigned to the server
    """
    address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-aaa:address', title='AddressLeaf'),
    ] = None
    """
    Address used to reach the server
    """
    tacacs: Annotated[
        Optional[TacacsContainer2], Field(alias='srl_nokia-aaa:tacacs')
    ] = None
    radius: Annotated[
        Optional[RadiusContainer], Field(alias='srl_nokia-aaa:radius')
    ] = None
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-aaa:oper-state', title='Oper-stateLeaf3'),
    ] = None
    """
    Details the operational state of the server

    A server is defined as being down if it fails to respond before the timeout period, or if a path towards the server is not available.
    """
    statistics: Annotated[
        Optional[StatisticsContainer2], Field(alias='srl_nokia-aaa:statistics')
    ] = None


class SourceContainer(BaseModel):
    """
    Source for this input frequency reference

    This shall be either a leafref to an interface or an application.  The leafref must point to an existing physical ethernet interface.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface_or_other: Annotated[
        Union[InterfaceCase, PtpCase, Sync0Case, GnssCase],
        Field(alias='srl_nokia-sync:interface-or-other'),
    ]


class SourceContainer2(BaseModel):
    """
    Source interface used by this PTP port
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    interface_or_sync0: Annotated[
        Union[InterfaceCase2, Sync0Case2],
        Field(alias='srl_nokia-sync:interface-or-sync0'),
    ]


class SshServerListEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-ssh:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    User-provided name of this server instance
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-ssh:admin-state', title='Admin-stateLeaf2'),
    ] = 'disable'
    """
    Enable or disable the SSH server instance
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-ssh:oper-state', title='Oper-stateLeaf2'),
    ] = None
    """
    Operational state of the SSH server instance
    """
    source_address: Annotated[
        Optional[List[Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(alias='srl_nokia-ssh:source-address'),
    ] = []
    """
    List of IP addresses for the SSH server to listen on within the network-instance
    """
    port: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ssh:port', ge=0, le=65535, title='PortLeaf'),
    ] = 22
    """
    Port the SSH server instance will listen on for incoming connections
    """
    disable_shell: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-ssh:disable-shell', title='Disable-shellLeaf'),
    ] = False
    """
    Disable the ability to spawn a shell for incoming connections
    """
    timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ssh:timeout', ge=0, le=65535, title='TimeoutLeaf'),
    ] = 0
    """
    Set the idle timeout in seconds on SSH connections
    """
    rate_limit: Annotated[
        Optional[int],
        Field(alias='srl_nokia-ssh:rate-limit', ge=0, le=65535, title='Rate-limitLeaf'),
    ] = 20
    """
    Set a limit on the number of unauthenticated sessions to the SSH server
     after this number is met, the server will start dropping connection attempts
    """
    protocol_version: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-ssh:protocol-version',
            ge=0,
            le=255,
            title='Protocol-versionLeaf',
        ),
    ] = None
    """
    Protocol version in use by the SSH server
    """
    use_credentialz: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-ssh:use-credentialz', title='Use-credentialzLeaf'),
    ] = None
    """
    Use the gNSI Credentialz service global SSH configuration for this SSH server instance

    Setting this to true will apply any gNSI Credentialz configuration for this SSH server instance. Static
    configuration will override any gNSI Credentialz configuration.
    """
    trust_anchors: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-ssh:trust-anchors')
    ] = []
    """
    List of public keys used to verify user certificates during authentication

     Each items value should be the public key of a CA, e.g. 'ssh-rsa AAAA<...>= comment'. If no trust anchors are configured, authentication using SSH certificates will not function.

     This sets the TrustedUserCAKeys option within each SSH servers configuration file.
    """
    revoked_keys: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-ssh:revoked-keys')
    ] = []
    """
    List of revoked public keys

     Each items value should be the public key of a revoked keypair, e.g. 'ssh-rsa AAAA<...>= comment'. Any keys provided here cannot be used for public key authentication.

     This sets the RevokedKeys option within each SSH servers configuration file.
    """
    allowed_authentication_types: Annotated[
        Optional[List[EnumerationEnum6]],
        Field(alias='srl_nokia-ssh:allowed-authentication-types'),
    ] = ['publickey', 'password']
    """
    List of allowed authentication types

     This sets the AuthenticationMethods option within each SSH servers configuration file. Also sets
     PasswordAuthentication PubkeyAuthentication KbdInteractiveAuthentication options within each SSH servers
     configuration file.
    """
    authorized_principal_check_tool: Annotated[
        Optional[EnumerationEnum7],
        Field(
            alias='srl_nokia-ssh:authorized-principal-check-tool',
            title='Authorized-principal-check-toolLeaf',
        ),
    ] = None
    """
    Configure the tool used to check the authorized principals

    Setting the value to hiba-chk sets the AuthorizedPrincipalsCommand to hiba-chk tool. If
    unset, the aaamgr will do the principal checking.
    """
    host_key: Annotated[
        Optional[HostKeyContainer], Field(alias='srl_nokia-ssh:host-key')
    ] = None
    credentialz: Annotated[
        Optional[CredentialzContainer],
        Field(alias='srl_nokia-gnsi-credentialz:credentialz'),
    ] = None
    counters: Annotated[
        Optional[CountersContainer], Field(alias='srl_nokia-gnsi-credentialz:counters')
    ] = None


class StaticAllocationContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    host: Annotated[
        Optional[List[HostListEntry]], Field(alias='srl_nokia-dhcp-server:host')
    ] = None


class StaticAllocationContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    host: Annotated[
        Optional[List[HostListEntry2]], Field(alias='srl_nokia-dhcp-server:host')
    ] = None


class StatisticsContainer17(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subscribers: Annotated[
        Optional[SubscribersContainer],
        Field(alias='srl_nokia-lawful-intercept:subscribers'),
    ] = None


class TargetsContainer(BaseModel):
    """
    Lawful-intercept targets configured on the local system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    subscriber: Annotated[
        Optional[List[SubscriberListEntry]],
        Field(alias='srl_nokia-lawful-intercept:subscriber'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer17],
        Field(alias='srl_nokia-lawful-intercept:statistics'),
    ] = None


class TlsContainer(BaseModel):
    """
    Top-level container for TLS configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    server_profile: Annotated[
        Optional[List[ServerProfileListEntry]],
        Field(alias='srl_nokia-tls:server-profile'),
    ] = None


class TunnelEndPointsContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    source_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-mirroring:source-address', title='Source-addressLeaf4'),
    ] = None
    """
    remote mirror tunnel source endpoint ip-address
    """
    destination_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(
            alias='srl_nokia-mirroring:destination-address',
            title='Destination-addressLeaf',
        ),
    ] = None
    """
    remote mirror tunnel destination endpoint ip-address
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-mirroring:admin-state', title='Admin-stateLeaf8'),
    ] = 'enable'
    """
    This leaf contains the configured, desired state of the remote mirror tunnel
    """
    service_label: Annotated[
        int,
        Field(
            alias='srl_nokia-mirroring:service-label',
            ge=16,
            le=1048575,
            title='Service-labelLeaf',
        ),
    ]
    """
    Service label for encapsultion type mpls-gre tunnel
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-mirroring:oper-state', title='Oper-stateLeaf8'),
    ] = None
    """
    This leaf contains the operational state of the remote mirror tunnel
    """


class UserListEntry(BaseModel):
    """
    List of local users configured on the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    username: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:username',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    Assigned username for this user
    """
    password: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:password', title='PasswordLeaf3')
    ] = None
    """
    The user password, supplied either as cleartext or as a hashed value

    If provided as cleartext, the system will hash the value on input, storing only the hashed value.
    If provided as a hashed value, the value should include any '$' characters, for example '$ar2$aOvsuj0ALlU=$r750fMa3ZEA/Di8dIfU2fQ=='.
    """
    role: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-aaa:role',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = []
    """
    List of roles to assign to this user

    The most specific rule for a particular role takes precedence.
    Rules from all user roles are evaluated together, most permissive privilege taking precedence.
    """
    superuser: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:superuser', title='SuperuserLeaf2')
    ] = False
    """
    Indicates that this user is a superuser

    A superuser is granted implicit authorization to all YANG paths, has the ability to execute all CLI plugins, and by default is permitted to access the device through any interface.

    Additionally, users with the superuser attribute are able to execute 'sudo' in bash. A user may also be assigned a role or list of roles, but these are only evaluated for service authorization.
    """
    spiffe_ids: Annotated[
        Optional[List[str]],
        Field(alias='srl_nokia-aaa:spiffe-ids', pattern='^(?=^spiffe://.*$).*$'),
    ] = []
    """
    The SPIFFE ID list for the user, including the spiffe:// URI

    This list of IDs is evaluated by TLS-consuming servers (e.g. gNMI, JSON-RPC) that use a TLS server-profile with authenticate-client set to true.

    If a match is found in any incoming offered client certificates, the provider of the certificate is associated with this local user, and given resulting permissions.
    """
    ssh_principals: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-principals')
    ] = []
    """
    List of principals to associate with this user

    If any of the principals in the list are matched in a SSH client's certificate, and that clients username matches this user, and the certificate is verified, the client will authenticate.
    """
    ssh_key: Annotated[Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-key')] = []
    """
    SSH public key(s) for the user

    If defined, the user may login to the system over SSH with this key. This should use the SSH public authorized key format.
    """
    failed_login_attempts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:failed-login-attempts',
            ge=0,
            le=18446744073709551615,
            title='Failed-login-attemptsLeaf2',
        ),
    ] = 0
    """
    Number of failed login attempts from the user
    """
    last_failed_login: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:last-failed-login',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-failed-loginLeaf2',
        ),
    ] = None
    """
    The date and time of the last login failure from this user
    """
    last_successful_login: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:last-successful-login',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-successful-loginLeaf2',
        ),
    ] = None
    """
    The date and time of the last successful login from this user
    """
    password_change_required: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-aaa:password-change-required',
            title='Password-change-requiredLeaf2',
        ),
    ] = None
    """
    Indicates if the user must change their password on next login
    """
    lockout: Annotated[
        Optional[LockoutContainer2], Field(alias='srl_nokia-aaa:lockout')
    ] = None
    credentialz: Annotated[
        Optional[CredentialzContainer4], Field(alias='srl_nokia-aaa:credentialz')
    ] = None


class AdminUserContainer(BaseModel):
    """
    Enclosing container for admin user
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    username: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:username', title='UsernameLeaf')
    ] = 'admin'
    """
    Assigned username for admin user
    """
    password: Annotated[
        Optional[str], Field(alias='srl_nokia-aaa:password', title='PasswordLeaf')
    ] = '$y$j9T$pNVjOgcNNGIWjBcdDfK/7.$Ir4uYxszxtqzVj5AGiZvdWJGs.bpLWBJvHON3YgqnC2'
    """
    The admin password, supplied either as cleartext or as a hashed value

    If provided as cleartext, the system will hash the value on input, storing only the hashed value.
    If provided as a hashed value, the value should include any '$' characters, for example '$ar2$aOvsuj0ALlU=$r750fMa3ZEA/Di8dIfU2fQ=='.
    """
    role: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-aaa:role',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = []
    """
    List of roles to assign to this user

    The most specific rule for a particular role takes precedence.
    Rules from all user roles are evaluated together, most permissive privilege taking precedence.
    """
    superuser: Annotated[
        Optional[bool], Field(alias='srl_nokia-aaa:superuser', title='SuperuserLeaf')
    ] = True
    """
    Indicates if the admin user is a superuser

    A superuser is granted implicit authorization to all YANG paths, has the ability to execute all CLI plugins, and by default is permitted to access the device through any interface.

    Additionally, users with the superuser attribute are able to execute 'sudo' in bash. A user may also be assigned a role or list of roles, but these are only evaluated for service authorization.
    """
    spiffe_ids: Annotated[
        Optional[List[str]],
        Field(alias='srl_nokia-aaa:spiffe-ids', pattern='^(?=^spiffe://.*$).*$'),
    ] = []
    """
    The SPIFFE ID list for the user, including the spiffe:// URI

    This list of IDs is evaluated by TLS-consuming servers (e.g. gNMI, JSON-RPC) that use a TLS server-profile with authenticate-client set to true.

    If a match is found in any incoming offered client certificates, the provider of the certificate is associated with this local user, and given resulting permissions.
    """
    ssh_principals: Annotated[
        Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-principals')
    ] = []
    """
    List of principals to associate with this user

    If any of the principals in the list are matched in a SSH client's certificate, and that clients username matches this user, and the certificate is verified, the client will authenticate.
    """
    ssh_key: Annotated[Optional[List[str]], Field(alias='srl_nokia-aaa:ssh-key')] = []
    """
    SSH public key(s) for the user

    If defined, the user may login to the system over SSH with this key. This should use the SSH public authorized key format.
    """
    failed_login_attempts: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:failed-login-attempts',
            ge=0,
            le=18446744073709551615,
            title='Failed-login-attemptsLeaf',
        ),
    ] = 0
    """
    Number of failed login attempts from the user
    """
    last_failed_login: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:last-failed-login',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-failed-loginLeaf',
        ),
    ] = None
    """
    The date and time of the last login failure from this user
    """
    last_successful_login: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:last-successful-login',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-successful-loginLeaf',
        ),
    ] = None
    """
    The date and time of the last successful login from this user
    """
    password_change_required: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-aaa:password-change-required',
            title='Password-change-requiredLeaf',
        ),
    ] = None
    """
    Indicates if the user must change their password on next login
    """
    lockout: Annotated[
        Optional[LockoutContainer], Field(alias='srl_nokia-aaa:lockout')
    ] = None
    credentialz: Annotated[
        Optional[CredentialzContainer2], Field(alias='srl_nokia-aaa:credentialz')
    ] = None


class AppManagementContainer(BaseModel):
    """
    Top-level container for application configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    application: Annotated[
        Optional[List[ApplicationListEntry]],
        Field(alias='srl_nokia-app-mgmt:application'),
    ] = None


class AuthenticationContainer(BaseModel):
    """
    Top-level container for global authentication data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    authentication_method: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-aaa:authentication-method',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = []
    """
    Ordered list of server-groups to be used during user authentication

    If authentication fails with one method, the next defined method is tried -- failure of all methods results in the user being denied access.
    """
    exit_on_reject: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-aaa:exit-on-reject', title='Exit-on-rejectLeaf'),
    ] = False
    """
    Enable/disable exit-on-reject behaviour for authentication attempts

    With this behaviour enabled, when a reject is received from any server the system will not try further methods, and will reject the user authentication attempt. Default behaviour is to continue trying methods until one accepts the user, or the system runs out of methods to try.
    """
    idle_timeout: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-aaa:idle-timeout',
            ge=0,
            le=4294967295,
            title='Idle-timeoutLeaf',
        ),
    ] = 600
    """
    Set the idle timeout of all CLI sessions

    After the timeout is reached, the session is disconnected from the system.
    """
    dynamic_spiffe: Annotated[
        Optional[DynamicSpiffeContainer], Field(alias='srl_nokia-aaa:dynamic-spiffe')
    ] = None
    admin_user: Annotated[
        Optional[AdminUserContainer], Field(alias='srl_nokia-aaa:admin-user')
    ] = None
    linuxadmin_user: Annotated[
        Optional[LinuxadminUserContainer], Field(alias='srl_nokia-aaa:linuxadmin-user')
    ] = None
    local_linux_users: Annotated[
        Optional[LocalLinuxUsersContainer],
        Field(alias='srl_nokia-aaa:local-linux-users'),
    ] = None
    user: Annotated[
        Optional[List[UserListEntry]], Field(alias='srl_nokia-aaa:user')
    ] = None
    session: Annotated[
        Optional[List[SessionListEntry]], Field(alias='srl_nokia-aaa:session')
    ] = None
    password: Annotated[
        Optional[PasswordContainer4], Field(alias='srl_nokia-aaa:password')
    ] = None


class AuthenticationContainer2(BaseModel):
    """
    Container for protocol authentication options available system wide
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    keychain: Annotated[
        Optional[List[KeychainListEntry]], Field(alias='srl_nokia-keychains:keychain')
    ] = None


class AuthorizationContainer(BaseModel):
    """
    Top-level container for authorization configuration and operational state data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    role: Annotated[
        Optional[List[RoleListEntry]], Field(alias='srl_nokia-aaa:role')
    ] = None
    authz_policy: Annotated[
        Optional[AuthzPolicyContainer], Field(alias='srl_nokia-gnsi-authz:authz-policy')
    ] = None


class BootContainer(BaseModel):
    """
    Top-level container for configuration and state data related to booting the system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    image: Annotated[
        Optional[List[str]],
        Field(alias='srl_nokia-boot:image', pattern='^(?=^[0-9A-Za-z_\\-\\.]*$).*$'),
    ] = []
    """
    Ordered list of local images used to boot the system

          This directly translates into boot configuration in grub, where the images are tried in the order specified by the user. Images are sourced via the internal SD card, and the value passed is the folder that contains the initramfs, kernel, and squashfs image. The search path for these directories is /mnt/nokiaos/<folder>
    """
    golden_image: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-boot:golden-image',
            pattern='^(?=^[0-9A-Za-z_\\-\\.]*$).*$',
            title='Golden-imageLeaf',
        ),
    ] = None
    """
    The local image the system reverts to when a factory reset operation is requested

    The value is the folder that contains the initramfs, kernel, and squashfs image.
    The search path for these directories is /mnt/nokiaos/<folder>
    """
    fips_140: Annotated[
        Optional[Fips140Container], Field(alias='srl_nokia-boot:fips-140')
    ] = None
    autoboot: Annotated[
        Optional[AutobootContainer], Field(alias='srl_nokia-boot:autoboot')
    ] = None


class ComputedDesignatedForwarderCandidatesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    designated_forwarder_candidate: Annotated[
        Optional[List[DesignatedForwarderCandidateListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder-candidate'
        ),
    ] = None


class ControlPlaneTrafficContainer(BaseModel):
    """
    Container for the control plane traffic.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    output: Annotated[
        Optional[OutputContainer], Field(alias='srl_nokia-system:output')
    ] = None
    input: Annotated[
        Optional[InputContainer], Field(alias='srl_nokia-system:input')
    ] = None


class DefaultDsContainer(BaseModel):
    """
    The default data set of the PTP instance

    In the context of the protocol, this data set is required
    for an Ordinary Clock or Boundary Clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance_type: Annotated[
        Optional[EnumerationEnum76],
        Field(alias='srl_nokia-sync:instance-type', title='Instance-typeLeaf'),
    ] = 'bc'
    """
    The type of PTP instance as per IEEE1588 standard

    For G.8275.1:
     oc is for T-GM,
     bc is for T-BC;
     T-TSC not supported since T-BC can be used for this role
    For G.8275.2:
     oc is for T-GM,
     bc is for T-BC-A and T-BC-P;
     T-TSC-A and T-TSC-P are not supported since T-BC-A or T-BC-P can be used for this role
    """
    instance_enable: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:instance-enable', title='Instance-enableLeaf'),
    ] = False
    """
    Enable PTP clock
    """
    clock_identity: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:clock-identity',
            max_length=8,
            min_length=8,
            title='Clock-identityLeaf',
        ),
    ] = None
    """
    The clockIdentity of the local clock
    """
    number_ports: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:number-ports',
            ge=0,
            le=65535,
            title='Number-portsLeaf',
        ),
    ] = None
    """
    The number of PTP ports on the instance
    """
    clock_quality: Annotated[
        Optional[ClockQualityContainer], Field(alias='srl_nokia-sync:clock-quality')
    ] = None
    priority1: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:priority1', ge=0, le=255, title='Priority1Leaf'),
    ] = 128
    """
    The IEEE Std 1588 priority1 of the PTP instance

    Since priority1 is one of the first comparisons
    performed by the Best Master Clock Algorithm (BMCA).
    Range is 0-255.
    """
    priority2: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:priority2', ge=0, le=255, title='Priority2Leaf'),
    ] = 128
    """
    The IEEE Std 1588 priority2 of the PTP instance

    The priority2 member is compared by the Best Master
    Clock Algorithm (BMCA) after priority1 and clockQuality.
    Lower values take precedence.
    """
    domain_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:domain-number',
            ge=0,
            le=255,
            title='Domain-numberLeaf',
        ),
    ] = None
    """
    The IEEE Std 1588 domainNumber of the PTP instance

    A domain consists of one or more PTP instances
    communicating with each other as defined by the
    protocol. A domain shall define the scope of PTP message
    communication, state, operations, data sets, and
    timescale. Therefore, each domain represents a distinct
    time.
    The default domain number is defined by the profile.
       itug8275dot1: 24
       itug8275dot2: 44
    """
    log_announce_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-announce-interval',
            ge=-3,
            le=4,
            title='Log-announce-intervalLeaf',
        ),
    ] = None
    """
    The base-2 logarithm of the mean announceInterval

    This is the mean time interval between successive Announce messages.
    The default log announce interval is defined by the profile.
       itug8275dot1: -3 (8 messages per second)
       itug8275dot2: 1 (1 message every two seconds)
    """
    announce_receipt_timeout: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:announce-receipt-timeout',
            ge=2,
            le=10,
            title='Announce-receipt-timeoutLeaf',
        ),
    ] = 3
    """
    Sets the time limit for missed Announce packets before the master clock is deemed down

    This command configures the announceReceiptTimeout value for all peer associations.
    This defines the number of Announce message intervals that must expire with no received
    Announce messages before declaring an ANNOUNCE_RECEIPT_TIMEOUT event.
    """
    current_time: Annotated[
        Optional[CurrentTimeContainer], Field(alias='srl_nokia-sync:current-time')
    ] = None
    local_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:local-priority',
            ge=1,
            le=255,
            title='Local-priorityLeaf',
        ),
    ] = 128
    """
    The IEEE Std 1588 priority2 of the PTP instance

    The priority2 member is compared by the Best Master
    Clock Algorithm (BMCA) after priority1 and clockQuality.
    Lower values take precedence.
    """
    two_step_flag: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:two-step-flag', title='Two-step-flagLeaf'),
    ] = None
    """
    Indicates if the clock is operating in two-step mode
    """
    statistics: Annotated[
        Optional[StatisticsContainer18], Field(alias='srl_nokia-sync:statistics')
    ] = None
    time_recovery_engine: Annotated[
        Optional[TimeRecoveryEngineContainer],
        Field(alias='srl_nokia-sync:time-recovery-engine'),
    ] = None
    freq_recovery_engine: Annotated[
        Optional[FreqRecoveryEngineContainer],
        Field(alias='srl_nokia-sync:freq-recovery-engine'),
    ] = None


class Dhcpv4Container(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-dhcp-server:admin-state', title='Admin-stateLeaf20'),
    ] = 'disable'
    """
    Administratively enable or disable the dhcp server
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-dhcp-server:oper-state', title='Oper-stateLeaf15'),
    ] = None
    """
    Details if the dhcp server is operationally available
    """
    trace_options: Annotated[
        Optional[TraceOptionsContainer2],
        Field(alias='srl_nokia-dhcp-server:trace-options'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer14], Field(alias='srl_nokia-dhcp-server:statistics')
    ] = None
    options: Annotated[
        Optional[OptionsContainer2], Field(alias='srl_nokia-dhcp-server:options')
    ] = None
    static_allocation: Annotated[
        Optional[StaticAllocationContainer],
        Field(alias='srl_nokia-dhcp-server:static-allocation'),
    ] = None


class Dhcpv6Container(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-dhcp-server:admin-state', title='Admin-stateLeaf21'),
    ] = 'disable'
    """
    Administratively enable or disable the dhcp server
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-dhcp-server:oper-state', title='Oper-stateLeaf16'),
    ] = None
    """
    Details if the dhcp server is operationally available
    """
    trace_options: Annotated[
        Optional[TraceOptionsContainer3],
        Field(alias='srl_nokia-dhcp-server:trace-options'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer15], Field(alias='srl_nokia-dhcp-server:statistics')
    ] = None
    options: Annotated[
        Optional[OptionsContainer4], Field(alias='srl_nokia-dhcp-server:options')
    ] = None
    static_allocation: Annotated[
        Optional[StaticAllocationContainer2],
        Field(alias='srl_nokia-dhcp-server:static-allocation'),
    ] = None


class DnsContainer(BaseModel):
    """
    Top-level container for DNS configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-dns:oper-state', title='Oper-stateLeaf5'),
    ] = None
    """
    Details the operational state of the DNS client
    """
    search_list: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-dns:search-list',
            pattern='^(?=^((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.$).*$',
        ),
    ] = []
    """
    An ordered list of domains to search when resolving a host name
    """
    server_list: Annotated[
        Optional[List[Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(alias='srl_nokia-dns:server-list'),
    ] = []
    """
    List of the DNS servers that the resolver should query
    """
    source_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-dns:source-address', title='Source-addressLeaf3'),
    ] = None
    """
    Source address for DNS to use for messages sent to a remote server
    """
    host_entry: Annotated[
        Optional[List[HostEntryListEntry]], Field(alias='srl_nokia-dns:host-entry')
    ] = None


class EventHandlerContainer(BaseModel):
    """
    Top-level container for configuration and state of event handler and event handling instances
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    run_as_user: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-event-handler:run-as-user',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Run-as-userLeaf',
        ),
    ] = None
    """
    The user to run event handler instances as

    If no user is configured, scripts are executed as the 'admin' user.
    """
    instance: Annotated[
        Optional[List[InstanceListEntry]],
        Field(alias='srl_nokia-event-handler:instance'),
    ] = None


class EvpnContainer2(BaseModel):
    """
    System bridge-table BGP-EVPN information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mpls_multicast_tep: Annotated[
        Optional[MplsMulticastTepContainer],
        Field(
            alias='srl_nokia-system-bridge-table-evpn-mpls-multicast-tep:mpls-multicast-tep'
        ),
    ] = None


class GroupListEntry(BaseModel):
    """
    List of user-configured maintenance groups
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-maintenance-mode:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf40',
        ),
    ] = None
    """
    Name of the maintenance group.
    """
    maintenance_mode: Annotated[
        Optional[MaintenanceModeContainer],
        Field(alias='srl_nokia-maintenance-mode:maintenance-mode'),
    ] = None
    maintenance_profile: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-maintenance-mode:maintenance-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Maintenance-profileLeaf',
        ),
    ] = None
    """
    Leaf reference to /system/maintenance/profile/name
    """
    members: Annotated[
        Optional[MembersContainer], Field(alias='srl_nokia-maintenance-mode:members')
    ] = None


class GrpcServerListEntry(BaseModel):
    """
    List of configured gRPC server instances
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf8',
        ),
    ] = None
    """
    User-provided name of this server instance
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-grpc:admin-state', title='Admin-stateLeaf3'),
    ] = 'disable'
    """
    Globally enable or disable the gRPC server instance

    Disabling this will disable all gRPC server sockets in all network instances, and any configured unix domain sockets.
    """
    trace_options: Annotated[
        Optional[List[EnumerationEnum14]], Field(alias='srl_nokia-grpc:trace-options')
    ] = []
    """
    gRPC trace options
    """
    timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:timeout', ge=0, le=65535, title='TimeoutLeaf3'),
    ] = 7200
    """
    Set the idle timeout in seconds on gRPC connections
    """
    rate_limit: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:rate-limit', ge=0, le=65535, title='Rate-limitLeaf2'
        ),
    ] = 60
    """
    Set a limit on the number of RPC calls per minute
    """
    session_limit: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:session-limit',
            ge=0,
            le=65535,
            title='Session-limitLeaf',
        ),
    ] = 20
    """
    Set a limit on the number of simultaneous active gRPC sessions

    A session is defined as an individual RPC invocation, which could result in a single client generating multiple sessions.
    In the context of a Subscribe RPC this is the number of simultaneously active SubscribeRequests across all Subscribe RPCs.
    """
    max_concurrent_streams: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-grpc:max-concurrent-streams',
            ge=0,
            le=2147483647,
            title='Max-concurrent-streamsLeaf',
        ),
    ] = 65535
    """
    Set a limit on the number of concurrent gRPC streams
    """
    metadata_authentication: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-grpc:metadata-authentication',
            title='Metadata-authenticationLeaf',
        ),
    ] = True
    """
    Enable or disable the use of username/password metadata authentication for every gRPC request
    """
    yang_models: Annotated[
        Optional[EnumerationEnum15],
        Field(alias='srl_nokia-grpc:yang-models', title='Yang-modelsLeaf'),
    ] = 'native'
    """
    Specify yang-models to be used when origin field is not present in requests
    """
    services: Annotated[Optional[List[Any]], Field(alias='srl_nokia-grpc:services')] = (
        []
    )
    """
    The gRPC service definitions that should be enabled for this gRPC server instance
    """
    tls_profile: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-grpc:tls-profile',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='Tls-profileLeaf',
        ),
    ] = None
    """
    Reference to the TLS profile to use on the gRPC server

    If none is specified, then TLS is not used.
    """
    default_tls_profile: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-grpc:default-tls-profile', title='Default-tls-profileLeaf'
        ),
    ] = False
    """
    Whether to use default TLS profile (generated by the system) if none is configured via tls-profile field
    """
    gnmi: Annotated[Optional[GnmiContainer], Field(alias='srl_nokia-grpc:gnmi')] = None
    source_address: Annotated[
        Optional[List[Union[Ipv4AddressType, Ipv6AddressType]]],
        Field(alias='srl_nokia-grpc:source-address'),
    ] = ['::']
    """
    List of IP addresses the gRPC server will listen on within the network instance
    """
    port: Annotated[
        Optional[int],
        Field(alias='srl_nokia-grpc:port', ge=0, le=65535, title='PortLeaf3'),
    ] = 57400
    """
    Port the gRPC server will listen on for incoming connections
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-grpc:oper-state', title='Oper-stateLeaf4'),
    ] = None
    """
    Details if the gRPC server is operationally available
    """
    statistics: Annotated[
        Optional[StatisticsContainer3], Field(alias='srl_nokia-grpc:statistics')
    ] = None
    certz: Annotated[Optional[CertzContainer2], Field(alias='srl_nokia-grpc:certz')] = (
        None
    )
    unix_socket: Annotated[
        Optional[UnixSocketContainer], Field(alias='srl_nokia-grpc:unix-socket')
    ] = None
    client: Annotated[
        Optional[List[ClientListEntry]], Field(alias='srl_nokia-grpc:client')
    ] = None
    pathz: Annotated[
        Optional[PathzContainer], Field(alias='srl_nokia-gnsi-pathz:pathz')
    ] = None


class InstanceListEntry2(BaseModel):
    """
    List of line references configured for frequency
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:instance-number',
            ge=1,
            le=5,
            title='Instance-numberLeaf',
        ),
    ] = None
    """
    The instance number of the each line reference
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-sync:admin-state', title='Admin-stateLeaf29'),
    ] = 'disable'
    """
    Configure the administrative state of this frequency reference instance
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-sync:oper-state', title='Oper-stateLeaf23'),
    ] = None
    """
    Indicates the operational state of this line reference
    """
    source: Annotated[
        Optional[SourceContainer], Field(alias='srl_nokia-sync:source')
    ] = None
    priority: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:priority', ge=1, le=5, title='PriorityLeaf'),
    ] = 3
    """
    Sets the priority of this line timing reference for the system timing selection process
    1 = highest priority
    5 = lowest priority
    Duplicate numbers are not allowed
    """
    ql_override: Annotated[
        Optional[EnumerationEnum68],
        Field(alias='srl_nokia-sync:ql-override', title='Ql-overrideLeaf'),
    ] = 'unused'
    """
    Override the incoming QL/SSM value for this line reference
    Quality level override of a timing reference
    Options are unused, prs, stu, st2, tnc, st3e, st3, prc, ssua, ssub, sec, eec1, eec2
    """
    ql_value: Annotated[
        Optional[EnumerationEnum69],
        Field(alias='srl_nokia-sync:ql-value', title='Ql-valueLeaf'),
    ] = None
    """
    The incoming QL/SSM value from this line reference
    """
    reference_status: Annotated[
        Optional[EnumerationEnum70],
        Field(alias='srl_nokia-sync:reference-status', title='Reference-statusLeaf'),
    ] = None
    """
    The current status this line reference
    """
    not_qualified_reason: Annotated[
        Optional[EnumerationEnum71],
        Field(
            alias='srl_nokia-sync:not-qualified-reason',
            title='Not-qualified-reasonLeaf',
        ),
    ] = None
    """
    If the reference is not qualified, this identifies the reason
    """


class InterfaceListEntry3(BaseModel):
    """
    List of interfaces on which LLDP can be enabled
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str], Field(alias='srl_nokia-lldp:name', title='NameLeaf26')
    ] = None
    """
    Reference to the LLDP Ethernet interface
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-lldp:admin-state', title='Admin-stateLeaf15'),
    ] = 'enable'
    """
    Enable or disable LLDP on the interface
    """
    bgp_auto_discovery: Annotated[
        Optional[BgpAutoDiscoveryContainer2],
        Field(alias='srl_nokia-lldp:bgp-auto-discovery'),
    ] = None
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-lldp:oper-state', title='Oper-stateLeaf12'),
    ] = None
    """
    Details the operational state of LLDP on the interface
    """
    statistics: Annotated[
        Optional[StatisticsContainer12], Field(alias='srl_nokia-lldp:statistics')
    ] = None
    neighbor: Annotated[
        Optional[List[NeighborListEntry]], Field(alias='srl_nokia-lldp:neighbor')
    ] = None


class JsonRpcServerContainer(BaseModel):
    """
    Configures the JSON RPC access API
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-json-rpc:admin-state', title='Admin-stateLeaf22'),
    ] = 'disable'
    """
    Globally enable or disable the JSON RPC server
    Disabling this will disable all JSON RPC servers.
    """
    commit_confirmed_timeout: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-json-rpc:commit-confirmed-timeout',
            ge=0,
            le=86400,
            title='Commit-confirmed-timeoutLeaf2',
        ),
    ] = 0
    """
    Number of seconds to wait for confirmation. A value of 0 means commit confirmed is not used
    """
    network_instance: Annotated[
        Optional[List[NetworkInstanceListEntry3]],
        Field(alias='srl_nokia-json-rpc:network-instance'),
    ] = None
    trace_options: Annotated[
        Optional[List[EnumerationEnum64]],
        Field(alias='srl_nokia-json-rpc:trace-options'),
    ] = []
    """
    JSON RPC trace options
    """
    unix_socket: Annotated[
        Optional[UnixSocketContainer3], Field(alias='srl_nokia-json-rpc:unix-socket')
    ] = None


class LawfulInterceptContainer(BaseModel):
    """
    Top level container for configuration and operational state for lawful-intercept
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    li_hourly_status: Annotated[
        Optional[LiHourlyStatusContainer],
        Field(alias='srl_nokia-lawful-intercept:li-hourly-status'),
    ] = None
    targets: Annotated[
        Optional[TargetsContainer], Field(alias='srl_nokia-lawful-intercept:targets')
    ] = None
    system_name: Annotated[
        Optional[str],
        Field(alias='srl_nokia-lawful-intercept:system-name', title='System-nameLeaf3'),
    ] = None
    """
    Specify the LI management system host name
    """
    pfcp: Annotated[
        Optional[PfcpContainer], Field(alias='srl_nokia-lawful-intercept:pfcp')
    ] = None
    admf: Annotated[
        Optional[AdmfContainer], Field(alias='srl_nokia-lawful-intercept:admf')
    ] = None
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(
            alias='srl_nokia-lawful-intercept:admin-state', title='Admin-stateLeaf28'
        ),
    ] = 'enable'
    """
    This leaf contains the configured, desired state of lawful intercept
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-lawful-intercept:oper-state', title='Oper-stateLeaf22'),
    ] = None
    """
    This leaf reflects the admin state of the lawful intercept
    """


class LldpContainer(BaseModel):
    """
    Top-level container for LLDP configuration and state data
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    trace_options: Annotated[
        Optional[List[EnumerationEnum47]], Field(alias='srl_nokia-lldp:trace-options')
    ] = []
    """
    LLDP trace options
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-lldp:admin-state', title='Admin-stateLeaf13'),
    ] = 'enable'
    """
    Enable or disable LLDP at the system level
    """
    hello_timer: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:hello-timer',
            ge=0,
            le=18446744073709551615,
            title='Hello-timerLeaf',
        ),
    ] = 30
    """
    System level hello timer for the LLDP protocol
    """
    hold_multiplier: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-lldp:hold-multiplier',
            ge=0,
            le=255,
            title='Hold-multiplierLeaf',
        ),
    ] = 4
    """
    System level hold multiplier, used to define neighbor aging

    This field defines how many hellos need to be missed before
    a neighbor is aged out.

    This field also is used along with the 'hello-timer' field
    to define the TTL TLV in outgoing LLDPDUs.
    """
    bgp_auto_discovery: Annotated[
        Optional[BgpAutoDiscoveryContainer],
        Field(alias='srl_nokia-lldp:bgp-auto-discovery'),
    ] = None
    system_name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:system-name',
            max_length=255,
            min_length=0,
            title='System-nameLeaf',
        ),
    ] = None
    """
    The systems administratively assigned name

    The system name field shall contain an alpha-numeric string
    that indicates the system's administratively assigned name.
    The system name should be the system's fully qualified domain
    name.
    """
    system_description: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-lldp:system-description',
            max_length=255,
            min_length=0,
            title='System-descriptionLeaf',
        ),
    ] = None
    """
    Field detailing system description, including name and versions

    The system description field shall contain an alpha-numeric
    string that is the textual description of the network entity.
    The system description should include the full name and
    version identification of the system's hardware type,
    software operating system, and networking software.
    """
    chassis_id: Annotated[
        Optional[str], Field(alias='srl_nokia-lldp:chassis-id', title='Chassis-idLeaf')
    ] = None
    """
    The Chassis ID is a mandatory TLV which identifies the
    chassis component of the endpoint identifier associated with
    the transmitting LLDP agent
    """
    chassis_id_type: Annotated[
        Optional[EnumerationEnum48],
        Field(alias='srl_nokia-lldp:chassis-id-type', title='Chassis-id-typeLeaf'),
    ] = 'MAC_ADDRESS'
    """
    The source for the chassis identifier string

    It is an enumerator defined by the LldpChassisIdSubtype object
    from IEEE 802.1AB MIB.
    """
    management_address: Annotated[
        Optional[List[ManagementAddressListEntry]],
        Field(alias='srl_nokia-lldp:management-address'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer11], Field(alias='srl_nokia-lldp:statistics')
    ] = None
    interface: Annotated[
        Optional[List[InterfaceListEntry3]], Field(alias='srl_nokia-lldp:interface')
    ] = None


class MaintenanceContainer(BaseModel):
    """
    Top-level container for Maintenance Mode configuration
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    group: Annotated[
        Optional[List[GroupListEntry]], Field(alias='srl_nokia-maintenance-mode:group')
    ] = None
    profile: Annotated[
        Optional[List[ProfileListEntry2]],
        Field(alias='srl_nokia-maintenance-mode:profile'),
    ] = None


class ManagementContainer(BaseModel):
    """
    Enclosing container for options relating to management server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    openconfig: Annotated[
        Optional[OpenconfigContainer], Field(alias='srl_nokia-openconfig:openconfig')
    ] = None


class MulticastForwardingInformationBaseContainer(BaseModel):
    """
    System Multicast Forwarding Information Base table
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    multicast_route: Annotated[
        Optional[List[MulticastRouteListEntry]],
        Field(alias='srl_nokia-system-multicast-mfib-table:multicast-route'),
    ] = None


class NetworkInstanceListEntry2(BaseModel):
    """
    List of network instances to run a dhcp server in
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-dhcp-server:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='NameLeaf36',
        ),
    ] = None
    """
    Reference to a configured network instance
    """
    dhcpv4: Annotated[
        Optional[Dhcpv4Container], Field(alias='srl_nokia-dhcp-server:dhcpv4')
    ] = None
    dhcpv6: Annotated[
        Optional[Dhcpv6Container], Field(alias='srl_nokia-dhcp-server:dhcpv6')
    ] = None


class NtpContainer2(BaseModel):
    """
    Top-level container for NTP configuration and state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-ntp:admin-state', title='Admin-stateLeaf27'),
    ] = None
    """
    Enables the system NTP client
    and indicates that the system should attempt to synchronize
    the clock
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-ntp:oper-state', title='Oper-stateLeaf20'),
    ] = None
    """
    Details the operational state of the NTP client
    """
    synchronized: Annotated[
        Optional[
            Union[
                SynchronizedLeaf1,
                Union[DomainNameType, Union[Ipv4AddressType, Ipv6AddressType]],
            ]
        ],
        Field(alias='srl_nokia-ntp:synchronized', title='SynchronizedLeaf'),
    ] = None
    """
    Address of the NTP server that the local client is synchronized to
    This field is set to 'unsynchronized', if the local client is not
    synchronized
    """
    source_address: Annotated[
        Optional[Union[Ipv4AddressType, Ipv6AddressType]],
        Field(alias='srl_nokia-ntp:source-address', title='Source-addressLeaf5'),
    ] = None
    """
    Source address for NTP to use for messages sent to a remote server
    """
    server: Annotated[
        Optional[List[ServerListEntry2]], Field(alias='srl_nokia-ntp:server')
    ] = None


class PacketLinkQualificationContainer(BaseModel):
    """
    Top-level container for gNOI Packet Link Qualification profiles
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    profile: Annotated[
        Optional[List[ProfileListEntry]],
        Field(alias='srl_nokia-packet-link-qual:profile'),
    ] = None


class ParentDsContainer(BaseModel):
    """
    The parent data set of the clock
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    parent_port_identity: Annotated[
        Optional[ParentPortIdentityContainer],
        Field(alias='srl_nokia-sync:parent-port-identity'),
    ] = None
    grandmaster_identity: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:grandmaster-identity',
            max_length=8,
            min_length=8,
            title='Grandmaster-identityLeaf',
        ),
    ] = None
    """
    The clockIdentity of the grandmaster clock
    """
    grandmaster_clock_quality: Annotated[
        Optional[GrandmasterClockQualityContainer],
        Field(alias='srl_nokia-sync:grandmaster-clock-quality'),
    ] = None
    grandmaster_priority1: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grandmaster-priority1',
            ge=0,
            le=255,
            title='Grandmaster-priority1Leaf',
        ),
    ] = None
    """
    The priority1 attribute of the grandmaster clock
    """
    grandmaster_priority2: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:grandmaster-priority2',
            ge=0,
            le=255,
            title='Grandmaster-priority2Leaf',
        ),
    ] = None
    """
    The priority2 attribute of the grandmaster clock
    """
    protocol_address: Annotated[
        Optional[ProtocolAddressContainer],
        Field(alias='srl_nokia-sync:protocol-address'),
    ] = None


class PathzContainer2(BaseModel):
    """
    Information relating to the active Pathz authorization policy instances

    This policies is provided by the gNSI gRPC service, and can be changed using the gNSI.Pathz.Rotate RPC
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    collect_policy_success_failure_counters: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-configuration:collect-policy-success-failure-counters',
            title='Collect-policy-success-failure-countersLeaf',
        ),
    ] = False
    """
    Indicates whether the gNSI.pathz module should collect access counters information.
    """
    use_exclusively: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-configuration:use-exclusively', title='Use-exclusivelyLeaf'
        ),
    ] = False
    """
    Indicates whether the Pathz authorization policy should be used exclusively for access authorization.

    If set to true, the Pathz authorization policy will be used exclusively, any statically configured RBAC
    rules will be ignored. If set to false, the Pathz authorization policy will be used together with the
    statically configured RBAC rules (evaluating both policies and taking the logical conjunction of the
    results).
    """
    policy: Annotated[
        Optional[List[PolicyListEntry]], Field(alias='srl_nokia-configuration:policy')
    ] = None


class PortDsInterfaceListListEntry(BaseModel):
    """
    List of port data sets for interfaces
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    port_index: Annotated[
        Optional[int],
        Field(alias='srl_nokia-sync:port-index', ge=1, le=999, title='Port-indexLeaf'),
    ] = None
    """
    Index into the port-ds list

    This is not the PTP port number.
    Configurable ports use port indices 1 through 999 but there is a limit on the overall number of these configured ports based on the platform and software release.

    The data sets (i.e., information model) of IEEE Std
    1588-2008 specify a member portDS.portIdentity, which
    uses a typed struct with members clockIdentity and
    portNumber.

    In this YANG data model, portIdentity is not modeled
    in the port-ds.  However, its members are provided
    as follows:
    portIdentity.portNumber is provided as this
    ptp-port-number leaf in port-ds, and
    portIdentity.clockIdentity is provided as the
    clock-identity leaf in default-ds of the instance
    (i.e., ../../default-ds/clock-identity).
    """
    ptp_port_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:ptp-port-number',
            ge=0,
            le=65535,
            title='Ptp-port-numberLeaf',
        ),
    ] = None
    """
    IEEE Std 1588 portNumber

    This is the port-number that will appear in messages sent for this port-index.
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-sync:admin-state', title='Admin-stateLeaf30'),
    ] = 'disable'
    """
    The administrative state of the ptp port
    """
    port_state: Annotated[
        Optional[EnumerationEnum80],
        Field(alias='srl_nokia-sync:port-state', title='Port-stateLeaf'),
    ] = None
    """
    Current state associated with the port
    """
    source: Annotated[
        Optional[SourceContainer2], Field(alias='srl_nokia-sync:source')
    ] = None
    best_master: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:best-master', title='Best-masterLeaf'),
    ] = None
    """
    Indicates if this interface was selected by the BMCA to be the best master
    """
    parent_clock: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:parent-clock', title='Parent-clockLeaf'),
    ] = None
    """
    Indicates if this interface is the current parent clock of this PTP clock

    May differ from best-master due to use of local GNSS as time source.
    """
    log_min_delay_req_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-min-delay-req-interval',
            ge=-6,
            le=0,
            title='Log-min-delay-req-intervalLeaf',
        ),
    ] = None
    """
    The base-2 logarithm of the minDelayReqInterval

    The minimum permitted mean time interval between successive Delay_Req messages.
    The default log-min-delay-req-interval is defined by the profile.
       itug8275dot1: -4 (16 messages per second)
       itug8275dot2: -6 (64 messages per second)
    """
    log_announce_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-announce-interval',
            ge=-3,
            le=4,
            title='Log-announce-intervalLeaf2',
        ),
    ] = None
    """
    The base-2 logarithm of the mean announceInterval

    Mean time interval between successive Announce messages. To change this setting,
    refer to log-announce-interval in the Default data set.
    """
    announce_receipt_timeout: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:announce-receipt-timeout',
            ge=2,
            le=10,
            title='Announce-receipt-timeoutLeaf2',
        ),
    ] = None
    """
    Sets the time limit for missed Announce packets before the master clock is deemed down

    This defines the number of Announce message intervals that must expire with no received
    Announce messages before declaring an ANNOUNCE_RECEIPT_TIMEOUT event. To change this
    setting, refer to announce-receipt-timeout in the Default data set.
    """
    log_sync_interval: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:log-sync-interval',
            ge=-6,
            le=0,
            title='Log-sync-intervalLeaf',
        ),
    ] = None
    """
    The base-2 logarithm of the mean SyncInterval for multicast messages

    The default log sync interval is defined by the profile.
       itug8275dot1: -4 (16 messages per second)
       itug8275dot2: -6 (64 messages per second)
    """
    major_version_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:major-version-number',
            ge=0,
            le=255,
            title='Major-version-numberLeaf',
        ),
    ] = None
    """
    The PTP major version number in use on the port
    """
    minor_version_number: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:minor-version-number',
            ge=0,
            le=255,
            title='Minor-version-numberLeaf',
        ),
    ] = None
    """
    The PTP minor version number in use on the port
    """
    local_priority: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:local-priority',
            ge=1,
            le=255,
            title='Local-priorityLeaf2',
        ),
    ] = 128
    """
    Specifies the local priority of the ptp port
    """
    master_only: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-sync:master-only', title='Master-onlyLeaf'),
    ] = True
    """
    Specifies the masterOnly attribute of the ptp port
    """
    dest_mac: Annotated[
        Optional[EnumerationEnum81],
        Field(alias='srl_nokia-sync:dest-mac', title='Dest-macLeaf'),
    ] = 'forwardable'
    """
    Configure the MAC address associated with forwardable or non-forwardable
    """
    statistics: Annotated[
        Optional[StatisticsContainer21], Field(alias='srl_nokia-sync:statistics')
    ] = None
    neighbor_count: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:neighbor-count',
            ge=0,
            le=4294967295,
            title='Neighbor-countLeaf',
        ),
    ] = None
    """
    The number of neighbors for the port
    """
    neighbor_list: Annotated[
        Optional[List[NeighborListListEntry]],
        Field(alias='srl_nokia-sync:neighbor-list'),
    ] = None


class RemoteContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    encap: Annotated[
        EnumerationEnum28, Field(alias='srl_nokia-mirroring:encap', title='EncapLeaf')
    ]
    network_instance: Annotated[
        str,
        Field(
            alias='srl_nokia-mirroring:network-instance',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='Network-instanceLeaf',
        ),
    ]
    """
    network instance to intitiate remote mirror tunnel
    """
    tunnel_end_points: Annotated[
        Optional[TunnelEndPointsContainer],
        Field(alias='srl_nokia-mirroring:tunnel-end-points'),
    ] = None


class ServerGroupListEntry(BaseModel):
    """
    List of AAA server-groups in the system

    Each server group specifies a type, of which all servers must use. If using the 'local' type, then no servers may be specified.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-aaa:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = None
    """
    User defined name for the server group
    """
    type: Annotated[Any, Field(alias='srl_nokia-aaa:type', title='TypeLeaf4')]
    """
    AAA server type -- all servers in the group must be of this type
    """
    timeout: Annotated[
        Optional[int],
        Field(alias='srl_nokia-aaa:timeout', ge=1, le=3600, title='TimeoutLeaf2'),
    ] = 10
    """
    Set the timeout in seconds on responses from servers in this group
    """
    priv_lvl_authorization: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-aaa:priv-lvl-authorization',
            title='Priv-lvl-authorizationLeaf',
        ),
    ] = False
    """
    Use TACACS+ priv-lvl based authorization

    If false, then authorization is skipped for TACACS+ users granting full admin access for those users.
    """
    server: Annotated[
        Optional[List[ServerListEntry]], Field(alias='srl_nokia-aaa:server')
    ] = None


class AaaContainer(BaseModel):
    """
    Top-level container for AAA services
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    authentication: Annotated[
        Optional[AuthenticationContainer], Field(alias='srl_nokia-aaa:authentication')
    ] = None
    authorization: Annotated[
        Optional[AuthorizationContainer], Field(alias='srl_nokia-aaa:authorization')
    ] = None
    accounting: Annotated[
        Optional[AccountingContainer], Field(alias='srl_nokia-aaa:accounting')
    ] = None
    server_group: Annotated[
        Optional[List[ServerGroupListEntry]], Field(alias='srl_nokia-aaa:server-group')
    ] = None


class BgpInstanceListEntry(BaseModel):
    """
    bgp-instance associated to this ethernet-segment
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:instance',
            ge=0,
            le=4294967295,
            title='InstanceLeaf',
        ),
    ] = None
    designated_forwarder_role_last_change: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder-role-last-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Designated-forwarder-role-last-changeLeaf',
        ),
    ] = None
    """
    Indicates the time at which the designated-forwarder role was changed.
    """
    designated_forwarder_activation_start_time: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder-activation-start-time',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Designated-forwarder-activation-start-timeLeaf',
        ),
    ] = None
    """
    Indicates the time at which the designated-forwarder activation timer started.
    """
    designated_forwarder_activation_time: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:designated-forwarder-activation-time',
            ge=0,
            le=4294967295,
            title='Designated-forwarder-activation-timeLeaf',
        ),
    ] = None
    """
    Indicates the number of seconds for the activation timer to run, for this node to become the designated forwarder for this bgp instance.
    """
    computed_designated_forwarder_candidates: Annotated[
        Optional[ComputedDesignatedForwarderCandidatesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:computed-designated-forwarder-candidates'
        ),
    ] = None


class BridgeTableContainer(BaseModel):
    """
    system bridge-table information
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mac_learning: Annotated[
        Optional[MacLearningContainer],
        Field(alias='srl_nokia-system-bridge-table:mac-learning'),
    ] = None
    mac_limit: Annotated[
        Optional[MacLimitContainer],
        Field(alias='srl_nokia-system-bridge-table:mac-limit'),
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer5],
        Field(alias='srl_nokia-system-bridge-table:statistics'),
    ] = None
    evpn: Annotated[
        Optional[EvpnContainer2], Field(alias='srl_nokia-system-bridge-table-evpn:evpn')
    ] = None
    proxy_arp: Annotated[
        Optional[ProxyArpContainer],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:proxy-arp'),
    ] = None
    proxy_nd: Annotated[
        Optional[ProxyNdContainer],
        Field(alias='srl_nokia-system-bridge-table-proxy-arp:proxy-nd'),
    ] = None


class ConfigurationContainer(BaseModel):
    """
    Top-level container for configuration and state data related to the system configuration
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    last_change: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-configuration:last-change',
            pattern='^(?=^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})$).*$',
            title='Last-changeLeaf',
        ),
    ] = None
    """
    Date and time of the last successful commit

    Set to the time the configuration was loaded by management server, so is refreshed at boot time.
    """
    max_checkpoints: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-configuration:max-checkpoints',
            ge=1,
            le=255,
            title='Max-checkpointsLeaf',
        ),
    ] = 10
    """
    The number of checkpoints kept by the system
    """
    max_candidates: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-configuration:max-candidates',
            ge=1,
            le=255,
            title='Max-candidatesLeaf',
        ),
    ] = 10
    """
    The maximum number of combined private and shared candidates
    """
    idle_timeout: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-configuration:idle-timeout',
            ge=0,
            le=65535,
            title='Idle-timeoutLeaf2',
        ),
    ] = 10080
    """
    The idle timeout of configuration candidates

    After this period of no activity, the candidate is emptied and removed from the system.
    """
    auto_checkpoint: Annotated[
        Optional[bool],
        Field(
            alias='srl_nokia-configuration:auto-checkpoint', title='Auto-checkpointLeaf'
        ),
    ] = False
    """
    Configuration checkpoint will be automatically created after every successful commit (if set to true).
    """
    auto_save: Annotated[
        Optional[bool],
        Field(alias='srl_nokia-configuration:auto-save', title='Auto-saveLeaf'),
    ] = False
    """
    Configuration save will be automatically done after every successful commit (if set to true).
    """
    checkpoint: Annotated[
        Optional[List[CheckpointListEntry]],
        Field(alias='srl_nokia-configuration:checkpoint'),
    ] = None
    session: Annotated[
        Optional[List[SessionListEntry3]],
        Field(alias='srl_nokia-configuration:session'),
    ] = None
    candidate: Annotated[
        Optional[List[CandidateListEntry]],
        Field(alias='srl_nokia-configuration:candidate'),
    ] = None
    commit: Annotated[
        Optional[List[CommitListEntry]], Field(alias='srl_nokia-configuration:commit')
    ] = None
    pathz: Annotated[
        Optional[PathzContainer2], Field(alias='srl_nokia-configuration:pathz')
    ] = None
    role: Annotated[
        Optional[List[RoleListEntry2]], Field(alias='srl_nokia-configuration-role:role')
    ] = None


class DhcpServerContainer(BaseModel):
    """
    Configures the dhcp server
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-dhcp-server:admin-state', title='Admin-stateLeaf19'),
    ] = 'disable'
    """
    Globally enable or disable the dhcp server
    Disabling this will disable all dhcp servers.
    """
    network_instance: Annotated[
        Optional[List[NetworkInstanceListEntry2]],
        Field(alias='srl_nokia-dhcp-server:network-instance'),
    ] = None


class FreqReferencesContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance: Annotated[
        Optional[List[InstanceListEntry2]], Field(alias='srl_nokia-sync:instance')
    ] = None


class InstanceListEntry3(BaseModel):
    """
    List of one or more PTP instances in the product (PTP Node)

    Each PTP instance represents a distinct instance of PTP
    implementation (i.e. distinct Ordinary Clock, Boundary Clock,
    or Transparent Clock), maintaining a distinct time.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    instance_index: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-sync:instance-index',
            ge=1,
            le=2,
            title='Instance-indexLeaf',
        ),
    ] = None
    """
    The instance index of the current PTP instance

    This instance index is used for management purposes
    only.  This instance index does not represent the PTP
    domain number and is not used in PTP messages.
    """
    default_ds: Annotated[
        Optional[DefaultDsContainer], Field(alias='srl_nokia-sync:default-ds')
    ] = None
    current_ds: Annotated[
        Optional[CurrentDsContainer], Field(alias='srl_nokia-sync:current-ds')
    ] = None
    parent_ds: Annotated[
        Optional[ParentDsContainer], Field(alias='srl_nokia-sync:parent-ds')
    ] = None
    time_properties_ds: Annotated[
        Optional[TimePropertiesDsContainer],
        Field(alias='srl_nokia-sync:time-properties-ds'),
    ] = None
    port_ds_interface_list: Annotated[
        Optional[List[PortDsInterfaceListListEntry]],
        Field(alias='srl_nokia-sync:port-ds-interface-list'),
    ] = None
    port_ds_cfg_ip_list: Annotated[
        Optional[List[PortDsCfgIpListListEntry]],
        Field(alias='srl_nokia-sync:port-ds-cfg-ip-list'),
    ] = None
    port_ds_dsc_ip_list: Annotated[
        Optional[List[PortDsDscIpListListEntry]],
        Field(alias='srl_nokia-sync:port-ds-dsc-ip-list'),
    ] = None
    port_ds_gnss: Annotated[
        Optional[PortDsGnssContainer], Field(alias='srl_nokia-sync:port-ds-gnss')
    ] = None


class MirrorDestinationContainer(BaseModel):
    """
    Configure mirror destination
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    local: Annotated[
        Optional[str], Field(alias='srl_nokia-mirroring:local', title='LocalLeaf')
    ] = None
    """
    subinterface of type local-mirror-dest used as local mirror destination
    """
    remote: Annotated[
        Optional[RemoteContainer], Field(alias='srl_nokia-mirroring:remote')
    ] = None
    statistics: Annotated[
        Optional[StatisticsContainer4], Field(alias='srl_nokia-mirroring:statistics')
    ] = None


class MirroringInstanceListEntry(BaseModel):
    """
    Mirroring instances configured on the local system
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-mirroring:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf15',
        ),
    ] = None
    """
    A unique name identifying the mirroring instance
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(alias='srl_nokia-mirroring:admin-state', title='Admin-stateLeaf7'),
    ] = 'enable'
    """
    This leaf contains the configured, desired state of the mirroring instance.
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(alias='srl_nokia-mirroring:oper-state', title='Oper-stateLeaf6'),
    ] = None
    """
    This leaf contains the operational state of the mirroring instance.
    """
    description: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-mirroring:description',
            max_length=255,
            min_length=1,
            title='DescriptionLeaf2',
        ),
    ] = None
    """
    A user-entered description of this mirroring instance.
    """
    oper_down_reason: Annotated[
        Optional[EnumerationEnum25],
        Field(
            alias='srl_nokia-mirroring:oper-down-reason', title='Oper-down-reasonLeaf'
        ),
    ] = None
    """
    The reason for the mirroring instance being operational down
    """
    mirror_source: Annotated[
        Optional[MirrorSourceContainer],
        Field(alias='srl_nokia-mirroring:mirror-source'),
    ] = None
    mirror_destination: Annotated[
        Optional[MirrorDestinationContainer],
        Field(alias='srl_nokia-mirroring:mirror-destination'),
    ] = None


class MirroringContainer(BaseModel):
    """
    Top level container for configuration and operational state for mirroring
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    mirroring_instance: Annotated[
        Optional[List[MirroringInstanceListEntry]],
        Field(alias='srl_nokia-mirroring:mirroring-instance'),
    ] = None


class NetworkInstanceListEntry(BaseModel):
    """
    network instance associated to this ethernet-segment
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:name',
            title='NameLeaf22',
        ),
    ] = None
    bgp_instance: Annotated[
        Optional[List[BgpInstanceListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:bgp-instance'
        ),
    ] = None


class PtpContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ptp_profile: Annotated[
        Optional[EnumerationEnum75],
        Field(alias='srl_nokia-sync:ptp-profile', title='Ptp-profileLeaf'),
    ] = 'itug8275dot1'
    """
    Specifies the PTP profile mode for the PTP clock
    """
    timing_source_net_inst: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-sync:timing-source-net-inst',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,_:;?-]*$).*$',
            title='Timing-source-net-instLeaf',
        ),
    ] = None
    """
    Network instance to be used for configured peers

    This is the network instance that will be used to provide timing into the local clock via PTP over IP.
    """
    instance: Annotated[
        Optional[List[InstanceListEntry3]], Field(alias='srl_nokia-sync:instance')
    ] = None


class SyncContainer(BaseModel):
    """
    Context to configure sync parameters and report sessions state
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    freq_references: Annotated[
        Optional[FreqReferencesContainer], Field(alias='srl_nokia-sync:freq-references')
    ] = None
    freq_clock: Annotated[
        Optional[FreqClockContainer], Field(alias='srl_nokia-sync:freq-clock')
    ] = None
    ptp: Annotated[Optional[PtpContainer2], Field(alias='srl_nokia-sync:ptp')] = None
    gnss: Annotated[Optional[GnssContainer2], Field(alias='srl_nokia-sync:gnss')] = None
    one_pps: Annotated[
        Optional[OnePpsContainer], Field(alias='srl_nokia-sync:one-pps')
    ] = None


class AssociationContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    network_instance: Annotated[
        Optional[List[NetworkInstanceListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:network-instance'
        ),
    ] = None


class EthernetSegmentListEntry(BaseModel):
    """
    Ethernet Segment configuration and state.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    name: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:name',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
            title='NameLeaf20',
        ),
    ] = None
    """
    A unique name identifying the ethernet segment.
    """
    type: Annotated[
        Optional[EnumerationEnum32],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:type',
            title='TypeLeaf9',
        ),
    ] = 'none'
    """
    Ethernet Segment type.
    """
    admin_state: Annotated[
        Optional[EnumerationEnum2],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:admin-state',
            title='Admin-stateLeaf10',
        ),
    ] = 'disable'
    """
    Admin state of the ethernet segment
    """
    oper_state: Annotated[
        Optional[EnumerationEnum3],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-state',
            title='Oper-stateLeaf9',
        ),
    ] = None
    """
    This leaf contains the operational state of ethernet segment.
    """
    esi: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:esi',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){9}$).*$',
            title='EsiLeaf',
        ),
    ] = None
    """
    The 10-byte Ethernet Segment Identifier of the ethernet segment.

    ESI-0 or MAX-ESI values are not allowed.
    ESI values with bytes 1-6 all zeros are not allowed since they would produce a null ESI-import route-target.
    """
    oper_esi: Annotated[
        Optional[str],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-esi',
            pattern='^(?=^[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){9}$).*$',
            title='Oper-esiLeaf',
        ),
    ] = None
    """
    The operational Ethernet Segment Identifier used in the ethernet segment.
    """
    esi_label: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:esi-label',
            ge=16,
            le=1048575,
            title='Esi-labelLeaf',
        ),
    ] = None
    """
    The esi label allocated for this ethernet-segment.

    The esi-label is advertised by the EVPN Auto-Discovery-Ethernet-Segment
    Advertisement routes and it is expected on received EVPN packets
    that were generated as multicast packets from this ethernet-segments peers.
    """
    interface_association: Annotated[
        Optional[Union[Layer2InterfaceCase, Layer3NextHopCase]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:interface-association'
        ),
    ] = None
    multi_homing_mode: Annotated[
        Optional[EnumerationEnum33],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:multi-homing-mode',
            title='Multi-homing-modeLeaf',
        ),
    ] = 'all-active'
    """
    Multi-homing mode of the ethernet segment.

    The state of this leaf can be different than the configured value in cases where the configured value is 'all-active' and the
    multi-homing mode advertised by the ES peers in the AD per-ES routes is 'single-active'. In this case, the state of this
    leaf will show 'single-active'.
    """
    oper_multi_homing_mode: Annotated[
        Optional[EnumerationEnum33],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-multi-homing-mode',
            title='Oper-multi-homing-modeLeaf',
        ),
    ] = None
    """
    Operational Multi-homing mode of the ethernet segment.

    The state of this leaf can be different than the configured value in cases where the configured value is 'all-active' and the
    multi-homing mode advertised by the ES peers in the AD per-ES routes is 'single-active'. In this case, the state of this leaf
    will show 'single-active'.
    """
    df_election: Annotated[
        Optional[DfElectionContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:df-election'
        ),
    ] = None
    routes: Annotated[
        Optional[RoutesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:routes'
        ),
    ] = None
    autodiscovery_per_ethernet_segment_routes: Annotated[
        Optional[AutodiscoveryPerEthernetSegmentRoutesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:autodiscovery-per-ethernet-segment-routes'
        ),
    ] = None
    ethernet_segment_routes: Annotated[
        Optional[EthernetSegmentRoutesContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-segment-routes'
        ),
    ] = None
    oper_down_reason: Annotated[
        Optional[EnumerationEnum39],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:oper-down-reason',
            title='Oper-down-reasonLeaf3',
        ),
    ] = None
    """
    The reason for the ethernet-segment being down in the bgp-instance
    """
    association: Annotated[
        Optional[AssociationContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:association'
        ),
    ] = None


class BgpInstanceListEntry2(BaseModel):
    """
    bgp global instances configured in net-instance
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    id: Annotated[
        Optional[int],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:id',
            ge=1,
            le=2,
            title='IdLeaf6',
        ),
    ] = None
    """
    The index of the bgp-vpn instance
    """
    ethernet_segment: Annotated[
        Optional[List[EthernetSegmentListEntry]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-segment'
        ),
    ] = None


class EthernetSegmentsContainer(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    timers: Annotated[
        Optional[TimersContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:timers'
        ),
    ] = None
    bgp_instance: Annotated[
        Optional[List[BgpInstanceListEntry2]],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:bgp-instance'
        ),
    ] = None


class EvpnContainer3(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    ethernet_segments: Annotated[
        Optional[EthernetSegmentsContainer],
        Field(
            alias='srl_nokia-system-network-instance-bgp-evpn-ethernet-segments:ethernet-segments'
        ),
    ] = None
    multicast: Annotated[
        Optional[MulticastContainer],
        Field(alias='srl_nokia-system-network-instance-bgp-evpn-multicast:multicast'),
    ] = None


class ProtocolsContainer2(BaseModel):
    """
    The routing protocols that are enabled for this
    network-instance.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    evpn: Annotated[
        Optional[EvpnContainer3], Field(alias='srl_nokia-system-network-instance:evpn')
    ] = None
    bgp_vpn: Annotated[
        Optional[BgpVpnContainer],
        Field(alias='srl_nokia-system-network-instance-bgp-vpn:bgp-vpn'),
    ] = None


class NetworkInstanceContainer2(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    protocols: Annotated[
        Optional[ProtocolsContainer2],
        Field(alias='srl_nokia-system-network-instance:protocols'),
    ] = None


class SystemContainer(BaseModel):
    """
    Enclosing container for system management
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    features: Annotated[
        Optional[List[str]],
        Field(
            alias='srl_nokia-system:features',
            pattern='^(?=^[A-Za-z0-9!@#$%^&()|+=`~.,/_:;?-][A-Za-z0-9 !@#$%^&()|+=`~.,/_:;?-]*$).*$',
        ),
    ] = []
    """
    Features enabled on this platform
    """
    trace_options: Annotated[
        Optional[List[EnumerationEnum]], Field(alias='srl_nokia-system:trace-options')
    ] = []
    """
    Management server trace options
    """
    management: Annotated[
        Optional[ManagementContainer], Field(alias='srl_nokia-system:management')
    ] = None
    control_plane_traffic: Annotated[
        Optional[ControlPlaneTrafficContainer],
        Field(alias='srl_nokia-system:control-plane-traffic'),
    ] = None
    dot1x: Annotated[Optional[Dot1xContainer], Field(alias='srl_nokia-dot1x:dot1x')] = (
        None
    )
    ssh_server: Annotated[
        Optional[List[SshServerListEntry]], Field(alias='srl_nokia-ssh:ssh-server')
    ] = None
    tls: Annotated[Optional[TlsContainer], Field(alias='srl_nokia-tls:tls')] = None
    aaa: Annotated[Optional[AaaContainer], Field(alias='srl_nokia-aaa:aaa')] = None
    grpc_server: Annotated[
        Optional[List[GrpcServerListEntry]], Field(alias='srl_nokia-grpc:grpc-server')
    ] = None
    mpls: Annotated[
        Optional[MplsContainer], Field(alias='srl_nokia-mpls-label-management:mpls')
    ] = None
    protocols: Annotated[
        Optional[ProtocolsContainer],
        Field(alias='srl_nokia-system-protocols:protocols'),
    ] = None
    authentication: Annotated[
        Optional[AuthenticationContainer2],
        Field(alias='srl_nokia-keychains:authentication'),
    ] = None
    dns: Annotated[Optional[DnsContainer], Field(alias='srl_nokia-dns:dns')] = None
    mirroring: Annotated[
        Optional[MirroringContainer], Field(alias='srl_nokia-mirroring:mirroring')
    ] = None
    datapath: Annotated[
        Optional[DatapathContainer], Field(alias='srl_nokia-system-datapath:datapath')
    ] = None
    bridge_table: Annotated[
        Optional[BridgeTableContainer],
        Field(alias='srl_nokia-system-bridge-table:bridge-table'),
    ] = None
    name: Annotated[
        Optional[NameContainer], Field(alias='srl_nokia-system-name:name')
    ] = None
    license: Annotated[
        Optional[List[LicenseListEntry]], Field(alias='srl_nokia-license:license')
    ] = None
    network_instance: Annotated[
        Optional[NetworkInstanceContainer2],
        Field(alias='srl_nokia-system-network-instance:network-instance'),
    ] = None
    netconf_server: Annotated[
        Optional[List[NetconfServerListEntry]],
        Field(alias='srl_nokia-netconf-server:netconf-server'),
    ] = None
    event_handler: Annotated[
        Optional[EventHandlerContainer],
        Field(alias='srl_nokia-event-handler:event-handler'),
    ] = None
    lldp: Annotated[Optional[LldpContainer], Field(alias='srl_nokia-lldp:lldp')] = None
    boot: Annotated[Optional[BootContainer], Field(alias='srl_nokia-boot:boot')] = None
    configuration: Annotated[
        Optional[ConfigurationContainer],
        Field(alias='srl_nokia-configuration:configuration'),
    ] = None
    ra_guard_policy: Annotated[
        Optional[List[RaGuardPolicyListEntry]],
        Field(alias='srl_nokia-ra_guard:ra-guard-policy'),
    ] = None
    app_management: Annotated[
        Optional[AppManagementContainer],
        Field(alias='srl_nokia-app-mgmt:app-management'),
    ] = None
    dhcp_server: Annotated[
        Optional[DhcpServerContainer], Field(alias='srl_nokia-dhcp-server:dhcp-server')
    ] = None
    packet_link_qualification: Annotated[
        Optional[PacketLinkQualificationContainer],
        Field(alias='srl_nokia-packet-link-qual:packet-link-qualification'),
    ] = None
    json_rpc_server: Annotated[
        Optional[JsonRpcServerContainer],
        Field(alias='srl_nokia-json-rpc:json-rpc-server'),
    ] = None
    banner: Annotated[
        Optional[BannerContainer], Field(alias='srl_nokia-system-banner:banner')
    ] = None
    information: Annotated[
        Optional[InformationContainer], Field(alias='srl_nokia-system-info:information')
    ] = None
    utilization: Annotated[
        Optional[UtilizationContainer],
        Field(alias='srl_nokia-system-utilization:utilization'),
    ] = None
    maintenance: Annotated[
        Optional[MaintenanceContainer],
        Field(alias='srl_nokia-maintenance-mode:maintenance'),
    ] = None
    multicast_forwarding_information_base: Annotated[
        Optional[MulticastForwardingInformationBaseContainer],
        Field(
            alias='srl_nokia-system-multicast-mfib-table:multicast-forwarding-information-base'
        ),
    ] = None
    multicast: Annotated[
        Optional[MulticastContainer2],
        Field(alias='srl_nokia-system-multicast:multicast'),
    ] = None
    ntp: Annotated[Optional[NtpContainer2], Field(alias='srl_nokia-ntp:ntp')] = None
    clock: Annotated[Optional[ClockContainer], Field(alias='srl_nokia-ntp:clock')] = (
        None
    )
    lawful_intercept: Annotated[
        Optional[LawfulInterceptContainer],
        Field(alias='srl_nokia-lawful-intercept:lawful-intercept'),
    ] = None
    mtu: Annotated[Optional[MtuContainer], Field(alias='srl_nokia-mtu:mtu')] = None
    sync: Annotated[Optional[SyncContainer], Field(alias='srl_nokia-sync:sync')] = None
    lacp: Annotated[Optional[LacpContainer], Field(alias='srl_nokia-lacp:lacp')] = None
    l2cp_transparency: Annotated[
        Optional[L2cpTransparencyContainer],
        Field(alias='srl_nokia-interfaces-l2cp:l2cp-transparency'),
    ] = None


class Model(BaseModel):
    """
    Initialize an instance of this class and serialize it to JSON; this results in a RESTCONF payload.

    ## Tips
    Initialization:
    - all values have to be set via keyword arguments
    - if a class contains only a `root` field, it can be initialized as follows:
        - `member=MyNode(root=<value>)`
        - `member=<value>`

    Serialziation:
    - `exclude_defaults=True` omits fields set to their default value (recommended)
    - `by_alias=True` ensures qualified names are used (necessary)
    """

    model_config = ConfigDict(
        populate_by_name=True,
        regex_engine="python-re",
    )
    system: Annotated[
        Optional[SystemContainer], Field(alias='srl_nokia-system:system')
    ] = None


if __name__ == "__main__":
    model = Model(
        # <Initialize model here>
    )

    restconf_payload = model.model_dump_json(
        exclude_defaults=True, by_alias=True, indent=2
    )

    print(f"Generated output: {restconf_payload}")

    # Send config to network device:
    # from pydantify.utility import restconf_patch_request
    # restconf_patch_request(url='...', user_pw_auth=('usr', 'pw'), data=restconf_payload)