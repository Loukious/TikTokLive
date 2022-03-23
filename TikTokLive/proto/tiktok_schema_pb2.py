# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tiktok_schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13tiktok_schema.proto\x12\x06TikTok\"\x8c\x01\n\x0fWebcastResponse\x12!\n\x08messages\x18\x01 \x03(\x0b\x32\x0f.TikTok.Message\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\t\x12\x0e\n\x06\x61\x63kIds\x18\x05 \x01(\t\x12\'\n\x07wsParam\x18\x07 \x01(\x0b\x32\x16.TikTok.WebsocketParam\x12\r\n\x05wsUrl\x18\n \x01(\t\"\'\n\x07Message\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x62inary\x18\x02 \x01(\x0c\"-\n\x0eWebsocketParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\'\n\x15WebcastControlMessage\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\x05\"0\n\x19WebcastRoomUserSeqMessage\x12\x13\n\x0bviewerCount\x18\x03 \x01(\x05\"A\n\x12WebcastChatMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\"^\n\x14WebcastMemberMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12*\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1b.TikTok.WebcastMessageEvent\"B\n\x12WebcastGiftMessage\x12\x1a\n\x04user\x18\x07 \x01(\x0b\x32\x0c.TikTok.User\x12\x10\n\x08giftJson\x18\x16 \x01(\t\"N\n\x14WebcastLinkMicBattle\x12\x36\n\x0b\x62\x61ttleUsers\x18\n \x03(\x0b\x32!.TikTok.WebcastLinkMicBattleItems\"S\n\x19WebcastLinkMicBattleItems\x12\x36\n\x0b\x62\x61ttleGroup\x18\x02 \x01(\x0b\x32!.TikTok.WebcastLinkMicBattleGroup\";\n\x19WebcastLinkMicBattleGroup\x12\x1e\n\x04user\x18\x01 \x01(\x0b\x32\x10.TikTok.LinkUser\"d\n\x14WebcastLinkMicArmies\x12\x36\n\x0b\x62\x61ttleItems\x18\x03 \x03(\x0b\x32!.TikTok.WebcastLinkMicArmiesItems\x12\x14\n\x0c\x62\x61ttleStatus\x18\x07 \x01(\x05\"h\n\x19WebcastLinkMicArmiesItems\x12\x12\n\nhostUserId\x18\x01 \x01(\x04\x12\x37\n\x0c\x62\x61ttleGroups\x18\x02 \x03(\x0b\x32!.TikTok.WebcastLinkMicArmiesGroup\"H\n\x19WebcastLinkMicArmiesGroup\x12\x1b\n\x05users\x18\x01 \x03(\x0b\x32\x0c.TikTok.User\x12\x0e\n\x06points\x18\x02 \x01(\x05\"^\n\x14WebcastSocialMessage\x12\x1a\n\x04user\x18\x02 \x01(\x0b\x32\x0c.TikTok.User\x12*\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1b.TikTok.WebcastMessageEvent\"\x87\x01\n\x12WebcastLikeMessage\x12\x1a\n\x04user\x18\x05 \x01(\x0b\x32\x0c.TikTok.User\x12*\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1b.TikTok.WebcastMessageEvent\x12\x11\n\tlikeCount\x18\x02 \x01(\x05\x12\x16\n\x0etotalLikeCount\x18\x03 \x01(\x05\"M\n\x19WebcastQuestionNewMessage\x12\x30\n\x0fquestionDetails\x18\x02 \x01(\x0b\x32\x17.TikTok.QuestionDetails\"C\n\x0fQuestionDetails\x12\x14\n\x0cquestionText\x18\x02 \x01(\t\x12\x1a\n\x04user\x18\x05 \x01(\x0b\x32\x0c.TikTok.User\"O\n\x13WebcastMessageEvent\x12\x38\n\x0c\x65ventDetails\x18\x08 \x01(\x0b\x32\".TikTok.WebcastMessageEventDetails\"@\n\x1aWebcastMessageEventDetails\x12\x13\n\x0b\x64isplayType\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"\xcd\x01\n\x04User\x12\x0e\n\x06userId\x18\x01 \x01(\x04\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12.\n\x0eprofilePicture\x18\t \x01(\x0b\x32\x16.TikTok.ProfilePicture\x12\x34\n\x0f\x65xtraAttributes\x18\x16 \x01(\x0b\x32\x1b.TikTok.UserExtraAttributes\x12+\n\x05\x62\x61\x64ge\x18@ \x01(\x0b\x32\x1c.TikTok.UserBadgesAttributes\x12\x10\n\x08uniqueId\x18& \x01(\t\"n\n\x08LinkUser\x12\x0e\n\x06userId\x18\x01 \x01(\x04\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12.\n\x0eprofilePicture\x18\x03 \x01(\x0b\x32\x16.TikTok.ProfilePicture\x12\x10\n\x08uniqueId\x18\x04 \x01(\t\"\x1e\n\x0eProfilePicture\x12\x0c\n\x04urls\x18\x01 \x03(\t\")\n\x13UserExtraAttributes\x12\x12\n\nfollowRole\x18\x03 \x01(\x05\"9\n\x14UserBadgesAttributes\x12!\n\x06\x62\x61\x64ges\x18\x15 \x03(\x0b\x32\x11.TikTok.UserBadge\"\'\n\tUserBadge\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"C\n\x17WebcastWebsocketMessage\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x07 \x01(\t\x12\x0e\n\x06\x62inary\x18\x08 \x01(\x0c\"/\n\x13WebcastWebsocketAck\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0c\n\x04type\x18\x07 \x01(\t\"V\n\x17WebcastLiveIntroMessage\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x1a\n\x04user\x18\x05 \x01(\x0b\x32\x0c.TikTok.User\"$\n\rSystemMessage\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"*\n\x1aWebcastInRoomBannerMessage\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"&\n\x08RankItem\x12\x0e\n\x06\x63olour\x18\x01 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\x04\"L\n\rWeeklyRanking\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x1e\n\x04rank\x18\x03 \x01(\x0b\x32\x10.TikTok.RankItem\"8\n\rRankContainer\x12\'\n\x08rankings\x18\x04 \x01(\x0b\x32\x15.TikTok.WeeklyRanking\"?\n\x18WebcastHourlyRankMessage\x12#\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x15.TikTok.RankContainerb\x06proto3')

