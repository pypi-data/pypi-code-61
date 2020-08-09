# -*- coding: utf-8 -*-
# cython: language_level=3
# Copyright (c) 2020 Nekokatt
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Application and entities that are used to describe audit logs on Discord."""

from __future__ import annotations

__all__: typing.Final[typing.List[str]] = [
    "AuditLog",
    "AuditLogChange",
    "AuditLogChangeKey",
    "AuditLogEntry",
    "AuditLogEventType",
    "BaseAuditLogEntryInfo",
    "ChannelOverwriteEntryInfo",
    "MemberDisconnectEntryInfo",
    "MemberMoveEntryInfo",
    "MemberPruneEntryInfo",
    "MessageBulkDeleteEntryInfo",
    "MessageDeleteEntryInfo",
    "MessagePinEntryInfo",
    "UnrecognisedAuditLogEntryInfo",
]

import abc
import datetime
import enum
import itertools
import typing

import attr

from hikari.utilities import attr_extensions
from hikari.utilities import snowflake

if typing.TYPE_CHECKING:
    from hikari.api import rest as rest_app
    from hikari.models import channels
    from hikari.models import guilds
    from hikari.models import users as users_
    from hikari.models import webhooks as webhooks_


@typing.final
class AuditLogChangeKey(str, enum.Enum):
    """Commonly known and documented keys for audit log change objects.

    Others may exist. These should be expected to default to the raw string
    Discord provided us. These are defined for documentation purposes and
    can be treated as regular strings for all other purposes.
    """

    NAME = "name"
    ICON_HASH = "icon_hash"
    SPLASH_HASH = "splash_hash"
    OWNER_ID = "owner_id"
    REGION = "region"
    AFK_CHANNEL_ID = "afk_channel_id"
    AFK_TIMEOUT = "afk_timeout"
    MFA_LEVEL = "mfa_level"
    VERIFICATION_LEVEL = "verification"
    EXPLICIT_CONTENT_FILTER = "explicit_content_filter"
    DEFAULT_MESSAGE_NOTIFICATIONS = "notifications"
    VANITY_URL_CODE = "vanity_url_code"
    PRUNE_DELETE_DAYS = "prune_delete_days"
    WIDGET_ENABLED = "widget_enabled"
    WIDGET_CHANNEL_ID = "widget_channel_id"
    POSITION = "position"
    TOPIC = "topic"
    BITRATE = "bitrate"
    PERMISSION_OVERWRITES = "permission_overwrites"
    NSFW = "nsfw"
    APPLICATION_ID = "application_id"
    PERMISSIONS = "permissions"
    COLOR = "color"
    HOIST = "hoist"
    MENTIONABLE = "mentionable"
    ALLOW = "allow"
    DENY = "deny"
    INVITE_CODE = "code"
    CHANNEL_ID = "channel"
    INVITER_ID = "inviter_id"
    MAX_USES = "max_uses"
    USES = "uses"
    MAX_AGE = "max_age"
    TEMPORARY = "temporary"
    DEAF = "deaf"
    MUTE = "mute"
    NICK = "nick"
    AVATAR_HASH = "avatar_hash"
    ID = "id"
    TYPE = "type"
    ENABLE_EMOTICONS = "enable_emoticons"
    EXPIRE_BEHAVIOR = "expire_behavior"
    EXPIRE_GRACE_PERIOD = "expire_grace_period"
    RATE_LIMIT_PER_USER = "rate_limit_per_user"
    SYSTEM_CHANNEL_ID = "system_channel_id"

    # Who needs consistency?
    ADD_ROLE_TO_MEMBER = "$add"
    REMOVE_ROLE_FROM_MEMBER = "$remove"

    COLOUR = COLOR
    """Alias for "COLOR"""

    def __str__(self) -> str:
        return self.name

    __repr__ = __str__


@attr_extensions.with_copy
@attr.s(eq=True, hash=False, init=True, kw_only=True, slots=True, weakref_slot=False)
class AuditLogChange:
    """Represents a change made to an audit log entry's target entity."""

    new_value: typing.Optional[typing.Any] = attr.ib(repr=True)
    """The new value of the key, if something was added or changed."""

    old_value: typing.Optional[typing.Any] = attr.ib(repr=True)
    """The old value of the key, if something was removed or changed."""

    key: typing.Union[AuditLogChangeKey, str] = attr.ib(repr=True)
    """The name of the audit log change's key."""


