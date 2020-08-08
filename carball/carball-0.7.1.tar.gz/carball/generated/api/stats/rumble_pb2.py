# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/stats/rumble.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/stats/rumble.proto',
  package='api.stats',
  serialized_pb=_b('\n\x16\x61pi/stats/rumble.proto\x12\tapi.stats\"X\n\x0bRumbleStats\x12\x31\n\x0crumble_items\x18\x01 \x03(\x0b\x32\x1b.api.stats.RumbleItemsUsage\x12\x16\n\x0epre_item_goals\x18\x02 \x01(\x05\"h\n\x10RumbleItemsUsage\x12 \n\x04item\x18\x01 \x01(\x0e\x32\x12.api.stats.PowerUp\x12\x0c\n\x04used\x18\x02 \x01(\x05\x12\x0e\n\x06unused\x18\x03 \x01(\x05\x12\x14\n\x0c\x61verage_hold\x18\x04 \x01(\x02*\xd7\x01\n\x07PowerUp\x12\x0f\n\x0b\x42\x41LL_FREEZE\x10\x01\x12\x17\n\x13\x42\x41LL_GRAPPLING_HOOK\x10\x02\x12\x0e\n\nBALL_LASSO\x10\x03\x12\x0c\n\x08\x42\x41TARANG\x10\x03\x12\x0f\n\x0b\x42\x41LL_SPRING\x10\x04\x12\x0f\n\x0b\x42\x41LL_VELCRO\x10\x05\x12\x12\n\x0e\x42OOST_OVERRIDE\x10\x06\x12\x0e\n\nCAR_SPRING\x10\x07\x12\x10\n\x0cGRAVITY_WELL\x10\x08\x12\x0e\n\nSTRONG_HIT\x10\t\x12\x0b\n\x07SWAPPER\x10\n\x12\x0b\n\x07TORNADO\x10\x0b\x1a\x02\x10\x01')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_POWERUP = _descriptor.EnumDescriptor(
  name='PowerUp',
  full_name='api.stats.PowerUp',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BALL_FREEZE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALL_GRAPPLING_HOOK', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALL_LASSO', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BATARANG', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALL_SPRING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BALL_VELCRO', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOST_OVERRIDE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAR_SPRING', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GRAVITY_WELL', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRONG_HIT', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SWAPPER', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TORNADO', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001')),
  serialized_start=234,
  serialized_end=449,
)
_sym_db.RegisterEnumDescriptor(_POWERUP)

PowerUp = enum_type_wrapper.EnumTypeWrapper(_POWERUP)
BALL_FREEZE = 1
BALL_GRAPPLING_HOOK = 2
BALL_LASSO = 3
BATARANG = 3
BALL_SPRING = 4
BALL_VELCRO = 5
BOOST_OVERRIDE = 6
CAR_SPRING = 7
GRAVITY_WELL = 8
STRONG_HIT = 9
SWAPPER = 10
TORNADO = 11



_RUMBLESTATS = _descriptor.Descriptor(
  name='RumbleStats',
  full_name='api.stats.RumbleStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rumble_items', full_name='api.stats.RumbleStats.rumble_items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_item_goals', full_name='api.stats.RumbleStats.pre_item_goals', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=125,
)


_RUMBLEITEMSUSAGE = _descriptor.Descriptor(
  name='RumbleItemsUsage',
  full_name='api.stats.RumbleItemsUsage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='api.stats.RumbleItemsUsage.item', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used', full_name='api.stats.RumbleItemsUsage.used', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unused', full_name='api.stats.RumbleItemsUsage.unused', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='average_hold', full_name='api.stats.RumbleItemsUsage.average_hold', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=231,
)

_RUMBLESTATS.fields_by_name['rumble_items'].message_type = _RUMBLEITEMSUSAGE
_RUMBLEITEMSUSAGE.fields_by_name['item'].enum_type = _POWERUP
DESCRIPTOR.message_types_by_name['RumbleStats'] = _RUMBLESTATS
DESCRIPTOR.message_types_by_name['RumbleItemsUsage'] = _RUMBLEITEMSUSAGE
DESCRIPTOR.enum_types_by_name['PowerUp'] = _POWERUP

RumbleStats = _reflection.GeneratedProtocolMessageType('RumbleStats', (_message.Message,), dict(
  DESCRIPTOR = _RUMBLESTATS,
  __module__ = 'api.stats.rumble_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.RumbleStats)
  ))
_sym_db.RegisterMessage(RumbleStats)

RumbleItemsUsage = _reflection.GeneratedProtocolMessageType('RumbleItemsUsage', (_message.Message,), dict(
  DESCRIPTOR = _RUMBLEITEMSUSAGE,
  __module__ = 'api.stats.rumble_pb2'
  # @@protoc_insertion_point(class_scope:api.stats.RumbleItemsUsage)
  ))
_sym_db.RegisterMessage(RumbleItemsUsage)


_POWERUP.has_options = True
_POWERUP._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