_WEBCASTRESPONSE = DESCRIPTOR.message_types_by_name['WebcastResponse']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_WEBSOCKETPARAM = DESCRIPTOR.message_types_by_name['WebsocketParam']
_WEBCASTCONTROLMESSAGE = DESCRIPTOR.message_types_by_name['WebcastControlMessage']
_WEBCASTROOMUSERSEQMESSAGE = DESCRIPTOR.message_types_by_name['WebcastRoomUserSeqMessage']
_WEBCASTCHATMESSAGE = DESCRIPTOR.message_types_by_name['WebcastChatMessage']
_WEBCASTMEMBERMESSAGE = DESCRIPTOR.message_types_by_name['WebcastMemberMessage']
_WEBCASTGIFTMESSAGE = DESCRIPTOR.message_types_by_name['WebcastGiftMessage']
_WEBCASTLINKMICBATTLE = DESCRIPTOR.message_types_by_name['WebcastLinkMicBattle']
_WEBCASTLINKMICBATTLEITEMS = DESCRIPTOR.message_types_by_name['WebcastLinkMicBattleItems']
_WEBCASTLINKMICBATTLEGROUP = DESCRIPTOR.message_types_by_name['WebcastLinkMicBattleGroup']
_WEBCASTLINKMICARMIES = DESCRIPTOR.message_types_by_name['WebcastLinkMicArmies']
_WEBCASTLINKMICARMIESITEMS = DESCRIPTOR.message_types_by_name['WebcastLinkMicArmiesItems']
_WEBCASTLINKMICARMIESGROUP = DESCRIPTOR.message_types_by_name['WebcastLinkMicArmiesGroup']
_WEBCASTSOCIALMESSAGE = DESCRIPTOR.message_types_by_name['WebcastSocialMessage']
_WEBCASTLIKEMESSAGE = DESCRIPTOR.message_types_by_name['WebcastLikeMessage']
_WEBCASTQUESTIONNEWMESSAGE = DESCRIPTOR.message_types_by_name['WebcastQuestionNewMessage']
_QUESTIONDETAILS = DESCRIPTOR.message_types_by_name['QuestionDetails']
_WEBCASTMESSAGEEVENT = DESCRIPTOR.message_types_by_name['WebcastMessageEvent']
_WEBCASTMESSAGEEVENTDETAILS = DESCRIPTOR.message_types_by_name['WebcastMessageEventDetails']
_USER = DESCRIPTOR.message_types_by_name['User']
_LINKUSER = DESCRIPTOR.message_types_by_name['LinkUser']
_PROFILEPICTURE = DESCRIPTOR.message_types_by_name['ProfilePicture']
_USEREXTRAATTRIBUTES = DESCRIPTOR.message_types_by_name['UserExtraAttributes']
_USERBADGESATTRIBUTES = DESCRIPTOR.message_types_by_name['UserBadgesAttributes']
_USERBADGE = DESCRIPTOR.message_types_by_name['UserBadge']
_WEBCASTWEBSOCKETMESSAGE = DESCRIPTOR.message_types_by_name['WebcastWebsocketMessage']
_WEBCASTWEBSOCKETACK = DESCRIPTOR.message_types_by_name['WebcastWebsocketAck']
_WEBCASTLIVEINTROMESSAGE = DESCRIPTOR.message_types_by_name['WebcastLiveIntroMessage']
_SYSTEMMESSAGE = DESCRIPTOR.message_types_by_name['SystemMessage']
_WEBCASTINROOMBANNERMESSAGE = DESCRIPTOR.message_types_by_name['WebcastInRoomBannerMessage']
_RANKITEM = DESCRIPTOR.message_types_by_name['RankItem']
_WEEKLYRANKING = DESCRIPTOR.message_types_by_name['WeeklyRanking']
_RANKCONTAINER = DESCRIPTOR.message_types_by_name['RankContainer']
_WEBCASTHOURLYRANKMESSAGE = DESCRIPTOR.message_types_by_name['WebcastHourlyRankMessage']
WebcastResponse = _reflection.GeneratedProtocolMessageType('WebcastResponse', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTRESPONSE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastResponse)
})
_sym_db.RegisterMessage(WebcastResponse)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
    'DESCRIPTOR': _MESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.Message)
})
_sym_db.RegisterMessage(Message)