@enum.unique
@typing.final
class AuditLogEventType(enum.IntEnum):
    """The type of event that occurred."""

    GUILD_UPDATE = 1
    CHANNEL_CREATE = 10
    CHANNEL_UPDATE = 11
    CHANNEL_DELETE = 12
    CHANNEL_OVERWRITE_CREATE = 13
    CHANNEL_OVERWRITE_UPDATE = 14
    CHANNEL_OVERWRITE_DELETE = 15
    MEMBER_KICK = 20
    MEMBER_PRUNE = 21
    MEMBER_BAN_ADD = 22
    MEMBER_BAN_REMOVE = 23
    MEMBER_UPDATE = 24
    MEMBER_ROLE_UPDATE = 25
    MEMBER_MOVE = 26
    MEMBER_DISCONNECT = 27
    BOT_ADD = 28
    ROLE_CREATE = 30
    ROLE_UPDATE = 31
    ROLE_DELETE = 32
    INVITE_CREATE = 40
    INVITE_UPDATE = 41
    INVITE_DELETE = 42
    WEBHOOK_CREATE = 50
    WEBHOOK_UPDATE = 51
    WEBHOOK_DELETE = 52
    EMOJI_CREATE = 60
    EMOJI_UPDATE = 61
    EMOJI_DELETE = 62
    MESSAGE_DELETE = 72
    MESSAGE_BULK_DELETE = 73
    MESSAGE_PIN = 74
    MESSAGE_UNPIN = 75
    INTEGRATION_CREATE = 80
    INTEGRATION_UPDATE = 81
    INTEGRATION_DELETE = 82

    def __str__(self) -> str:
        return self.name


@attr.s(eq=True, hash=False, init=True, kw_only=True, slots=True, weakref_slot=False)
class BaseAuditLogEntryInfo(abc.ABC):
    """A base object that all audit log entry info objects will inherit from."""


@attr_extensions.with_copy
@attr.s(eq=True, hash=False, init=True, kw_only=True, slots=True, weakref_slot=False)
class ChannelOverwriteEntryInfo(BaseAuditLogEntryInfo, snowflake.Unique):
    """Represents the extra information for overwrite related audit log entries.

    Will be attached to the overwrite create, update and delete audit log
    entries.
    """

    id: snowflake.Snowflake = attr.ib(eq=True, hash=True, repr=True)
    """The ID of this entity."""

    type: channels.PermissionOverwriteType = attr.ib(repr=True)
    """The type of entity this overwrite targets."""

    role_name: typing.Optional[str] = attr.ib(repr=True)
    """The name of the role this overwrite targets, if it targets a role."""


@attr_extensions.with_copy
@attr.s(eq=True, hash=False, init=True, kw_only=True, slots=True, weakref_slot=False)
class MessagePinEntryInfo(BaseAuditLogEntryInfo):
    """The extra information for message pin related audit log entries.

    Will be attached to the message pin and message unpin audit log entries.
    """

    channel_id: snowflake.Snowflake = attr.ib(repr=True)
    """The ID of the text based channel where a pinned message is being targeted."""

    message_id: snowflake.Snowflake = attr.ib(repr=True)
    """The ID of the message that's being pinned or unpinned."""


@attr_extensions.with_copy
@attr.s(eq=True, hash=False, init=True, kw_only=True, slots=True, weakref_slot=False)
class MemberPruneEntryInfo(BaseAuditLogEntryInfo):
    """Extra information attached to guild prune log entries."""

    delete_member_days: datetime.timedelta = attr.ib(repr=True)
    """The timedelta of how many days members were pruned for inactivity based on."""

    members_removed: int = attr.ib(repr=True)
    """The number of members who were removed by this prune."""


@attr_extensions.with_copy
@attr.s(eq=True, hash=False, init=True, kw_only=True, slots=True, weakref_slot=False)
class MessageBulkDeleteEntryInfo(BaseAuditLogEntryInfo):
    """Extra information for the message bulk delete audit entry."""

    count: int = attr.ib(repr=True)
    """The amount of messages that were deleted."""


@attr.s(eq=True, hash=False, init=True, kw_only=True, slots=True, weakref_slot=False)
class MessageDeleteEntryInfo(MessageBulkDeleteEntryInfo):
    """Extra information attached to the message delete audit entry."""

    channel_id: snowflake.Snowflake = attr.ib(repr=True)
    """The guild text based channel where these message(s) were deleted."""


@attr_extensions.with_copy
@attr.s(eq=True, hash=False, init=True, kw_only=True, slots=True, weakref_slot=False)
class MemberDisconnectEntryInfo(BaseAuditLogEntryInfo):
    """Extra information for the voice chat member disconnect entry."""

    count: int = attr.ib(repr=True)
    """The amount of members who were disconnected from voice in this entry."""


