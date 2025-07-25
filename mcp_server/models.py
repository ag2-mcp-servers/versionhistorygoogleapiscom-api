# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:05:41+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class ChannelType(Enum):
    CHANNEL_TYPE_UNSPECIFIED = 'CHANNEL_TYPE_UNSPECIFIED'
    STABLE = 'STABLE'
    BETA = 'BETA'
    DEV = 'DEV'
    CANARY = 'CANARY'
    CANARY_ASAN = 'CANARY_ASAN'
    ALL = 'ALL'
    EXTENDED = 'EXTENDED'


class Channel(BaseModel):
    channelType: Optional[ChannelType] = Field(None, description='Type of channel.')
    name: Optional[str] = Field(
        None,
        description='Channel name. Format is "{product}/platforms/{platform}/channels/{channel}"',
    )


class Interval(BaseModel):
    endTime: Optional[str] = Field(
        None,
        description='Optional. Exclusive end of the interval. If specified, a Timestamp matching this interval will have to be before the end.',
    )
    startTime: Optional[str] = Field(
        None,
        description='Optional. Inclusive start of the interval. If specified, a Timestamp matching this interval will have to be the same or after the start.',
    )


class ListChannelsResponse(BaseModel):
    channels: Optional[List[Channel]] = Field(None, description='The list of channels.')
    nextPageToken: Optional[str] = Field(
        None,
        description='A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )


class PlatformType(Enum):
    PLATFORM_TYPE_UNSPECIFIED = 'PLATFORM_TYPE_UNSPECIFIED'
    WIN = 'WIN'
    WIN64 = 'WIN64'
    MAC = 'MAC'
    LINUX = 'LINUX'
    ANDROID = 'ANDROID'
    WEBVIEW = 'WEBVIEW'
    IOS = 'IOS'
    ALL = 'ALL'
    MAC_ARM64 = 'MAC_ARM64'
    LACROS = 'LACROS'
    LACROS_ARM32 = 'LACROS_ARM32'
    CHROMEOS = 'CHROMEOS'
    LACROS_ARM64 = 'LACROS_ARM64'
    FUCHSIA = 'FUCHSIA'


class Platform(BaseModel):
    name: Optional[str] = Field(
        None, description='Platform name. Format is "{product}/platforms/{platform}"'
    )
    platformType: Optional[PlatformType] = Field(None, description='Type of platform.')


class Release(BaseModel):
    fraction: Optional[float] = Field(
        None,
        description='Rollout fraction. This fraction indicates the fraction of people that should receive this version in this release. If the fraction is not specified in ReleaseManager, the API will assume fraction is 1.',
    )
    fractionGroup: Optional[str] = Field(
        None,
        description='Rollout fraction group. Only fractions with the same fraction_group are statistically comparable: there may be non-fractional differences between different fraction groups.',
    )
    name: Optional[str] = Field(
        None,
        description='Release name. Format is "{product}/platforms/{platform}/channels/{channel}/versions/{version}/releases/{release}"',
    )
    serving: Optional[Interval] = Field(
        None,
        description='Timestamp interval of when the release was live. If end_time is unspecified, the release is currently live.',
    )
    version: Optional[str] = Field(
        None,
        description='String containing just the version number. e.g. "84.0.4147.38"',
    )


class Version(BaseModel):
    name: Optional[str] = Field(
        None,
        description='Version name. Format is "{product}/platforms/{platform}/channels/{channel}/versions/{version}" e.g. "chrome/platforms/win/channels/beta/versions/84.0.4147.38"',
    )
    version: Optional[str] = Field(
        None,
        description='String containing just the version number. e.g. "84.0.4147.38"',
    )


class FieldXgafv(Enum):
    field_1 = '1'
    field_2 = '2'


class Alt(Enum):
    json = 'json'
    media = 'media'
    proto = 'proto'


class ListPlatformsResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )
    platforms: Optional[List[Platform]] = Field(
        None, description='The list of platforms.'
    )


class ListReleasesResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )
    releases: Optional[List[Release]] = Field(None, description='The list of releases.')


class ListVersionsResponse(BaseModel):
    nextPageToken: Optional[str] = Field(
        None,
        description='A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.',
    )
    versions: Optional[List[Version]] = Field(None, description='The list of versions.')