WebsocketParam = _reflection.GeneratedProtocolMessageType('WebsocketParam', (_message.Message,), {
    'DESCRIPTOR': _WEBSOCKETPARAM,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebsocketParam)
})
_sym_db.RegisterMessage(WebsocketParam)

WebcastControlMessage = _reflection.GeneratedProtocolMessageType('WebcastControlMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTCONTROLMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastControlMessage)
})
_sym_db.RegisterMessage(WebcastControlMessage)

WebcastRoomUserSeqMessage = _reflection.GeneratedProtocolMessageType('WebcastRoomUserSeqMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTROOMUSERSEQMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastRoomUserSeqMessage)
})
_sym_db.RegisterMessage(WebcastRoomUserSeqMessage)

WebcastChatMessage = _reflection.GeneratedProtocolMessageType('WebcastChatMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTCHATMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastChatMessage)
})
_sym_db.RegisterMessage(WebcastChatMessage)

WebcastMemberMessage = _reflection.GeneratedProtocolMessageType('WebcastMemberMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTMEMBERMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastMemberMessage)
})
_sym_db.RegisterMessage(WebcastMemberMessage)

WebcastGiftMessage = _reflection.GeneratedProtocolMessageType('WebcastGiftMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTGIFTMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastGiftMessage)
})
_sym_db.RegisterMessage(WebcastGiftMessage)