@attr.s(eq=True, hash=False, init=True, kw_only=True, slots=True, weakref_slot=False)
class MemberMoveEntryInfo(MemberDisconnectEntryInfo):
    """Extra information for the voice chat based member move entry."""

    channel_id: snowflake.Snowflake = attr.ib(repr=True)
    """The amount of members who were disconnected from voice in this entry."""


class UnrecognisedAuditLogEntryInfo(BaseAuditLogEntryInfo):
    """Audit log entry options that haven't been implemented in the library.

    The attributes on this object are undocumented and dynamic.

    Example
    -------
        >>> entry_info.foobar.baz

    !!! note
        This model has no slots and will have arbitrary undocumented attributes
        (in it's `__dict__` based on the received payload).
    """

    def __init__(self, payload: typing.Mapping[str, str]) -> None:
        self.__dict__.update(payload)


@attr_extensions.with_copy
@attr.s(eq=True, hash=True, init=True, kw_only=True, slots=True, weakref_slot=False)
class AuditLogEntry(snowflake.Unique):
    """Represents an entry in a guild's audit log."""

    app: rest_app.IRESTApp = attr.ib(repr=False, eq=False, hash=False, metadata={attr_extensions.SKIP_DEEP_COPY: True})
    """The client application that models may use for procedures."""

    id: snowflake.Snowflake = attr.ib(eq=True, hash=True, repr=True)
    """The ID of this entity."""

    target_id: typing.Optional[snowflake.Snowflake] = attr.ib(eq=False, hash=False, repr=True)
    """The ID of the entity affected by this change, if applicable."""

    changes: typing.Sequence[AuditLogChange] = attr.ib(eq=False, hash=False, repr=False)
    """A sequence of the changes made to `AuditLogEntry.target_id`."""

    user_id: typing.Optional[snowflake.Snowflake] = attr.ib(eq=False, hash=False, repr=True)
    """The ID of the user who made this change."""

    action_type: typing.Union[AuditLogEventType, int] = attr.ib(eq=False, hash=False, repr=True)
    """The type of action this entry represents."""

    options: typing.Optional[BaseAuditLogEntryInfo] = attr.ib(eq=False, hash=False, repr=False)
    """Extra information about this entry. Only be provided for certain `event_type`."""

    reason: typing.Optional[str] = attr.ib(eq=False, hash=False, repr=False)
    """The reason for this change, if set (between 0-512 characters)."""


@attr_extensions.with_copy
@attr.s(eq=True, hash=False, init=True, kw_only=True, repr=False, slots=True, weakref_slot=False)
class AuditLog(typing.Sequence[AuditLogEntry]):
    """Represents a guilds audit log."""

    entries: typing.Mapping[snowflake.Snowflake, AuditLogEntry] = attr.ib(repr=False)
    """A sequence of the audit log's entries."""

    integrations: typing.Mapping[snowflake.Snowflake, guilds.PartialIntegration] = attr.ib(repr=False)
    """A mapping of the partial objects of integrations found in this audit log."""

    users: typing.Mapping[snowflake.Snowflake, users_.User] = attr.ib(repr=False)
    """A mapping of the objects of users found in this audit log."""

    webhooks: typing.Mapping[snowflake.Snowflake, webhooks_.Webhook] = attr.ib(repr=False)
    """A mapping of the objects of webhooks found in this audit log."""

    @typing.overload
    def __getitem__(self, index: int, /) -> AuditLogEntry:
        ...

    @typing.overload
    def __getitem__(self, slice_: slice, /) -> typing.Sequence[AuditLogEntry]:
        ...

    def __getitem__(
        self, index_or_slice: typing.Union[int, slice], /
    ) -> typing.Union[AuditLogEntry, typing.Sequence[AuditLogEntry]]:
        if isinstance(index_or_slice, slice):
            return tuple(
                itertools.islice(self.entries.values(), index_or_slice.start, index_or_slice.stop, index_or_slice.step)
            )
        elif isinstance(index_or_slice, int):
            return next(iter(itertools.islice(self.entries.values(), index_or_slice, None)))
        else:
            raise TypeError(f"sequence indices must be integers or slices, not {type(index_or_slice).__name__}")

    def __iter__(self) -> typing.Iterator[AuditLogEntry]:
        return iter(self.entries.values())

    def __len__(self) -> int:
        return len(self.entries)
