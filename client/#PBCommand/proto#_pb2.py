# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: #PBCommand.proto#

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import PBMessage_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='#PBCommand.proto#',
  package='netty',
  serialized_pb='\n\x11#PBCommand.proto#\x12\x05netty\x1a\x0fPBMessage.proto\"@\n\x08\x43\x32SLogin\x12\x10\n\x08userName\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x02(\t\x12\x10\n\x08\x64\x65viceID\x18\x03 \x02(\t\":\n\x08S2CLogin\x12\r\n\x05token\x18\x01 \x02(\t\x12\x1f\n\x08userInfo\x18\x02 \x02(\x0b\x32\r.netty.PBUser\"\r\n\x0b\x43\x32SUserInfo\".\n\x0bS2CUserInfo\x12\x1f\n\x08userInfo\x18\x01 \x02(\x0b\x32\r.netty.PBUser\"\r\n\x0b\x43\x32SHeroInfo\".\n\x0bS2CHeroInfo\x12\x1f\n\x08heroList\x18\x01 \x03(\x0b\x32\r.netty.PBHero\"\x0e\n\x0c\x43\x32SEquipInfo\"1\n\x0cS2CEquipInfo\x12!\n\tequipList\x18\x01 \x03(\x0b\x32\x0e.netty.PBEquip\"0\n\rC2SPutOnEquip\x12\x0e\n\x06heroId\x18\x01 \x02(\x03\x12\x0f\n\x07\x65quipId\x18\x02 \x02(\x03\",\n\rS2CPutOnEquip\x12\x1b\n\x04hero\x18\x01 \x02(\x0b\x32\r.netty.PBHero\"1\n\x0e\x43\x32SPutOffEquip\x12\x0e\n\x06heroId\x18\x01 \x02(\x03\x12\x0f\n\x07\x65quipId\x18\x02 \x02(\x03\"1\n\x0eS2CPutOffEquip\x12\x0e\n\x06heroId\x18\x01 \x02(\x03\x12\x0f\n\x07\x65quipId\x18\x02 \x02(\x03\"\x1d\n\x0b\x43\x32SSaleHero\x12\x0e\n\x06heroId\x18\x01 \x02(\x03\"/\n\x0bS2CSaleHero\x12\x0e\n\x06heroId\x18\x01 \x02(\x03\x12\x10\n\x08saleGold\x18\x02 \x02(\x05\x42%\n\x18\x63om.ease.nogame.protobufB\tPBCommand')




_C2SLOGIN = _descriptor.Descriptor(
  name='C2SLogin',
  full_name='netty.C2SLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='netty.C2SLogin.userName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='netty.C2SLogin.password', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='netty.C2SLogin.deviceID', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  serialized_start=45,
  serialized_end=109,
)


_S2CLOGIN = _descriptor.Descriptor(
  name='S2CLogin',
  full_name='netty.S2CLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='netty.S2CLogin.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='netty.S2CLogin.userInfo', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=111,
  serialized_end=169,
)


_C2SUSERINFO = _descriptor.Descriptor(
  name='C2SUserInfo',
  full_name='netty.C2SUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=171,
  serialized_end=184,
)


_S2CUSERINFO = _descriptor.Descriptor(
  name='S2CUserInfo',
  full_name='netty.S2CUserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userInfo', full_name='netty.S2CUserInfo.userInfo', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=186,
  serialized_end=232,
)


_C2SHEROINFO = _descriptor.Descriptor(
  name='C2SHeroInfo',
  full_name='netty.C2SHeroInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=234,
  serialized_end=247,
)


_S2CHEROINFO = _descriptor.Descriptor(
  name='S2CHeroInfo',
  full_name='netty.S2CHeroInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heroList', full_name='netty.S2CHeroInfo.heroList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=249,
  serialized_end=295,
)


_C2SEQUIPINFO = _descriptor.Descriptor(
  name='C2SEquipInfo',
  full_name='netty.C2SEquipInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=297,
  serialized_end=311,
)


_S2CEQUIPINFO = _descriptor.Descriptor(
  name='S2CEquipInfo',
  full_name='netty.S2CEquipInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='equipList', full_name='netty.S2CEquipInfo.equipList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=313,
  serialized_end=362,
)


_C2SPUTONEQUIP = _descriptor.Descriptor(
  name='C2SPutOnEquip',
  full_name='netty.C2SPutOnEquip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heroId', full_name='netty.C2SPutOnEquip.heroId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipId', full_name='netty.C2SPutOnEquip.equipId', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=364,
  serialized_end=412,
)


_S2CPUTONEQUIP = _descriptor.Descriptor(
  name='S2CPutOnEquip',
  full_name='netty.S2CPutOnEquip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hero', full_name='netty.S2CPutOnEquip.hero', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=414,
  serialized_end=458,
)


_C2SPUTOFFEQUIP = _descriptor.Descriptor(
  name='C2SPutOffEquip',
  full_name='netty.C2SPutOffEquip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heroId', full_name='netty.C2SPutOffEquip.heroId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipId', full_name='netty.C2SPutOffEquip.equipId', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=460,
  serialized_end=509,
)