WebcastLinkMicBattle = _reflection.GeneratedProtocolMessageType('WebcastLinkMicBattle', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTLINKMICBATTLE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicBattle)
})
_sym_db.RegisterMessage(WebcastLinkMicBattle)

WebcastLinkMicBattleItems = _reflection.GeneratedProtocolMessageType('WebcastLinkMicBattleItems', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTLINKMICBATTLEITEMS,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicBattleItems)
})
_sym_db.RegisterMessage(WebcastLinkMicBattleItems)

WebcastLinkMicBattleGroup = _reflection.GeneratedProtocolMessageType('WebcastLinkMicBattleGroup', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTLINKMICBATTLEGROUP,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicBattleGroup)
})
_sym_db.RegisterMessage(WebcastLinkMicBattleGroup)

WebcastLinkMicArmies = _reflection.GeneratedProtocolMessageType('WebcastLinkMicArmies', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTLINKMICARMIES,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicArmies)
})
_sym_db.RegisterMessage(WebcastLinkMicArmies)

WebcastLinkMicArmiesItems = _reflection.GeneratedProtocolMessageType('WebcastLinkMicArmiesItems', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTLINKMICARMIESITEMS,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicArmiesItems)
})
_sym_db.RegisterMessage(WebcastLinkMicArmiesItems)

WebcastLinkMicArmiesGroup = _reflection.GeneratedProtocolMessageType('WebcastLinkMicArmiesGroup', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTLINKMICARMIESGROUP,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastLinkMicArmiesGroup)
})
_sym_db.RegisterMessage(WebcastLinkMicArmiesGroup)

WebcastSocialMessage = _reflection.GeneratedProtocolMessageType('WebcastSocialMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTSOCIALMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastSocialMessage)
})
_sym_db.RegisterMessage(WebcastSocialMessage)

WebcastLikeMessage = _reflection.GeneratedProtocolMessageType('WebcastLikeMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTLIKEMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastLikeMessage)
})
_sym_db.RegisterMessage(WebcastLikeMessage)

WebcastQuestionNewMessage = _reflection.GeneratedProtocolMessageType('WebcastQuestionNewMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTQUESTIONNEWMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastQuestionNewMessage)
})
_sym_db.RegisterMessage(WebcastQuestionNewMessage)

QuestionDetails = _reflection.GeneratedProtocolMessageType('QuestionDetails', (_message.Message,), {
    'DESCRIPTOR': _QUESTIONDETAILS,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.QuestionDetails)
})
_sym_db.RegisterMessage(QuestionDetails)

WebcastMessageEvent = _reflection.GeneratedProtocolMessageType('WebcastMessageEvent', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTMESSAGEEVENT,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastMessageEvent)
})
_sym_db.RegisterMessage(WebcastMessageEvent)

WebcastMessageEventDetails = _reflection.GeneratedProtocolMessageType('WebcastMessageEventDetails', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTMESSAGEEVENTDETAILS,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastMessageEventDetails)
})
_sym_db.RegisterMessage(WebcastMessageEventDetails)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
    'DESCRIPTOR': _USER,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.User)
})
_sym_db.RegisterMessage(User)

LinkUser = _reflection.GeneratedProtocolMessageType('LinkUser', (_message.Message,), {
    'DESCRIPTOR': _LINKUSER,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.LinkUser)
})
_sym_db.RegisterMessage(LinkUser)

ProfilePicture = _reflection.GeneratedProtocolMessageType('ProfilePicture', (_message.Message,), {
    'DESCRIPTOR': _PROFILEPICTURE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.ProfilePicture)
})
_sym_db.RegisterMessage(ProfilePicture)

UserExtraAttributes = _reflection.GeneratedProtocolMessageType('UserExtraAttributes', (_message.Message,), {
    'DESCRIPTOR': _USEREXTRAATTRIBUTES,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.UserExtraAttributes)
})
_sym_db.RegisterMessage(UserExtraAttributes)

