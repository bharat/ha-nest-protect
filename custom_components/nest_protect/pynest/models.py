"""Models used by PyNest."""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class NestLimits:
    """Nest Limits."""

    thermostats_per_structure: int
    structures: int
    smoke_detectors_per_structure: int
    smoke_detectors: int
    thermostats: int


@dataclass
class NestUrls:
    """Nest Urls."""

    rubyapi_url: str
    czfe_url: str
    log_upload_url: str
    transport_url: str
    weather_url: str
    support_url: str
    direct_transport_url: str


@dataclass
class NestResponse:
    """Class that reflects a Nest API response."""

    access_token: float
    email: str
    expires_in: str
    userid: str
    is_superuser: bool
    language: str
    weave: dict[str, str]
    user: str
    is_staff: bool
    urls: NestUrls = field(default_factory=NestUrls)
    limits: NestLimits = field(default_factory=NestLimits)

    _2fa_state: str = None
    _2fa_enabled: bool = None
    _2fa_state_changed: str = None

    # field(repr=bool, default=None)

    # field(default_factory=lambda: [CalendarSlot])


@dataclass
class Bucket:
    """Class that reflects a Nest API response."""

    object_key: str
    object_revision: str
    object_timestamp: str
    value: Any


@dataclass
class WhereBucket(Bucket):
    """Class that reflects a Nest API response."""

    object_key: str
    object_revision: str
    object_timestamp: str
    value: Any


@dataclass
class TopazBucketValue:
    """Nest Protect values."""

    spoken_where_id: str
    creation_time: int
    installed_locale: str
    ntp_green_led_brightness: int
    component_buzzer_test_passed: bool
    wifi_ip_address: str
    wired_led_enable: bool
    wifi_regulatory_domain: str
    co_blame_duration: int
    is_rcs_capable: bool
    fabric_id: str
    battery_health_state: int
    steam_detection_enable: bool
    hushed_state: bool
    capability_level: float
    home_alarm_link_type: int
    model: str
    component_smoke_test_passed: bool
    component_speaker_test_passed: bool
    removed_from_base: bool
    smoke_sequence_number: int
    home_away_input: bool
    device_locale: str
    co_blame_threshold: int
    kl_software_version: str
    component_us_test_passed: bool
    auto_away: bool
    night_light_enable: bool
    component_als_test_passed: bool
    speaker_test_results: 32768
    wired_or_battery: int
    is_rcs_used: bool
    replace_by_date_utc_secs: int
    certification_body: 2
    component_pir_test_passed: bool
    structure_id: str
    software_version: str
    component_hum_test_passed: bool
    home_alarm_link_capable: bool
    night_light_brightness: int
    device_external_color: str
    latest_manual_test_end_utc_secs: int
    smoke_status: int
    latest_manual_test_start_utc_secs: int
    component_temp_test_passed: bool
    home_alarm_link_connected: bool
    co_status: int
    heat_status: int
    product_id: int
    night_light_continuous: bool
    co_previous_peak: int
    auto_away_decision_time_secs: int
    component_co_test_passed: bool
    where_id: str
    serial_number: str
    component_heat_test_passed: bool
    latest_manual_test_cancelled: bool
    thread_mac_address: str
    resource_id: str
    buzzer_test_results: int
    wifi_mac_address: str
    line_power_present: bool
    gesture_hush_enable: bool
    device_born_on_date_utc_secs: int
    ntp_green_led_enable: bool
    component_led_test_passed: bool
    co_sequence_number: int
    thread_ip_address: list[str]
    component_wifi_test_passed: bool
    heads_up_enable: bool
    battery_level: int


@dataclass
class TopazBucket(Bucket):
    """Class that reflects a Nest API response."""

    value: TopazBucketValue = field(default_factory=TopazBucketValue)