_S2CPUTOFFEQUIP = _descriptor.Descriptor(
  name='S2CPutOffEquip',
  full_name='netty.S2CPutOffEquip',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heroId', full_name='netty.S2CPutOffEquip.heroId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipId', full_name='netty.S2CPutOffEquip.equipId', index=1,
      number=2, type=3, cpp_type=2, label=2,
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
  serialized_start=511,
  serialized_end=560,
)


_C2SSALEHERO = _descriptor.Descriptor(
  name='C2SSaleHero',
  full_name='netty.C2SSaleHero',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heroId', full_name='netty.C2SSaleHero.heroId', index=0,
      number=1, type=3, cpp_type=2, label=2,
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
  serialized_start=562,
  serialized_end=591,
)


_S2CSALEHERO = _descriptor.Descriptor(
  name='S2CSaleHero',
  full_name='netty.S2CSaleHero',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heroId', full_name='netty.S2CSaleHero.heroId', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='saleGold', full_name='netty.S2CSaleHero.saleGold', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=593,
  serialized_end=640,
)

_S2CLOGIN.fields_by_name['userInfo'].message_type = PBMessage_pb2._PBUSER
_S2CUSERINFO.fields_by_name['userInfo'].message_type = PBMessage_pb2._PBUSER
_S2CHEROINFO.fields_by_name['heroList'].message_type = PBMessage_pb2._PBHERO
_S2CEQUIPINFO.fields_by_name['equipList'].message_type = PBMessage_pb2._PBEQUIP
_S2CPUTONEQUIP.fields_by_name['hero'].message_type = PBMessage_pb2._PBHERO
DESCRIPTOR.message_types_by_name['C2SLogin'] = _C2SLOGIN
DESCRIPTOR.message_types_by_name['S2CLogin'] = _S2CLOGIN
DESCRIPTOR.message_types_by_name['C2SUserInfo'] = _C2SUSERINFO
DESCRIPTOR.message_types_by_name['S2CUserInfo'] = _S2CUSERINFO
DESCRIPTOR.message_types_by_name['C2SHeroInfo'] = _C2SHEROINFO
DESCRIPTOR.message_types_by_name['S2CHeroInfo'] = _S2CHEROINFO
DESCRIPTOR.message_types_by_name['C2SEquipInfo'] = _C2SEQUIPINFO
DESCRIPTOR.message_types_by_name['S2CEquipInfo'] = _S2CEQUIPINFO
DESCRIPTOR.message_types_by_name['C2SPutOnEquip'] = _C2SPUTONEQUIP
DESCRIPTOR.message_types_by_name['S2CPutOnEquip'] = _S2CPUTONEQUIP
DESCRIPTOR.message_types_by_name['C2SPutOffEquip'] = _C2SPUTOFFEQUIP
DESCRIPTOR.message_types_by_name['S2CPutOffEquip'] = _S2CPUTOFFEQUIP
DESCRIPTOR.message_types_by_name['C2SSaleHero'] = _C2SSALEHERO
DESCRIPTOR.message_types_by_name['S2CSaleHero'] = _S2CSALEHERO

class C2SLogin(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2SLOGIN

  # @@protoc_insertion_point(class_scope:netty.C2SLogin)

class S2CLogin(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2CLOGIN

  # @@protoc_insertion_point(class_scope:netty.S2CLogin)

class C2SUserInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2SUSERINFO

  # @@protoc_insertion_point(class_scope:netty.C2SUserInfo)

class S2CUserInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2CUSERINFO

  # @@protoc_insertion_point(class_scope:netty.S2CUserInfo)

class C2SHeroInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2SHEROINFO

  # @@protoc_insertion_point(class_scope:netty.C2SHeroInfo)

class S2CHeroInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2CHEROINFO

  # @@protoc_insertion_point(class_scope:netty.S2CHeroInfo)

class C2SEquipInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2SEQUIPINFO

  # @@protoc_insertion_point(class_scope:netty.C2SEquipInfo)

class S2CEquipInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2CEQUIPINFO

  # @@protoc_insertion_point(class_scope:netty.S2CEquipInfo)

class C2SPutOnEquip(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2SPUTONEQUIP

  # @@protoc_insertion_point(class_scope:netty.C2SPutOnEquip)

class S2CPutOnEquip(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2CPUTONEQUIP

  # @@protoc_insertion_point(class_scope:netty.S2CPutOnEquip)

class C2SPutOffEquip(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2SPUTOFFEQUIP

  # @@protoc_insertion_point(class_scope:netty.C2SPutOffEquip)

class S2CPutOffEquip(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2CPUTOFFEQUIP

  # @@protoc_insertion_point(class_scope:netty.S2CPutOffEquip)

class C2SSaleHero(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _C2SSALEHERO

  # @@protoc_insertion_point(class_scope:netty.C2SSaleHero)

class S2CSaleHero(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _S2CSALEHERO

  # @@protoc_insertion_point(class_scope:netty.S2CSaleHero)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\030com.ease.nogame.protobufB\tPBCommand')
# @@protoc_insertion_point(module_scope)