UserBadgesAttributes = _reflection.GeneratedProtocolMessageType('UserBadgesAttributes', (_message.Message,), {
    'DESCRIPTOR': _USERBADGESATTRIBUTES,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.UserBadgesAttributes)
})
_sym_db.RegisterMessage(UserBadgesAttributes)

UserBadge = _reflection.GeneratedProtocolMessageType('UserBadge', (_message.Message,), {
    'DESCRIPTOR': _USERBADGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.UserBadge)
})
_sym_db.RegisterMessage(UserBadge)

WebcastWebsocketMessage = _reflection.GeneratedProtocolMessageType('WebcastWebsocketMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTWEBSOCKETMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastWebsocketMessage)
})
_sym_db.RegisterMessage(WebcastWebsocketMessage)

WebcastWebsocketAck = _reflection.GeneratedProtocolMessageType('WebcastWebsocketAck', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTWEBSOCKETACK,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastWebsocketAck)
})
_sym_db.RegisterMessage(WebcastWebsocketAck)

WebcastLiveIntroMessage = _reflection.GeneratedProtocolMessageType('WebcastLiveIntroMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTLIVEINTROMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastLiveIntroMessage)
})
_sym_db.RegisterMessage(WebcastLiveIntroMessage)

SystemMessage = _reflection.GeneratedProtocolMessageType('SystemMessage', (_message.Message,), {
    'DESCRIPTOR': _SYSTEMMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.SystemMessage)
})
_sym_db.RegisterMessage(SystemMessage)

WebcastInRoomBannerMessage = _reflection.GeneratedProtocolMessageType('WebcastInRoomBannerMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTINROOMBANNERMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastInRoomBannerMessage)
})
_sym_db.RegisterMessage(WebcastInRoomBannerMessage)

RankItem = _reflection.GeneratedProtocolMessageType('RankItem', (_message.Message,), {
    'DESCRIPTOR': _RANKITEM,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.RankItem)
})
_sym_db.RegisterMessage(RankItem)

WeeklyRanking = _reflection.GeneratedProtocolMessageType('WeeklyRanking', (_message.Message,), {
    'DESCRIPTOR': _WEEKLYRANKING,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WeeklyRanking)
})
_sym_db.RegisterMessage(WeeklyRanking)

RankContainer = _reflection.GeneratedProtocolMessageType('RankContainer', (_message.Message,), {
    'DESCRIPTOR': _RANKCONTAINER,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.RankContainer)
})
_sym_db.RegisterMessage(RankContainer)

WebcastHourlyRankMessage = _reflection.GeneratedProtocolMessageType('WebcastHourlyRankMessage', (_message.Message,), {
    'DESCRIPTOR': _WEBCASTHOURLYRANKMESSAGE,
    '__module__': 'tiktok_schema_pb2'
    # @@protoc_insertion_point(class_scope:TikTok.WebcastHourlyRankMessage)
})
_sym_db.RegisterMessage(WebcastHourlyRankMessage)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _WEBCASTRESPONSE._serialized_start = 32
    _WEBCASTRESPONSE._serialized_end = 172
    _MESSAGE._serialized_start = 174
    _MESSAGE._serialized_end = 213
    _WEBSOCKETPARAM._serialized_start = 215
    _WEBSOCKETPARAM._serialized_end = 260
    _WEBCASTCONTROLMESSAGE._serialized_start = 262
    _WEBCASTCONTROLMESSAGE._serialized_end = 301
    _WEBCASTROOMUSERSEQMESSAGE._serialized_start = 303
    _WEBCASTROOMUSERSEQMESSAGE._serialized_end = 351
    _WEBCASTCHATMESSAGE._serialized_start = 353
    _WEBCASTCHATMESSAGE._serialized_end = 418
    _WEBCASTMEMBERMESSAGE._serialized_start = 420
    _WEBCASTMEMBERMESSAGE._serialized_end = 514
    _WEBCASTGIFTMESSAGE._serialized_start = 516
    _WEBCASTGIFTMESSAGE._serialized_end = 582
    _WEBCASTLINKMICBATTLE._serialized_start = 584
    _WEBCASTLINKMICBATTLE._serialized_end = 662
    _WEBCASTLINKMICBATTLEITEMS._serialized_start = 664
    _WEBCASTLINKMICBATTLEITEMS._serialized_end = 747
    _WEBCASTLINKMICBATTLEGROUP._serialized_start = 749
    _WEBCASTLINKMICBATTLEGROUP._serialized_end = 808
    _WEBCASTLINKMICARMIES._serialized_start = 810
    _WEBCASTLINKMICARMIES._serialized_end = 910
    _WEBCASTLINKMICARMIESITEMS._serialized_start = 912
    _WEBCASTLINKMICARMIESITEMS._serialized_end = 1016
    _WEBCASTLINKMICARMIESGROUP._serialized_start = 1018
    _WEBCASTLINKMICARMIESGROUP._serialized_end = 1090
    _WEBCASTSOCIALMESSAGE._serialized_start = 1092
    _WEBCASTSOCIALMESSAGE._serialized_end = 1186
    _WEBCASTLIKEMESSAGE._serialized_start = 1189
    _WEBCASTLIKEMESSAGE._serialized_end = 1324
    _WEBCASTQUESTIONNEWMESSAGE._serialized_start = 1326
    _WEBCASTQUESTIONNEWMESSAGE._serialized_end = 1403
    _QUESTIONDETAILS._serialized_start = 1405
    _QUESTIONDETAILS._serialized_end = 1472
    _WEBCASTMESSAGEEVENT._serialized_start = 1474
    _WEBCASTMESSAGEEVENT._serialized_end = 1553
    _WEBCASTMESSAGEEVENTDETAILS._serialized_start = 1555
    _WEBCASTMESSAGEEVENTDETAILS._serialized_end = 1619
    _USER._serialized_start = 1622
    _USER._serialized_end = 1827
    _LINKUSER._serialized_start = 1829
    _LINKUSER._serialized_end = 1939
    _PROFILEPICTURE._serialized_start = 1941
    _PROFILEPICTURE._serialized_end = 1971
    _USEREXTRAATTRIBUTES._serialized_start = 1973
    _USEREXTRAATTRIBUTES._serialized_end = 2014
    _USERBADGESATTRIBUTES._serialized_start = 2016
    _USERBADGESATTRIBUTES._serialized_end = 2073
    _USERBADGE._serialized_start = 2075
    _USERBADGE._serialized_end = 2114
    _WEBCASTWEBSOCKETMESSAGE._serialized_start = 2116
    _WEBCASTWEBSOCKETMESSAGE._serialized_end = 2183
    _WEBCASTWEBSOCKETACK._serialized_start = 2185
    _WEBCASTWEBSOCKETACK._serialized_end = 2232
    _WEBCASTLIVEINTROMESSAGE._serialized_start = 2234
    _WEBCASTLIVEINTROMESSAGE._serialized_end = 2320
    _SYSTEMMESSAGE._serialized_start = 2322
    _SYSTEMMESSAGE._serialized_end = 2358
    _WEBCASTINROOMBANNERMESSAGE._serialized_start = 2360
    _WEBCASTINROOMBANNERMESSAGE._serialized_end = 2402
    _RANKITEM._serialized_start = 2404
    _RANKITEM._serialized_end = 2442
    _WEEKLYRANKING._serialized_start = 2444
    _WEEKLYRANKING._serialized_end = 2520
    _RANKCONTAINER._serialized_start = 2522
    _RANKCONTAINER._serialized_end = 2578
    _WEBCASTHOURLYRANKMESSAGE._serialized_start = 2580
    _WEBCASTHOURLYRANKMESSAGE._serialized_end = 2643
# @@protoc_insertion_point(module_scope)
