# SNMP MIB module (NSCRTV-FTTX-EPON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/NSCRTV-FTTX-EPON-MIB
# Produced by pysmi-1.6.1 at Mon May 26 12:26:59 2025
# On host user-HP platform Linux version 6.11.0-26-generic by user user
# Using Python version 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(BridgeId,
 Timeout) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eponWifiGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1)
)
if mibBuilder.loadTexts:
    eponWifiGroup.setRevisions(
        ("2016-06-01 14:16",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EponAlarmInstance(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class EponAlarmCode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class EponSeverityType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("info", 5),
          ("clear", 6))
    )



class TAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class EponCardIndex(TextualConvention, Unsigned32):
    status = "current"


class EponPortIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EponDeviceIndex(TextualConvention, Unsigned32):
    status = "current"


class AutoNegotiationTechAbility(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("none", 0),
          ("tenBaseTFullDuplex", 1),
          ("tenBaseTHalfDuplex", 2),
          ("hundredBaseTFullDuplex", 3),
          ("hundredBaseTHalfDuplex", 4),
          ("thousandBaseTFullDuplex", 5),
          ("thousandBaseTHalfDuplex", 6),
          ("thousandBaseXFullDuplex", 7),
          ("thousandBaseXHalfDuplex", 8),
          ("fdxPause", 9),
          ("fdxApause", 10),
          ("fdxSpause", 11),
          ("fdxBpause", 12))
    )


class EponStats15MinRecordType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )



class EponStats24HourRecordType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )



class EponStatsThresholdType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_NscrtvRoot_ObjectIdentity = ObjectIdentity
nscrtvRoot = _NscrtvRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409)
)
_NscrtvHFCemsTree_ObjectIdentity = ObjectIdentity
nscrtvHFCemsTree = _NscrtvHFCemsTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 1)
)
_NscrtvEponEocTree_ObjectIdentity = ObjectIdentity
nscrtvEponEocTree = _NscrtvEponEocTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2)
)
_PropertyIdent_ObjectIdentity = ObjectIdentity
propertyIdent = _PropertyIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 1)
)
_AlarmsIdent_ObjectIdentity = ObjectIdentity
alarmsIdent = _AlarmsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2)
)
_EponAlarmTree_ObjectIdentity = ObjectIdentity
eponAlarmTree = _EponAlarmTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11)
)
_EponTrapObjectGroup_ObjectIdentity = ObjectIdentity
eponTrapObjectGroup = _EponTrapObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1)
)
_EponNotifications_ObjectIdentity = ObjectIdentity
eponNotifications = _EponNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 1)
)
_EponTrapObjects_ObjectIdentity = ObjectIdentity
eponTrapObjects = _EponTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2)
)
_EponTrapInstance_Type = EponAlarmInstance
_EponTrapInstance_Object = MibScalar
eponTrapInstance = _EponTrapInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 1),
    _EponTrapInstance_Type()
)
eponTrapInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapInstance.setStatus("current")
_EponTrapCorrelationId_Type = Unsigned32
_EponTrapCorrelationId_Object = MibScalar
eponTrapCorrelationId = _EponTrapCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 2),
    _EponTrapCorrelationId_Type()
)
eponTrapCorrelationId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapCorrelationId.setStatus("current")


class _EponTrapAdditionalText_Type(OctetString):
    """Custom type eponTrapAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EponTrapAdditionalText_Type.__name__ = "OctetString"
_EponTrapAdditionalText_Object = MibScalar
eponTrapAdditionalText = _EponTrapAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 3),
    _EponTrapAdditionalText_Type()
)
eponTrapAdditionalText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapAdditionalText.setStatus("current")
_EponTrapCode_Type = EponAlarmCode
_EponTrapCode_Object = MibScalar
eponTrapCode = _EponTrapCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 4),
    _EponTrapCode_Type()
)
eponTrapCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapCode.setStatus("current")
_EponTrapSeverity_Type = EponSeverityType
_EponTrapSeverity_Object = MibScalar
eponTrapSeverity = _EponTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 5),
    _EponTrapSeverity_Type()
)
eponTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapSeverity.setStatus("current")
_EponTrapOccurTime_Type = DateAndTime
_EponTrapOccurTime_Object = MibScalar
eponTrapOccurTime = _EponTrapOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 6),
    _EponTrapOccurTime_Type()
)
eponTrapOccurTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapOccurTime.setStatus("current")
_EponTrapSequenceNumber_Type = Unsigned32
_EponTrapSequenceNumber_Object = MibScalar
eponTrapSequenceNumber = _EponTrapSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 2, 7),
    _EponTrapSequenceNumber_Type()
)
eponTrapSequenceNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eponTrapSequenceNumber.setStatus("current")
_EponAlarmObjGroup_ObjectIdentity = ObjectIdentity
eponAlarmObjGroup = _EponAlarmObjGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2)
)
_ActiveAlarmTable_Object = MibTable
activeAlarmTable = _ActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    activeAlarmTable.setStatus("current")
_ActiveAlarmEntry_Object = MibTableRow
activeAlarmEntry = _ActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1)
)
activeAlarmEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "activeAlarmSeqNum"),
    (0, "NSCRTV-FTTX-EPON-MIB", "activeAlarmRaisingNumber"),
)
if mibBuilder.loadTexts:
    activeAlarmEntry.setStatus("current")


class _ActiveAlarmSeqNum_Type(Unsigned32):
    """Custom type activeAlarmSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ActiveAlarmSeqNum_Type.__name__ = "Unsigned32"
_ActiveAlarmSeqNum_Object = MibTableColumn
activeAlarmSeqNum = _ActiveAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 1),
    _ActiveAlarmSeqNum_Type()
)
activeAlarmSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeAlarmSeqNum.setStatus("current")
_ActiveAlarmCode_Type = EponAlarmCode
_ActiveAlarmCode_Object = MibTableColumn
activeAlarmCode = _ActiveAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 2),
    _ActiveAlarmCode_Type()
)
activeAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmCode.setStatus("current")
_ActiveAlarmInstance_Type = EponAlarmInstance
_ActiveAlarmInstance_Object = MibTableColumn
activeAlarmInstance = _ActiveAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 3),
    _ActiveAlarmInstance_Type()
)
activeAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmInstance.setStatus("current")
_ActiveAlarmSeverity_Type = EponSeverityType
_ActiveAlarmSeverity_Object = MibTableColumn
activeAlarmSeverity = _ActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 4),
    _ActiveAlarmSeverity_Type()
)
activeAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmSeverity.setStatus("current")


class _ActiveAlarmRaisingNumber_Type(Unsigned32):
    """Custom type activeAlarmRaisingNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ActiveAlarmRaisingNumber_Type.__name__ = "Unsigned32"
_ActiveAlarmRaisingNumber_Object = MibTableColumn
activeAlarmRaisingNumber = _ActiveAlarmRaisingNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 5),
    _ActiveAlarmRaisingNumber_Type()
)
activeAlarmRaisingNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeAlarmRaisingNumber.setStatus("current")
_ActiveAlarmFirstOccurTime_Type = DateAndTime
_ActiveAlarmFirstOccurTime_Object = MibTableColumn
activeAlarmFirstOccurTime = _ActiveAlarmFirstOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 6),
    _ActiveAlarmFirstOccurTime_Type()
)
activeAlarmFirstOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmFirstOccurTime.setStatus("current")
_ActiveAlarmLastOccurTime_Type = DateAndTime
_ActiveAlarmLastOccurTime_Object = MibTableColumn
activeAlarmLastOccurTime = _ActiveAlarmLastOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 7),
    _ActiveAlarmLastOccurTime_Type()
)
activeAlarmLastOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmLastOccurTime.setStatus("current")
_ActiveAlarmRepeats_Type = Counter32
_ActiveAlarmRepeats_Object = MibTableColumn
activeAlarmRepeats = _ActiveAlarmRepeats_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 8),
    _ActiveAlarmRepeats_Type()
)
activeAlarmRepeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmRepeats.setStatus("current")
_ActiveAlarmConfirm_Type = TruthValue
_ActiveAlarmConfirm_Object = MibTableColumn
activeAlarmConfirm = _ActiveAlarmConfirm_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 9),
    _ActiveAlarmConfirm_Type()
)
activeAlarmConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeAlarmConfirm.setStatus("current")


class _ActiveAlarmAdditionalText_Type(OctetString):
    """Custom type activeAlarmAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ActiveAlarmAdditionalText_Type.__name__ = "OctetString"
_ActiveAlarmAdditionalText_Object = MibTableColumn
activeAlarmAdditionalText = _ActiveAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 1, 1, 10),
    _ActiveAlarmAdditionalText_Type()
)
activeAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeAlarmAdditionalText.setStatus("current")
_HistoryAlarmTable_Object = MibTable
historyAlarmTable = _HistoryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2)
)
if mibBuilder.loadTexts:
    historyAlarmTable.setStatus("current")
_HistoryAlarmEntry_Object = MibTableRow
historyAlarmEntry = _HistoryAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1)
)
historyAlarmEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "historyAlarmSeqNum"),
    (0, "NSCRTV-FTTX-EPON-MIB", "historyAlarmRaisingNumber"),
)
if mibBuilder.loadTexts:
    historyAlarmEntry.setStatus("current")


class _HistoryAlarmSeqNum_Type(Unsigned32):
    """Custom type historyAlarmSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HistoryAlarmSeqNum_Type.__name__ = "Unsigned32"
_HistoryAlarmSeqNum_Object = MibTableColumn
historyAlarmSeqNum = _HistoryAlarmSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 1),
    _HistoryAlarmSeqNum_Type()
)
historyAlarmSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyAlarmSeqNum.setStatus("current")
_HistoryAlarmCode_Type = EponAlarmCode
_HistoryAlarmCode_Object = MibTableColumn
historyAlarmCode = _HistoryAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 2),
    _HistoryAlarmCode_Type()
)
historyAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmCode.setStatus("current")
_HistoryAlarmInstance_Type = EponAlarmInstance
_HistoryAlarmInstance_Object = MibTableColumn
historyAlarmInstance = _HistoryAlarmInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 3),
    _HistoryAlarmInstance_Type()
)
historyAlarmInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmInstance.setStatus("current")
_HistoryAlarmSeverity_Type = EponSeverityType
_HistoryAlarmSeverity_Object = MibTableColumn
historyAlarmSeverity = _HistoryAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 4),
    _HistoryAlarmSeverity_Type()
)
historyAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmSeverity.setStatus("current")


class _HistoryAlarmRaisingNumber_Type(Unsigned32):
    """Custom type historyAlarmRaisingNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HistoryAlarmRaisingNumber_Type.__name__ = "Unsigned32"
_HistoryAlarmRaisingNumber_Object = MibTableColumn
historyAlarmRaisingNumber = _HistoryAlarmRaisingNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 5),
    _HistoryAlarmRaisingNumber_Type()
)
historyAlarmRaisingNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyAlarmRaisingNumber.setStatus("current")
_HistoryAlarmFirstOccurTime_Type = DateAndTime
_HistoryAlarmFirstOccurTime_Object = MibTableColumn
historyAlarmFirstOccurTime = _HistoryAlarmFirstOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 6),
    _HistoryAlarmFirstOccurTime_Type()
)
historyAlarmFirstOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmFirstOccurTime.setStatus("current")
_HistoryAlarmLastOccurTime_Type = DateAndTime
_HistoryAlarmLastOccurTime_Object = MibTableColumn
historyAlarmLastOccurTime = _HistoryAlarmLastOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 7),
    _HistoryAlarmLastOccurTime_Type()
)
historyAlarmLastOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmLastOccurTime.setStatus("current")
_HistoryAlarmRepeats_Type = Counter32
_HistoryAlarmRepeats_Object = MibTableColumn
historyAlarmRepeats = _HistoryAlarmRepeats_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 8),
    _HistoryAlarmRepeats_Type()
)
historyAlarmRepeats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmRepeats.setStatus("current")
_HistoryAlarmCorrelationId_Type = Unsigned32
_HistoryAlarmCorrelationId_Object = MibTableColumn
historyAlarmCorrelationId = _HistoryAlarmCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 9),
    _HistoryAlarmCorrelationId_Type()
)
historyAlarmCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmCorrelationId.setStatus("current")


class _HistoryAlarmAdditionalText_Type(OctetString):
    """Custom type historyAlarmAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HistoryAlarmAdditionalText_Type.__name__ = "OctetString"
_HistoryAlarmAdditionalText_Object = MibTableColumn
historyAlarmAdditionalText = _HistoryAlarmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 10),
    _HistoryAlarmAdditionalText_Type()
)
historyAlarmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmAdditionalText.setStatus("current")
_HistoryAlarmClearTime_Type = DateAndTime
_HistoryAlarmClearTime_Object = MibTableColumn
historyAlarmClearTime = _HistoryAlarmClearTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 2, 1, 11),
    _HistoryAlarmClearTime_Type()
)
historyAlarmClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyAlarmClearTime.setStatus("current")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("current")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1)
)
eventLogEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "eventSeqNum"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("current")


class _EventSeqNum_Type(Unsigned32):
    """Custom type eventSeqNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EventSeqNum_Type.__name__ = "Unsigned32"
_EventSeqNum_Object = MibTableColumn
eventSeqNum = _EventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 1),
    _EventSeqNum_Type()
)
eventSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventSeqNum.setStatus("current")
_EventCode_Type = EponAlarmCode
_EventCode_Object = MibTableColumn
eventCode = _EventCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 2),
    _EventCode_Type()
)
eventCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCode.setStatus("current")
_EventInstance_Type = EponAlarmInstance
_EventInstance_Object = MibTableColumn
eventInstance = _EventInstance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 3),
    _EventInstance_Type()
)
eventInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstance.setStatus("current")
_EventOccurTime_Type = DateAndTime
_EventOccurTime_Object = MibTableColumn
eventOccurTime = _EventOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 4),
    _EventOccurTime_Type()
)
eventOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventOccurTime.setStatus("current")


class _EventAdditionalText_Type(OctetString):
    """Custom type eventAdditionalText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_EventAdditionalText_Type.__name__ = "OctetString"
_EventAdditionalText_Object = MibTableColumn
eventAdditionalText = _EventAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 2, 3, 1, 5),
    _EventAdditionalText_Type()
)
eventAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAdditionalText.setStatus("current")
_EponManagementObjGroup_ObjectIdentity = ObjectIdentity
eponManagementObjGroup = _EponManagementObjGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3)
)
_EponManagementAddrTable_Object = MibTable
eponManagementAddrTable = _EponManagementAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1)
)
if mibBuilder.loadTexts:
    eponManagementAddrTable.setStatus("current")
_EponManagementAddrEntry_Object = MibTableRow
eponManagementAddrEntry = _EponManagementAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1)
)
eponManagementAddrEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "eponManagementAddrName"),
)
if mibBuilder.loadTexts:
    eponManagementAddrEntry.setStatus("current")


class _EponManagementAddrName_Type(OctetString):
    """Custom type eponManagementAddrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EponManagementAddrName_Type.__name__ = "OctetString"
_EponManagementAddrName_Object = MibTableColumn
eponManagementAddrName = _EponManagementAddrName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1, 1),
    _EponManagementAddrName_Type()
)
eponManagementAddrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponManagementAddrName.setStatus("current")
_EponManagementAddrTAddress_Type = TAddress
_EponManagementAddrTAddress_Object = MibTableColumn
eponManagementAddrTAddress = _EponManagementAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1, 2),
    _EponManagementAddrTAddress_Type()
)
eponManagementAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponManagementAddrTAddress.setStatus("current")


class _EponManagementAddrCommunity_Type(OctetString):
    """Custom type eponManagementAddrCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EponManagementAddrCommunity_Type.__name__ = "OctetString"
_EponManagementAddrCommunity_Object = MibTableColumn
eponManagementAddrCommunity = _EponManagementAddrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1, 3),
    _EponManagementAddrCommunity_Type()
)
eponManagementAddrCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponManagementAddrCommunity.setStatus("current")
_EponManagementAddrRowStatus_Type = RowStatus
_EponManagementAddrRowStatus_Object = MibTableColumn
eponManagementAddrRowStatus = _EponManagementAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 3, 1, 1, 4),
    _EponManagementAddrRowStatus_Type()
)
eponManagementAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponManagementAddrRowStatus.setStatus("current")
_EponTree_ObjectIdentity = ObjectIdentity
eponTree = _EponTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3)
)
_SystemObjects_ObjectIdentity = ObjectIdentity
systemObjects = _SystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1)
)
_SystemGlobalObjects_ObjectIdentity = ObjectIdentity
systemGlobalObjects = _SystemGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    systemGlobalObjects.setStatus("current")
_SystemTime_Type = DateAndTime
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 1),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_InbandIpAddress_Type = IpAddress
_InbandIpAddress_Object = MibScalar
inbandIpAddress = _InbandIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 2),
    _InbandIpAddress_Type()
)
inbandIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpAddress.setStatus("current")
_InbandIpSubnetMask_Type = IpAddress
_InbandIpSubnetMask_Object = MibScalar
inbandIpSubnetMask = _InbandIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 3),
    _InbandIpSubnetMask_Type()
)
inbandIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpSubnetMask.setStatus("current")
_InbandIpGateway_Type = IpAddress
_InbandIpGateway_Object = MibScalar
inbandIpGateway = _InbandIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 4),
    _InbandIpGateway_Type()
)
inbandIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpGateway.setStatus("current")
_InbandVlanId_Type = Integer32
_InbandVlanId_Object = MibScalar
inbandVlanId = _InbandVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 5),
    _InbandVlanId_Type()
)
inbandVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandVlanId.setStatus("current")
_InbandMacAddress_Type = MacAddress
_InbandMacAddress_Object = MibScalar
inbandMacAddress = _InbandMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 6),
    _InbandMacAddress_Type()
)
inbandMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inbandMacAddress.setStatus("current")
_OutbandIpAddress_Type = IpAddress
_OutbandIpAddress_Object = MibScalar
outbandIpAddress = _OutbandIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 7),
    _OutbandIpAddress_Type()
)
outbandIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbandIpAddress.setStatus("current")
_OutbandIpSubnetMask_Type = IpAddress
_OutbandIpSubnetMask_Object = MibScalar
outbandIpSubnetMask = _OutbandIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 8),
    _OutbandIpSubnetMask_Type()
)
outbandIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbandIpSubnetMask.setStatus("current")
_OutbandIpGateway_Type = IpAddress
_OutbandIpGateway_Object = MibScalar
outbandIpGateway = _OutbandIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 9),
    _OutbandIpGateway_Type()
)
outbandIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outbandIpGateway.setStatus("current")
_OutbandMacAddress_Type = MacAddress
_OutbandMacAddress_Object = MibScalar
outbandMacAddress = _OutbandMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 10),
    _OutbandMacAddress_Type()
)
outbandMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outbandMacAddress.setStatus("current")


class _SystemOUI_Type(OctetString):
    """Custom type systemOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_SystemOUI_Type.__name__ = "OctetString"
_SystemOUI_Object = MibScalar
systemOUI = _SystemOUI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 11),
    _SystemOUI_Type()
)
systemOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemOUI.setStatus("current")
_VendorName_Type = DisplayString
_VendorName_Object = MibScalar
vendorName = _VendorName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 12),
    _VendorName_Type()
)
vendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vendorName.setStatus("current")
_DevSn_Type = DisplayString
_DevSn_Object = MibScalar
devSn = _DevSn_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 13),
    _DevSn_Type()
)
devSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSn.setStatus("current")
_SaveConfig_Type = Integer32
_SaveConfig_Object = MibScalar
saveConfig = _SaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 14),
    _SaveConfig_Type()
)
saveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    saveConfig.setStatus("current")


class _SaveConfigStatus_Type(Integer32):
    """Custom type saveConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 0),
          ("success", 1),
          ("inProcess", 2))
    )


_SaveConfigStatus_Type.__name__ = "Integer32"
_SaveConfigStatus_Object = MibScalar
saveConfigStatus = _SaveConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 1, 15),
    _SaveConfigStatus_Type()
)
saveConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    saveConfigStatus.setStatus("current")
_OltObjects_ObjectIdentity = ObjectIdentity
oltObjects = _OltObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    oltObjects.setStatus("current")
_OltPropertyTable_Object = MibTable
oltPropertyTable = _OltPropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    oltPropertyTable.setStatus("current")
_OltPropertyEntry_Object = MibTableRow
oltPropertyEntry = _OltPropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1)
)
oltPropertyEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "oltDeviceIndex"),
)
if mibBuilder.loadTexts:
    oltPropertyEntry.setStatus("current")


class _OltDeviceIndex_Type(Integer32):
    """Custom type oltDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OltDeviceIndex_Type.__name__ = "Integer32"
_OltDeviceIndex_Object = MibTableColumn
oltDeviceIndex = _OltDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1, 1),
    _OltDeviceIndex_Type()
)
oltDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltDeviceIndex.setStatus("current")
_OltName_Type = DisplayString
_OltName_Object = MibTableColumn
oltName = _OltName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1, 2),
    _OltName_Type()
)
oltName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltName.setStatus("current")
_OltType_Type = DisplayString
_OltType_Object = MibTableColumn
oltType = _OltType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1, 3),
    _OltType_Type()
)
oltType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltType.setStatus("current")


class _OltAdminStatus_Type(Integer32):
    """Custom type oltAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_OltAdminStatus_Type.__name__ = "Integer32"
_OltAdminStatus_Object = MibTableColumn
oltAdminStatus = _OltAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1, 4),
    _OltAdminStatus_Type()
)
oltAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltAdminStatus.setStatus("current")
_OltDeviceUpTime_Type = TimeStamp
_OltDeviceUpTime_Object = MibTableColumn
oltDeviceUpTime = _OltDeviceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1, 5),
    _OltDeviceUpTime_Type()
)
oltDeviceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltDeviceUpTime.setStatus("current")
_OltDeviceNumOfTotalServiceSlot_Type = Integer32
_OltDeviceNumOfTotalServiceSlot_Object = MibTableColumn
oltDeviceNumOfTotalServiceSlot = _OltDeviceNumOfTotalServiceSlot_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1, 6),
    _OltDeviceNumOfTotalServiceSlot_Type()
)
oltDeviceNumOfTotalServiceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltDeviceNumOfTotalServiceSlot.setStatus("current")
_OltDeviceNumOfTotalPowerSlot_Type = Integer32
_OltDeviceNumOfTotalPowerSlot_Object = MibTableColumn
oltDeviceNumOfTotalPowerSlot = _OltDeviceNumOfTotalPowerSlot_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1, 7),
    _OltDeviceNumOfTotalPowerSlot_Type()
)
oltDeviceNumOfTotalPowerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltDeviceNumOfTotalPowerSlot.setStatus("current")
_OltDeviceNumOfTotalFanSlot_Type = Integer32
_OltDeviceNumOfTotalFanSlot_Object = MibTableColumn
oltDeviceNumOfTotalFanSlot = _OltDeviceNumOfTotalFanSlot_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1, 8),
    _OltDeviceNumOfTotalFanSlot_Type()
)
oltDeviceNumOfTotalFanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltDeviceNumOfTotalFanSlot.setStatus("current")


class _OltDeviceStyle_Type(Integer32):
    """Custom type oltDeviceStyle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("chassisBased", 2),
          ("other", 3))
    )


_OltDeviceStyle_Type.__name__ = "Integer32"
_OltDeviceStyle_Object = MibTableColumn
oltDeviceStyle = _OltDeviceStyle_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 2, 1, 1, 9),
    _OltDeviceStyle_Type()
)
oltDeviceStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltDeviceStyle.setStatus("current")
_BoardObjects_ObjectIdentity = ObjectIdentity
boardObjects = _BoardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3)
)
if mibBuilder.loadTexts:
    boardObjects.setStatus("current")
_BoardTable_Object = MibTable
boardTable = _BoardTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    boardTable.setStatus("current")
_BoardEntry_Object = MibTableRow
boardEntry = _BoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1)
)
boardEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "bDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "bCardIndex"),
)
if mibBuilder.loadTexts:
    boardEntry.setStatus("current")


class _BDeviceIndex_Type(Integer32):
    """Custom type bDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BDeviceIndex_Type.__name__ = "Integer32"
_BDeviceIndex_Object = MibTableColumn
bDeviceIndex = _BDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 1),
    _BDeviceIndex_Type()
)
bDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bDeviceIndex.setStatus("current")


class _BCardIndex_Type(EponCardIndex):
    """Custom type bCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BCardIndex_Type.__name__ = "EponCardIndex"
_BCardIndex_Object = MibTableColumn
bCardIndex = _BCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 2),
    _BCardIndex_Type()
)
bCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bCardIndex.setStatus("current")


class _BType_Type(Integer32):
    """Custom type bType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("controlBoard", 1),
          ("geponBoard", 2),
          ("uplinkBoard", 3),
          ("switchBoard", 4),
          ("other", 5),
          ("vacant", 6))
    )


_BType_Type.__name__ = "Integer32"
_BType_Object = MibTableColumn
bType = _BType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 3),
    _BType_Type()
)
bType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bType.setStatus("current")


class _BAttribute_Type(Integer32):
    """Custom type bAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("standalone", 3),
          ("notApplicable", 4))
    )


_BAttribute_Type.__name__ = "Integer32"
_BAttribute_Object = MibTableColumn
bAttribute = _BAttribute_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 4),
    _BAttribute_Type()
)
bAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAttribute.setStatus("current")


class _BOperationStatus_Type(Integer32):
    """Custom type bOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_BOperationStatus_Type.__name__ = "Integer32"
_BOperationStatus_Object = MibTableColumn
bOperationStatus = _BOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 5),
    _BOperationStatus_Type()
)
bOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bOperationStatus.setStatus("current")


class _BAdminStatus_Type(Integer32):
    """Custom type bAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_BAdminStatus_Type.__name__ = "Integer32"
_BAdminStatus_Object = MibTableColumn
bAdminStatus = _BAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 6),
    _BAdminStatus_Type()
)
bAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bAdminStatus.setStatus("current")
_BHardwareVersion_Type = DisplayString
_BHardwareVersion_Object = MibTableColumn
bHardwareVersion = _BHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 7),
    _BHardwareVersion_Type()
)
bHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHardwareVersion.setStatus("current")
_BFirmwareVersion_Type = DisplayString
_BFirmwareVersion_Object = MibTableColumn
bFirmwareVersion = _BFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 8),
    _BFirmwareVersion_Type()
)
bFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bFirmwareVersion.setStatus("current")
_BSoftwareVersion_Type = DisplayString
_BSoftwareVersion_Object = MibTableColumn
bSoftwareVersion = _BSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 9),
    _BSoftwareVersion_Type()
)
bSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSoftwareVersion.setStatus("current")
_BUpTime_Type = TimeStamp
_BUpTime_Object = MibTableColumn
bUpTime = _BUpTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 10),
    _BUpTime_Type()
)
bUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bUpTime.setStatus("current")


class _BAlarmStatus_Type(Bits):
    """Custom type bAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("warning", 3))
    )

_BAlarmStatus_Type.__name__ = "Bits"
_BAlarmStatus_Object = MibTableColumn
bAlarmStatus = _BAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 11),
    _BAlarmStatus_Type()
)
bAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bAlarmStatus.setStatus("current")
_BSerialNumber_Type = DisplayString
_BSerialNumber_Object = MibTableColumn
bSerialNumber = _BSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 12),
    _BSerialNumber_Type()
)
bSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSerialNumber.setStatus("current")


class _BAction_Type(Integer32):
    """Custom type bAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("switchover", 2),
          ("upgrade", 3))
    )


_BAction_Type.__name__ = "Integer32"
_BAction_Object = MibTableColumn
bAction = _BAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 13),
    _BAction_Type()
)
bAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bAction.setStatus("current")


class _BName_Type(OctetString):
    """Custom type bName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BName_Type.__name__ = "OctetString"
_BName_Object = MibTableColumn
bName = _BName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 14),
    _BName_Type()
)
bName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bName.setStatus("current")


class _BPresenceStatus_Type(Integer32):
    """Custom type bPresenceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2),
          ("others", 3))
    )


_BPresenceStatus_Type.__name__ = "Integer32"
_BPresenceStatus_Object = MibTableColumn
bPresenceStatus = _BPresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 3, 1, 1, 15),
    _BPresenceStatus_Type()
)
bPresenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bPresenceStatus.setStatus("current")
_PowerObjects_ObjectIdentity = ObjectIdentity
powerObjects = _PowerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4)
)
if mibBuilder.loadTexts:
    powerObjects.setStatus("current")
_PowerPropertyTable_Object = MibTable
powerPropertyTable = _PowerPropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    powerPropertyTable.setStatus("current")
_PowerPropertyEntry_Object = MibTableRow
powerPropertyEntry = _PowerPropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1, 1)
)
powerPropertyEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "powerDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "powerCardIndex"),
)
if mibBuilder.loadTexts:
    powerPropertyEntry.setStatus("current")


class _PowerDeviceIndex_Type(Integer32):
    """Custom type powerDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PowerDeviceIndex_Type.__name__ = "Integer32"
_PowerDeviceIndex_Object = MibTableColumn
powerDeviceIndex = _PowerDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1, 1, 1),
    _PowerDeviceIndex_Type()
)
powerDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerDeviceIndex.setStatus("current")
_PowerCardIndex_Type = EponCardIndex
_PowerCardIndex_Object = MibTableColumn
powerCardIndex = _PowerCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1, 1, 2),
    _PowerCardIndex_Type()
)
powerCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerCardIndex.setStatus("current")


class _PowerCardOperationStatus_Type(Integer32):
    """Custom type powerCardOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_PowerCardOperationStatus_Type.__name__ = "Integer32"
_PowerCardOperationStatus_Object = MibTableColumn
powerCardOperationStatus = _PowerCardOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1, 1, 3),
    _PowerCardOperationStatus_Type()
)
powerCardOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCardOperationStatus.setStatus("current")


class _PowerCardAlarmStatus_Type(Bits):
    """Custom type powerCardAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("warning", 3))
    )

_PowerCardAlarmStatus_Type.__name__ = "Bits"
_PowerCardAlarmStatus_Object = MibTableColumn
powerCardAlarmStatus = _PowerCardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1, 1, 4),
    _PowerCardAlarmStatus_Type()
)
powerCardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCardAlarmStatus.setStatus("current")


class _PowerCardAction_Type(Integer32):
    """Custom type powerCardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("switchover", 2))
    )


_PowerCardAction_Type.__name__ = "Integer32"
_PowerCardAction_Object = MibTableColumn
powerCardAction = _PowerCardAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1, 1, 5),
    _PowerCardAction_Type()
)
powerCardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerCardAction.setStatus("current")


class _PowerCardName_Type(OctetString):
    """Custom type powerCardName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_PowerCardName_Type.__name__ = "OctetString"
_PowerCardName_Object = MibTableColumn
powerCardName = _PowerCardName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1, 1, 6),
    _PowerCardName_Type()
)
powerCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCardName.setStatus("current")


class _PowerCardPresenceStatus_Type(Integer32):
    """Custom type powerCardPresenceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2),
          ("others", 3))
    )


_PowerCardPresenceStatus_Type.__name__ = "Integer32"
_PowerCardPresenceStatus_Object = MibTableColumn
powerCardPresenceStatus = _PowerCardPresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1, 1, 7),
    _PowerCardPresenceStatus_Type()
)
powerCardPresenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCardPresenceStatus.setStatus("current")


class _PowerCardRedundancyStatus_Type(Integer32):
    """Custom type powerCardRedundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("stanby", 2),
          ("standalone", 3),
          ("loadShareing", 4))
    )


_PowerCardRedundancyStatus_Type.__name__ = "Integer32"
_PowerCardRedundancyStatus_Object = MibTableColumn
powerCardRedundancyStatus = _PowerCardRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 4, 1, 1, 8),
    _PowerCardRedundancyStatus_Type()
)
powerCardRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerCardRedundancyStatus.setStatus("current")
_FanObjects_ObjectIdentity = ObjectIdentity
fanObjects = _FanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 5)
)
if mibBuilder.loadTexts:
    fanObjects.setStatus("current")
_FanPropertyTable_Object = MibTable
fanPropertyTable = _FanPropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    fanPropertyTable.setStatus("current")
_FanPropertyEntry_Object = MibTableRow
fanPropertyEntry = _FanPropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 5, 1, 1)
)
fanPropertyEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "fanDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "fanCardIndex"),
)
if mibBuilder.loadTexts:
    fanPropertyEntry.setStatus("current")


class _FanDeviceIndex_Type(Integer32):
    """Custom type fanDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanDeviceIndex_Type.__name__ = "Integer32"
_FanDeviceIndex_Object = MibTableColumn
fanDeviceIndex = _FanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 5, 1, 1, 1),
    _FanDeviceIndex_Type()
)
fanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanDeviceIndex.setStatus("current")


class _FanCardIndex_Type(EponCardIndex):
    """Custom type fanCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FanCardIndex_Type.__name__ = "EponCardIndex"
_FanCardIndex_Object = MibTableColumn
fanCardIndex = _FanCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 5, 1, 1, 2),
    _FanCardIndex_Type()
)
fanCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanCardIndex.setStatus("current")


class _FanCardOperationStatus_Type(Integer32):
    """Custom type fanCardOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_FanCardOperationStatus_Type.__name__ = "Integer32"
_FanCardOperationStatus_Object = MibTableColumn
fanCardOperationStatus = _FanCardOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 5, 1, 1, 3),
    _FanCardOperationStatus_Type()
)
fanCardOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardOperationStatus.setStatus("current")


class _FanCardAlarmStatus_Type(Bits):
    """Custom type fanCardAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("warning", 3))
    )

_FanCardAlarmStatus_Type.__name__ = "Bits"
_FanCardAlarmStatus_Object = MibTableColumn
fanCardAlarmStatus = _FanCardAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 5, 1, 1, 4),
    _FanCardAlarmStatus_Type()
)
fanCardAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardAlarmStatus.setStatus("current")


class _FanCardName_Type(OctetString):
    """Custom type fanCardName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FanCardName_Type.__name__ = "OctetString"
_FanCardName_Object = MibTableColumn
fanCardName = _FanCardName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 5, 1, 1, 5),
    _FanCardName_Type()
)
fanCardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardName.setStatus("current")


class _FanCardPresenceStatus_Type(Integer32):
    """Custom type fanCardPresenceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("notInstalled", 2),
          ("others", 3))
    )


_FanCardPresenceStatus_Type.__name__ = "Integer32"
_FanCardPresenceStatus_Object = MibTableColumn
fanCardPresenceStatus = _FanCardPresenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 5, 1, 1, 6),
    _FanCardPresenceStatus_Type()
)
fanCardPresenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanCardPresenceStatus.setStatus("current")
_FileTransferManagement_ObjectIdentity = ObjectIdentity
fileTransferManagement = _FileTransferManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6)
)
if mibBuilder.loadTexts:
    fileTransferManagement.setStatus("current")
_FileTransferTable_Object = MibTable
fileTransferTable = _FileTransferTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fileTransferTable.setStatus("current")
_FileTransferEntry_Object = MibTableRow
fileTransferEntry = _FileTransferEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1)
)
fileTransferEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "fileTransferIndex"),
)
if mibBuilder.loadTexts:
    fileTransferEntry.setStatus("current")


class _FileTransferIndex_Type(Integer32):
    """Custom type fileTransferIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FileTransferIndex_Type.__name__ = "Integer32"
_FileTransferIndex_Object = MibTableColumn
fileTransferIndex = _FileTransferIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1, 1),
    _FileTransferIndex_Type()
)
fileTransferIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileTransferIndex.setStatus("current")


class _FileTransferProtocolType_Type(Integer32):
    """Custom type fileTransferProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("tftp", 2))
    )


_FileTransferProtocolType_Type.__name__ = "Integer32"
_FileTransferProtocolType_Object = MibTableColumn
fileTransferProtocolType = _FileTransferProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1, 2),
    _FileTransferProtocolType_Type()
)
fileTransferProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileTransferProtocolType.setStatus("current")
_ServerIpAddress_Type = IpAddress
_ServerIpAddress_Object = MibTableColumn
serverIpAddress = _ServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1, 3),
    _ServerIpAddress_Type()
)
serverIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverIpAddress.setStatus("current")
_FtpUserName_Type = DisplayString
_FtpUserName_Object = MibTableColumn
ftpUserName = _FtpUserName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1, 4),
    _FtpUserName_Type()
)
ftpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUserName.setStatus("current")
_FtpUserPassword_Type = DisplayString
_FtpUserPassword_Object = MibTableColumn
ftpUserPassword = _FtpUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1, 5),
    _FtpUserPassword_Type()
)
ftpUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUserPassword.setStatus("current")
_TransferFileSrcNamePath_Type = DisplayString
_TransferFileSrcNamePath_Object = MibTableColumn
transferFileSrcNamePath = _TransferFileSrcNamePath_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1, 6),
    _TransferFileSrcNamePath_Type()
)
transferFileSrcNamePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferFileSrcNamePath.setStatus("current")
_TransferFileDstNamePath_Type = DisplayString
_TransferFileDstNamePath_Object = MibTableColumn
transferFileDstNamePath = _TransferFileDstNamePath_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1, 7),
    _TransferFileDstNamePath_Type()
)
transferFileDstNamePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferFileDstNamePath.setStatus("current")


class _TransferAction_Type(Integer32):
    """Custom type transferAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("put", 2),
          ("get", 3),
          ("halt", 4))
    )


_TransferAction_Type.__name__ = "Integer32"
_TransferAction_Object = MibTableColumn
transferAction = _TransferAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1, 8),
    _TransferAction_Type()
)
transferAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferAction.setStatus("current")


class _TransferStatus_Type(Integer32):
    """Custom type transferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failure", 4))
    )


_TransferStatus_Type.__name__ = "Integer32"
_TransferStatus_Object = MibTableColumn
transferStatus = _TransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 1, 1, 9),
    _TransferStatus_Type()
)
transferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferStatus.setStatus("current")
_FileInfoManagementTable_Object = MibTable
fileInfoManagementTable = _FileInfoManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 2)
)
if mibBuilder.loadTexts:
    fileInfoManagementTable.setStatus("current")
_FileInfoManagementEntry_Object = MibTableRow
fileInfoManagementEntry = _FileInfoManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 2, 1)
)
fileInfoManagementEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "filePath"),
    (0, "NSCRTV-FTTX-EPON-MIB", "fileName"),
)
if mibBuilder.loadTexts:
    fileInfoManagementEntry.setStatus("current")
_FilePath_Type = DisplayString
_FilePath_Object = MibTableColumn
filePath = _FilePath_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 2, 1, 1),
    _FilePath_Type()
)
filePath.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filePath.setStatus("current")
_FileName_Type = DisplayString
_FileName_Object = MibTableColumn
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 2, 1, 2),
    _FileName_Type()
)
fileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileName.setStatus("current")
_FileSize_Type = Counter32
_FileSize_Object = MibTableColumn
fileSize = _FileSize_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 2, 1, 3),
    _FileSize_Type()
)
fileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSize.setStatus("current")
if mibBuilder.loadTexts:
    fileSize.setUnits("bytes")
_FileModifyTime_Type = DateAndTime
_FileModifyTime_Object = MibTableColumn
fileModifyTime = _FileModifyTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 2, 1, 4),
    _FileModifyTime_Type()
)
fileModifyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileModifyTime.setStatus("current")


class _FileManagementAction_Type(Integer32):
    """Custom type fileManagementAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("erase", 2))
    )


_FileManagementAction_Type.__name__ = "Integer32"
_FileManagementAction_Object = MibTableColumn
fileManagementAction = _FileManagementAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 2, 1, 5),
    _FileManagementAction_Type()
)
fileManagementAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileManagementAction.setStatus("current")


class _FileAttribute_Type(Integer32):
    """Custom type fileAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("dir", 2))
    )


_FileAttribute_Type.__name__ = "Integer32"
_FileAttribute_Object = MibTableColumn
fileAttribute = _FileAttribute_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 6, 2, 1, 6),
    _FileAttribute_Type()
)
fileAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAttribute.setStatus("current")
_OnuBatchUpgradeTable_Object = MibTable
onuBatchUpgradeTable = _OnuBatchUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 7)
)
if mibBuilder.loadTexts:
    onuBatchUpgradeTable.setStatus("current")
_OnuBatchUpgradeEntry_Object = MibTableRow
onuBatchUpgradeEntry = _OnuBatchUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 7, 1)
)
onuBatchUpgradeEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuBatchUpgradeIndex"),
)
if mibBuilder.loadTexts:
    onuBatchUpgradeEntry.setStatus("current")


class _OnuBatchUpgradeIndex_Type(Integer32):
    """Custom type onuBatchUpgradeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_OnuBatchUpgradeIndex_Type.__name__ = "Integer32"
_OnuBatchUpgradeIndex_Object = MibTableColumn
onuBatchUpgradeIndex = _OnuBatchUpgradeIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 7, 1, 1),
    _OnuBatchUpgradeIndex_Type()
)
onuBatchUpgradeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuBatchUpgradeIndex.setStatus("current")
_OnuBatchUpgradeOnuList_Type = OctetString
_OnuBatchUpgradeOnuList_Object = MibTableColumn
onuBatchUpgradeOnuList = _OnuBatchUpgradeOnuList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 7, 1, 2),
    _OnuBatchUpgradeOnuList_Type()
)
onuBatchUpgradeOnuList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuBatchUpgradeOnuList.setStatus("current")
_OnuBatchUpgradeAction_Type = Integer32
_OnuBatchUpgradeAction_Object = MibTableColumn
onuBatchUpgradeAction = _OnuBatchUpgradeAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 7, 1, 3),
    _OnuBatchUpgradeAction_Type()
)
onuBatchUpgradeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuBatchUpgradeAction.setStatus("current")
_OnuBatchUpgradeStatus_Type = OctetString
_OnuBatchUpgradeStatus_Object = MibTableColumn
onuBatchUpgradeStatus = _OnuBatchUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 7, 1, 4),
    _OnuBatchUpgradeStatus_Type()
)
onuBatchUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuBatchUpgradeStatus.setStatus("current")
_OnuBatchUpgradeImageName_Type = DisplayString
_OnuBatchUpgradeImageName_Object = MibTableColumn
onuBatchUpgradeImageName = _OnuBatchUpgradeImageName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 1, 7, 1, 5),
    _OnuBatchUpgradeImageName_Type()
)
onuBatchUpgradeImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuBatchUpgradeImageName.setStatus("current")
_SniObjects_ObjectIdentity = ObjectIdentity
sniObjects = _SniObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2)
)
_SniAttributeTable_Object = MibTable
sniAttributeTable = _SniAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sniAttributeTable.setStatus("current")
_SniAttributeEntry_Object = MibTableRow
sniAttributeEntry = _SniAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1)
)
sniAttributeEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "sniAttributeDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "sniAttributeCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "sniAttributePortIndex"),
)
if mibBuilder.loadTexts:
    sniAttributeEntry.setStatus("current")


class _SniAttributeDeviceIndex_Type(Integer32):
    """Custom type sniAttributeDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniAttributeDeviceIndex_Type.__name__ = "Integer32"
_SniAttributeDeviceIndex_Object = MibTableColumn
sniAttributeDeviceIndex = _SniAttributeDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 1),
    _SniAttributeDeviceIndex_Type()
)
sniAttributeDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniAttributeDeviceIndex.setStatus("current")


class _SniAttributeCardIndex_Type(EponCardIndex):
    """Custom type sniAttributeCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniAttributeCardIndex_Type.__name__ = "EponCardIndex"
_SniAttributeCardIndex_Object = MibTableColumn
sniAttributeCardIndex = _SniAttributeCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 2),
    _SniAttributeCardIndex_Type()
)
sniAttributeCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniAttributeCardIndex.setStatus("current")


class _SniAttributePortIndex_Type(EponPortIndex):
    """Custom type sniAttributePortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniAttributePortIndex_Type.__name__ = "EponPortIndex"
_SniAttributePortIndex_Object = MibTableColumn
sniAttributePortIndex = _SniAttributePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 3),
    _SniAttributePortIndex_Type()
)
sniAttributePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniAttributePortIndex.setStatus("current")
_SniPortName_Type = DisplayString
_SniPortName_Object = MibTableColumn
sniPortName = _SniPortName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 4),
    _SniPortName_Type()
)
sniPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniPortName.setStatus("current")


class _SniAdminStatus_Type(Integer32):
    """Custom type sniAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_SniAdminStatus_Type.__name__ = "Integer32"
_SniAdminStatus_Object = MibTableColumn
sniAdminStatus = _SniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 5),
    _SniAdminStatus_Type()
)
sniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniAdminStatus.setStatus("current")


class _SniOperationStatus_Type(Integer32):
    """Custom type sniOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_SniOperationStatus_Type.__name__ = "Integer32"
_SniOperationStatus_Object = MibTableColumn
sniOperationStatus = _SniOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 6),
    _SniOperationStatus_Type()
)
sniOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniOperationStatus.setStatus("current")


class _SniMediaType_Type(Integer32):
    """Custom type sniMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("twistedPair", 1),
          ("fiber", 2),
          ("other", 3))
    )


_SniMediaType_Type.__name__ = "Integer32"
_SniMediaType_Object = MibTableColumn
sniMediaType = _SniMediaType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 7),
    _SniMediaType_Type()
)
sniMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniMediaType.setStatus("current")


class _SniAutoNegotiationStatus_Type(Integer32):
    """Custom type sniAutoNegotiationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("full-1000", 6),
          ("full-10000", 7),
          ("unknown", 8))
    )


_SniAutoNegotiationStatus_Type.__name__ = "Integer32"
_SniAutoNegotiationStatus_Object = MibTableColumn
sniAutoNegotiationStatus = _SniAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 8),
    _SniAutoNegotiationStatus_Type()
)
sniAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniAutoNegotiationStatus.setStatus("current")


class _SniAutoNegotiationMode_Type(Integer32):
    """Custom type sniAutoNegotiationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("full-1000", 6),
          ("full-10000", 7))
    )


_SniAutoNegotiationMode_Type.__name__ = "Integer32"
_SniAutoNegotiationMode_Object = MibTableColumn
sniAutoNegotiationMode = _SniAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 9),
    _SniAutoNegotiationMode_Type()
)
sniAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniAutoNegotiationMode.setStatus("current")
_SniPerfStats15minuteEnable_Type = TruthValue
_SniPerfStats15minuteEnable_Object = MibTableColumn
sniPerfStats15minuteEnable = _SniPerfStats15minuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 10),
    _SniPerfStats15minuteEnable_Type()
)
sniPerfStats15minuteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniPerfStats15minuteEnable.setStatus("current")
_SniPerfStats24hourEnable_Type = TruthValue
_SniPerfStats24hourEnable_Object = MibTableColumn
sniPerfStats24hourEnable = _SniPerfStats24hourEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 11),
    _SniPerfStats24hourEnable_Type()
)
sniPerfStats24hourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniPerfStats24hourEnable.setStatus("current")
_SniLastStatusChangeTime_Type = TimeTicks
_SniLastStatusChangeTime_Object = MibTableColumn
sniLastStatusChangeTime = _SniLastStatusChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 12),
    _SniLastStatusChangeTime_Type()
)
sniLastStatusChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniLastStatusChangeTime.setStatus("current")
_SniMacAddrLearnMaxNum_Type = Integer32
_SniMacAddrLearnMaxNum_Object = MibTableColumn
sniMacAddrLearnMaxNum = _SniMacAddrLearnMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 13),
    _SniMacAddrLearnMaxNum_Type()
)
sniMacAddrLearnMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMacAddrLearnMaxNum.setStatus("current")
_SniIsolationEnable_Type = TruthValue
_SniIsolationEnable_Object = MibTableColumn
sniIsolationEnable = _SniIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 14),
    _SniIsolationEnable_Type()
)
sniIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniIsolationEnable.setStatus("current")


class _SniPortType_Type(Integer32):
    """Custom type sniPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ge-Port", 1),
          ("te-Port", 2))
    )


_SniPortType_Type.__name__ = "Integer32"
_SniPortType_Object = MibTableColumn
sniPortType = _SniPortType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 1, 1, 15),
    _SniPortType_Type()
)
sniPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniPortType.setStatus("current")
_SniTrunkManagement_ObjectIdentity = ObjectIdentity
sniTrunkManagement = _SniTrunkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sniTrunkManagement.setStatus("current")
_SniTrunkGroupConfigTable_Object = MibTable
sniTrunkGroupConfigTable = _SniTrunkGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sniTrunkGroupConfigTable.setStatus("current")
_SniTrunkGroupConfigEntry_Object = MibTableRow
sniTrunkGroupConfigEntry = _SniTrunkGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1)
)
sniTrunkGroupConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "sniTrunkGroupConfigIndex"),
)
if mibBuilder.loadTexts:
    sniTrunkGroupConfigEntry.setStatus("current")


class _SniTrunkGroupConfigIndex_Type(Integer32):
    """Custom type sniTrunkGroupConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniTrunkGroupConfigIndex_Type.__name__ = "Integer32"
_SniTrunkGroupConfigIndex_Object = MibTableColumn
sniTrunkGroupConfigIndex = _SniTrunkGroupConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 1),
    _SniTrunkGroupConfigIndex_Type()
)
sniTrunkGroupConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigIndex.setStatus("current")
_SniTrunkGroupConfigName_Type = DisplayString
_SniTrunkGroupConfigName_Object = MibTableColumn
sniTrunkGroupConfigName = _SniTrunkGroupConfigName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 2),
    _SniTrunkGroupConfigName_Type()
)
sniTrunkGroupConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigName.setStatus("current")
_SniTrunkGroupConfigMember_Type = OctetString
_SniTrunkGroupConfigMember_Object = MibTableColumn
sniTrunkGroupConfigMember = _SniTrunkGroupConfigMember_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 3),
    _SniTrunkGroupConfigMember_Type()
)
sniTrunkGroupConfigMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigMember.setStatus("current")


class _SniTrunkGroupConfigPolicy_Type(Integer32):
    """Custom type sniTrunkGroupConfigPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("srcMac", 1),
          ("destMac", 2),
          ("srcMacNDestMac", 3),
          ("srcIp", 4),
          ("destIp", 5),
          ("srcIpNDestIp", 6))
    )


_SniTrunkGroupConfigPolicy_Type.__name__ = "Integer32"
_SniTrunkGroupConfigPolicy_Object = MibTableColumn
sniTrunkGroupConfigPolicy = _SniTrunkGroupConfigPolicy_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 4),
    _SniTrunkGroupConfigPolicy_Type()
)
sniTrunkGroupConfigPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigPolicy.setStatus("current")
_SniTrunkGroupConfigRowstatus_Type = RowStatus
_SniTrunkGroupConfigRowstatus_Object = MibTableColumn
sniTrunkGroupConfigRowstatus = _SniTrunkGroupConfigRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 1, 1, 5),
    _SniTrunkGroupConfigRowstatus_Type()
)
sniTrunkGroupConfigRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniTrunkGroupConfigRowstatus.setStatus("current")
_SniTrunkGroupTable_Object = MibTable
sniTrunkGroupTable = _SniTrunkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sniTrunkGroupTable.setStatus("current")
_SniTrunkGroupEntry_Object = MibTableRow
sniTrunkGroupEntry = _SniTrunkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1)
)
sniTrunkGroupEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "sniTrunkGroupIndex"),
)
if mibBuilder.loadTexts:
    sniTrunkGroupEntry.setStatus("current")


class _SniTrunkGroupIndex_Type(Integer32):
    """Custom type sniTrunkGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniTrunkGroupIndex_Type.__name__ = "Integer32"
_SniTrunkGroupIndex_Object = MibTableColumn
sniTrunkGroupIndex = _SniTrunkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1, 1),
    _SniTrunkGroupIndex_Type()
)
sniTrunkGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniTrunkGroupIndex.setStatus("current")


class _SniTrunkGroupOperationStatus_Type(Integer32):
    """Custom type sniTrunkGroupOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_SniTrunkGroupOperationStatus_Type.__name__ = "Integer32"
_SniTrunkGroupOperationStatus_Object = MibTableColumn
sniTrunkGroupOperationStatus = _SniTrunkGroupOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1, 2),
    _SniTrunkGroupOperationStatus_Type()
)
sniTrunkGroupOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTrunkGroupOperationStatus.setStatus("current")
_SniTrunkGroupActualSpeed_Type = Integer32
_SniTrunkGroupActualSpeed_Object = MibTableColumn
sniTrunkGroupActualSpeed = _SniTrunkGroupActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1, 3),
    _SniTrunkGroupActualSpeed_Type()
)
sniTrunkGroupActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sniTrunkGroupActualSpeed.setStatus("current")
if mibBuilder.loadTexts:
    sniTrunkGroupActualSpeed.setUnits("Mbps")


class _SniTrunkGroupAdminStatus_Type(Integer32):
    """Custom type sniTrunkGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_SniTrunkGroupAdminStatus_Type.__name__ = "Integer32"
_SniTrunkGroupAdminStatus_Object = MibTableColumn
sniTrunkGroupAdminStatus = _SniTrunkGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 2, 2, 1, 4),
    _SniTrunkGroupAdminStatus_Type()
)
sniTrunkGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniTrunkGroupAdminStatus.setStatus("current")
_SniMirrorTable_Object = MibTable
sniMirrorTable = _SniMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3)
)
if mibBuilder.loadTexts:
    sniMirrorTable.setStatus("current")
_SniMirrorEntry_Object = MibTableRow
sniMirrorEntry = _SniMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1)
)
sniMirrorEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "sniMirrorGroupIndex"),
)
if mibBuilder.loadTexts:
    sniMirrorEntry.setStatus("current")


class _SniMirrorGroupIndex_Type(Integer32):
    """Custom type sniMirrorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniMirrorGroupIndex_Type.__name__ = "Integer32"
_SniMirrorGroupIndex_Object = MibTableColumn
sniMirrorGroupIndex = _SniMirrorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 1),
    _SniMirrorGroupIndex_Type()
)
sniMirrorGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniMirrorGroupIndex.setStatus("current")
_SniMirrorGroupName_Type = DisplayString
_SniMirrorGroupName_Object = MibTableColumn
sniMirrorGroupName = _SniMirrorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 2),
    _SniMirrorGroupName_Type()
)
sniMirrorGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupName.setStatus("current")
_SniMirrorGroupDstPortList_Type = OctetString
_SniMirrorGroupDstPortList_Object = MibTableColumn
sniMirrorGroupDstPortList = _SniMirrorGroupDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 3),
    _SniMirrorGroupDstPortList_Type()
)
sniMirrorGroupDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupDstPortList.setStatus("current")
_SniMirrorGroupSrcInPortList_Type = OctetString
_SniMirrorGroupSrcInPortList_Object = MibTableColumn
sniMirrorGroupSrcInPortList = _SniMirrorGroupSrcInPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 4),
    _SniMirrorGroupSrcInPortList_Type()
)
sniMirrorGroupSrcInPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupSrcInPortList.setStatus("current")
_SniMirrorGroupSrcOutPortList_Type = OctetString
_SniMirrorGroupSrcOutPortList_Object = MibTableColumn
sniMirrorGroupSrcOutPortList = _SniMirrorGroupSrcOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 5),
    _SniMirrorGroupSrcOutPortList_Type()
)
sniMirrorGroupSrcOutPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupSrcOutPortList.setStatus("current")
_SniMirrorGroupRowstatus_Type = RowStatus
_SniMirrorGroupRowstatus_Object = MibTableColumn
sniMirrorGroupRowstatus = _SniMirrorGroupRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 3, 1, 6),
    _SniMirrorGroupRowstatus_Type()
)
sniMirrorGroupRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMirrorGroupRowstatus.setStatus("current")
_SniMacAddressManagement_ObjectIdentity = ObjectIdentity
sniMacAddressManagement = _SniMacAddressManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4)
)
if mibBuilder.loadTexts:
    sniMacAddressManagement.setStatus("current")
_SniMacAddressManagementTable_Object = MibTable
sniMacAddressManagementTable = _SniMacAddressManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sniMacAddressManagementTable.setStatus("current")
_SniMacAddressManagementEntry_Object = MibTableRow
sniMacAddressManagementEntry = _SniMacAddressManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1, 1)
)
sniMacAddressManagementEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "sniMacAddressManagementDeviceIndex"),
)
if mibBuilder.loadTexts:
    sniMacAddressManagementEntry.setStatus("current")


class _SniMacAddressManagementDeviceIndex_Type(Integer32):
    """Custom type sniMacAddressManagementDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniMacAddressManagementDeviceIndex_Type.__name__ = "Integer32"
_SniMacAddressManagementDeviceIndex_Object = MibTableColumn
sniMacAddressManagementDeviceIndex = _SniMacAddressManagementDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1, 1, 1),
    _SniMacAddressManagementDeviceIndex_Type()
)
sniMacAddressManagementDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniMacAddressManagementDeviceIndex.setStatus("current")


class _SniMacAddrTableAgingTime_Type(Integer32):
    """Custom type sniMacAddrTableAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_SniMacAddrTableAgingTime_Type.__name__ = "Integer32"
_SniMacAddrTableAgingTime_Object = MibTableColumn
sniMacAddrTableAgingTime = _SniMacAddrTableAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1, 1, 2),
    _SniMacAddrTableAgingTime_Type()
)
sniMacAddrTableAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMacAddrTableAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    sniMacAddrTableAgingTime.setUnits("Seconds")


class _SniMacAddrTableClear_Type(Integer32):
    """Custom type sniMacAddrTableClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allDynamic", 1),
          ("allStatic", 2),
          ("allBlackhole", 3),
          ("all", 4),
          ("none", 5))
    )


_SniMacAddrTableClear_Type.__name__ = "Integer32"
_SniMacAddrTableClear_Object = MibTableColumn
sniMacAddrTableClear = _SniMacAddrTableClear_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 1, 1, 3),
    _SniMacAddrTableClear_Type()
)
sniMacAddrTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMacAddrTableClear.setStatus("current")
_SniMacAddressTable_Object = MibTable
sniMacAddressTable = _SniMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2)
)
if mibBuilder.loadTexts:
    sniMacAddressTable.setStatus("current")
_SniMacAddressEntry_Object = MibTableRow
sniMacAddressEntry = _SniMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1)
)
sniMacAddressEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "sniMacAddrIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "sniMacAddrVlanIdIndex"),
)
if mibBuilder.loadTexts:
    sniMacAddressEntry.setStatus("current")
_SniMacAddrIndex_Type = MacAddress
_SniMacAddrIndex_Object = MibTableColumn
sniMacAddrIndex = _SniMacAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 1),
    _SniMacAddrIndex_Type()
)
sniMacAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniMacAddrIndex.setStatus("current")


class _SniMacAddrVlanIdIndex_Type(Integer32):
    """Custom type sniMacAddrVlanIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SniMacAddrVlanIdIndex_Type.__name__ = "Integer32"
_SniMacAddrVlanIdIndex_Object = MibTableColumn
sniMacAddrVlanIdIndex = _SniMacAddrVlanIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 2),
    _SniMacAddrVlanIdIndex_Type()
)
sniMacAddrVlanIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniMacAddrVlanIdIndex.setStatus("current")


class _SniMacAddrType_Type(Integer32):
    """Custom type sniMacAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("blackhole", 3))
    )


_SniMacAddrType_Type.__name__ = "Integer32"
_SniMacAddrType_Object = MibTableColumn
sniMacAddrType = _SniMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 3),
    _SniMacAddrType_Type()
)
sniMacAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMacAddrType.setStatus("current")
_SniMacAddrPortId_Type = EponDeviceIndex
_SniMacAddrPortId_Object = MibTableColumn
sniMacAddrPortId = _SniMacAddrPortId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 4),
    _SniMacAddrPortId_Type()
)
sniMacAddrPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMacAddrPortId.setStatus("current")
_SniMacAddrRowStatus_Type = RowStatus
_SniMacAddrRowStatus_Object = MibTableColumn
sniMacAddrRowStatus = _SniMacAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 4, 2, 1, 5),
    _SniMacAddrRowStatus_Type()
)
sniMacAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMacAddrRowStatus.setStatus("current")
_SniBroadcastStormSuppressionTable_Object = MibTable
sniBroadcastStormSuppressionTable = _SniBroadcastStormSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5)
)
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionTable.setStatus("current")
_SniBroadcastStormSuppressionEntry_Object = MibTableRow
sniBroadcastStormSuppressionEntry = _SniBroadcastStormSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1)
)
sniBroadcastStormSuppressionEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "sniBroadcastStormSuppressionDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "sniBroadcastStormSuppressionCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "sniBroadcastStormSuppressionPortIndex"),
)
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionEntry.setStatus("current")


class _SniBroadcastStormSuppressionDeviceIndex_Type(Integer32):
    """Custom type sniBroadcastStormSuppressionDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniBroadcastStormSuppressionDeviceIndex_Type.__name__ = "Integer32"
_SniBroadcastStormSuppressionDeviceIndex_Object = MibTableColumn
sniBroadcastStormSuppressionDeviceIndex = _SniBroadcastStormSuppressionDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 1),
    _SniBroadcastStormSuppressionDeviceIndex_Type()
)
sniBroadcastStormSuppressionDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionDeviceIndex.setStatus("current")


class _SniBroadcastStormSuppressionCardIndex_Type(EponCardIndex):
    """Custom type sniBroadcastStormSuppressionCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniBroadcastStormSuppressionCardIndex_Type.__name__ = "EponCardIndex"
_SniBroadcastStormSuppressionCardIndex_Object = MibTableColumn
sniBroadcastStormSuppressionCardIndex = _SniBroadcastStormSuppressionCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 2),
    _SniBroadcastStormSuppressionCardIndex_Type()
)
sniBroadcastStormSuppressionCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionCardIndex.setStatus("current")


class _SniBroadcastStormSuppressionPortIndex_Type(EponPortIndex):
    """Custom type sniBroadcastStormSuppressionPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SniBroadcastStormSuppressionPortIndex_Type.__name__ = "EponPortIndex"
_SniBroadcastStormSuppressionPortIndex_Object = MibTableColumn
sniBroadcastStormSuppressionPortIndex = _SniBroadcastStormSuppressionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 3),
    _SniBroadcastStormSuppressionPortIndex_Type()
)
sniBroadcastStormSuppressionPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniBroadcastStormSuppressionPortIndex.setStatus("current")
_SniUnicastStormEnable_Type = TruthValue
_SniUnicastStormEnable_Object = MibTableColumn
sniUnicastStormEnable = _SniUnicastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 4),
    _SniUnicastStormEnable_Type()
)
sniUnicastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniUnicastStormEnable.setStatus("current")
_SniUnicastStormInPacketRate_Type = Integer32
_SniUnicastStormInPacketRate_Object = MibTableColumn
sniUnicastStormInPacketRate = _SniUnicastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 5),
    _SniUnicastStormInPacketRate_Type()
)
sniUnicastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniUnicastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniUnicastStormInPacketRate.setUnits("pps")
_SniUnicastStormOutPacketRate_Type = Integer32
_SniUnicastStormOutPacketRate_Object = MibTableColumn
sniUnicastStormOutPacketRate = _SniUnicastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 6),
    _SniUnicastStormOutPacketRate_Type()
)
sniUnicastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniUnicastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniUnicastStormOutPacketRate.setUnits("pps")
_SniMulticastStormEnable_Type = TruthValue
_SniMulticastStormEnable_Object = MibTableColumn
sniMulticastStormEnable = _SniMulticastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 7),
    _SniMulticastStormEnable_Type()
)
sniMulticastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMulticastStormEnable.setStatus("current")
_SniMulticastStormInPacketRate_Type = Integer32
_SniMulticastStormInPacketRate_Object = MibTableColumn
sniMulticastStormInPacketRate = _SniMulticastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 8),
    _SniMulticastStormInPacketRate_Type()
)
sniMulticastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMulticastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniMulticastStormInPacketRate.setUnits("pps")
_SniMulticastStormOutPacketRate_Type = Integer32
_SniMulticastStormOutPacketRate_Object = MibTableColumn
sniMulticastStormOutPacketRate = _SniMulticastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 9),
    _SniMulticastStormOutPacketRate_Type()
)
sniMulticastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniMulticastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniMulticastStormOutPacketRate.setUnits("pps")
_SniBroadcastStormEnable_Type = TruthValue
_SniBroadcastStormEnable_Object = MibTableColumn
sniBroadcastStormEnable = _SniBroadcastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 10),
    _SniBroadcastStormEnable_Type()
)
sniBroadcastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniBroadcastStormEnable.setStatus("current")
_SniBroadcastStormInPacketRate_Type = Integer32
_SniBroadcastStormInPacketRate_Object = MibTableColumn
sniBroadcastStormInPacketRate = _SniBroadcastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 11),
    _SniBroadcastStormInPacketRate_Type()
)
sniBroadcastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniBroadcastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniBroadcastStormInPacketRate.setUnits("pps")
_SniBroadcastStormOutPacketRate_Type = Integer32
_SniBroadcastStormOutPacketRate_Object = MibTableColumn
sniBroadcastStormOutPacketRate = _SniBroadcastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 2, 5, 1, 12),
    _SniBroadcastStormOutPacketRate_Type()
)
sniBroadcastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sniBroadcastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    sniBroadcastStormOutPacketRate.setUnits("pps")
_PonPortObjects_ObjectIdentity = ObjectIdentity
ponPortObjects = _PonPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3)
)
_PonPortInfoTable_Object = MibTable
ponPortInfoTable = _PonPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    ponPortInfoTable.setStatus("current")
_PonPortInfoEntry_Object = MibTableRow
ponPortInfoEntry = _PonPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1)
)
ponPortInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "ponDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "ponCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "ponPortIndex"),
)
if mibBuilder.loadTexts:
    ponPortInfoEntry.setStatus("current")


class _PonDeviceIndex_Type(Integer32):
    """Custom type ponDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonDeviceIndex_Type.__name__ = "Integer32"
_PonDeviceIndex_Object = MibTableColumn
ponDeviceIndex = _PonDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 1),
    _PonDeviceIndex_Type()
)
ponDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ponDeviceIndex.setStatus("current")


class _PonCardIndex_Type(EponCardIndex):
    """Custom type ponCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonCardIndex_Type.__name__ = "EponCardIndex"
_PonCardIndex_Object = MibTableColumn
ponCardIndex = _PonCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 2),
    _PonCardIndex_Type()
)
ponCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ponCardIndex.setStatus("current")


class _PonPortIndex_Type(EponPortIndex):
    """Custom type ponPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonPortIndex_Type.__name__ = "EponPortIndex"
_PonPortIndex_Object = MibTableColumn
ponPortIndex = _PonPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 3),
    _PonPortIndex_Type()
)
ponPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ponPortIndex.setStatus("current")


class _PonPortType_Type(Integer32):
    """Custom type ponPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ge-epon", 1),
          ("tenge-epon", 2),
          ("gpon", 3),
          ("other", 4))
    )


_PonPortType_Type.__name__ = "Integer32"
_PonPortType_Object = MibTableColumn
ponPortType = _PonPortType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 4),
    _PonPortType_Type()
)
ponPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortType.setStatus("current")


class _PonOperationStatus_Type(Integer32):
    """Custom type ponOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_PonOperationStatus_Type.__name__ = "Integer32"
_PonOperationStatus_Object = MibTableColumn
ponOperationStatus = _PonOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 5),
    _PonOperationStatus_Type()
)
ponOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponOperationStatus.setStatus("current")


class _PonPortAdminStatus_Type(Integer32):
    """Custom type ponPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_PonPortAdminStatus_Type.__name__ = "Integer32"
_PonPortAdminStatus_Object = MibTableColumn
ponPortAdminStatus = _PonPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 6),
    _PonPortAdminStatus_Type()
)
ponPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortAdminStatus.setStatus("current")
_PonPortMaxOnuNumSupport_Type = Integer32
_PonPortMaxOnuNumSupport_Object = MibTableColumn
ponPortMaxOnuNumSupport = _PonPortMaxOnuNumSupport_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 7),
    _PonPortMaxOnuNumSupport_Type()
)
ponPortMaxOnuNumSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortMaxOnuNumSupport.setStatus("current")
_PonPortUpOnuNum_Type = Integer32
_PonPortUpOnuNum_Object = MibTableColumn
ponPortUpOnuNum = _PonPortUpOnuNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 8),
    _PonPortUpOnuNum_Type()
)
ponPortUpOnuNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponPortUpOnuNum.setStatus("current")


class _PonPortEncryptMode_Type(Integer32):
    """Custom type ponPortEncryptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 1),
          ("ctcTripleChurning", 2),
          ("other", 3))
    )


_PonPortEncryptMode_Type.__name__ = "Integer32"
_PonPortEncryptMode_Object = MibTableColumn
ponPortEncryptMode = _PonPortEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 9),
    _PonPortEncryptMode_Type()
)
ponPortEncryptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortEncryptMode.setStatus("current")
_PonPortEncryptKeyExchangeTime_Type = Integer32
_PonPortEncryptKeyExchangeTime_Object = MibTableColumn
ponPortEncryptKeyExchangeTime = _PonPortEncryptKeyExchangeTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 10),
    _PonPortEncryptKeyExchangeTime_Type()
)
ponPortEncryptKeyExchangeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortEncryptKeyExchangeTime.setStatus("current")
if mibBuilder.loadTexts:
    ponPortEncryptKeyExchangeTime.setUnits("seconds")
_PonPortIsolationEnable_Type = TruthValue
_PonPortIsolationEnable_Object = MibTableColumn
ponPortIsolationEnable = _PonPortIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 11),
    _PonPortIsolationEnable_Type()
)
ponPortIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortIsolationEnable.setStatus("current")
_MaxDsBandwidth_Type = Integer32
_MaxDsBandwidth_Object = MibTableColumn
maxDsBandwidth = _MaxDsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 12),
    _MaxDsBandwidth_Type()
)
maxDsBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxDsBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    maxDsBandwidth.setUnits("kbps")
_ActualDsBandwidthInUse_Type = Integer32
_ActualDsBandwidthInUse_Object = MibTableColumn
actualDsBandwidthInUse = _ActualDsBandwidthInUse_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 13),
    _ActualDsBandwidthInUse_Type()
)
actualDsBandwidthInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualDsBandwidthInUse.setStatus("current")
if mibBuilder.loadTexts:
    actualDsBandwidthInUse.setUnits("kbps")
_RemainDsBandwidth_Type = Integer32
_RemainDsBandwidth_Object = MibTableColumn
remainDsBandwidth = _RemainDsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 14),
    _RemainDsBandwidth_Type()
)
remainDsBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remainDsBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    remainDsBandwidth.setUnits("kbps")
_PerfStats15minuteEnable_Type = TruthValue
_PerfStats15minuteEnable_Object = MibTableColumn
perfStats15minuteEnable = _PerfStats15minuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 15),
    _PerfStats15minuteEnable_Type()
)
perfStats15minuteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfStats15minuteEnable.setStatus("current")
_PerfStats24hourEnable_Type = TruthValue
_PerfStats24hourEnable_Object = MibTableColumn
perfStats24hourEnable = _PerfStats24hourEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 16),
    _PerfStats24hourEnable_Type()
)
perfStats24hourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfStats24hourEnable.setStatus("current")
_PonPortMacAddrLearnMaxNum_Type = Integer32
_PonPortMacAddrLearnMaxNum_Object = MibTableColumn
ponPortMacAddrLearnMaxNum = _PonPortMacAddrLearnMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 17),
    _PonPortMacAddrLearnMaxNum_Type()
)
ponPortMacAddrLearnMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortMacAddrLearnMaxNum.setStatus("current")
_MaxUsBandwidth_Type = Integer32
_MaxUsBandwidth_Object = MibTableColumn
maxUsBandwidth = _MaxUsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 18),
    _MaxUsBandwidth_Type()
)
maxUsBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxUsBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    maxUsBandwidth.setUnits("kbps")
_ActualUsBandwidthInUse_Type = Integer32
_ActualUsBandwidthInUse_Object = MibTableColumn
actualUsBandwidthInUse = _ActualUsBandwidthInUse_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 19),
    _ActualUsBandwidthInUse_Type()
)
actualUsBandwidthInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actualUsBandwidthInUse.setStatus("current")
if mibBuilder.loadTexts:
    actualUsBandwidthInUse.setUnits("kbps")
_RemainUsBandwidth_Type = Integer32
_RemainUsBandwidth_Object = MibTableColumn
remainUsBandwidth = _RemainUsBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 20),
    _RemainUsBandwidth_Type()
)
remainUsBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remainUsBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    remainUsBandwidth.setUnits("kbps")
_PonPortName_Type = DisplayString
_PonPortName_Object = MibTableColumn
ponPortName = _PonPortName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 21),
    _PonPortName_Type()
)
ponPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ponPortName.setStatus("current")


class _OnuLongEmitDetectEnable_Type(Integer32):
    """Custom type onuLongEmitDetectEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_OnuLongEmitDetectEnable_Type.__name__ = "Integer32"
_OnuLongEmitDetectEnable_Object = MibTableColumn
onuLongEmitDetectEnable = _OnuLongEmitDetectEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 1, 1, 22),
    _OnuLongEmitDetectEnable_Type()
)
onuLongEmitDetectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuLongEmitDetectEnable.setStatus("current")
_AclManagementGroup_ObjectIdentity = ObjectIdentity
aclManagementGroup = _AclManagementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    aclManagementGroup.setStatus("current")
_AclListTable_Object = MibTable
aclListTable = _AclListTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aclListTable.setStatus("current")
_AclListEntry_Object = MibTableRow
aclListEntry = _AclListEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 1, 1)
)
aclListEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "aclListIndex"),
)
if mibBuilder.loadTexts:
    aclListEntry.setStatus("current")


class _AclListIndex_Type(Integer32):
    """Custom type aclListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AclListIndex_Type.__name__ = "Integer32"
_AclListIndex_Object = MibTableColumn
aclListIndex = _AclListIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 1, 1, 1),
    _AclListIndex_Type()
)
aclListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclListIndex.setStatus("current")
_AclDescription_Type = DisplayString
_AclDescription_Object = MibTableColumn
aclDescription = _AclDescription_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 1, 1, 2),
    _AclDescription_Type()
)
aclDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclDescription.setStatus("current")
_RuleRowStatus_Type = RowStatus
_RuleRowStatus_Object = MibTableColumn
ruleRowStatus = _RuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 1, 1, 3),
    _RuleRowStatus_Type()
)
ruleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruleRowStatus.setStatus("current")
_AclRuleTable_Object = MibTable
aclRuleTable = _AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    aclRuleTable.setStatus("current")
_AclRuleEntry_Object = MibTableRow
aclRuleEntry = _AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1)
)
aclRuleEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "aclRuleListIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "aclRuleIndex"),
)
if mibBuilder.loadTexts:
    aclRuleEntry.setStatus("current")
_AclRuleListIndex_Type = Integer32
_AclRuleListIndex_Object = MibTableColumn
aclRuleListIndex = _AclRuleListIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 1),
    _AclRuleListIndex_Type()
)
aclRuleListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclRuleListIndex.setStatus("current")
_AclRuleIndex_Type = Integer32
_AclRuleIndex_Object = MibTableColumn
aclRuleIndex = _AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 2),
    _AclRuleIndex_Type()
)
aclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclRuleIndex.setStatus("current")
_MatchedSourseMac_Type = MacAddress
_MatchedSourseMac_Object = MibTableColumn
matchedSourseMac = _MatchedSourseMac_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 3),
    _MatchedSourseMac_Type()
)
matchedSourseMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedSourseMac.setStatus("current")
_MatchedDestinationMac_Type = MacAddress
_MatchedDestinationMac_Object = MibTableColumn
matchedDestinationMac = _MatchedDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 4),
    _MatchedDestinationMac_Type()
)
matchedDestinationMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedDestinationMac.setStatus("current")


class _MatchedVlanId_Type(Integer32):
    """Custom type matchedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MatchedVlanId_Type.__name__ = "Integer32"
_MatchedVlanId_Object = MibTableColumn
matchedVlanId = _MatchedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 5),
    _MatchedVlanId_Type()
)
matchedVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedVlanId.setStatus("current")
_MatchedEthernetType_Type = Integer32
_MatchedEthernetType_Object = MibTableColumn
matchedEthernetType = _MatchedEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 6),
    _MatchedEthernetType_Type()
)
matchedEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedEthernetType.setStatus("current")
_MatchedSourseIP_Type = IpAddress
_MatchedSourseIP_Object = MibTableColumn
matchedSourseIP = _MatchedSourseIP_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 7),
    _MatchedSourseIP_Type()
)
matchedSourseIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedSourseIP.setStatus("current")
_MatchedDestinationIP_Type = IpAddress
_MatchedDestinationIP_Object = MibTableColumn
matchedDestinationIP = _MatchedDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 8),
    _MatchedDestinationIP_Type()
)
matchedDestinationIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedDestinationIP.setStatus("current")


class _MatchedIpMessageType_Type(Integer32):
    """Custom type matchedIpMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MatchedIpMessageType_Type.__name__ = "Integer32"
_MatchedIpMessageType_Object = MibTableColumn
matchedIpMessageType = _MatchedIpMessageType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 9),
    _MatchedIpMessageType_Type()
)
matchedIpMessageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedIpMessageType.setStatus("current")


class _MatchedDscp_Type(Integer32):
    """Custom type matchedDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MatchedDscp_Type.__name__ = "Integer32"
_MatchedDscp_Object = MibTableColumn
matchedDscp = _MatchedDscp_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 10),
    _MatchedDscp_Type()
)
matchedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedDscp.setStatus("current")


class _MatchedSoursePort_Type(Integer32):
    """Custom type matchedSoursePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MatchedSoursePort_Type.__name__ = "Integer32"
_MatchedSoursePort_Object = MibTableColumn
matchedSoursePort = _MatchedSoursePort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 11),
    _MatchedSoursePort_Type()
)
matchedSoursePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedSoursePort.setStatus("current")


class _MatchedDestinationPort_Type(Integer32):
    """Custom type matchedDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MatchedDestinationPort_Type.__name__ = "Integer32"
_MatchedDestinationPort_Object = MibTableColumn
matchedDestinationPort = _MatchedDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 12),
    _MatchedDestinationPort_Type()
)
matchedDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedDestinationPort.setStatus("current")
_AclRuleRowStatus_Type = RowStatus
_AclRuleRowStatus_Object = MibTableColumn
aclRuleRowStatus = _AclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 13),
    _AclRuleRowStatus_Type()
)
aclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleRowStatus.setStatus("current")


class _MatchedFieldSelection_Type(OctetString):
    """Custom type matchedFieldSelection based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_MatchedFieldSelection_Type.__name__ = "OctetString"
_MatchedFieldSelection_Object = MibTableColumn
matchedFieldSelection = _MatchedFieldSelection_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 14),
    _MatchedFieldSelection_Type()
)
matchedFieldSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedFieldSelection.setStatus("current")


class _AclAction_Type(Integer32):
    """Custom type aclAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2),
          ("mark", 3))
    )


_AclAction_Type.__name__ = "Integer32"
_AclAction_Object = MibTableColumn
aclAction = _AclAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 15),
    _AclAction_Type()
)
aclAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAction.setStatus("current")
_AclActionParameter_Type = OctetString
_AclActionParameter_Object = MibTableColumn
aclActionParameter = _AclActionParameter_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 16),
    _AclActionParameter_Type()
)
aclActionParameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclActionParameter.setStatus("current")
_MatchedSourseMacMask_Type = MacAddress
_MatchedSourseMacMask_Object = MibTableColumn
matchedSourseMacMask = _MatchedSourseMacMask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 17),
    _MatchedSourseMacMask_Type()
)
matchedSourseMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedSourseMacMask.setStatus("current")
_MatchedDestinationMacMask_Type = MacAddress
_MatchedDestinationMacMask_Object = MibTableColumn
matchedDestinationMacMask = _MatchedDestinationMacMask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 18),
    _MatchedDestinationMacMask_Type()
)
matchedDestinationMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedDestinationMacMask.setStatus("current")
_MatchedSourseIPMask_Type = IpAddress
_MatchedSourseIPMask_Object = MibTableColumn
matchedSourseIPMask = _MatchedSourseIPMask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 19),
    _MatchedSourseIPMask_Type()
)
matchedSourseIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedSourseIPMask.setStatus("current")
_MatchedDestinationIPMask_Type = IpAddress
_MatchedDestinationIPMask_Object = MibTableColumn
matchedDestinationIPMask = _MatchedDestinationIPMask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 2, 1, 20),
    _MatchedDestinationIPMask_Type()
)
matchedDestinationIPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    matchedDestinationIPMask.setStatus("current")
_PortACLListTable_Object = MibTable
portACLListTable = _PortACLListTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    portACLListTable.setStatus("current")
_PortACLListEntry_Object = MibTableRow
portACLListEntry = _PortACLListEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 3, 1)
)
portACLListEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "aclDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "aclCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "aclPortIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "portAclListIndex"),
)
if mibBuilder.loadTexts:
    portACLListEntry.setStatus("current")


class _AclDeviceIndex_Type(EponDeviceIndex):
    """Custom type aclDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AclDeviceIndex_Type.__name__ = "EponDeviceIndex"
_AclDeviceIndex_Object = MibTableColumn
aclDeviceIndex = _AclDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 3, 1, 1),
    _AclDeviceIndex_Type()
)
aclDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclDeviceIndex.setStatus("current")


class _AclCardIndex_Type(EponCardIndex):
    """Custom type aclCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AclCardIndex_Type.__name__ = "EponCardIndex"
_AclCardIndex_Object = MibTableColumn
aclCardIndex = _AclCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 3, 1, 2),
    _AclCardIndex_Type()
)
aclCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclCardIndex.setStatus("current")


class _AclPortIndex_Type(EponPortIndex):
    """Custom type aclPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AclPortIndex_Type.__name__ = "EponPortIndex"
_AclPortIndex_Object = MibTableColumn
aclPortIndex = _AclPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 3, 1, 3),
    _AclPortIndex_Type()
)
aclPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclPortIndex.setStatus("current")


class _PortAclListIndex_Type(Integer32):
    """Custom type portAclListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortAclListIndex_Type.__name__ = "Integer32"
_PortAclListIndex_Object = MibTableColumn
portAclListIndex = _PortAclListIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 3, 1, 4),
    _PortAclListIndex_Type()
)
portAclListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portAclListIndex.setStatus("current")


class _AclPortDirection_Type(Bits):
    """Custom type aclPortDirection based on Bits"""
    namedValues = NamedValues(
        *(("ingress", 0),
          ("egress", 1))
    )

_AclPortDirection_Type.__name__ = "Bits"
_AclPortDirection_Object = MibTableColumn
aclPortDirection = _AclPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 3, 1, 5),
    _AclPortDirection_Type()
)
aclPortDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclPortDirection.setStatus("current")
_AclRowStatus_Type = RowStatus
_AclRowStatus_Object = MibTableColumn
aclRowStatus = _AclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 2, 3, 1, 6),
    _AclRowStatus_Type()
)
aclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRowStatus.setStatus("current")
_PonBroadcastStormSuppressionTable_Object = MibTable
ponBroadcastStormSuppressionTable = _PonBroadcastStormSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3)
)
if mibBuilder.loadTexts:
    ponBroadcastStormSuppressionTable.setStatus("current")
_PonBroadcastStormSuppressionEntry_Object = MibTableRow
ponBroadcastStormSuppressionEntry = _PonBroadcastStormSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1)
)
ponBroadcastStormSuppressionEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "bsDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "bsCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "bsPortIndex"),
)
if mibBuilder.loadTexts:
    ponBroadcastStormSuppressionEntry.setStatus("current")


class _BsDeviceIndex_Type(Integer32):
    """Custom type bsDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BsDeviceIndex_Type.__name__ = "Integer32"
_BsDeviceIndex_Object = MibTableColumn
bsDeviceIndex = _BsDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 1),
    _BsDeviceIndex_Type()
)
bsDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsDeviceIndex.setStatus("current")


class _BsCardIndex_Type(EponCardIndex):
    """Custom type bsCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BsCardIndex_Type.__name__ = "EponCardIndex"
_BsCardIndex_Object = MibTableColumn
bsCardIndex = _BsCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 2),
    _BsCardIndex_Type()
)
bsCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsCardIndex.setStatus("current")
_BsPortIndex_Type = EponPortIndex
_BsPortIndex_Object = MibTableColumn
bsPortIndex = _BsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 3),
    _BsPortIndex_Type()
)
bsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsPortIndex.setStatus("current")
_UnicastStormEnable_Type = TruthValue
_UnicastStormEnable_Object = MibTableColumn
unicastStormEnable = _UnicastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 4),
    _UnicastStormEnable_Type()
)
unicastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unicastStormEnable.setStatus("current")
_UnicastStormInPacketRate_Type = Integer32
_UnicastStormInPacketRate_Object = MibTableColumn
unicastStormInPacketRate = _UnicastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 5),
    _UnicastStormInPacketRate_Type()
)
unicastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unicastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    unicastStormInPacketRate.setUnits("pps")
_UnicastStormOutPacketRate_Type = Integer32
_UnicastStormOutPacketRate_Object = MibTableColumn
unicastStormOutPacketRate = _UnicastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 6),
    _UnicastStormOutPacketRate_Type()
)
unicastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unicastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    unicastStormOutPacketRate.setUnits("pps")
_MulticastStormEnable_Type = TruthValue
_MulticastStormEnable_Object = MibTableColumn
multicastStormEnable = _MulticastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 7),
    _MulticastStormEnable_Type()
)
multicastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastStormEnable.setStatus("current")
_MulticastStormInPacketRate_Type = Integer32
_MulticastStormInPacketRate_Object = MibTableColumn
multicastStormInPacketRate = _MulticastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 8),
    _MulticastStormInPacketRate_Type()
)
multicastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    multicastStormInPacketRate.setUnits("pps")
_MulticastStormOutPacketRate_Type = Integer32
_MulticastStormOutPacketRate_Object = MibTableColumn
multicastStormOutPacketRate = _MulticastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 9),
    _MulticastStormOutPacketRate_Type()
)
multicastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    multicastStormOutPacketRate.setUnits("pps")
_BroadcastStormEnable_Type = TruthValue
_BroadcastStormEnable_Object = MibTableColumn
broadcastStormEnable = _BroadcastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 10),
    _BroadcastStormEnable_Type()
)
broadcastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormEnable.setStatus("current")
_BroadcastStormInPacketRate_Type = Integer32
_BroadcastStormInPacketRate_Object = MibTableColumn
broadcastStormInPacketRate = _BroadcastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 11),
    _BroadcastStormInPacketRate_Type()
)
broadcastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    broadcastStormInPacketRate.setUnits("pps")
_BroadcastStormOutPacketRate_Type = Integer32
_BroadcastStormOutPacketRate_Object = MibTableColumn
broadcastStormOutPacketRate = _BroadcastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 3, 1, 12),
    _BroadcastStormOutPacketRate_Type()
)
broadcastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    broadcastStormOutPacketRate.setUnits("pps")
_PonOnuAuthenticationModeTable_Object = MibTable
ponOnuAuthenticationModeTable = _PonOnuAuthenticationModeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 4)
)
if mibBuilder.loadTexts:
    ponOnuAuthenticationModeTable.setStatus("optional")
_PonOnuAuthenticationModeEntry_Object = MibTableRow
ponOnuAuthenticationModeEntry = _PonOnuAuthenticationModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 4, 1)
)
ponOnuAuthenticationModeEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "ponAuthenDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "ponAuthenCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "ponAuthenPortIndex"),
)
if mibBuilder.loadTexts:
    ponOnuAuthenticationModeEntry.setStatus("current")


class _PonAuthenDeviceIndex_Type(Integer32):
    """Custom type ponAuthenDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonAuthenDeviceIndex_Type.__name__ = "Integer32"
_PonAuthenDeviceIndex_Object = MibTableColumn
ponAuthenDeviceIndex = _PonAuthenDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 4, 1, 1),
    _PonAuthenDeviceIndex_Type()
)
ponAuthenDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ponAuthenDeviceIndex.setStatus("current")


class _PonAuthenCardIndex_Type(EponCardIndex):
    """Custom type ponAuthenCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonAuthenCardIndex_Type.__name__ = "EponCardIndex"
_PonAuthenCardIndex_Object = MibTableColumn
ponAuthenCardIndex = _PonAuthenCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 4, 1, 2),
    _PonAuthenCardIndex_Type()
)
ponAuthenCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ponAuthenCardIndex.setStatus("current")


class _PonAuthenPortIndex_Type(EponPortIndex):
    """Custom type ponAuthenPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonAuthenPortIndex_Type.__name__ = "EponPortIndex"
_PonAuthenPortIndex_Object = MibTableColumn
ponAuthenPortIndex = _PonAuthenPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 4, 1, 3),
    _PonAuthenPortIndex_Type()
)
ponAuthenPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ponAuthenPortIndex.setStatus("current")


class _PonOnuAuthenMode_Type(Integer32):
    """Custom type ponOnuAuthenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("loid-password", 1),
          ("mac_or_loid-password", 2),
          ("loid", 3),
          ("mac_or_loid", 4),
          ("mac", 5),
          ("all", 6))
    )


_PonOnuAuthenMode_Type.__name__ = "Integer32"
_PonOnuAuthenMode_Object = MibTableColumn
ponOnuAuthenMode = _PonOnuAuthenMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 4, 1, 4),
    _PonOnuAuthenMode_Type()
)
ponOnuAuthenMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ponOnuAuthenMode.setStatus("current")
_OnuAuthenModeRowStatus_Type = Integer32
_OnuAuthenModeRowStatus_Object = MibTableColumn
onuAuthenModeRowStatus = _OnuAuthenModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 4, 1, 5),
    _OnuAuthenModeRowStatus_Type()
)
onuAuthenModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenModeRowStatus.setStatus("current")
_PonPortOpticalTransmissionPropertyTable_Object = MibTable
ponPortOpticalTransmissionPropertyTable = _PonPortOpticalTransmissionPropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 5)
)
if mibBuilder.loadTexts:
    ponPortOpticalTransmissionPropertyTable.setStatus("current")
_PonPortOpticalTransmissionPropertyEntry_Object = MibTableRow
ponPortOpticalTransmissionPropertyEntry = _PonPortOpticalTransmissionPropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 5, 1)
)
ponPortOpticalTransmissionPropertyEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "ponOpDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "ponOpCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "ponOpPortIndex"),
)
if mibBuilder.loadTexts:
    ponPortOpticalTransmissionPropertyEntry.setStatus("current")


class _PonOpDeviceIndex_Type(Integer32):
    """Custom type ponOpDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonOpDeviceIndex_Type.__name__ = "Integer32"
_PonOpDeviceIndex_Object = MibTableColumn
ponOpDeviceIndex = _PonOpDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 5, 1, 1),
    _PonOpDeviceIndex_Type()
)
ponOpDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponOpDeviceIndex.setStatus("current")


class _PonOpCardIndex_Type(EponCardIndex):
    """Custom type ponOpCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonOpCardIndex_Type.__name__ = "EponCardIndex"
_PonOpCardIndex_Object = MibTableColumn
ponOpCardIndex = _PonOpCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 5, 1, 2),
    _PonOpCardIndex_Type()
)
ponOpCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponOpCardIndex.setStatus("current")


class _PonOpPortIndex_Type(EponPortIndex):
    """Custom type ponOpPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PonOpPortIndex_Type.__name__ = "EponPortIndex"
_PonOpPortIndex_Object = MibTableColumn
ponOpPortIndex = _PonOpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 5, 1, 3),
    _PonOpPortIndex_Type()
)
ponOpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponOpPortIndex.setStatus("current")
_PonOpVcc_Type = Integer32
_PonOpVcc_Object = MibTableColumn
ponOpVcc = _PonOpVcc_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 5, 1, 4),
    _PonOpVcc_Type()
)
ponOpVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponOpVcc.setStatus("current")
if mibBuilder.loadTexts:
    ponOpVcc.setUnits("centi-mV")
_PonOpBias_Type = Integer32
_PonOpBias_Object = MibTableColumn
ponOpBias = _PonOpBias_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 5, 1, 5),
    _PonOpBias_Type()
)
ponOpBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponOpBias.setStatus("current")
if mibBuilder.loadTexts:
    ponOpBias.setUnits("centi-mA")
_PonOpTxPower_Type = Integer32
_PonOpTxPower_Object = MibTableColumn
ponOpTxPower = _PonOpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 5, 1, 6),
    _PonOpTxPower_Type()
)
ponOpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponOpTxPower.setStatus("current")
if mibBuilder.loadTexts:
    ponOpTxPower.setUnits("centi-dBm")
_PonOpRxPower_Type = Integer32
_PonOpRxPower_Object = MibTableColumn
ponOpRxPower = _PonOpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 5, 1, 7),
    _PonOpRxPower_Type()
)
ponOpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponOpRxPower.setStatus("current")
if mibBuilder.loadTexts:
    ponOpRxPower.setUnits("centi-dBm")
_PonPortOpticalRxPowerTable_Object = MibTable
ponPortOpticalRxPowerTable = _PonPortOpticalRxPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 6)
)
if mibBuilder.loadTexts:
    ponPortOpticalRxPowerTable.setStatus("optional")
_PonPortOpticalRxPowerEntry_Object = MibTableRow
ponPortOpticalRxPowerEntry = _PonPortOpticalRxPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 6, 1)
)
ponPortOpticalRxPowerEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "ponOpRxOfOnuDeviceIndex"),
)
if mibBuilder.loadTexts:
    ponPortOpticalRxPowerEntry.setStatus("current")
_PonOpRxOfOnuDeviceIndex_Type = EponDeviceIndex
_PonOpRxOfOnuDeviceIndex_Object = MibTableColumn
ponOpRxOfOnuDeviceIndex = _PonOpRxOfOnuDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 6, 1, 1),
    _PonOpRxOfOnuDeviceIndex_Type()
)
ponOpRxOfOnuDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ponOpRxOfOnuDeviceIndex.setStatus("current")
_PonOpRxPowerOfOnu_Type = Integer32
_PonOpRxPowerOfOnu_Object = MibTableColumn
ponOpRxPowerOfOnu = _PonOpRxPowerOfOnu_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 3, 6, 1, 2),
    _PonOpRxPowerOfOnu_Type()
)
ponOpRxPowerOfOnu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ponOpRxPowerOfOnu.setStatus("current")
if mibBuilder.loadTexts:
    ponOpRxPowerOfOnu.setUnits("centi-dBm")
_OnuObjects_ObjectIdentity = ObjectIdentity
onuObjects = _OnuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4)
)
_OnuInfoTable_Object = MibTable
onuInfoTable = _OnuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    onuInfoTable.setStatus("current")
_OnuInfoEntry_Object = MibTableRow
onuInfoEntry = _OnuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1)
)
onuInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuDeviceIndex"),
)
if mibBuilder.loadTexts:
    onuInfoEntry.setStatus("current")


class _OnuDeviceIndex_Type(EponDeviceIndex):
    """Custom type onuDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuDeviceIndex_Type.__name__ = "EponDeviceIndex"
_OnuDeviceIndex_Object = MibTableColumn
onuDeviceIndex = _OnuDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 1),
    _OnuDeviceIndex_Type()
)
onuDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuDeviceIndex.setStatus("current")
_OnuName_Type = DisplayString
_OnuName_Object = MibTableColumn
onuName = _OnuName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 2),
    _OnuName_Type()
)
onuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuName.setStatus("current")


class _OnuType_Type(Integer32):
    """Custom type onuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("chassisBased", 2))
    )


_OnuType_Type.__name__ = "Integer32"
_OnuType_Object = MibTableColumn
onuType = _OnuType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 3),
    _OnuType_Type()
)
onuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuType.setStatus("current")
_OnuIpAddress_Type = IpAddress
_OnuIpAddress_Object = MibTableColumn
onuIpAddress = _OnuIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 4),
    _OnuIpAddress_Type()
)
onuIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpAddress.setStatus("current")
_OnuIpSubnetMask_Type = IpAddress
_OnuIpSubnetMask_Object = MibTableColumn
onuIpSubnetMask = _OnuIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 5),
    _OnuIpSubnetMask_Type()
)
onuIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpSubnetMask.setStatus("current")
_OnuIpGateway_Type = IpAddress
_OnuIpGateway_Object = MibTableColumn
onuIpGateway = _OnuIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 6),
    _OnuIpGateway_Type()
)
onuIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIpGateway.setStatus("current")
_OnuMacAddress_Type = MacAddress
_OnuMacAddress_Object = MibTableColumn
onuMacAddress = _OnuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 7),
    _OnuMacAddress_Type()
)
onuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuMacAddress.setStatus("current")


class _OnuOperationStatus_Type(Integer32):
    """Custom type onuOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_OnuOperationStatus_Type.__name__ = "Integer32"
_OnuOperationStatus_Object = MibTableColumn
onuOperationStatus = _OnuOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 8),
    _OnuOperationStatus_Type()
)
onuOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuOperationStatus.setStatus("current")


class _OnuAdminStatus_Type(Integer32):
    """Custom type onuAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_OnuAdminStatus_Type.__name__ = "Integer32"
_OnuAdminStatus_Object = MibTableColumn
onuAdminStatus = _OnuAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 9),
    _OnuAdminStatus_Type()
)
onuAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAdminStatus.setStatus("current")
_OnuChipVendor_Type = DisplayString
_OnuChipVendor_Object = MibTableColumn
onuChipVendor = _OnuChipVendor_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 10),
    _OnuChipVendor_Type()
)
onuChipVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipVendor.setStatus("current")
_OnuChipType_Type = DisplayString
_OnuChipType_Object = MibTableColumn
onuChipType = _OnuChipType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 11),
    _OnuChipType_Type()
)
onuChipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipType.setStatus("current")
_OnuChipVersion_Type = DisplayString
_OnuChipVersion_Object = MibTableColumn
onuChipVersion = _OnuChipVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 12),
    _OnuChipVersion_Type()
)
onuChipVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuChipVersion.setStatus("current")
_OnuSoftwareVersion_Type = DisplayString
_OnuSoftwareVersion_Object = MibTableColumn
onuSoftwareVersion = _OnuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 13),
    _OnuSoftwareVersion_Type()
)
onuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuSoftwareVersion.setStatus("current")
_OnuFirmwareVersion_Type = DisplayString
_OnuFirmwareVersion_Object = MibTableColumn
onuFirmwareVersion = _OnuFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 14),
    _OnuFirmwareVersion_Type()
)
onuFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuFirmwareVersion.setStatus("current")
_OnuTestDistance_Type = Integer32
_OnuTestDistance_Object = MibTableColumn
onuTestDistance = _OnuTestDistance_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 15),
    _OnuTestDistance_Type()
)
onuTestDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTestDistance.setStatus("current")
if mibBuilder.loadTexts:
    onuTestDistance.setUnits("Meter")
_OnuLlidId_Type = Integer32
_OnuLlidId_Object = MibTableColumn
onuLlidId = _OnuLlidId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 16),
    _OnuLlidId_Type()
)
onuLlidId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuLlidId.setStatus("current")


class _ResetONU_Type(Integer32):
    """Custom type resetONU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ResetONU_Type.__name__ = "Integer32"
_ResetONU_Object = MibTableColumn
resetONU = _ResetONU_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 17),
    _ResetONU_Type()
)
resetONU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetONU.setStatus("current")
_OnuTimeSinceLastRegister_Type = Counter32
_OnuTimeSinceLastRegister_Object = MibTableColumn
onuTimeSinceLastRegister = _OnuTimeSinceLastRegister_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 18),
    _OnuTimeSinceLastRegister_Type()
)
onuTimeSinceLastRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTimeSinceLastRegister.setStatus("current")
if mibBuilder.loadTexts:
    onuTimeSinceLastRegister.setUnits("seconds")
_OnuMgmtCvlan_Type = Integer32
_OnuMgmtCvlan_Object = MibTableColumn
onuMgmtCvlan = _OnuMgmtCvlan_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 19),
    _OnuMgmtCvlan_Type()
)
onuMgmtCvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMgmtCvlan.setStatus("current")
_OnuMgmtSvlan_Type = Integer32
_OnuMgmtSvlan_Object = MibTableColumn
onuMgmtSvlan = _OnuMgmtSvlan_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 20),
    _OnuMgmtSvlan_Type()
)
onuMgmtSvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMgmtSvlan.setStatus("optional")


class _OnuMgmtPriority_Type(Integer32):
    """Custom type onuMgmtPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OnuMgmtPriority_Type.__name__ = "Integer32"
_OnuMgmtPriority_Object = MibTableColumn
onuMgmtPriority = _OnuMgmtPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 21),
    _OnuMgmtPriority_Type()
)
onuMgmtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMgmtPriority.setStatus("optional")
_OnuMgmtSnmpTrapHost_Type = IpAddress
_OnuMgmtSnmpTrapHost_Object = MibTableColumn
onuMgmtSnmpTrapHost = _OnuMgmtSnmpTrapHost_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 22),
    _OnuMgmtSnmpTrapHost_Type()
)
onuMgmtSnmpTrapHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMgmtSnmpTrapHost.setStatus("current")
_OnuMgmtSnmpCommunityForRead_Type = DisplayString
_OnuMgmtSnmpCommunityForRead_Object = MibTableColumn
onuMgmtSnmpCommunityForRead = _OnuMgmtSnmpCommunityForRead_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 23),
    _OnuMgmtSnmpCommunityForRead_Type()
)
onuMgmtSnmpCommunityForRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMgmtSnmpCommunityForRead.setStatus("current")
_OnuMgmtSnmpCommunityForWrite_Type = DisplayString
_OnuMgmtSnmpCommunityForWrite_Object = MibTableColumn
onuMgmtSnmpCommunityForWrite = _OnuMgmtSnmpCommunityForWrite_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 24),
    _OnuMgmtSnmpCommunityForWrite_Type()
)
onuMgmtSnmpCommunityForWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuMgmtSnmpCommunityForWrite.setStatus("current")
_OnuVendorId_Type = DisplayString
_OnuVendorId_Object = MibTableColumn
onuVendorId = _OnuVendorId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 25),
    _OnuVendorId_Type()
)
onuVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuVendorId.setStatus("current")
_OnuModelId_Type = DisplayString
_OnuModelId_Object = MibTableColumn
onuModelId = _OnuModelId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 26),
    _OnuModelId_Type()
)
onuModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuModelId.setStatus("current")
_OnuHardwareVersion_Type = DisplayString
_OnuHardwareVersion_Object = MibTableColumn
onuHardwareVersion = _OnuHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 27),
    _OnuHardwareVersion_Type()
)
onuHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuHardwareVersion.setStatus("current")
_OnuSn_Type = DisplayString
_OnuSn_Object = MibTableColumn
onuSn = _OnuSn_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 28),
    _OnuSn_Type()
)
onuSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuSn.setStatus("current")
_OnuTimeLastRegister_Type = TimeTicks
_OnuTimeLastRegister_Object = MibTableColumn
onuTimeLastRegister = _OnuTimeLastRegister_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 1, 1, 29),
    _OnuTimeLastRegister_Type()
)
onuTimeLastRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTimeLastRegister.setStatus("current")
_OnuPonPortOpticalTransmissionPropertyTable_Object = MibTable
onuPonPortOpticalTransmissionPropertyTable = _OnuPonPortOpticalTransmissionPropertyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2)
)
if mibBuilder.loadTexts:
    onuPonPortOpticalTransmissionPropertyTable.setStatus("current")
_OnuPonPortOpticalTransmissionPropertyEntry_Object = MibTableRow
onuPonPortOpticalTransmissionPropertyEntry = _OnuPonPortOpticalTransmissionPropertyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2, 1)
)
onuPonPortOpticalTransmissionPropertyEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuPonPortOpticalTransmissionPropertyDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "onuPonPortOpticalTransmissionPropertyCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "onuPonPortOpticalTransmissionPropertyPortIndex"),
)
if mibBuilder.loadTexts:
    onuPonPortOpticalTransmissionPropertyEntry.setStatus("current")


class _OnuPonPortOpticalTransmissionPropertyDeviceIndex_Type(EponDeviceIndex):
    """Custom type onuPonPortOpticalTransmissionPropertyDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuPonPortOpticalTransmissionPropertyDeviceIndex_Type.__name__ = "EponDeviceIndex"
_OnuPonPortOpticalTransmissionPropertyDeviceIndex_Object = MibTableColumn
onuPonPortOpticalTransmissionPropertyDeviceIndex = _OnuPonPortOpticalTransmissionPropertyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2, 1, 1),
    _OnuPonPortOpticalTransmissionPropertyDeviceIndex_Type()
)
onuPonPortOpticalTransmissionPropertyDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuPonPortOpticalTransmissionPropertyDeviceIndex.setStatus("current")


class _OnuPonPortOpticalTransmissionPropertyCardIndex_Type(Integer32):
    """Custom type onuPonPortOpticalTransmissionPropertyCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuPonPortOpticalTransmissionPropertyCardIndex_Type.__name__ = "Integer32"
_OnuPonPortOpticalTransmissionPropertyCardIndex_Object = MibTableColumn
onuPonPortOpticalTransmissionPropertyCardIndex = _OnuPonPortOpticalTransmissionPropertyCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2, 1, 2),
    _OnuPonPortOpticalTransmissionPropertyCardIndex_Type()
)
onuPonPortOpticalTransmissionPropertyCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuPonPortOpticalTransmissionPropertyCardIndex.setStatus("current")


class _OnuPonPortOpticalTransmissionPropertyPortIndex_Type(Integer32):
    """Custom type onuPonPortOpticalTransmissionPropertyPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuPonPortOpticalTransmissionPropertyPortIndex_Type.__name__ = "Integer32"
_OnuPonPortOpticalTransmissionPropertyPortIndex_Object = MibTableColumn
onuPonPortOpticalTransmissionPropertyPortIndex = _OnuPonPortOpticalTransmissionPropertyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2, 1, 3),
    _OnuPonPortOpticalTransmissionPropertyPortIndex_Type()
)
onuPonPortOpticalTransmissionPropertyPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuPonPortOpticalTransmissionPropertyPortIndex.setStatus("current")
_OnuReceivedOpticalPower_Type = Integer32
_OnuReceivedOpticalPower_Object = MibTableColumn
onuReceivedOpticalPower = _OnuReceivedOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2, 1, 4),
    _OnuReceivedOpticalPower_Type()
)
onuReceivedOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuReceivedOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    onuReceivedOpticalPower.setUnits("centi-dBm")
_OnuTramsmittedOpticalPower_Type = Integer32
_OnuTramsmittedOpticalPower_Object = MibTableColumn
onuTramsmittedOpticalPower = _OnuTramsmittedOpticalPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2, 1, 5),
    _OnuTramsmittedOpticalPower_Type()
)
onuTramsmittedOpticalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuTramsmittedOpticalPower.setStatus("current")
if mibBuilder.loadTexts:
    onuTramsmittedOpticalPower.setUnits("centi-dBm")
_OnuBiasCurrent_Type = Integer32
_OnuBiasCurrent_Object = MibTableColumn
onuBiasCurrent = _OnuBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2, 1, 6),
    _OnuBiasCurrent_Type()
)
onuBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    onuBiasCurrent.setUnits("centi-mA")
_OnuWorkingVoltage_Type = Integer32
_OnuWorkingVoltage_Object = MibTableColumn
onuWorkingVoltage = _OnuWorkingVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2, 1, 7),
    _OnuWorkingVoltage_Type()
)
onuWorkingVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuWorkingVoltage.setStatus("current")
if mibBuilder.loadTexts:
    onuWorkingVoltage.setUnits("centi-mV")
_OnuWorkingTemperature_Type = Integer32
_OnuWorkingTemperature_Object = MibTableColumn
onuWorkingTemperature = _OnuWorkingTemperature_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 2, 1, 8),
    _OnuWorkingTemperature_Type()
)
onuWorkingTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuWorkingTemperature.setStatus("current")
if mibBuilder.loadTexts:
    onuWorkingTemperature.setUnits("Centi-degree centigrade")
_OnuCapabilityTable_Object = MibTable
onuCapabilityTable = _OnuCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3)
)
if mibBuilder.loadTexts:
    onuCapabilityTable.setStatus("current")
_OnuCapabilityEntry_Object = MibTableRow
onuCapabilityEntry = _OnuCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1)
)
onuCapabilityEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuCapabilityDeviceIndex"),
)
if mibBuilder.loadTexts:
    onuCapabilityEntry.setStatus("current")


class _OnuCapabilityDeviceIndex_Type(EponDeviceIndex):
    """Custom type onuCapabilityDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuCapabilityDeviceIndex_Type.__name__ = "EponDeviceIndex"
_OnuCapabilityDeviceIndex_Object = MibTableColumn
onuCapabilityDeviceIndex = _OnuCapabilityDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 1),
    _OnuCapabilityDeviceIndex_Type()
)
onuCapabilityDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuCapabilityDeviceIndex.setStatus("current")
_OnuGePortNum_Type = Integer32
_OnuGePortNum_Object = MibTableColumn
onuGePortNum = _OnuGePortNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 2),
    _OnuGePortNum_Type()
)
onuGePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuGePortNum.setStatus("current")
_OnuGePortBitmap_Type = OctetString
_OnuGePortBitmap_Object = MibTableColumn
onuGePortBitmap = _OnuGePortBitmap_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 3),
    _OnuGePortBitmap_Type()
)
onuGePortBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuGePortBitmap.setStatus("current")
_OnuFePortNum_Type = Integer32
_OnuFePortNum_Object = MibTableColumn
onuFePortNum = _OnuFePortNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 4),
    _OnuFePortNum_Type()
)
onuFePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuFePortNum.setStatus("current")
_OnuFePortBitmap_Type = OctetString
_OnuFePortBitmap_Object = MibTableColumn
onuFePortBitmap = _OnuFePortBitmap_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 5),
    _OnuFePortBitmap_Type()
)
onuFePortBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuFePortBitmap.setStatus("current")
_OnuQueueNumUplink_Type = Integer32
_OnuQueueNumUplink_Object = MibTableColumn
onuQueueNumUplink = _OnuQueueNumUplink_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 6),
    _OnuQueueNumUplink_Type()
)
onuQueueNumUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuQueueNumUplink.setStatus("current")
_OnuMaxQueueNumUplink_Type = Integer32
_OnuMaxQueueNumUplink_Object = MibTableColumn
onuMaxQueueNumUplink = _OnuMaxQueueNumUplink_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 7),
    _OnuMaxQueueNumUplink_Type()
)
onuMaxQueueNumUplink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuMaxQueueNumUplink.setStatus("current")
_OnuQueueNumDownlink_Type = Integer32
_OnuQueueNumDownlink_Object = MibTableColumn
onuQueueNumDownlink = _OnuQueueNumDownlink_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 8),
    _OnuQueueNumDownlink_Type()
)
onuQueueNumDownlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuQueueNumDownlink.setStatus("current")
_OnuMaxQueueNumDownlink_Type = Integer32
_OnuMaxQueueNumDownlink_Object = MibTableColumn
onuMaxQueueNumDownlink = _OnuMaxQueueNumDownlink_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 9),
    _OnuMaxQueueNumDownlink_Type()
)
onuMaxQueueNumDownlink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuMaxQueueNumDownlink.setStatus("current")
_OnuFecEnable_Type = TruthValue
_OnuFecEnable_Object = MibTableColumn
onuFecEnable = _OnuFecEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 10),
    _OnuFecEnable_Type()
)
onuFecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuFecEnable.setStatus("current")


class _OnuEncryptMode_Type(Integer32):
    """Custom type onuEncryptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 1),
          ("ctcTripleChurning", 2),
          ("other", 3))
    )


_OnuEncryptMode_Type.__name__ = "Integer32"
_OnuEncryptMode_Object = MibTableColumn
onuEncryptMode = _OnuEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 11),
    _OnuEncryptMode_Type()
)
onuEncryptMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuEncryptMode.setStatus("current")
_OnuEncryptKeyExchangeTime_Type = TimeTicks
_OnuEncryptKeyExchangeTime_Object = MibTableColumn
onuEncryptKeyExchangeTime = _OnuEncryptKeyExchangeTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 12),
    _OnuEncryptKeyExchangeTime_Type()
)
onuEncryptKeyExchangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuEncryptKeyExchangeTime.setStatus("current")
_OnuIsolationEnable_Type = TruthValue
_OnuIsolationEnable_Object = MibTableColumn
onuIsolationEnable = _OnuIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 3, 1, 13),
    _OnuIsolationEnable_Type()
)
onuIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIsolationEnable.setStatus("current")
_SlaTable_Object = MibTable
slaTable = _SlaTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 4)
)
if mibBuilder.loadTexts:
    slaTable.setStatus("current")
_SlaEntry_Object = MibTableRow
slaEntry = _SlaEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 4, 1)
)
slaEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "slaIndex"),
)
if mibBuilder.loadTexts:
    slaEntry.setStatus("current")


class _SlaIndex_Type(EponDeviceIndex):
    """Custom type slaIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SlaIndex_Type.__name__ = "EponDeviceIndex"
_SlaIndex_Object = MibTableColumn
slaIndex = _SlaIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 4, 1, 1),
    _SlaIndex_Type()
)
slaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slaIndex.setStatus("current")
_SlaDsFixedBW_Type = Integer32
_SlaDsFixedBW_Object = MibTableColumn
slaDsFixedBW = _SlaDsFixedBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 4, 1, 2),
    _SlaDsFixedBW_Type()
)
slaDsFixedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaDsFixedBW.setStatus("current")
if mibBuilder.loadTexts:
    slaDsFixedBW.setUnits("kbps")
_SlaDsPeakBW_Type = Integer32
_SlaDsPeakBW_Object = MibTableColumn
slaDsPeakBW = _SlaDsPeakBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 4, 1, 3),
    _SlaDsPeakBW_Type()
)
slaDsPeakBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaDsPeakBW.setStatus("current")
if mibBuilder.loadTexts:
    slaDsPeakBW.setUnits("kbps")
_SlaDsCommittedBW_Type = Integer32
_SlaDsCommittedBW_Object = MibTableColumn
slaDsCommittedBW = _SlaDsCommittedBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 4, 1, 4),
    _SlaDsCommittedBW_Type()
)
slaDsCommittedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaDsCommittedBW.setStatus("current")
if mibBuilder.loadTexts:
    slaDsCommittedBW.setUnits("kbps")
_SlaUsFixedBW_Type = Integer32
_SlaUsFixedBW_Object = MibTableColumn
slaUsFixedBW = _SlaUsFixedBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 4, 1, 5),
    _SlaUsFixedBW_Type()
)
slaUsFixedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUsFixedBW.setStatus("current")
if mibBuilder.loadTexts:
    slaUsFixedBW.setUnits("kbps")
_SlaUsPeakBW_Type = Integer32
_SlaUsPeakBW_Object = MibTableColumn
slaUsPeakBW = _SlaUsPeakBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 4, 1, 6),
    _SlaUsPeakBW_Type()
)
slaUsPeakBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUsPeakBW.setStatus("current")
if mibBuilder.loadTexts:
    slaUsPeakBW.setUnits("kbps")
_SlaUsCommittedBW_Type = Integer32
_SlaUsCommittedBW_Object = MibTableColumn
slaUsCommittedBW = _SlaUsCommittedBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 4, 1, 7),
    _SlaUsCommittedBW_Type()
)
slaUsCommittedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaUsCommittedBW.setStatus("current")
if mibBuilder.loadTexts:
    slaUsCommittedBW.setUnits("kbps")
_OnuAuthenticationManagement_ObjectIdentity = ObjectIdentity
onuAuthenticationManagement = _OnuAuthenticationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5)
)
if mibBuilder.loadTexts:
    onuAuthenticationManagement.setStatus("current")


class _OnuAuthenticationPolicy_Type(Integer32):
    """Custom type onuAuthenticationPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acceptAll", 1),
          ("rejectNotConfigured", 2))
    )


_OnuAuthenticationPolicy_Type.__name__ = "Integer32"
_OnuAuthenticationPolicy_Object = MibScalar
onuAuthenticationPolicy = _OnuAuthenticationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 1),
    _OnuAuthenticationPolicy_Type()
)
onuAuthenticationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuAuthenticationPolicy.setStatus("current")
_OnuAuthenticationPreConfigTable_Object = MibTable
onuAuthenticationPreConfigTable = _OnuAuthenticationPreConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 2)
)
if mibBuilder.loadTexts:
    onuAuthenticationPreConfigTable.setStatus("current")
_OnuAuthenticationPreConfigEntry_Object = MibTableRow
onuAuthenticationPreConfigEntry = _OnuAuthenticationPreConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 2, 1)
)
onuAuthenticationPreConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuAuthenOnuId"),
)
if mibBuilder.loadTexts:
    onuAuthenticationPreConfigEntry.setStatus("current")


class _OnuAuthenOnuId_Type(EponDeviceIndex):
    """Custom type onuAuthenOnuId based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuAuthenOnuId_Type.__name__ = "EponDeviceIndex"
_OnuAuthenOnuId_Object = MibTableColumn
onuAuthenOnuId = _OnuAuthenOnuId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 2, 1, 1),
    _OnuAuthenOnuId_Type()
)
onuAuthenOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuAuthenOnuId.setStatus("current")
_OnuAuthenMacAddress_Type = MacAddress
_OnuAuthenMacAddress_Object = MibTableColumn
onuAuthenMacAddress = _OnuAuthenMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 2, 1, 2),
    _OnuAuthenMacAddress_Type()
)
onuAuthenMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenMacAddress.setStatus("current")


class _OnuAuthenAction_Type(Integer32):
    """Custom type onuAuthenAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_OnuAuthenAction_Type.__name__ = "Integer32"
_OnuAuthenAction_Object = MibTableColumn
onuAuthenAction = _OnuAuthenAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 2, 1, 3),
    _OnuAuthenAction_Type()
)
onuAuthenAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenAction.setStatus("current")


class _OnuAuthenRowStatus_Type(Integer32):
    """Custom type onuAuthenRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_OnuAuthenRowStatus_Type.__name__ = "Integer32"
_OnuAuthenRowStatus_Object = MibTableColumn
onuAuthenRowStatus = _OnuAuthenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 2, 1, 4),
    _OnuAuthenRowStatus_Type()
)
onuAuthenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenRowStatus.setStatus("current")
_OnuAuthenticationBlockTable_Object = MibTable
onuAuthenticationBlockTable = _OnuAuthenticationBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 3)
)
if mibBuilder.loadTexts:
    onuAuthenticationBlockTable.setStatus("current")
_OnuAuthenticationBlockEntry_Object = MibTableRow
onuAuthenticationBlockEntry = _OnuAuthenticationBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 3, 1)
)
onuAuthenticationBlockEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuAuthenBlockOnuId"),
)
if mibBuilder.loadTexts:
    onuAuthenticationBlockEntry.setStatus("current")
_OnuAuthenBlockOnuId_Type = EponDeviceIndex
_OnuAuthenBlockOnuId_Object = MibTableColumn
onuAuthenBlockOnuId = _OnuAuthenBlockOnuId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 3, 1, 1),
    _OnuAuthenBlockOnuId_Type()
)
onuAuthenBlockOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuAuthenBlockOnuId.setStatus("current")
_OnuAuthenBlockMacAddress_Type = MacAddress
_OnuAuthenBlockMacAddress_Object = MibTableColumn
onuAuthenBlockMacAddress = _OnuAuthenBlockMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 3, 1, 2),
    _OnuAuthenBlockMacAddress_Type()
)
onuAuthenBlockMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenBlockMacAddress.setStatus("current")
_AuthenBlockTime_Type = TimeTicks
_AuthenBlockTime_Object = MibTableColumn
authenBlockTime = _AuthenBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 3, 1, 3),
    _AuthenBlockTime_Type()
)
authenBlockTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authenBlockTime.setStatus("current")
_OnuAuthenBlockRowStatus_Type = RowStatus
_OnuAuthenBlockRowStatus_Object = MibTableColumn
onuAuthenBlockRowStatus = _OnuAuthenBlockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 3, 1, 4),
    _OnuAuthenBlockRowStatus_Type()
)
onuAuthenBlockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuAuthenBlockRowStatus.setStatus("current")
_OnuLoidAuthenticationConfigTable_Object = MibTable
onuLoidAuthenticationConfigTable = _OnuLoidAuthenticationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 4)
)
if mibBuilder.loadTexts:
    onuLoidAuthenticationConfigTable.setStatus("current")
_OnuLoidAuthenticationConfigEntry_Object = MibTableRow
onuLoidAuthenticationConfigEntry = _OnuLoidAuthenticationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 4, 1)
)
onuLoidAuthenticationConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuLoidAuthenOnuId"),
)
if mibBuilder.loadTexts:
    onuLoidAuthenticationConfigEntry.setStatus("current")
_OnuLoidAuthenOnuId_Type = EponDeviceIndex
_OnuLoidAuthenOnuId_Object = MibTableColumn
onuLoidAuthenOnuId = _OnuLoidAuthenOnuId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 4, 1, 1),
    _OnuLoidAuthenOnuId_Type()
)
onuLoidAuthenOnuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuLoidAuthenOnuId.setStatus("current")


class _OnuLoidAuthenLOID_Type(OctetString):
    """Custom type onuLoidAuthenLOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_OnuLoidAuthenLOID_Type.__name__ = "OctetString"
_OnuLoidAuthenLOID_Object = MibTableColumn
onuLoidAuthenLOID = _OnuLoidAuthenLOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 4, 1, 2),
    _OnuLoidAuthenLOID_Type()
)
onuLoidAuthenLOID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuLoidAuthenLOID.setStatus("current")


class _OnuLoidAuthenPassword_Type(OctetString):
    """Custom type onuLoidAuthenPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_OnuLoidAuthenPassword_Type.__name__ = "OctetString"
_OnuLoidAuthenPassword_Object = MibTableColumn
onuLoidAuthenPassword = _OnuLoidAuthenPassword_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 4, 1, 3),
    _OnuLoidAuthenPassword_Type()
)
onuLoidAuthenPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuLoidAuthenPassword.setStatus("current")
_OnuLoidAuthenRowStatus_Type = RowStatus
_OnuLoidAuthenRowStatus_Object = MibTableColumn
onuLoidAuthenRowStatus = _OnuLoidAuthenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 5, 4, 1, 4),
    _OnuLoidAuthenRowStatus_Type()
)
onuLoidAuthenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuLoidAuthenRowStatus.setStatus("current")
_OnuAutoFindTable_Object = MibTable
onuAutoFindTable = _OnuAutoFindTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 6)
)
if mibBuilder.loadTexts:
    onuAutoFindTable.setStatus("current")
_OnuAutoFindEntry_Object = MibTableRow
onuAutoFindEntry = _OnuAutoFindEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 6, 1)
)
onuAutoFindEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuAutoFindOnuIndex"),
)
if mibBuilder.loadTexts:
    onuAutoFindEntry.setStatus("current")
_OnuAutoFindOnuIndex_Type = EponDeviceIndex
_OnuAutoFindOnuIndex_Object = MibTableColumn
onuAutoFindOnuIndex = _OnuAutoFindOnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 6, 1, 1),
    _OnuAutoFindOnuIndex_Type()
)
onuAutoFindOnuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuAutoFindOnuIndex.setStatus("current")
_OnuAutoFindMacAddress_Type = MacAddress
_OnuAutoFindMacAddress_Object = MibTableColumn
onuAutoFindMacAddress = _OnuAutoFindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 6, 1, 2),
    _OnuAutoFindMacAddress_Type()
)
onuAutoFindMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindMacAddress.setStatus("current")
_OnuAutoFindTime_Type = TimeTicks
_OnuAutoFindTime_Object = MibTableColumn
onuAutoFindTime = _OnuAutoFindTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 6, 1, 3),
    _OnuAutoFindTime_Type()
)
onuAutoFindTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindTime.setStatus("current")


class _OnuAutoFindAuthenLOID_Type(OctetString):
    """Custom type onuAutoFindAuthenLOID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_OnuAutoFindAuthenLOID_Type.__name__ = "OctetString"
_OnuAutoFindAuthenLOID_Object = MibTableColumn
onuAutoFindAuthenLOID = _OnuAutoFindAuthenLOID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 6, 1, 4),
    _OnuAutoFindAuthenLOID_Type()
)
onuAutoFindAuthenLOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindAuthenLOID.setStatus("current")


class _OnuAutoFindAuthenPassword_Type(OctetString):
    """Custom type onuAutoFindAuthenPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_OnuAutoFindAuthenPassword_Type.__name__ = "OctetString"
_OnuAutoFindAuthenPassword_Object = MibTableColumn
onuAutoFindAuthenPassword = _OnuAutoFindAuthenPassword_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 4, 6, 1, 5),
    _OnuAutoFindAuthenPassword_Type()
)
onuAutoFindAuthenPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuAutoFindAuthenPassword.setStatus("current")
_UniObjects_ObjectIdentity = ObjectIdentity
uniObjects = _UniObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5)
)
_UniAttributeTable_Object = MibTable
uniAttributeTable = _UniAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    uniAttributeTable.setStatus("current")
_UniAttributeEntry_Object = MibTableRow
uniAttributeEntry = _UniAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1)
)
uniAttributeEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniAttributeDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "uniAttributeCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "uniAttributePortIndex"),
)
if mibBuilder.loadTexts:
    uniAttributeEntry.setStatus("current")
_UniAttributeDeviceIndex_Type = EponDeviceIndex
_UniAttributeDeviceIndex_Object = MibTableColumn
uniAttributeDeviceIndex = _UniAttributeDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 1),
    _UniAttributeDeviceIndex_Type()
)
uniAttributeDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniAttributeDeviceIndex.setStatus("current")


class _UniAttributeCardIndex_Type(EponCardIndex):
    """Custom type uniAttributeCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniAttributeCardIndex_Type.__name__ = "EponCardIndex"
_UniAttributeCardIndex_Object = MibTableColumn
uniAttributeCardIndex = _UniAttributeCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 2),
    _UniAttributeCardIndex_Type()
)
uniAttributeCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniAttributeCardIndex.setStatus("current")


class _UniAttributePortIndex_Type(EponPortIndex):
    """Custom type uniAttributePortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniAttributePortIndex_Type.__name__ = "EponPortIndex"
_UniAttributePortIndex_Object = MibTableColumn
uniAttributePortIndex = _UniAttributePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 3),
    _UniAttributePortIndex_Type()
)
uniAttributePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniAttributePortIndex.setStatus("current")


class _UniAdminStatus_Type(Integer32):
    """Custom type uniAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_UniAdminStatus_Type.__name__ = "Integer32"
_UniAdminStatus_Object = MibTableColumn
uniAdminStatus = _UniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 4),
    _UniAdminStatus_Type()
)
uniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniAdminStatus.setStatus("current")


class _UniOperationStatus_Type(Integer32):
    """Custom type uniOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_UniOperationStatus_Type.__name__ = "Integer32"
_UniOperationStatus_Object = MibTableColumn
uniOperationStatus = _UniOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 5),
    _UniOperationStatus_Type()
)
uniOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniOperationStatus.setStatus("current")
_UniAutoNegotiationEnable_Type = TruthValue
_UniAutoNegotiationEnable_Object = MibTableColumn
uniAutoNegotiationEnable = _UniAutoNegotiationEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 6),
    _UniAutoNegotiationEnable_Type()
)
uniAutoNegotiationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniAutoNegotiationEnable.setStatus("current")
_UniAutoNegotiationLocalTechAbility_Type = AutoNegotiationTechAbility
_UniAutoNegotiationLocalTechAbility_Object = MibTableColumn
uniAutoNegotiationLocalTechAbility = _UniAutoNegotiationLocalTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 7),
    _UniAutoNegotiationLocalTechAbility_Type()
)
uniAutoNegotiationLocalTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniAutoNegotiationLocalTechAbility.setStatus("current")


class _UniAutoNegotiationRestart_Type(Integer32):
    """Custom type uniAutoNegotiationRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_UniAutoNegotiationRestart_Type.__name__ = "Integer32"
_UniAutoNegotiationRestart_Object = MibTableColumn
uniAutoNegotiationRestart = _UniAutoNegotiationRestart_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 8),
    _UniAutoNegotiationRestart_Type()
)
uniAutoNegotiationRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniAutoNegotiationRestart.setStatus("current")
_UniMacAddrLearnMaxNum_Type = Integer32
_UniMacAddrLearnMaxNum_Object = MibTableColumn
uniMacAddrLearnMaxNum = _UniMacAddrLearnMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 9),
    _UniMacAddrLearnMaxNum_Type()
)
uniMacAddrLearnMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMacAddrLearnMaxNum.setStatus("current")
_UniCurrentPerfStatsEnable_Type = TruthValue
_UniCurrentPerfStatsEnable_Object = MibTableColumn
uniCurrentPerfStatsEnable = _UniCurrentPerfStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 10),
    _UniCurrentPerfStatsEnable_Type()
)
uniCurrentPerfStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniCurrentPerfStatsEnable.setStatus("current")
_UniMacAddressManagement_ObjectIdentity = ObjectIdentity
uniMacAddressManagement = _UniMacAddressManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    uniMacAddressManagement.setStatus("current")
_UniMacAddressManagementTable_Object = MibTable
uniMacAddressManagementTable = _UniMacAddressManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    uniMacAddressManagementTable.setStatus("current")
_UniMacAddressManagementEntry_Object = MibTableRow
uniMacAddressManagementEntry = _UniMacAddressManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 1, 1)
)
uniMacAddressManagementEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniMacAddrONUIndex"),
)
if mibBuilder.loadTexts:
    uniMacAddressManagementEntry.setStatus("current")
_UniMacAddrONUIndex_Type = EponDeviceIndex
_UniMacAddrONUIndex_Object = MibTableColumn
uniMacAddrONUIndex = _UniMacAddrONUIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 1, 1, 1),
    _UniMacAddrONUIndex_Type()
)
uniMacAddrONUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniMacAddrONUIndex.setStatus("current")
_UniMacAddrAgingTime_Type = Integer32
_UniMacAddrAgingTime_Object = MibTableColumn
uniMacAddrAgingTime = _UniMacAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 1, 1, 2),
    _UniMacAddrAgingTime_Type()
)
uniMacAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMacAddrAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    uniMacAddrAgingTime.setUnits("Seconds")


class _UniMacAddrClear_Type(Integer32):
    """Custom type uniMacAddrClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("allDynamic", 1)
    )


_UniMacAddrClear_Type.__name__ = "Integer32"
_UniMacAddrClear_Object = MibTableColumn
uniMacAddrClear = _UniMacAddrClear_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 1, 1, 3),
    _UniMacAddrClear_Type()
)
uniMacAddrClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMacAddrClear.setStatus("current")
_UniMacAddressTable_Object = MibTable
uniMacAddressTable = _UniMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    uniMacAddressTable.setStatus("current")
_UniMacAddressEntry_Object = MibTableRow
uniMacAddressEntry = _UniMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1)
)
uniMacAddressEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniMacAddrIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "uniMacAddrVlanIdIndex"),
)
if mibBuilder.loadTexts:
    uniMacAddressEntry.setStatus("current")
_UniMacAddrIndex_Type = MacAddress
_UniMacAddrIndex_Object = MibTableColumn
uniMacAddrIndex = _UniMacAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 1),
    _UniMacAddrIndex_Type()
)
uniMacAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniMacAddrIndex.setStatus("current")


class _UniMacAddrVlanIdIndex_Type(Integer32):
    """Custom type uniMacAddrVlanIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniMacAddrVlanIdIndex_Type.__name__ = "Integer32"
_UniMacAddrVlanIdIndex_Object = MibTableColumn
uniMacAddrVlanIdIndex = _UniMacAddrVlanIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 2),
    _UniMacAddrVlanIdIndex_Type()
)
uniMacAddrVlanIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniMacAddrVlanIdIndex.setStatus("current")


class _UniMacAddrType_Type(Integer32):
    """Custom type uniMacAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("other", 3))
    )


_UniMacAddrType_Type.__name__ = "Integer32"
_UniMacAddrType_Object = MibTableColumn
uniMacAddrType = _UniMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 3),
    _UniMacAddrType_Type()
)
uniMacAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMacAddrType.setStatus("current")


class _UniMacAddrPortId_Type(OctetString):
    """Custom type uniMacAddrPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_UniMacAddrPortId_Type.__name__ = "OctetString"
_UniMacAddrPortId_Object = MibTableColumn
uniMacAddrPortId = _UniMacAddrPortId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 4),
    _UniMacAddrPortId_Type()
)
uniMacAddrPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMacAddrPortId.setStatus("current")
_UniMacAddrRowStatus_Type = RowStatus
_UniMacAddrRowStatus_Object = MibTableColumn
uniMacAddrRowStatus = _UniMacAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 5),
    _UniMacAddrRowStatus_Type()
)
uniMacAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMacAddrRowStatus.setStatus("current")
_UniTrunkManagement_ObjectIdentity = ObjectIdentity
uniTrunkManagement = _UniTrunkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3)
)
if mibBuilder.loadTexts:
    uniTrunkManagement.setStatus("current")
_UniTrunkGroupConfigTable_Object = MibTable
uniTrunkGroupConfigTable = _UniTrunkGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    uniTrunkGroupConfigTable.setStatus("current")
_UniTrunkGroupConfigEntry_Object = MibTableRow
uniTrunkGroupConfigEntry = _UniTrunkGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1)
)
uniTrunkGroupConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniTrunkGroupConfigIndex"),
)
if mibBuilder.loadTexts:
    uniTrunkGroupConfigEntry.setStatus("current")


class _UniTrunkGroupConfigIndex_Type(Integer32):
    """Custom type uniTrunkGroupConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniTrunkGroupConfigIndex_Type.__name__ = "Integer32"
_UniTrunkGroupConfigIndex_Object = MibTableColumn
uniTrunkGroupConfigIndex = _UniTrunkGroupConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 1),
    _UniTrunkGroupConfigIndex_Type()
)
uniTrunkGroupConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigIndex.setStatus("current")
_UniTrunkGroupConfigName_Type = DisplayString
_UniTrunkGroupConfigName_Object = MibTableColumn
uniTrunkGroupConfigName = _UniTrunkGroupConfigName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 2),
    _UniTrunkGroupConfigName_Type()
)
uniTrunkGroupConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigName.setStatus("current")
_UniTrunkGroupConfigMember_Type = OctetString
_UniTrunkGroupConfigMember_Object = MibTableColumn
uniTrunkGroupConfigMember = _UniTrunkGroupConfigMember_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 3),
    _UniTrunkGroupConfigMember_Type()
)
uniTrunkGroupConfigMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigMember.setStatus("current")


class _UniTrunkGroupConfigPolicy_Type(Integer32):
    """Custom type uniTrunkGroupConfigPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("srcMac", 1),
          ("destMac", 2),
          ("srcMacNDestMac", 3),
          ("srcIp", 4),
          ("destIp", 5),
          ("srcIpNDestIp", 6))
    )


_UniTrunkGroupConfigPolicy_Type.__name__ = "Integer32"
_UniTrunkGroupConfigPolicy_Object = MibTableColumn
uniTrunkGroupConfigPolicy = _UniTrunkGroupConfigPolicy_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 4),
    _UniTrunkGroupConfigPolicy_Type()
)
uniTrunkGroupConfigPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigPolicy.setStatus("current")
_UniTrunkGroupConfigRowstatus_Type = RowStatus
_UniTrunkGroupConfigRowstatus_Object = MibTableColumn
uniTrunkGroupConfigRowstatus = _UniTrunkGroupConfigRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 5),
    _UniTrunkGroupConfigRowstatus_Type()
)
uniTrunkGroupConfigRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigRowstatus.setStatus("current")
_UniTrunkGroupTable_Object = MibTable
uniTrunkGroupTable = _UniTrunkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    uniTrunkGroupTable.setStatus("current")
_UniTrunkGroupEntry_Object = MibTableRow
uniTrunkGroupEntry = _UniTrunkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1)
)
uniTrunkGroupEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniTrunkGroupIndex"),
)
if mibBuilder.loadTexts:
    uniTrunkGroupEntry.setStatus("current")


class _UniTrunkGroupIndex_Type(Integer32):
    """Custom type uniTrunkGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniTrunkGroupIndex_Type.__name__ = "Integer32"
_UniTrunkGroupIndex_Object = MibTableColumn
uniTrunkGroupIndex = _UniTrunkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1, 1),
    _UniTrunkGroupIndex_Type()
)
uniTrunkGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniTrunkGroupIndex.setStatus("current")


class _UniTrunkGroupOperationStatus_Type(Integer32):
    """Custom type uniTrunkGroupOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_UniTrunkGroupOperationStatus_Type.__name__ = "Integer32"
_UniTrunkGroupOperationStatus_Object = MibTableColumn
uniTrunkGroupOperationStatus = _UniTrunkGroupOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1, 2),
    _UniTrunkGroupOperationStatus_Type()
)
uniTrunkGroupOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniTrunkGroupOperationStatus.setStatus("current")
_UniTrunkGroupActualSpeed_Type = Integer32
_UniTrunkGroupActualSpeed_Object = MibTableColumn
uniTrunkGroupActualSpeed = _UniTrunkGroupActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1, 3),
    _UniTrunkGroupActualSpeed_Type()
)
uniTrunkGroupActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniTrunkGroupActualSpeed.setStatus("current")
if mibBuilder.loadTexts:
    uniTrunkGroupActualSpeed.setUnits("Mbps")


class _UniTrunkGroupAdminStatus_Type(Integer32):
    """Custom type uniTrunkGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_UniTrunkGroupAdminStatus_Type.__name__ = "Integer32"
_UniTrunkGroupAdminStatus_Object = MibTableColumn
uniTrunkGroupAdminStatus = _UniTrunkGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1, 4),
    _UniTrunkGroupAdminStatus_Type()
)
uniTrunkGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniTrunkGroupAdminStatus.setStatus("current")
_UniPortRateLimitTable_Object = MibTable
uniPortRateLimitTable = _UniPortRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4)
)
if mibBuilder.loadTexts:
    uniPortRateLimitTable.setStatus("current")
_UniPortRateLimitEntry_Object = MibTableRow
uniPortRateLimitEntry = _UniPortRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1)
)
uniPortRateLimitEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniPortRateLimitDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "uniPortRateLimitCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "uniPortRateLimitPortIndex"),
)
if mibBuilder.loadTexts:
    uniPortRateLimitEntry.setStatus("current")


class _UniPortRateLimitDeviceIndex_Type(EponDeviceIndex):
    """Custom type uniPortRateLimitDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniPortRateLimitDeviceIndex_Type.__name__ = "EponDeviceIndex"
_UniPortRateLimitDeviceIndex_Object = MibTableColumn
uniPortRateLimitDeviceIndex = _UniPortRateLimitDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 1),
    _UniPortRateLimitDeviceIndex_Type()
)
uniPortRateLimitDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniPortRateLimitDeviceIndex.setStatus("current")


class _UniPortRateLimitCardIndex_Type(EponCardIndex):
    """Custom type uniPortRateLimitCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniPortRateLimitCardIndex_Type.__name__ = "EponCardIndex"
_UniPortRateLimitCardIndex_Object = MibTableColumn
uniPortRateLimitCardIndex = _UniPortRateLimitCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 2),
    _UniPortRateLimitCardIndex_Type()
)
uniPortRateLimitCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniPortRateLimitCardIndex.setStatus("current")


class _UniPortRateLimitPortIndex_Type(EponPortIndex):
    """Custom type uniPortRateLimitPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniPortRateLimitPortIndex_Type.__name__ = "EponPortIndex"
_UniPortRateLimitPortIndex_Object = MibTableColumn
uniPortRateLimitPortIndex = _UniPortRateLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 3),
    _UniPortRateLimitPortIndex_Type()
)
uniPortRateLimitPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniPortRateLimitPortIndex.setStatus("current")
_UniPortInCIR_Type = Integer32
_UniPortInCIR_Object = MibTableColumn
uniPortInCIR = _UniPortInCIR_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 4),
    _UniPortInCIR_Type()
)
uniPortInCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortInCIR.setStatus("current")
if mibBuilder.loadTexts:
    uniPortInCIR.setUnits("kbps")
_UniPortInCBS_Type = Integer32
_UniPortInCBS_Object = MibTableColumn
uniPortInCBS = _UniPortInCBS_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 5),
    _UniPortInCBS_Type()
)
uniPortInCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortInCBS.setStatus("current")
if mibBuilder.loadTexts:
    uniPortInCBS.setUnits("Kbytes")
_UniPortInEBS_Type = Integer32
_UniPortInEBS_Object = MibTableColumn
uniPortInEBS = _UniPortInEBS_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 6),
    _UniPortInEBS_Type()
)
uniPortInEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortInEBS.setStatus("current")
if mibBuilder.loadTexts:
    uniPortInEBS.setUnits("Kbytes")
_UniPortOutCIR_Type = Integer32
_UniPortOutCIR_Object = MibTableColumn
uniPortOutCIR = _UniPortOutCIR_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 7),
    _UniPortOutCIR_Type()
)
uniPortOutCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortOutCIR.setStatus("current")
if mibBuilder.loadTexts:
    uniPortOutCIR.setUnits("Kbps")
_UniPortOutPIR_Type = Integer32
_UniPortOutPIR_Object = MibTableColumn
uniPortOutPIR = _UniPortOutPIR_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 8),
    _UniPortOutPIR_Type()
)
uniPortOutPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortOutPIR.setStatus("current")
if mibBuilder.loadTexts:
    uniPortOutPIR.setUnits("Kbps")
_UniPortInRateLimitEnable_Type = TruthValue
_UniPortInRateLimitEnable_Object = MibTableColumn
uniPortInRateLimitEnable = _UniPortInRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 9),
    _UniPortInRateLimitEnable_Type()
)
uniPortInRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortInRateLimitEnable.setStatus("current")
_UniPortOutRateLimitEnable_Type = TruthValue
_UniPortOutRateLimitEnable_Object = MibTableColumn
uniPortOutRateLimitEnable = _UniPortOutRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 10),
    _UniPortOutRateLimitEnable_Type()
)
uniPortOutRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortOutRateLimitEnable.setStatus("current")
_UniMirrorTable_Object = MibTable
uniMirrorTable = _UniMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5)
)
if mibBuilder.loadTexts:
    uniMirrorTable.setStatus("current")
_UniMirrorEntry_Object = MibTableRow
uniMirrorEntry = _UniMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1)
)
uniMirrorEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniMirrorGroupIndex"),
)
if mibBuilder.loadTexts:
    uniMirrorEntry.setStatus("current")


class _UniMirrorGroupIndex_Type(Integer32):
    """Custom type uniMirrorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniMirrorGroupIndex_Type.__name__ = "Integer32"
_UniMirrorGroupIndex_Object = MibTableColumn
uniMirrorGroupIndex = _UniMirrorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 1),
    _UniMirrorGroupIndex_Type()
)
uniMirrorGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniMirrorGroupIndex.setStatus("current")
_UniMirrorGroupName_Type = DisplayString
_UniMirrorGroupName_Object = MibTableColumn
uniMirrorGroupName = _UniMirrorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 2),
    _UniMirrorGroupName_Type()
)
uniMirrorGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupName.setStatus("current")
_UniMirrorGroupDstPortList_Type = OctetString
_UniMirrorGroupDstPortList_Object = MibTableColumn
uniMirrorGroupDstPortList = _UniMirrorGroupDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 3),
    _UniMirrorGroupDstPortList_Type()
)
uniMirrorGroupDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupDstPortList.setStatus("current")
_UniMirrorGroupSrcInPortList_Type = OctetString
_UniMirrorGroupSrcInPortList_Object = MibTableColumn
uniMirrorGroupSrcInPortList = _UniMirrorGroupSrcInPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 4),
    _UniMirrorGroupSrcInPortList_Type()
)
uniMirrorGroupSrcInPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupSrcInPortList.setStatus("current")
_UniMirrorGroupSrcOutPortList_Type = OctetString
_UniMirrorGroupSrcOutPortList_Object = MibTableColumn
uniMirrorGroupSrcOutPortList = _UniMirrorGroupSrcOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 5),
    _UniMirrorGroupSrcOutPortList_Type()
)
uniMirrorGroupSrcOutPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupSrcOutPortList.setStatus("current")
_UniMirrorGroupRowstatus_Type = RowStatus
_UniMirrorGroupRowstatus_Object = MibTableColumn
uniMirrorGroupRowstatus = _UniMirrorGroupRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 6),
    _UniMirrorGroupRowstatus_Type()
)
uniMirrorGroupRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupRowstatus.setStatus("current")
_UniBroadcastStormSuppressionTable_Object = MibTable
uniBroadcastStormSuppressionTable = _UniBroadcastStormSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6)
)
if mibBuilder.loadTexts:
    uniBroadcastStormSuppressionTable.setStatus("current")
_UniBroadcastStormSuppressionEntry_Object = MibTableRow
uniBroadcastStormSuppressionEntry = _UniBroadcastStormSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1)
)
uniBroadcastStormSuppressionEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniBroadcastStormSuppressionCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "uniBroadcastStormSuppressionPortIndex"),
)
if mibBuilder.loadTexts:
    uniBroadcastStormSuppressionEntry.setStatus("current")


class _UniBroadcastStormSuppressionCardIndex_Type(EponCardIndex):
    """Custom type uniBroadcastStormSuppressionCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniBroadcastStormSuppressionCardIndex_Type.__name__ = "EponCardIndex"
_UniBroadcastStormSuppressionCardIndex_Object = MibTableColumn
uniBroadcastStormSuppressionCardIndex = _UniBroadcastStormSuppressionCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 1),
    _UniBroadcastStormSuppressionCardIndex_Type()
)
uniBroadcastStormSuppressionCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniBroadcastStormSuppressionCardIndex.setStatus("current")


class _UniBroadcastStormSuppressionPortIndex_Type(EponPortIndex):
    """Custom type uniBroadcastStormSuppressionPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniBroadcastStormSuppressionPortIndex_Type.__name__ = "EponPortIndex"
_UniBroadcastStormSuppressionPortIndex_Object = MibTableColumn
uniBroadcastStormSuppressionPortIndex = _UniBroadcastStormSuppressionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 2),
    _UniBroadcastStormSuppressionPortIndex_Type()
)
uniBroadcastStormSuppressionPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniBroadcastStormSuppressionPortIndex.setStatus("current")
_UniUnicastStormEnable_Type = TruthValue
_UniUnicastStormEnable_Object = MibTableColumn
uniUnicastStormEnable = _UniUnicastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 3),
    _UniUnicastStormEnable_Type()
)
uniUnicastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniUnicastStormEnable.setStatus("current")
_UniUnicastStormInPacketRate_Type = Integer32
_UniUnicastStormInPacketRate_Object = MibTableColumn
uniUnicastStormInPacketRate = _UniUnicastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 4),
    _UniUnicastStormInPacketRate_Type()
)
uniUnicastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniUnicastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniUnicastStormInPacketRate.setUnits("pps")
_UniUnicastStormOutPacketRate_Type = Integer32
_UniUnicastStormOutPacketRate_Object = MibTableColumn
uniUnicastStormOutPacketRate = _UniUnicastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 5),
    _UniUnicastStormOutPacketRate_Type()
)
uniUnicastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniUnicastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniUnicastStormOutPacketRate.setUnits("pps")
_UniMulticastStormEnable_Type = TruthValue
_UniMulticastStormEnable_Object = MibTableColumn
uniMulticastStormEnable = _UniMulticastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 6),
    _UniMulticastStormEnable_Type()
)
uniMulticastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMulticastStormEnable.setStatus("current")
_UniMulticastStormInPacketRate_Type = Integer32
_UniMulticastStormInPacketRate_Object = MibTableColumn
uniMulticastStormInPacketRate = _UniMulticastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 7),
    _UniMulticastStormInPacketRate_Type()
)
uniMulticastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMulticastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniMulticastStormInPacketRate.setUnits("pps")
_UniMulticastStormOutPacketRate_Type = Integer32
_UniMulticastStormOutPacketRate_Object = MibTableColumn
uniMulticastStormOutPacketRate = _UniMulticastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 8),
    _UniMulticastStormOutPacketRate_Type()
)
uniMulticastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMulticastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniMulticastStormOutPacketRate.setUnits("pps")
_UniBroadcastStormEnable_Type = TruthValue
_UniBroadcastStormEnable_Object = MibTableColumn
uniBroadcastStormEnable = _UniBroadcastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 9),
    _UniBroadcastStormEnable_Type()
)
uniBroadcastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniBroadcastStormEnable.setStatus("current")
_UniBroadcastStormInPacketRate_Type = Integer32
_UniBroadcastStormInPacketRate_Object = MibTableColumn
uniBroadcastStormInPacketRate = _UniBroadcastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 10),
    _UniBroadcastStormInPacketRate_Type()
)
uniBroadcastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniBroadcastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniBroadcastStormInPacketRate.setUnits("pps")
_UniBroadcastStormOutPacketRate_Type = Integer32
_UniBroadcastStormOutPacketRate_Object = MibTableColumn
uniBroadcastStormOutPacketRate = _UniBroadcastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 11),
    _UniBroadcastStormOutPacketRate_Type()
)
uniBroadcastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniBroadcastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniBroadcastStormOutPacketRate.setUnits("pps")
_UniExtAttributeTable_Object = MibTable
uniExtAttributeTable = _UniExtAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7)
)
if mibBuilder.loadTexts:
    uniExtAttributeTable.setStatus("current")
_UniExtAttributeEntry_Object = MibTableRow
uniExtAttributeEntry = _UniExtAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1)
)
uniExtAttributeEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniExtAttributeCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "uniExtAttributePortIndex"),
)
if mibBuilder.loadTexts:
    uniExtAttributeEntry.setStatus("current")


class _UniExtAttributeCardIndex_Type(EponCardIndex):
    """Custom type uniExtAttributeCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniExtAttributeCardIndex_Type.__name__ = "EponCardIndex"
_UniExtAttributeCardIndex_Object = MibTableColumn
uniExtAttributeCardIndex = _UniExtAttributeCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 1),
    _UniExtAttributeCardIndex_Type()
)
uniExtAttributeCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniExtAttributeCardIndex.setStatus("current")


class _UniExtAttributePortIndex_Type(EponPortIndex):
    """Custom type uniExtAttributePortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniExtAttributePortIndex_Type.__name__ = "EponPortIndex"
_UniExtAttributePortIndex_Object = MibTableColumn
uniExtAttributePortIndex = _UniExtAttributePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 2),
    _UniExtAttributePortIndex_Type()
)
uniExtAttributePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniExtAttributePortIndex.setStatus("current")
_UniPerfStats15minuteEnable_Type = TruthValue
_UniPerfStats15minuteEnable_Object = MibTableColumn
uniPerfStats15minuteEnable = _UniPerfStats15minuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 3),
    _UniPerfStats15minuteEnable_Type()
)
uniPerfStats15minuteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPerfStats15minuteEnable.setStatus("current")
_UniPerfStats24hourEnable_Type = TruthValue
_UniPerfStats24hourEnable_Object = MibTableColumn
uniPerfStats24hourEnable = _UniPerfStats24hourEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 4),
    _UniPerfStats24hourEnable_Type()
)
uniPerfStats24hourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPerfStats24hourEnable.setStatus("current")
_UniLastChangeTime_Type = TimeTicks
_UniLastChangeTime_Object = MibTableColumn
uniLastChangeTime = _UniLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 5),
    _UniLastChangeTime_Type()
)
uniLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniLastChangeTime.setStatus("current")
_UniIsolationEnable_Type = TruthValue
_UniIsolationEnable_Object = MibTableColumn
uniIsolationEnable = _UniIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 6),
    _UniIsolationEnable_Type()
)
uniIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniIsolationEnable.setStatus("current")
_UniExMacAddrLearnMaxNum_Type = Integer32
_UniExMacAddrLearnMaxNum_Object = MibTableColumn
uniExMacAddrLearnMaxNum = _UniExMacAddrLearnMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 7),
    _UniExMacAddrLearnMaxNum_Type()
)
uniExMacAddrLearnMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniExMacAddrLearnMaxNum.setStatus("current")
_UniAutoNegotiationAdvertisedTechAbility_Type = Integer32
_UniAutoNegotiationAdvertisedTechAbility_Object = MibTableColumn
uniAutoNegotiationAdvertisedTechAbility = _UniAutoNegotiationAdvertisedTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 8),
    _UniAutoNegotiationAdvertisedTechAbility_Type()
)
uniAutoNegotiationAdvertisedTechAbility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniAutoNegotiationAdvertisedTechAbility.setStatus("current")


class _UniMacAddrClearByPort_Type(Integer32):
    """Custom type uniMacAddrClearByPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearDynamic", 1)
    )


_UniMacAddrClearByPort_Type.__name__ = "Integer32"
_UniMacAddrClearByPort_Object = MibTableColumn
uniMacAddrClearByPort = _UniMacAddrClearByPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 9),
    _UniMacAddrClearByPort_Type()
)
uniMacAddrClearByPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMacAddrClearByPort.setStatus("current")
_IgmpManagementObjects_ObjectIdentity = ObjectIdentity
igmpManagementObjects = _IgmpManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6)
)
_IgmpEntityTable_Object = MibTable
igmpEntityTable = _IgmpEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    igmpEntityTable.setStatus("current")
_IgmpEntityEntry_Object = MibTableRow
igmpEntityEntry = _IgmpEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1, 1)
)
igmpEntityEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "igmpDeviceIndex"),
)
if mibBuilder.loadTexts:
    igmpEntityEntry.setStatus("current")


class _IgmpDeviceIndex_Type(Integer32):
    """Custom type igmpDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IgmpDeviceIndex_Type.__name__ = "Integer32"
_IgmpDeviceIndex_Object = MibTableColumn
igmpDeviceIndex = _IgmpDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1, 1, 1),
    _IgmpDeviceIndex_Type()
)
igmpDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpDeviceIndex.setStatus("current")


class _IgmpMode_Type(Integer32):
    """Custom type igmpMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("proxy", 1),
          ("ctc", 2),
          ("disabled", 3),
          ("snooping", 4))
    )


_IgmpMode_Type.__name__ = "Integer32"
_IgmpMode_Object = MibTableColumn
igmpMode = _IgmpMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1, 1, 2),
    _IgmpMode_Type()
)
igmpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMode.setStatus("current")
_MaxQueryResponseTime_Type = Integer32
_MaxQueryResponseTime_Object = MibTableColumn
maxQueryResponseTime = _MaxQueryResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1, 1, 3),
    _MaxQueryResponseTime_Type()
)
maxQueryResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxQueryResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    maxQueryResponseTime.setUnits("tenth second")
_RobustVariable_Type = Integer32
_RobustVariable_Object = MibTableColumn
robustVariable = _RobustVariable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1, 1, 4),
    _RobustVariable_Type()
)
robustVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    robustVariable.setStatus("current")
_QueryInterval_Type = Integer32
_QueryInterval_Object = MibTableColumn
queryInterval = _QueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1, 1, 5),
    _QueryInterval_Type()
)
queryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queryInterval.setStatus("current")
if mibBuilder.loadTexts:
    queryInterval.setUnits("seconds")
_LastMemberQueryInterval_Type = Integer32
_LastMemberQueryInterval_Object = MibTableColumn
lastMemberQueryInterval = _LastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1, 1, 6),
    _LastMemberQueryInterval_Type()
)
lastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    lastMemberQueryInterval.setUnits("tenth second")
_LastMemberQueryCount_Type = Integer32
_LastMemberQueryCount_Object = MibTableColumn
lastMemberQueryCount = _LastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1, 1, 7),
    _LastMemberQueryCount_Type()
)
lastMemberQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lastMemberQueryCount.setStatus("current")


class _IgmpVersion_Type(Integer32):
    """Custom type igmpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_IgmpVersion_Type.__name__ = "Integer32"
_IgmpVersion_Object = MibTableColumn
igmpVersion = _IgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 1, 1, 8),
    _IgmpVersion_Type()
)
igmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpVersion.setStatus("current")
_IgmpProxyParaTable_Object = MibTable
igmpProxyParaTable = _IgmpProxyParaTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2)
)
if mibBuilder.loadTexts:
    igmpProxyParaTable.setStatus("current")
_IgmpProxyParaEntry_Object = MibTableRow
igmpProxyParaEntry = _IgmpProxyParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2, 1)
)
igmpProxyParaEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "proxyIndex"),
)
if mibBuilder.loadTexts:
    igmpProxyParaEntry.setStatus("current")


class _ProxyIndex_Type(Integer32):
    """Custom type proxyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_ProxyIndex_Type.__name__ = "Integer32"
_ProxyIndex_Object = MibTableColumn
proxyIndex = _ProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2, 1, 1),
    _ProxyIndex_Type()
)
proxyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyIndex.setStatus("current")


class _ProxyName_Type(OctetString):
    """Custom type proxyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ProxyName_Type.__name__ = "OctetString"
_ProxyName_Object = MibTableColumn
proxyName = _ProxyName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2, 1, 2),
    _ProxyName_Type()
)
proxyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    proxyName.setStatus("current")
_ProxySrcIPAddress_Type = IpAddress
_ProxySrcIPAddress_Object = MibTableColumn
proxySrcIPAddress = _ProxySrcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2, 1, 3),
    _ProxySrcIPAddress_Type()
)
proxySrcIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    proxySrcIPAddress.setStatus("current")
_ProxyMulticastVID_Type = Integer32
_ProxyMulticastVID_Object = MibTableColumn
proxyMulticastVID = _ProxyMulticastVID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2, 1, 4),
    _ProxyMulticastVID_Type()
)
proxyMulticastVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    proxyMulticastVID.setStatus("current")
_ProxyMulticastIPAddress_Type = IpAddress
_ProxyMulticastIPAddress_Object = MibTableColumn
proxyMulticastIPAddress = _ProxyMulticastIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2, 1, 5),
    _ProxyMulticastIPAddress_Type()
)
proxyMulticastIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    proxyMulticastIPAddress.setStatus("current")
_MulticastAssuredBW_Type = Unsigned32
_MulticastAssuredBW_Object = MibTableColumn
multicastAssuredBW = _MulticastAssuredBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2, 1, 6),
    _MulticastAssuredBW_Type()
)
multicastAssuredBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastAssuredBW.setStatus("current")
if mibBuilder.loadTexts:
    multicastAssuredBW.setUnits("kbps")
_MulticastMaxBW_Type = Unsigned32
_MulticastMaxBW_Object = MibTableColumn
multicastMaxBW = _MulticastMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2, 1, 7),
    _MulticastMaxBW_Type()
)
multicastMaxBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastMaxBW.setStatus("current")
if mibBuilder.loadTexts:
    multicastMaxBW.setUnits("kbps")
_ProxyRowStatus_Type = RowStatus
_ProxyRowStatus_Object = MibTableColumn
proxyRowStatus = _ProxyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 2, 1, 8),
    _ProxyRowStatus_Type()
)
proxyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    proxyRowStatus.setStatus("current")
_IgmpForwardingTable_Object = MibTable
igmpForwardingTable = _IgmpForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 3)
)
if mibBuilder.loadTexts:
    igmpForwardingTable.setStatus("current")
_IgmpForwardingEntry_Object = MibTableRow
igmpForwardingEntry = _IgmpForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 3, 1)
)
igmpForwardingEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "groupDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "groupVlanIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "groupIPAddress"),
)
if mibBuilder.loadTexts:
    igmpForwardingEntry.setStatus("current")


class _GroupDeviceIndex_Type(Integer32):
    """Custom type groupDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GroupDeviceIndex_Type.__name__ = "Integer32"
_GroupDeviceIndex_Object = MibTableColumn
groupDeviceIndex = _GroupDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 3, 1, 1),
    _GroupDeviceIndex_Type()
)
groupDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupDeviceIndex.setStatus("current")


class _GroupVlanIndex_Type(Integer32):
    """Custom type groupVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_GroupVlanIndex_Type.__name__ = "Integer32"
_GroupVlanIndex_Object = MibTableColumn
groupVlanIndex = _GroupVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 3, 1, 2),
    _GroupVlanIndex_Type()
)
groupVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupVlanIndex.setStatus("current")
_GroupIPAddress_Type = IpAddress
_GroupIPAddress_Object = MibTableColumn
groupIPAddress = _GroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 3, 1, 3),
    _GroupIPAddress_Type()
)
groupIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupIPAddress.setStatus("current")
_GroupPortList_Type = OctetString
_GroupPortList_Object = MibTableColumn
groupPortList = _GroupPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 3, 1, 4),
    _GroupPortList_Type()
)
groupPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupPortList.setStatus("current")
_ControllededMulticastTable_ObjectIdentity = ObjectIdentity
controllededMulticastTable = _ControllededMulticastTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4)
)
if mibBuilder.loadTexts:
    controllededMulticastTable.setStatus("current")
_ControlledMulticastUserAuthorityTable_Object = MibTable
controlledMulticastUserAuthorityTable = _ControlledMulticastUserAuthorityTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 1)
)
if mibBuilder.loadTexts:
    controlledMulticastUserAuthorityTable.setStatus("current")
_ControlledMulticastUserAuthorityEntry_Object = MibTableRow
controlledMulticastUserAuthorityEntry = _ControlledMulticastUserAuthorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 1, 1)
)
controlledMulticastUserAuthorityEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "cmDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "cmCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "cmPortIndex"),
)
if mibBuilder.loadTexts:
    controlledMulticastUserAuthorityEntry.setStatus("current")


class _CmDeviceIndex_Type(EponDeviceIndex):
    """Custom type cmDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmDeviceIndex_Type.__name__ = "EponDeviceIndex"
_CmDeviceIndex_Object = MibTableColumn
cmDeviceIndex = _CmDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 1, 1, 1),
    _CmDeviceIndex_Type()
)
cmDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmDeviceIndex.setStatus("current")


class _CmCardIndex_Type(EponCardIndex):
    """Custom type cmCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmCardIndex_Type.__name__ = "EponCardIndex"
_CmCardIndex_Object = MibTableColumn
cmCardIndex = _CmCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 1, 1, 2),
    _CmCardIndex_Type()
)
cmCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmCardIndex.setStatus("current")


class _CmPortIndex_Type(EponPortIndex):
    """Custom type cmPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CmPortIndex_Type.__name__ = "EponPortIndex"
_CmPortIndex_Object = MibTableColumn
cmPortIndex = _CmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 1, 1, 3),
    _CmPortIndex_Type()
)
cmPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmPortIndex.setStatus("current")


class _MulticastPackageList_Type(OctetString):
    """Custom type multicastPackageList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_MulticastPackageList_Type.__name__ = "OctetString"
_MulticastPackageList_Object = MibTableColumn
multicastPackageList = _MulticastPackageList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 1, 1, 4),
    _MulticastPackageList_Type()
)
multicastPackageList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastPackageList.setStatus("current")
_IgmpGlobalBW_Type = Unsigned32
_IgmpGlobalBW_Object = MibTableColumn
igmpGlobalBW = _IgmpGlobalBW_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 1, 1, 5),
    _IgmpGlobalBW_Type()
)
igmpGlobalBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpGlobalBW.setStatus("current")
if mibBuilder.loadTexts:
    igmpGlobalBW.setUnits("kbps")
_IgmpGlobalBWUsed_Type = Unsigned32
_IgmpGlobalBWUsed_Object = MibTableColumn
igmpGlobalBWUsed = _IgmpGlobalBWUsed_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 1, 1, 6),
    _IgmpGlobalBWUsed_Type()
)
igmpGlobalBWUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGlobalBWUsed.setStatus("current")
if mibBuilder.loadTexts:
    igmpGlobalBWUsed.setUnits("kbps")
_CmUserAuthorityRowStatus_Type = RowStatus
_CmUserAuthorityRowStatus_Object = MibTableColumn
cmUserAuthorityRowStatus = _CmUserAuthorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 1, 1, 7),
    _CmUserAuthorityRowStatus_Type()
)
cmUserAuthorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmUserAuthorityRowStatus.setStatus("current")
_ControlledMulticastPackageTable_Object = MibTable
controlledMulticastPackageTable = _ControlledMulticastPackageTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2)
)
if mibBuilder.loadTexts:
    controlledMulticastPackageTable.setStatus("current")
_ControlledMulticastPackageEntry_Object = MibTableRow
controlledMulticastPackageEntry = _ControlledMulticastPackageEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1)
)
controlledMulticastPackageEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "cmIndex"),
)
if mibBuilder.loadTexts:
    controlledMulticastPackageEntry.setStatus("current")


class _CmIndex_Type(Integer32):
    """Custom type cmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_CmIndex_Type.__name__ = "Integer32"
_CmIndex_Object = MibTableColumn
cmIndex = _CmIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 1),
    _CmIndex_Type()
)
cmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmIndex.setStatus("current")


class _CmName_Type(OctetString):
    """Custom type cmName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CmName_Type.__name__ = "OctetString"
_CmName_Object = MibTableColumn
cmName = _CmName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 2),
    _CmName_Type()
)
cmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmName.setStatus("current")


class _CmProxyList_Type(OctetString):
    """Custom type cmProxyList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_CmProxyList_Type.__name__ = "OctetString"
_CmProxyList_Object = MibTableColumn
cmProxyList = _CmProxyList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 3),
    _CmProxyList_Type()
)
cmProxyList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmProxyList.setStatus("current")


class _MulticastUserAuthority_Type(Integer32):
    """Custom type multicastUserAuthority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("preview", 2),
          ("deny", 3))
    )


_MulticastUserAuthority_Type.__name__ = "Integer32"
_MulticastUserAuthority_Object = MibTableColumn
multicastUserAuthority = _MulticastUserAuthority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 4),
    _MulticastUserAuthority_Type()
)
multicastUserAuthority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    multicastUserAuthority.setStatus("current")
_MaxRequestChannelNum_Type = Integer32
_MaxRequestChannelNum_Object = MibTableColumn
maxRequestChannelNum = _MaxRequestChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 5),
    _MaxRequestChannelNum_Type()
)
maxRequestChannelNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    maxRequestChannelNum.setStatus("current")
_SinglePreviewTime_Type = Integer32
_SinglePreviewTime_Object = MibTableColumn
singlePreviewTime = _SinglePreviewTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 6),
    _SinglePreviewTime_Type()
)
singlePreviewTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    singlePreviewTime.setStatus("current")
if mibBuilder.loadTexts:
    singlePreviewTime.setUnits("seconds")
_TotalPreviewTime_Type = Integer32
_TotalPreviewTime_Object = MibTableColumn
totalPreviewTime = _TotalPreviewTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 7),
    _TotalPreviewTime_Type()
)
totalPreviewTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    totalPreviewTime.setStatus("current")
if mibBuilder.loadTexts:
    totalPreviewTime.setUnits("seconds")
_PreviewResetTime_Type = Integer32
_PreviewResetTime_Object = MibTableColumn
previewResetTime = _PreviewResetTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 8),
    _PreviewResetTime_Type()
)
previewResetTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    previewResetTime.setStatus("current")
if mibBuilder.loadTexts:
    previewResetTime.setUnits("seconds")
_PreviewCount_Type = Integer32
_PreviewCount_Object = MibTableColumn
previewCount = _PreviewCount_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 9),
    _PreviewCount_Type()
)
previewCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    previewCount.setStatus("current")
_CmRowStatus_Type = RowStatus
_CmRowStatus_Object = MibTableColumn
cmRowStatus = _CmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 4, 2, 1, 10),
    _CmRowStatus_Type()
)
cmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmRowStatus.setStatus("current")
_IgmpOnuUniTable_Object = MibTable
igmpOnuUniTable = _IgmpOnuUniTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 5)
)
if mibBuilder.loadTexts:
    igmpOnuUniTable.setStatus("current")
_IgmpOnuUniEntry_Object = MibTableRow
igmpOnuUniEntry = _IgmpOnuUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 5, 1)
)
igmpOnuUniEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "uniMvlanDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "uniMvlanCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "uniMvlanPortIndex"),
)
if mibBuilder.loadTexts:
    igmpOnuUniEntry.setStatus("current")


class _UniMvlanDeviceIndex_Type(EponDeviceIndex):
    """Custom type uniMvlanDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniMvlanDeviceIndex_Type.__name__ = "EponDeviceIndex"
_UniMvlanDeviceIndex_Object = MibTableColumn
uniMvlanDeviceIndex = _UniMvlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 5, 1, 1),
    _UniMvlanDeviceIndex_Type()
)
uniMvlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniMvlanDeviceIndex.setStatus("current")


class _UniMvlanCardIndex_Type(EponCardIndex):
    """Custom type uniMvlanCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UniMvlanCardIndex_Type.__name__ = "EponCardIndex"
_UniMvlanCardIndex_Object = MibTableColumn
uniMvlanCardIndex = _UniMvlanCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 5, 1, 2),
    _UniMvlanCardIndex_Type()
)
uniMvlanCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniMvlanCardIndex.setStatus("current")
_UniMvlanPortIndex_Type = EponPortIndex
_UniMvlanPortIndex_Object = MibTableColumn
uniMvlanPortIndex = _UniMvlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 5, 1, 3),
    _UniMvlanPortIndex_Type()
)
uniMvlanPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMvlanPortIndex.setStatus("current")


class _UniMvlanVid_Type(OctetString):
    """Custom type uniMvlanVid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_UniMvlanVid_Type.__name__ = "OctetString"
_UniMvlanVid_Object = MibTableColumn
uniMvlanVid = _UniMvlanVid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 5, 1, 4),
    _UniMvlanVid_Type()
)
uniMvlanVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMvlanVid.setStatus("current")
_UniMaxMultiNum_Type = Integer32
_UniMaxMultiNum_Object = MibTableColumn
uniMaxMultiNum = _UniMaxMultiNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 5, 1, 5),
    _UniMaxMultiNum_Type()
)
uniMaxMultiNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMaxMultiNum.setStatus("current")


class _UniMvlanTag_Type(Integer32):
    """Custom type uniMvlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("Strip", 0),
          ("NoStrip", 1))
    )


_UniMvlanTag_Type.__name__ = "Integer32"
_UniMvlanTag_Object = MibTableColumn
uniMvlanTag = _UniMvlanTag_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 5, 1, 6),
    _UniMvlanTag_Type()
)
uniMvlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMvlanTag.setStatus("current")


class _UniMvlanRowstatus_Type(Integer32):
    """Custom type uniMvlanRowstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_UniMvlanRowstatus_Type.__name__ = "Integer32"
_UniMvlanRowstatus_Object = MibTableColumn
uniMvlanRowstatus = _UniMvlanRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 5, 1, 7),
    _UniMvlanRowstatus_Type()
)
uniMvlanRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMvlanRowstatus.setStatus("current")
_IgmpOltMulticastVlanTable_Object = MibTable
igmpOltMulticastVlanTable = _IgmpOltMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6)
)
if mibBuilder.loadTexts:
    igmpOltMulticastVlanTable.setStatus("current")
_IgmpOltMulticastVlanEntry_Object = MibTableRow
igmpOltMulticastVlanEntry = _IgmpOltMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6, 1)
)
igmpOltMulticastVlanEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "igmpOltMulticastVlanDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "multicastVlanId"),
)
if mibBuilder.loadTexts:
    igmpOltMulticastVlanEntry.setStatus("current")
_IgmpOltMulticastVlanDeviceIndex_Type = Integer32
_IgmpOltMulticastVlanDeviceIndex_Object = MibTableColumn
igmpOltMulticastVlanDeviceIndex = _IgmpOltMulticastVlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6, 1, 1),
    _IgmpOltMulticastVlanDeviceIndex_Type()
)
igmpOltMulticastVlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpOltMulticastVlanDeviceIndex.setStatus("current")
_MulticastVlanId_Type = Integer32
_MulticastVlanId_Object = MibTableColumn
multicastVlanId = _MulticastVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6, 1, 2),
    _MulticastVlanId_Type()
)
multicastVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastVlanId.setStatus("current")
_MVlanMaxQueryResponseTime_Type = Integer32
_MVlanMaxQueryResponseTime_Object = MibTableColumn
mVlanMaxQueryResponseTime = _MVlanMaxQueryResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6, 1, 3),
    _MVlanMaxQueryResponseTime_Type()
)
mVlanMaxQueryResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mVlanMaxQueryResponseTime.setStatus("optional")
if mibBuilder.loadTexts:
    mVlanMaxQueryResponseTime.setUnits("tenth second")
_MVlanRobustVariable_Type = Integer32
_MVlanRobustVariable_Object = MibTableColumn
mVlanRobustVariable = _MVlanRobustVariable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6, 1, 4),
    _MVlanRobustVariable_Type()
)
mVlanRobustVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mVlanRobustVariable.setStatus("optional")
_MVlanQueryInterval_Type = Integer32
_MVlanQueryInterval_Object = MibTableColumn
mVlanQueryInterval = _MVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6, 1, 5),
    _MVlanQueryInterval_Type()
)
mVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mVlanQueryInterval.setStatus("optional")
if mibBuilder.loadTexts:
    mVlanQueryInterval.setUnits("seconds")
_MVlanLastMemberQueryInterval_Type = Integer32
_MVlanLastMemberQueryInterval_Object = MibTableColumn
mVlanLastMemberQueryInterval = _MVlanLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6, 1, 6),
    _MVlanLastMemberQueryInterval_Type()
)
mVlanLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mVlanLastMemberQueryInterval.setStatus("optional")
if mibBuilder.loadTexts:
    mVlanLastMemberQueryInterval.setUnits("tenth second")
_MVlanLastMemberQueryCount_Type = Integer32
_MVlanLastMemberQueryCount_Object = MibTableColumn
mVlanLastMemberQueryCount = _MVlanLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6, 1, 7),
    _MVlanLastMemberQueryCount_Type()
)
mVlanLastMemberQueryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mVlanLastMemberQueryCount.setStatus("optional")


class _MvlanRowstatus_Type(Integer32):
    """Custom type mvlanRowstatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_MvlanRowstatus_Type.__name__ = "Integer32"
_MvlanRowstatus_Object = MibTableColumn
mvlanRowstatus = _MvlanRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 6, 1, 8),
    _MvlanRowstatus_Type()
)
mvlanRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mvlanRowstatus.setStatus("current")
_IgmpSniMulticastVlanTable_Object = MibTable
igmpSniMulticastVlanTable = _IgmpSniMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 7)
)
if mibBuilder.loadTexts:
    igmpSniMulticastVlanTable.setStatus("current")
_IgmpSniMulticastVlanEntry_Object = MibTableRow
igmpSniMulticastVlanEntry = _IgmpSniMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 7, 1)
)
igmpSniMulticastVlanEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "sniMultiVlanVid"),
    (0, "NSCRTV-FTTX-EPON-MIB", "sniMultiVlanDeviceIndex"),
)
if mibBuilder.loadTexts:
    igmpSniMulticastVlanEntry.setStatus("current")
_SniMultiVlanVid_Type = Integer32
_SniMultiVlanVid_Object = MibTableColumn
sniMultiVlanVid = _SniMultiVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 7, 1, 1),
    _SniMultiVlanVid_Type()
)
sniMultiVlanVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMultiVlanVid.setStatus("current")
_SniMultiVlanDeviceIndex_Type = EponDeviceIndex
_SniMultiVlanDeviceIndex_Object = MibTableColumn
sniMultiVlanDeviceIndex = _SniMultiVlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 7, 1, 2),
    _SniMultiVlanDeviceIndex_Type()
)
sniMultiVlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sniMultiVlanDeviceIndex.setStatus("current")
_SniMultiVlanRowstatus_Type = Integer32
_SniMultiVlanRowstatus_Object = MibTableColumn
sniMultiVlanRowstatus = _SniMultiVlanRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 7, 1, 3),
    _SniMultiVlanRowstatus_Type()
)
sniMultiVlanRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sniMultiVlanRowstatus.setStatus("current")
_OnuIgmpModeTable_Object = MibTable
onuIgmpModeTable = _OnuIgmpModeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 8)
)
if mibBuilder.loadTexts:
    onuIgmpModeTable.setStatus("current")
_OnuIgmpModeEntry_Object = MibTableRow
onuIgmpModeEntry = _OnuIgmpModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 8, 1)
)
onuIgmpModeEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuIgmpModeDeviceIndex"),
)
if mibBuilder.loadTexts:
    onuIgmpModeEntry.setStatus("current")
_OnuIgmpModeDeviceIndex_Type = EponDeviceIndex
_OnuIgmpModeDeviceIndex_Object = MibTableColumn
onuIgmpModeDeviceIndex = _OnuIgmpModeDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 8, 1, 1),
    _OnuIgmpModeDeviceIndex_Type()
)
onuIgmpModeDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuIgmpModeDeviceIndex.setStatus("current")


class _OnuIgmpMode_Type(Integer32):
    """Custom type onuIgmpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("igmp-snooping", 2),
          ("ctc", 3))
    )


_OnuIgmpMode_Type.__name__ = "Integer32"
_OnuIgmpMode_Object = MibTableColumn
onuIgmpMode = _OnuIgmpMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 6, 8, 1, 2),
    _OnuIgmpMode_Type()
)
onuIgmpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuIgmpMode.setStatus("current")
_VlanManagementObjects_ObjectIdentity = ObjectIdentity
vlanManagementObjects = _VlanManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7)
)
_VlanGlobalInfoTable_Object = MibTable
vlanGlobalInfoTable = _VlanGlobalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    vlanGlobalInfoTable.setStatus("current")
_VlanGlobalInfoEntry_Object = MibTableRow
vlanGlobalInfoEntry = _VlanGlobalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1)
)
vlanGlobalInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "vlanDeviceIndex"),
)
if mibBuilder.loadTexts:
    vlanGlobalInfoEntry.setStatus("current")


class _VlanDeviceIndex_Type(Integer32):
    """Custom type vlanDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VlanDeviceIndex_Type.__name__ = "Integer32"
_VlanDeviceIndex_Object = MibTableColumn
vlanDeviceIndex = _VlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1, 1),
    _VlanDeviceIndex_Type()
)
vlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanDeviceIndex.setStatus("current")
_MaxVlanId_Type = Integer32
_MaxVlanId_Object = MibTableColumn
maxVlanId = _MaxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1, 2),
    _MaxVlanId_Type()
)
maxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxVlanId.setStatus("current")
_MaxSupportVlans_Type = Integer32
_MaxSupportVlans_Object = MibTableColumn
maxSupportVlans = _MaxSupportVlans_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1, 3),
    _MaxSupportVlans_Type()
)
maxSupportVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSupportVlans.setStatus("current")
_CreatedVlanNumber_Type = Integer32
_CreatedVlanNumber_Object = MibTableColumn
createdVlanNumber = _CreatedVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 1, 1, 4),
    _CreatedVlanNumber_Type()
)
createdVlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    createdVlanNumber.setStatus("current")
_VlanConfigGroup_ObjectIdentity = ObjectIdentity
vlanConfigGroup = _VlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2)
)
if mibBuilder.loadTexts:
    vlanConfigGroup.setStatus("current")
_OltVlanConfigTable_Object = MibTable
oltVlanConfigTable = _OltVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1)
)
if mibBuilder.loadTexts:
    oltVlanConfigTable.setStatus("current")
_OltVlanConfigEntry_Object = MibTableRow
oltVlanConfigEntry = _OltVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1)
)
oltVlanConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "oltVlanIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "oltVlanDeviceIndex"),
)
if mibBuilder.loadTexts:
    oltVlanConfigEntry.setStatus("current")


class _OltVlanIndex_Type(Integer32):
    """Custom type oltVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OltVlanIndex_Type.__name__ = "Integer32"
_OltVlanIndex_Object = MibTableColumn
oltVlanIndex = _OltVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 1),
    _OltVlanIndex_Type()
)
oltVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oltVlanIndex.setStatus("current")


class _OltVlanDeviceIndex_Type(Integer32):
    """Custom type oltVlanDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OltVlanDeviceIndex_Type.__name__ = "Integer32"
_OltVlanDeviceIndex_Object = MibTableColumn
oltVlanDeviceIndex = _OltVlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 2),
    _OltVlanDeviceIndex_Type()
)
oltVlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oltVlanDeviceIndex.setStatus("current")


class _OltVlanName_Type(OctetString):
    """Custom type oltVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OltVlanName_Type.__name__ = "OctetString"
_OltVlanName_Object = MibTableColumn
oltVlanName = _OltVlanName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 3),
    _OltVlanName_Type()
)
oltVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oltVlanName.setStatus("current")
_TaggedPort_Type = OctetString
_TaggedPort_Object = MibTableColumn
taggedPort = _TaggedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 4),
    _TaggedPort_Type()
)
taggedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    taggedPort.setStatus("current")
_UntaggedPort_Type = OctetString
_UntaggedPort_Object = MibTableColumn
untaggedPort = _UntaggedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 5),
    _UntaggedPort_Type()
)
untaggedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    untaggedPort.setStatus("current")
_OltVlanRowStatus_Type = RowStatus
_OltVlanRowStatus_Object = MibTableColumn
oltVlanRowStatus = _OltVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 1, 1, 6),
    _OltVlanRowStatus_Type()
)
oltVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oltVlanRowStatus.setStatus("current")
_OnuVlanConfigTable_Object = MibTable
onuVlanConfigTable = _OnuVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2)
)
if mibBuilder.loadTexts:
    onuVlanConfigTable.setStatus("current")
_OnuVlanConfigEntry_Object = MibTableRow
onuVlanConfigEntry = _OnuVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1)
)
onuVlanConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuVlanIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "onuVlanDeviceIndex"),
)
if mibBuilder.loadTexts:
    onuVlanConfigEntry.setStatus("current")


class _OnuVlanIndex_Type(Integer32):
    """Custom type onuVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuVlanIndex_Type.__name__ = "Integer32"
_OnuVlanIndex_Object = MibTableColumn
onuVlanIndex = _OnuVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 1),
    _OnuVlanIndex_Type()
)
onuVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuVlanIndex.setStatus("current")


class _OnuVlanDeviceIndex_Type(EponDeviceIndex):
    """Custom type onuVlanDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuVlanDeviceIndex_Type.__name__ = "EponDeviceIndex"
_OnuVlanDeviceIndex_Object = MibTableColumn
onuVlanDeviceIndex = _OnuVlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 2),
    _OnuVlanDeviceIndex_Type()
)
onuVlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuVlanDeviceIndex.setStatus("current")


class _OnuVlanName_Type(OctetString):
    """Custom type onuVlanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_OnuVlanName_Type.__name__ = "OctetString"
_OnuVlanName_Object = MibTableColumn
onuVlanName = _OnuVlanName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 3),
    _OnuVlanName_Type()
)
onuVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuVlanName.setStatus("current")
_OnuVlanTaggedPort_Type = OctetString
_OnuVlanTaggedPort_Object = MibTableColumn
onuVlanTaggedPort = _OnuVlanTaggedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 4),
    _OnuVlanTaggedPort_Type()
)
onuVlanTaggedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuVlanTaggedPort.setStatus("current")
_OnuVlanUntaggedPort_Type = OctetString
_OnuVlanUntaggedPort_Object = MibTableColumn
onuVlanUntaggedPort = _OnuVlanUntaggedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 5),
    _OnuVlanUntaggedPort_Type()
)
onuVlanUntaggedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuVlanUntaggedPort.setStatus("current")
_OnuVlanRowStatus_Type = RowStatus
_OnuVlanRowStatus_Object = MibTableColumn
onuVlanRowStatus = _OnuVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 2, 2, 1, 6),
    _OnuVlanRowStatus_Type()
)
onuVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    onuVlanRowStatus.setStatus("current")
_PortVlanGroup_ObjectIdentity = ObjectIdentity
portVlanGroup = _PortVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3)
)
if mibBuilder.loadTexts:
    portVlanGroup.setStatus("current")
_OnuPortortVlanTable_Object = MibTable
onuPortortVlanTable = _OnuPortortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1)
)
if mibBuilder.loadTexts:
    onuPortortVlanTable.setStatus("current")
_OnuPortVlanEntry_Object = MibTableRow
onuPortVlanEntry = _OnuPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1)
)
onuPortVlanEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "pvlanDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pvlanCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pvlanPortIndex"),
)
if mibBuilder.loadTexts:
    onuPortVlanEntry.setStatus("current")


class _PvlanDeviceIndex_Type(EponDeviceIndex):
    """Custom type pvlanDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PvlanDeviceIndex_Type.__name__ = "EponDeviceIndex"
_PvlanDeviceIndex_Object = MibTableColumn
pvlanDeviceIndex = _PvlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 1),
    _PvlanDeviceIndex_Type()
)
pvlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvlanDeviceIndex.setStatus("current")


class _PvlanCardIndex_Type(EponCardIndex):
    """Custom type pvlanCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PvlanCardIndex_Type.__name__ = "EponCardIndex"
_PvlanCardIndex_Object = MibTableColumn
pvlanCardIndex = _PvlanCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 2),
    _PvlanCardIndex_Type()
)
pvlanCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvlanCardIndex.setStatus("current")


class _PvlanPortIndex_Type(EponPortIndex):
    """Custom type pvlanPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PvlanPortIndex_Type.__name__ = "EponPortIndex"
_PvlanPortIndex_Object = MibTableColumn
pvlanPortIndex = _PvlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 3),
    _PvlanPortIndex_Type()
)
pvlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvlanPortIndex.setStatus("current")


class _VlanTagTpid_Type(OctetString):
    """Custom type vlanTagTpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_VlanTagTpid_Type.__name__ = "OctetString"
_VlanTagTpid_Object = MibTableColumn
vlanTagTpid = _VlanTagTpid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 4),
    _VlanTagTpid_Type()
)
vlanTagTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagTpid.setStatus("current")
_VlanTagCfi_Type = TruthValue
_VlanTagCfi_Object = MibTableColumn
vlanTagCfi = _VlanTagCfi_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 5),
    _VlanTagCfi_Type()
)
vlanTagCfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagCfi.setStatus("current")


class _VlanTagPriority_Type(Integer32):
    """Custom type vlanTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VlanTagPriority_Type.__name__ = "Integer32"
_VlanTagPriority_Object = MibTableColumn
vlanTagPriority = _VlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 6),
    _VlanTagPriority_Type()
)
vlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTagPriority.setStatus("current")
_VlanPVid_Type = Integer32
_VlanPVid_Object = MibTableColumn
vlanPVid = _VlanPVid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 7),
    _VlanPVid_Type()
)
vlanPVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPVid.setStatus("current")


class _VlanMode_Type(Integer32):
    """Custom type vlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 0),
          ("tag", 1),
          ("translation", 2),
          ("aggregation", 3),
          ("trunk", 4),
          ("stacking", 5))
    )


_VlanMode_Type.__name__ = "Integer32"
_VlanMode_Object = MibTableColumn
vlanMode = _VlanMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 1, 1, 8),
    _VlanMode_Type()
)
vlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMode.setStatus("current")
_PortVlanTranslationTable_Object = MibTable
portVlanTranslationTable = _PortVlanTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2)
)
if mibBuilder.loadTexts:
    portVlanTranslationTable.setStatus("current")
_PortVlanTranslationEntry_Object = MibTableRow
portVlanTranslationEntry = _PortVlanTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1)
)
portVlanTranslationEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "pvtDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pvtCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pvtPortIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "portVidIndex"),
)
if mibBuilder.loadTexts:
    portVlanTranslationEntry.setStatus("current")


class _PvtDeviceIndex_Type(EponDeviceIndex):
    """Custom type pvtDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PvtDeviceIndex_Type.__name__ = "EponDeviceIndex"
_PvtDeviceIndex_Object = MibTableColumn
pvtDeviceIndex = _PvtDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 1),
    _PvtDeviceIndex_Type()
)
pvtDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvtDeviceIndex.setStatus("current")


class _PvtCardIndex_Type(EponCardIndex):
    """Custom type pvtCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PvtCardIndex_Type.__name__ = "EponCardIndex"
_PvtCardIndex_Object = MibTableColumn
pvtCardIndex = _PvtCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 2),
    _PvtCardIndex_Type()
)
pvtCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvtCardIndex.setStatus("current")


class _PvtPortIndex_Type(EponPortIndex):
    """Custom type pvtPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PvtPortIndex_Type.__name__ = "EponPortIndex"
_PvtPortIndex_Object = MibTableColumn
pvtPortIndex = _PvtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 3),
    _PvtPortIndex_Type()
)
pvtPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvtPortIndex.setStatus("current")


class _PortVidIndex_Type(Unsigned32):
    """Custom type portVidIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortVidIndex_Type.__name__ = "Unsigned32"
_PortVidIndex_Object = MibTableColumn
portVidIndex = _PortVidIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 4),
    _PortVidIndex_Type()
)
portVidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portVidIndex.setStatus("current")
_TranslationNewVid_Type = Unsigned32
_TranslationNewVid_Object = MibTableColumn
translationNewVid = _TranslationNewVid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 5),
    _TranslationNewVid_Type()
)
translationNewVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    translationNewVid.setStatus("current")
_TranslationRowStatus_Type = RowStatus
_TranslationRowStatus_Object = MibTableColumn
translationRowStatus = _TranslationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 2, 1, 6),
    _TranslationRowStatus_Type()
)
translationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    translationRowStatus.setStatus("current")
_PortVlanAggregationManagement_ObjectIdentity = ObjectIdentity
portVlanAggregationManagement = _PortVlanAggregationManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3)
)
if mibBuilder.loadTexts:
    portVlanAggregationManagement.setStatus("current")
_PortVlanAggregationConfigTable_Object = MibTable
portVlanAggregationConfigTable = _PortVlanAggregationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1)
)
if mibBuilder.loadTexts:
    portVlanAggregationConfigTable.setStatus("current")
_PortVlanAggregationConfigEntry_Object = MibTableRow
portVlanAggregationConfigEntry = _PortVlanAggregationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1)
)
portVlanAggregationConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "pvaDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pvaCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pvaPortIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "portAggregationVidIndex"),
)
if mibBuilder.loadTexts:
    portVlanAggregationConfigEntry.setStatus("current")


class _PvaDeviceIndex_Type(EponDeviceIndex):
    """Custom type pvaDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PvaDeviceIndex_Type.__name__ = "EponDeviceIndex"
_PvaDeviceIndex_Object = MibTableColumn
pvaDeviceIndex = _PvaDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 1),
    _PvaDeviceIndex_Type()
)
pvaDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvaDeviceIndex.setStatus("current")


class _PvaCardIndex_Type(EponCardIndex):
    """Custom type pvaCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PvaCardIndex_Type.__name__ = "EponCardIndex"
_PvaCardIndex_Object = MibTableColumn
pvaCardIndex = _PvaCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 2),
    _PvaCardIndex_Type()
)
pvaCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvaCardIndex.setStatus("current")


class _PvaPortIndex_Type(EponPortIndex):
    """Custom type pvaPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PvaPortIndex_Type.__name__ = "EponPortIndex"
_PvaPortIndex_Object = MibTableColumn
pvaPortIndex = _PvaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 3),
    _PvaPortIndex_Type()
)
pvaPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pvaPortIndex.setStatus("current")


class _PortAggregationVidIndex_Type(Unsigned32):
    """Custom type portAggregationVidIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortAggregationVidIndex_Type.__name__ = "Unsigned32"
_PortAggregationVidIndex_Object = MibTableColumn
portAggregationVidIndex = _PortAggregationVidIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 4),
    _PortAggregationVidIndex_Type()
)
portAggregationVidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portAggregationVidIndex.setStatus("current")


class _AggregationVidList_Type(OctetString):
    """Custom type aggregationVidList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_AggregationVidList_Type.__name__ = "OctetString"
_AggregationVidList_Object = MibTableColumn
aggregationVidList = _AggregationVidList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 5),
    _AggregationVidList_Type()
)
aggregationVidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggregationVidList.setStatus("current")
_AggregationRowStatus_Type = RowStatus
_AggregationRowStatus_Object = MibTableColumn
aggregationRowStatus = _AggregationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 3, 1, 1, 6),
    _AggregationRowStatus_Type()
)
aggregationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aggregationRowStatus.setStatus("current")
_PortVlanTrunkTable_Object = MibTable
portVlanTrunkTable = _PortVlanTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4)
)
if mibBuilder.loadTexts:
    portVlanTrunkTable.setStatus("current")
_PortVlanTrunkEntry_Object = MibTableRow
portVlanTrunkEntry = _PortVlanTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1)
)
portVlanTrunkEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "trunkDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "trunkCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "trunkPortIndex"),
)
if mibBuilder.loadTexts:
    portVlanTrunkEntry.setStatus("current")


class _TrunkDeviceIndex_Type(EponDeviceIndex):
    """Custom type trunkDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrunkDeviceIndex_Type.__name__ = "EponDeviceIndex"
_TrunkDeviceIndex_Object = MibTableColumn
trunkDeviceIndex = _TrunkDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 1),
    _TrunkDeviceIndex_Type()
)
trunkDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkDeviceIndex.setStatus("current")


class _TrunkCardIndex_Type(EponCardIndex):
    """Custom type trunkCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrunkCardIndex_Type.__name__ = "EponCardIndex"
_TrunkCardIndex_Object = MibTableColumn
trunkCardIndex = _TrunkCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 2),
    _TrunkCardIndex_Type()
)
trunkCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkCardIndex.setStatus("current")


class _TrunkPortIndex_Type(EponPortIndex):
    """Custom type trunkPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrunkPortIndex_Type.__name__ = "EponPortIndex"
_TrunkPortIndex_Object = MibTableColumn
trunkPortIndex = _TrunkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 3),
    _TrunkPortIndex_Type()
)
trunkPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkPortIndex.setStatus("current")


class _TrunkVidList_Type(OctetString):
    """Custom type trunkVidList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_TrunkVidList_Type.__name__ = "OctetString"
_TrunkVidList_Object = MibTableColumn
trunkVidList = _TrunkVidList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 4),
    _TrunkVidList_Type()
)
trunkVidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkVidList.setStatus("current")
_PortVlanTrunkRowStatus_Type = RowStatus
_PortVlanTrunkRowStatus_Object = MibTableColumn
portVlanTrunkRowStatus = _PortVlanTrunkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 4, 1, 5),
    _PortVlanTrunkRowStatus_Type()
)
portVlanTrunkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portVlanTrunkRowStatus.setStatus("current")
_OltPortVlanTable_Object = MibTable
oltPortVlanTable = _OltPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 5)
)
if mibBuilder.loadTexts:
    oltPortVlanTable.setStatus("current")
_OltPortVlanEntry_Object = MibTableRow
oltPortVlanEntry = _OltPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 5, 1)
)
oltPortVlanEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "oltPortVlanDeviceIndex"),
)
if mibBuilder.loadTexts:
    oltPortVlanEntry.setStatus("current")
_OltPortVlanDeviceIndex_Type = EponDeviceIndex
_OltPortVlanDeviceIndex_Object = MibTableColumn
oltPortVlanDeviceIndex = _OltPortVlanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 5, 1, 1),
    _OltPortVlanDeviceIndex_Type()
)
oltPortVlanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oltPortVlanDeviceIndex.setStatus("current")


class _OltPortVlanTagPriority_Type(Integer32):
    """Custom type oltPortVlanTagPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OltPortVlanTagPriority_Type.__name__ = "Integer32"
_OltPortVlanTagPriority_Object = MibTableColumn
oltPortVlanTagPriority = _OltPortVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 5, 1, 2),
    _OltPortVlanTagPriority_Type()
)
oltPortVlanTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPortVlanTagPriority.setStatus("current")
_OltPortVlanPVid_Type = Integer32
_OltPortVlanPVid_Object = MibTableColumn
oltPortVlanPVid = _OltPortVlanPVid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 5, 1, 3),
    _OltPortVlanPVid_Type()
)
oltPortVlanPVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPortVlanPVid.setStatus("current")


class _OltPortVlanMode_Type(Integer32):
    """Custom type oltPortVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trunk", 1),
          ("access", 2),
          ("hybrid", 3))
    )


_OltPortVlanMode_Type.__name__ = "Integer32"
_OltPortVlanMode_Object = MibTableColumn
oltPortVlanMode = _OltPortVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 3, 5, 1, 4),
    _OltPortVlanMode_Type()
)
oltPortVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oltPortVlanMode.setStatus("current")
_QinQConfigGroup_ObjectIdentity = ObjectIdentity
qinQConfigGroup = _QinQConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4)
)
if mibBuilder.loadTexts:
    qinQConfigGroup.setStatus("current")
_PortQinQConfigTable_Object = MibTable
portQinQConfigTable = _PortQinQConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1)
)
if mibBuilder.loadTexts:
    portQinQConfigTable.setStatus("current")
_PortQinQConfigEntry_Object = MibTableRow
portQinQConfigEntry = _PortQinQConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1)
)
portQinQConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "pqDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pqCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pqPortIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pqStartVlanId"),
    (0, "NSCRTV-FTTX-EPON-MIB", "pqEndVlanId"),
)
if mibBuilder.loadTexts:
    portQinQConfigEntry.setStatus("current")


class _PqDeviceIndex_Type(EponDeviceIndex):
    """Custom type pqDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PqDeviceIndex_Type.__name__ = "EponDeviceIndex"
_PqDeviceIndex_Object = MibTableColumn
pqDeviceIndex = _PqDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 1),
    _PqDeviceIndex_Type()
)
pqDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqDeviceIndex.setStatus("current")


class _PqCardIndex_Type(EponCardIndex):
    """Custom type pqCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PqCardIndex_Type.__name__ = "EponCardIndex"
_PqCardIndex_Object = MibTableColumn
pqCardIndex = _PqCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 2),
    _PqCardIndex_Type()
)
pqCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqCardIndex.setStatus("current")


class _PqPortIndex_Type(EponPortIndex):
    """Custom type pqPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PqPortIndex_Type.__name__ = "EponPortIndex"
_PqPortIndex_Object = MibTableColumn
pqPortIndex = _PqPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 3),
    _PqPortIndex_Type()
)
pqPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqPortIndex.setStatus("current")


class _PqStartVlanId_Type(Integer32):
    """Custom type pqStartVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PqStartVlanId_Type.__name__ = "Integer32"
_PqStartVlanId_Object = MibTableColumn
pqStartVlanId = _PqStartVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 4),
    _PqStartVlanId_Type()
)
pqStartVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqStartVlanId.setStatus("current")


class _PqEndVlanId_Type(Integer32):
    """Custom type pqEndVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PqEndVlanId_Type.__name__ = "Integer32"
_PqEndVlanId_Object = MibTableColumn
pqEndVlanId = _PqEndVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 5),
    _PqEndVlanId_Type()
)
pqEndVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pqEndVlanId.setStatus("current")
_PqSVlanId_Type = Integer32
_PqSVlanId_Object = MibTableColumn
pqSVlanId = _PqSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 6),
    _PqSVlanId_Type()
)
pqSVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqSVlanId.setStatus("current")


class _PqSTagCosDetermine_Type(Integer32):
    """Custom type pqSTagCosDetermine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("NO", 1),
          ("YES", 2))
    )


_PqSTagCosDetermine_Type.__name__ = "Integer32"
_PqSTagCosDetermine_Object = MibTableColumn
pqSTagCosDetermine = _PqSTagCosDetermine_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 7),
    _PqSTagCosDetermine_Type()
)
pqSTagCosDetermine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqSTagCosDetermine.setStatus("current")


class _PqSTagCosNewValue_Type(Integer32):
    """Custom type pqSTagCosNewValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PqSTagCosNewValue_Type.__name__ = "Integer32"
_PqSTagCosNewValue_Object = MibTableColumn
pqSTagCosNewValue = _PqSTagCosNewValue_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 8),
    _PqSTagCosNewValue_Type()
)
pqSTagCosNewValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqSTagCosNewValue.setStatus("current")
_PqRowStatus_Type = RowStatus
_PqRowStatus_Object = MibTableColumn
pqRowStatus = _PqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 7, 4, 1, 1, 9),
    _PqRowStatus_Type()
)
pqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pqRowStatus.setStatus("current")
_QosManagementObjects_ObjectIdentity = ObjectIdentity
qosManagementObjects = _QosManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8)
)
_QosGlobalSetTable_Object = MibTable
qosGlobalSetTable = _QosGlobalSetTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1)
)
if mibBuilder.loadTexts:
    qosGlobalSetTable.setStatus("current")
_QosGlobalSetEntry_Object = MibTableRow
qosGlobalSetEntry = _QosGlobalSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1, 1)
)
qosGlobalSetEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "qosGlobalSetDeviceIndex"),
)
if mibBuilder.loadTexts:
    qosGlobalSetEntry.setStatus("current")


class _QosGlobalSetDeviceIndex_Type(EponDeviceIndex):
    """Custom type qosGlobalSetDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QosGlobalSetDeviceIndex_Type.__name__ = "EponDeviceIndex"
_QosGlobalSetDeviceIndex_Object = MibTableColumn
qosGlobalSetDeviceIndex = _QosGlobalSetDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1, 1, 1),
    _QosGlobalSetDeviceIndex_Type()
)
qosGlobalSetDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosGlobalSetDeviceIndex.setStatus("current")


class _QosGlobalSetMaxQueueCount_Type(Integer32):
    """Custom type qosGlobalSetMaxQueueCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_QosGlobalSetMaxQueueCount_Type.__name__ = "Integer32"
_QosGlobalSetMaxQueueCount_Object = MibTableColumn
qosGlobalSetMaxQueueCount = _QosGlobalSetMaxQueueCount_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1, 1, 2),
    _QosGlobalSetMaxQueueCount_Type()
)
qosGlobalSetMaxQueueCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosGlobalSetMaxQueueCount.setStatus("current")


class _QosGlobalSetMode_Type(Integer32):
    """Custom type qosGlobalSetMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deviceBased", 1),
          ("portBased", 2))
    )


_QosGlobalSetMode_Type.__name__ = "Integer32"
_QosGlobalSetMode_Object = MibTableColumn
qosGlobalSetMode = _QosGlobalSetMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 1, 1, 3),
    _QosGlobalSetMode_Type()
)
qosGlobalSetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosGlobalSetMode.setStatus("current")
_DeviceBaseQosMapTable_Object = MibTable
deviceBaseQosMapTable = _DeviceBaseQosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2)
)
if mibBuilder.loadTexts:
    deviceBaseQosMapTable.setStatus("current")
_DeviceBaseQosMapEntry_Object = MibTableRow
deviceBaseQosMapEntry = _DeviceBaseQosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2, 1)
)
deviceBaseQosMapEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "deviceBaseQosMapDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "deviceBaseQosMapRuleIndex"),
)
if mibBuilder.loadTexts:
    deviceBaseQosMapEntry.setStatus("current")


class _DeviceBaseQosMapDeviceIndex_Type(EponDeviceIndex):
    """Custom type deviceBaseQosMapDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceBaseQosMapDeviceIndex_Type.__name__ = "EponDeviceIndex"
_DeviceBaseQosMapDeviceIndex_Object = MibTableColumn
deviceBaseQosMapDeviceIndex = _DeviceBaseQosMapDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2, 1, 1),
    _DeviceBaseQosMapDeviceIndex_Type()
)
deviceBaseQosMapDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceBaseQosMapDeviceIndex.setStatus("current")


class _DeviceBaseQosMapRuleIndex_Type(Integer32):
    """Custom type deviceBaseQosMapRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("tos", 2),
          ("diffserv", 3))
    )


_DeviceBaseQosMapRuleIndex_Type.__name__ = "Integer32"
_DeviceBaseQosMapRuleIndex_Object = MibTableColumn
deviceBaseQosMapRuleIndex = _DeviceBaseQosMapRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2, 1, 2),
    _DeviceBaseQosMapRuleIndex_Type()
)
deviceBaseQosMapRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceBaseQosMapRuleIndex.setStatus("current")


class _DeviceBaseQosMapOctet_Type(OctetString):
    """Custom type deviceBaseQosMapOctet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(64, 64),
    )


_DeviceBaseQosMapOctet_Type.__name__ = "OctetString"
_DeviceBaseQosMapOctet_Object = MibTableColumn
deviceBaseQosMapOctet = _DeviceBaseQosMapOctet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 2, 1, 3),
    _DeviceBaseQosMapOctet_Type()
)
deviceBaseQosMapOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceBaseQosMapOctet.setStatus("current")
_DeviceBaseQosPolicyTable_Object = MibTable
deviceBaseQosPolicyTable = _DeviceBaseQosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3)
)
if mibBuilder.loadTexts:
    deviceBaseQosPolicyTable.setStatus("current")
_DeviceBaseQosPolicyEntry_Object = MibTableRow
deviceBaseQosPolicyEntry = _DeviceBaseQosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1)
)
deviceBaseQosPolicyEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "deviceBaseQosPolicyDeviceIndex"),
)
if mibBuilder.loadTexts:
    deviceBaseQosPolicyEntry.setStatus("current")


class _DeviceBaseQosPolicyDeviceIndex_Type(EponDeviceIndex):
    """Custom type deviceBaseQosPolicyDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DeviceBaseQosPolicyDeviceIndex_Type.__name__ = "EponDeviceIndex"
_DeviceBaseQosPolicyDeviceIndex_Object = MibTableColumn
deviceBaseQosPolicyDeviceIndex = _DeviceBaseQosPolicyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1, 1),
    _DeviceBaseQosPolicyDeviceIndex_Type()
)
deviceBaseQosPolicyDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceBaseQosPolicyDeviceIndex.setStatus("current")


class _DeviceBaseQosPolicyMode_Type(Integer32):
    """Custom type deviceBaseQosPolicyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr", 2),
          ("spWrr", 3),
          ("wfp", 4))
    )


_DeviceBaseQosPolicyMode_Type.__name__ = "Integer32"
_DeviceBaseQosPolicyMode_Object = MibTableColumn
deviceBaseQosPolicyMode = _DeviceBaseQosPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1, 2),
    _DeviceBaseQosPolicyMode_Type()
)
deviceBaseQosPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceBaseQosPolicyMode.setStatus("current")
_DeviceBaseQosPolicyWeightOctet_Type = OctetString
_DeviceBaseQosPolicyWeightOctet_Object = MibTableColumn
deviceBaseQosPolicyWeightOctet = _DeviceBaseQosPolicyWeightOctet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1, 3),
    _DeviceBaseQosPolicyWeightOctet_Type()
)
deviceBaseQosPolicyWeightOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceBaseQosPolicyWeightOctet.setStatus("current")
_DeviceBaseQosPolicySpBandwidthRange_Type = OctetString
_DeviceBaseQosPolicySpBandwidthRange_Object = MibTableColumn
deviceBaseQosPolicySpBandwidthRange = _DeviceBaseQosPolicySpBandwidthRange_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 3, 1, 4),
    _DeviceBaseQosPolicySpBandwidthRange_Type()
)
deviceBaseQosPolicySpBandwidthRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceBaseQosPolicySpBandwidthRange.setStatus("current")
_PortBaseQosMapTable_Object = MibTable
portBaseQosMapTable = _PortBaseQosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4)
)
if mibBuilder.loadTexts:
    portBaseQosMapTable.setStatus("current")
_PortBaseQosMapEntry_Object = MibTableRow
portBaseQosMapEntry = _PortBaseQosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1)
)
portBaseQosMapEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "portBaseQosMapDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "portBaseQosMapCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "portBaseQosMapPortIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "portBaseQosMapRuleIndex"),
)
if mibBuilder.loadTexts:
    portBaseQosMapEntry.setStatus("current")


class _PortBaseQosMapDeviceIndex_Type(EponDeviceIndex):
    """Custom type portBaseQosMapDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortBaseQosMapDeviceIndex_Type.__name__ = "EponDeviceIndex"
_PortBaseQosMapDeviceIndex_Object = MibTableColumn
portBaseQosMapDeviceIndex = _PortBaseQosMapDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 1),
    _PortBaseQosMapDeviceIndex_Type()
)
portBaseQosMapDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosMapDeviceIndex.setStatus("current")


class _PortBaseQosMapCardIndex_Type(EponPortIndex):
    """Custom type portBaseQosMapCardIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortBaseQosMapCardIndex_Type.__name__ = "EponPortIndex"
_PortBaseQosMapCardIndex_Object = MibTableColumn
portBaseQosMapCardIndex = _PortBaseQosMapCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 2),
    _PortBaseQosMapCardIndex_Type()
)
portBaseQosMapCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosMapCardIndex.setStatus("current")


class _PortBaseQosMapPortIndex_Type(EponPortIndex):
    """Custom type portBaseQosMapPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortBaseQosMapPortIndex_Type.__name__ = "EponPortIndex"
_PortBaseQosMapPortIndex_Object = MibTableColumn
portBaseQosMapPortIndex = _PortBaseQosMapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 3),
    _PortBaseQosMapPortIndex_Type()
)
portBaseQosMapPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosMapPortIndex.setStatus("current")


class _PortBaseQosMapRuleIndex_Type(Integer32):
    """Custom type portBaseQosMapRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cos", 1),
          ("tos", 2),
          ("diffserv", 3))
    )


_PortBaseQosMapRuleIndex_Type.__name__ = "Integer32"
_PortBaseQosMapRuleIndex_Object = MibTableColumn
portBaseQosMapRuleIndex = _PortBaseQosMapRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 4),
    _PortBaseQosMapRuleIndex_Type()
)
portBaseQosMapRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosMapRuleIndex.setStatus("current")


class _PortBaseQosMapOctet_Type(OctetString):
    """Custom type portBaseQosMapOctet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_PortBaseQosMapOctet_Type.__name__ = "OctetString"
_PortBaseQosMapOctet_Object = MibTableColumn
portBaseQosMapOctet = _PortBaseQosMapOctet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 4, 1, 5),
    _PortBaseQosMapOctet_Type()
)
portBaseQosMapOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseQosMapOctet.setStatus("current")
_PortBaseQosPolicyTable_Object = MibTable
portBaseQosPolicyTable = _PortBaseQosPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5)
)
if mibBuilder.loadTexts:
    portBaseQosPolicyTable.setStatus("current")
_PortBaseQosPolicyEntry_Object = MibTableRow
portBaseQosPolicyEntry = _PortBaseQosPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1)
)
portBaseQosPolicyEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "portBaseQosPolicyDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "portBaseQosPolicyCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "portBaseQosPolicyPortIndex"),
)
if mibBuilder.loadTexts:
    portBaseQosPolicyEntry.setStatus("current")
_PortBaseQosPolicyDeviceIndex_Type = EponDeviceIndex
_PortBaseQosPolicyDeviceIndex_Object = MibTableColumn
portBaseQosPolicyDeviceIndex = _PortBaseQosPolicyDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 1),
    _PortBaseQosPolicyDeviceIndex_Type()
)
portBaseQosPolicyDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosPolicyDeviceIndex.setStatus("current")


class _PortBaseQosPolicyCardIndex_Type(EponPortIndex):
    """Custom type portBaseQosPolicyCardIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortBaseQosPolicyCardIndex_Type.__name__ = "EponPortIndex"
_PortBaseQosPolicyCardIndex_Object = MibTableColumn
portBaseQosPolicyCardIndex = _PortBaseQosPolicyCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 2),
    _PortBaseQosPolicyCardIndex_Type()
)
portBaseQosPolicyCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosPolicyCardIndex.setStatus("current")


class _PortBaseQosPolicyPortIndex_Type(EponPortIndex):
    """Custom type portBaseQosPolicyPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortBaseQosPolicyPortIndex_Type.__name__ = "EponPortIndex"
_PortBaseQosPolicyPortIndex_Object = MibTableColumn
portBaseQosPolicyPortIndex = _PortBaseQosPolicyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 3),
    _PortBaseQosPolicyPortIndex_Type()
)
portBaseQosPolicyPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portBaseQosPolicyPortIndex.setStatus("current")


class _PortBaseQosPolicyMode_Type(Integer32):
    """Custom type portBaseQosPolicyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr", 2),
          ("spWrr", 3),
          ("wfp", 4))
    )


_PortBaseQosPolicyMode_Type.__name__ = "Integer32"
_PortBaseQosPolicyMode_Object = MibTableColumn
portBaseQosPolicyMode = _PortBaseQosPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 4),
    _PortBaseQosPolicyMode_Type()
)
portBaseQosPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseQosPolicyMode.setStatus("current")


class _PortBaseQosPolicyWeightOctet_Type(OctetString):
    """Custom type portBaseQosPolicyWeightOctet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PortBaseQosPolicyWeightOctet_Type.__name__ = "OctetString"
_PortBaseQosPolicyWeightOctet_Object = MibTableColumn
portBaseQosPolicyWeightOctet = _PortBaseQosPolicyWeightOctet_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 5),
    _PortBaseQosPolicyWeightOctet_Type()
)
portBaseQosPolicyWeightOctet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseQosPolicyWeightOctet.setStatus("current")
_PortBaseQosPolicySpBandwidthRange_Type = OctetString
_PortBaseQosPolicySpBandwidthRange_Object = MibTableColumn
portBaseQosPolicySpBandwidthRange = _PortBaseQosPolicySpBandwidthRange_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 8, 5, 1, 6),
    _PortBaseQosPolicySpBandwidthRange_Type()
)
portBaseQosPolicySpBandwidthRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBaseQosPolicySpBandwidthRange.setStatus("current")
_StpManagementObjects_ObjectIdentity = ObjectIdentity
stpManagementObjects = _StpManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9)
)
_StpGlobalSetTable_Object = MibTable
stpGlobalSetTable = _StpGlobalSetTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1)
)
if mibBuilder.loadTexts:
    stpGlobalSetTable.setStatus("current")
_StpGlobalSetEntry_Object = MibTableRow
stpGlobalSetEntry = _StpGlobalSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1)
)
stpGlobalSetEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "stpGlobalSetIndex"),
)
if mibBuilder.loadTexts:
    stpGlobalSetEntry.setStatus("current")
_StpGlobalSetIndex_Type = Counter32
_StpGlobalSetIndex_Object = MibTableColumn
stpGlobalSetIndex = _StpGlobalSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 1),
    _StpGlobalSetIndex_Type()
)
stpGlobalSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpGlobalSetIndex.setStatus("current")


class _StpGlobalSetVersion_Type(Integer32):
    """Custom type stpGlobalSetVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 1),
          ("stp", 2))
    )


_StpGlobalSetVersion_Type.__name__ = "Integer32"
_StpGlobalSetVersion_Object = MibTableColumn
stpGlobalSetVersion = _StpGlobalSetVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 2),
    _StpGlobalSetVersion_Type()
)
stpGlobalSetVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetVersion.setStatus("current")


class _StpGlobalSetPriority_Type(Integer32):
    """Custom type stpGlobalSetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpGlobalSetPriority_Type.__name__ = "Integer32"
_StpGlobalSetPriority_Object = MibTableColumn
stpGlobalSetPriority = _StpGlobalSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 3),
    _StpGlobalSetPriority_Type()
)
stpGlobalSetPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetPriority.setStatus("current")
_StpGlobalSetTimeSinceTopologyChange_Type = TimeTicks
_StpGlobalSetTimeSinceTopologyChange_Object = MibTableColumn
stpGlobalSetTimeSinceTopologyChange = _StpGlobalSetTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 4),
    _StpGlobalSetTimeSinceTopologyChange_Type()
)
stpGlobalSetTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetTimeSinceTopologyChange.setStatus("current")
_StpGlobalSetTopChanges_Type = Counter32
_StpGlobalSetTopChanges_Object = MibTableColumn
stpGlobalSetTopChanges = _StpGlobalSetTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 5),
    _StpGlobalSetTopChanges_Type()
)
stpGlobalSetTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetTopChanges.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetTopChanges.setUnits("topology changes")
_StpGlobalSetDesignatedRoot_Type = BridgeId
_StpGlobalSetDesignatedRoot_Object = MibTableColumn
stpGlobalSetDesignatedRoot = _StpGlobalSetDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 6),
    _StpGlobalSetDesignatedRoot_Type()
)
stpGlobalSetDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetDesignatedRoot.setStatus("current")
_StpGlobalSetRootCost_Type = Integer32
_StpGlobalSetRootCost_Object = MibTableColumn
stpGlobalSetRootCost = _StpGlobalSetRootCost_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 7),
    _StpGlobalSetRootCost_Type()
)
stpGlobalSetRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetRootCost.setStatus("current")


class _StpGlobalSetRootPort_Type(OctetString):
    """Custom type stpGlobalSetRootPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_StpGlobalSetRootPort_Type.__name__ = "OctetString"
_StpGlobalSetRootPort_Object = MibTableColumn
stpGlobalSetRootPort = _StpGlobalSetRootPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 8),
    _StpGlobalSetRootPort_Type()
)
stpGlobalSetRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetRootPort.setStatus("current")
_StpGlobalSetMaxAge_Type = Timeout
_StpGlobalSetMaxAge_Object = MibTableColumn
stpGlobalSetMaxAge = _StpGlobalSetMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 9),
    _StpGlobalSetMaxAge_Type()
)
stpGlobalSetMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetMaxAge.setUnits("centi-seconds")
_StpGlobalSetHelloTime_Type = Timeout
_StpGlobalSetHelloTime_Object = MibTableColumn
stpGlobalSetHelloTime = _StpGlobalSetHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 10),
    _StpGlobalSetHelloTime_Type()
)
stpGlobalSetHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetHelloTime.setUnits("centi-seconds")
_StpGlobalSetHoldTime_Type = Integer32
_StpGlobalSetHoldTime_Object = MibTableColumn
stpGlobalSetHoldTime = _StpGlobalSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 11),
    _StpGlobalSetHoldTime_Type()
)
stpGlobalSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetHoldTime.setUnits("centi-seconds")
_StpGlobalSetForwardDelay_Type = Timeout
_StpGlobalSetForwardDelay_Object = MibTableColumn
stpGlobalSetForwardDelay = _StpGlobalSetForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 12),
    _StpGlobalSetForwardDelay_Type()
)
stpGlobalSetForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpGlobalSetForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetForwardDelay.setUnits("centi-seconds")


class _StpGlobalSetBridgeMaxAge_Type(Timeout):
    """Custom type stpGlobalSetBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_StpGlobalSetBridgeMaxAge_Type.__name__ = "Timeout"
_StpGlobalSetBridgeMaxAge_Object = MibTableColumn
stpGlobalSetBridgeMaxAge = _StpGlobalSetBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 13),
    _StpGlobalSetBridgeMaxAge_Type()
)
stpGlobalSetBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeMaxAge.setUnits("centi-seconds")


class _StpGlobalSetBridgeHelloTime_Type(Timeout):
    """Custom type stpGlobalSetBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_StpGlobalSetBridgeHelloTime_Type.__name__ = "Timeout"
_StpGlobalSetBridgeHelloTime_Object = MibTableColumn
stpGlobalSetBridgeHelloTime = _StpGlobalSetBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 14),
    _StpGlobalSetBridgeHelloTime_Type()
)
stpGlobalSetBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeHelloTime.setUnits("centi-seconds")


class _StpGlobalSetBridgeForwardDelay_Type(Timeout):
    """Custom type stpGlobalSetBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_StpGlobalSetBridgeForwardDelay_Type.__name__ = "Timeout"
_StpGlobalSetBridgeForwardDelay_Object = MibTableColumn
stpGlobalSetBridgeForwardDelay = _StpGlobalSetBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 15),
    _StpGlobalSetBridgeForwardDelay_Type()
)
stpGlobalSetBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    stpGlobalSetBridgeForwardDelay.setUnits("centi-seconds")


class _StpGlobalSetRstpTxHoldCount_Type(Integer32):
    """Custom type stpGlobalSetRstpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpGlobalSetRstpTxHoldCount_Type.__name__ = "Integer32"
_StpGlobalSetRstpTxHoldCount_Object = MibTableColumn
stpGlobalSetRstpTxHoldCount = _StpGlobalSetRstpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 16),
    _StpGlobalSetRstpTxHoldCount_Type()
)
stpGlobalSetRstpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetRstpTxHoldCount.setStatus("current")
_StpGlobalSetEnable_Type = TruthValue
_StpGlobalSetEnable_Object = MibTableColumn
stpGlobalSetEnable = _StpGlobalSetEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 1, 1, 17),
    _StpGlobalSetEnable_Type()
)
stpGlobalSetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpGlobalSetEnable.setStatus("current")
_StpPortTable_Object = MibTable
stpPortTable = _StpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2)
)
if mibBuilder.loadTexts:
    stpPortTable.setStatus("current")
_StpPortEntry_Object = MibTableRow
stpPortEntry = _StpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1)
)
stpPortEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "stpPortStpIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "stpPortCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "stpPortIndex"),
)
if mibBuilder.loadTexts:
    stpPortEntry.setStatus("current")


class _StpPortStpIndex_Type(EponDeviceIndex):
    """Custom type stpPortStpIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StpPortStpIndex_Type.__name__ = "EponDeviceIndex"
_StpPortStpIndex_Object = MibTableColumn
stpPortStpIndex = _StpPortStpIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 1),
    _StpPortStpIndex_Type()
)
stpPortStpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpPortStpIndex.setStatus("current")


class _StpPortCardIndex_Type(EponCardIndex):
    """Custom type stpPortCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StpPortCardIndex_Type.__name__ = "EponCardIndex"
_StpPortCardIndex_Object = MibTableColumn
stpPortCardIndex = _StpPortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 2),
    _StpPortCardIndex_Type()
)
stpPortCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpPortCardIndex.setStatus("current")


class _StpPortIndex_Type(EponPortIndex):
    """Custom type stpPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StpPortIndex_Type.__name__ = "EponPortIndex"
_StpPortIndex_Object = MibTableColumn
stpPortIndex = _StpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 3),
    _StpPortIndex_Type()
)
stpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stpPortIndex.setStatus("current")


class _StpPortStatus_Type(Integer32):
    """Custom type stpPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("blocking", 2),
          ("listening", 3),
          ("learning", 4),
          ("forwarding", 5),
          ("broken", 6))
    )


_StpPortStatus_Type.__name__ = "Integer32"
_StpPortStatus_Object = MibTableColumn
stpPortStatus = _StpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 4),
    _StpPortStatus_Type()
)
stpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortStatus.setStatus("current")


class _StpPortPriority_Type(Integer32):
    """Custom type stpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_StpPortPriority_Type.__name__ = "Integer32"
_StpPortPriority_Object = MibTableColumn
stpPortPriority = _StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 5),
    _StpPortPriority_Type()
)
stpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPriority.setStatus("current")


class _StpPortPathCost_Type(Integer32):
    """Custom type stpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StpPortPathCost_Type.__name__ = "Integer32"
_StpPortPathCost_Object = MibTableColumn
stpPortPathCost = _StpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 6),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("current")
_StpPortDesignatedRoot_Type = BridgeId
_StpPortDesignatedRoot_Object = MibTableColumn
stpPortDesignatedRoot = _StpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 7),
    _StpPortDesignatedRoot_Type()
)
stpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedRoot.setStatus("current")
_StpPortDesignatedCost_Type = Integer32
_StpPortDesignatedCost_Object = MibTableColumn
stpPortDesignatedCost = _StpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 8),
    _StpPortDesignatedCost_Type()
)
stpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedCost.setStatus("current")
_StpPortDesignatedBridge_Type = BridgeId
_StpPortDesignatedBridge_Object = MibTableColumn
stpPortDesignatedBridge = _StpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 9),
    _StpPortDesignatedBridge_Type()
)
stpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedBridge.setStatus("current")
_StpPortDesignatedPort_Type = Gauge32
_StpPortDesignatedPort_Object = MibTableColumn
stpPortDesignatedPort = _StpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 10),
    _StpPortDesignatedPort_Type()
)
stpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedPort.setStatus("current")
_StpPortForwardTransitions_Type = Unsigned32
_StpPortForwardTransitions_Object = MibTableColumn
stpPortForwardTransitions = _StpPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 11),
    _StpPortForwardTransitions_Type()
)
stpPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortForwardTransitions.setStatus("current")
if mibBuilder.loadTexts:
    stpPortForwardTransitions.setUnits("seconds")
_StpPortRstpProtocolMigration_Type = TruthValue
_StpPortRstpProtocolMigration_Object = MibTableColumn
stpPortRstpProtocolMigration = _StpPortRstpProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 12),
    _StpPortRstpProtocolMigration_Type()
)
stpPortRstpProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRstpProtocolMigration.setStatus("current")
_StpPortRstpAdminEdgePort_Type = TruthValue
_StpPortRstpAdminEdgePort_Object = MibTableColumn
stpPortRstpAdminEdgePort = _StpPortRstpAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 13),
    _StpPortRstpAdminEdgePort_Type()
)
stpPortRstpAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortRstpAdminEdgePort.setStatus("current")
_StpPortRstpOperEdgePort_Type = TruthValue
_StpPortRstpOperEdgePort_Object = MibTableColumn
stpPortRstpOperEdgePort = _StpPortRstpOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 14),
    _StpPortRstpOperEdgePort_Type()
)
stpPortRstpOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortRstpOperEdgePort.setStatus("current")


class _StpPortPointToPointAdminStatus_Type(Integer32):
    """Custom type stpPortPointToPointAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1),
          ("auto", 2))
    )


_StpPortPointToPointAdminStatus_Type.__name__ = "Integer32"
_StpPortPointToPointAdminStatus_Object = MibTableColumn
stpPortPointToPointAdminStatus = _StpPortPointToPointAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 15),
    _StpPortPointToPointAdminStatus_Type()
)
stpPortPointToPointAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPointToPointAdminStatus.setStatus("current")
_StpPortPointToPointOperStatus_Type = TruthValue
_StpPortPointToPointOperStatus_Object = MibTableColumn
stpPortPointToPointOperStatus = _StpPortPointToPointOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 16),
    _StpPortPointToPointOperStatus_Type()
)
stpPortPointToPointOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortPointToPointOperStatus.setStatus("current")
_StpPortEnabled_Type = TruthValue
_StpPortEnabled_Object = MibTableColumn
stpPortEnabled = _StpPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 9, 2, 1, 17),
    _StpPortEnabled_Type()
)
stpPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortEnabled.setStatus("current")
_PerformanceStatisticObjects_ObjectIdentity = ObjectIdentity
performanceStatisticObjects = _PerformanceStatisticObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10)
)
_CurStatsTable_Object = MibTable
curStatsTable = _CurStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1)
)
if mibBuilder.loadTexts:
    curStatsTable.setStatus("current")
_CurStatsEntry_Object = MibTableRow
curStatsEntry = _CurStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1)
)
curStatsEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "curStatsDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "curStatsCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "curStatsPortIndex"),
)
if mibBuilder.loadTexts:
    curStatsEntry.setStatus("current")


class _CurStatsDeviceIndex_Type(EponDeviceIndex):
    """Custom type curStatsDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurStatsDeviceIndex_Type.__name__ = "EponDeviceIndex"
_CurStatsDeviceIndex_Object = MibTableColumn
curStatsDeviceIndex = _CurStatsDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 1),
    _CurStatsDeviceIndex_Type()
)
curStatsDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    curStatsDeviceIndex.setStatus("current")


class _CurStatsCardIndex_Type(EponCardIndex):
    """Custom type curStatsCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurStatsCardIndex_Type.__name__ = "EponCardIndex"
_CurStatsCardIndex_Object = MibTableColumn
curStatsCardIndex = _CurStatsCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 2),
    _CurStatsCardIndex_Type()
)
curStatsCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    curStatsCardIndex.setStatus("current")


class _CurStatsPortIndex_Type(EponPortIndex):
    """Custom type curStatsPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CurStatsPortIndex_Type.__name__ = "EponPortIndex"
_CurStatsPortIndex_Object = MibTableColumn
curStatsPortIndex = _CurStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 3),
    _CurStatsPortIndex_Type()
)
curStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    curStatsPortIndex.setStatus("current")
_CurStatsInOctets_Type = Counter64
_CurStatsInOctets_Object = MibTableColumn
curStatsInOctets = _CurStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 4),
    _CurStatsInOctets_Type()
)
curStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInOctets.setStatus("current")
_CurStatsInPkts_Type = Counter64
_CurStatsInPkts_Object = MibTableColumn
curStatsInPkts = _CurStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 5),
    _CurStatsInPkts_Type()
)
curStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts.setStatus("current")
_CurStatsInBroadcastPkts_Type = Counter64
_CurStatsInBroadcastPkts_Object = MibTableColumn
curStatsInBroadcastPkts = _CurStatsInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 6),
    _CurStatsInBroadcastPkts_Type()
)
curStatsInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInBroadcastPkts.setStatus("current")
_CurStatsInMulticastPkts_Type = Counter64
_CurStatsInMulticastPkts_Object = MibTableColumn
curStatsInMulticastPkts = _CurStatsInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 7),
    _CurStatsInMulticastPkts_Type()
)
curStatsInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInMulticastPkts.setStatus("current")
_CurStatsInPkts64Octets_Type = Counter64
_CurStatsInPkts64Octets_Object = MibTableColumn
curStatsInPkts64Octets = _CurStatsInPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 8),
    _CurStatsInPkts64Octets_Type()
)
curStatsInPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts64Octets.setStatus("current")
_CurStatsInPkts65to127Octets_Type = Counter64
_CurStatsInPkts65to127Octets_Object = MibTableColumn
curStatsInPkts65to127Octets = _CurStatsInPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 9),
    _CurStatsInPkts65to127Octets_Type()
)
curStatsInPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts65to127Octets.setStatus("current")
_CurStatsInPkts128to255Octets_Type = Counter64
_CurStatsInPkts128to255Octets_Object = MibTableColumn
curStatsInPkts128to255Octets = _CurStatsInPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 10),
    _CurStatsInPkts128to255Octets_Type()
)
curStatsInPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts128to255Octets.setStatus("current")
_CurStatsInPkts256to511Octets_Type = Counter64
_CurStatsInPkts256to511Octets_Object = MibTableColumn
curStatsInPkts256to511Octets = _CurStatsInPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 11),
    _CurStatsInPkts256to511Octets_Type()
)
curStatsInPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts256to511Octets.setStatus("current")
_CurStatsInPkts512to1023Octets_Type = Counter64
_CurStatsInPkts512to1023Octets_Object = MibTableColumn
curStatsInPkts512to1023Octets = _CurStatsInPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 12),
    _CurStatsInPkts512to1023Octets_Type()
)
curStatsInPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts512to1023Octets.setStatus("current")
_CurStatsInPkts1024to1518Octets_Type = Counter64
_CurStatsInPkts1024to1518Octets_Object = MibTableColumn
curStatsInPkts1024to1518Octets = _CurStatsInPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 13),
    _CurStatsInPkts1024to1518Octets_Type()
)
curStatsInPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts1024to1518Octets.setStatus("current")
_CurStatsInPkts1519to1522Octets_Type = Counter64
_CurStatsInPkts1519to1522Octets_Object = MibTableColumn
curStatsInPkts1519to1522Octets = _CurStatsInPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 14),
    _CurStatsInPkts1519to1522Octets_Type()
)
curStatsInPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInPkts1519to1522Octets.setStatus("current")
_CurStatsInUndersizePkts_Type = Counter64
_CurStatsInUndersizePkts_Object = MibTableColumn
curStatsInUndersizePkts = _CurStatsInUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 15),
    _CurStatsInUndersizePkts_Type()
)
curStatsInUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInUndersizePkts.setStatus("current")
_CurStatsInOversizePkts_Type = Counter64
_CurStatsInOversizePkts_Object = MibTableColumn
curStatsInOversizePkts = _CurStatsInOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 16),
    _CurStatsInOversizePkts_Type()
)
curStatsInOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInOversizePkts.setStatus("current")
_CurStatsInFragments_Type = Counter64
_CurStatsInFragments_Object = MibTableColumn
curStatsInFragments = _CurStatsInFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 17),
    _CurStatsInFragments_Type()
)
curStatsInFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInFragments.setStatus("current")
_CurStatsInMpcpFrames_Type = Counter64
_CurStatsInMpcpFrames_Object = MibTableColumn
curStatsInMpcpFrames = _CurStatsInMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 18),
    _CurStatsInMpcpFrames_Type()
)
curStatsInMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInMpcpFrames.setStatus("current")
_CurStatsInMpcpOctets_Type = Counter64
_CurStatsInMpcpOctets_Object = MibTableColumn
curStatsInMpcpOctets = _CurStatsInMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 19),
    _CurStatsInMpcpOctets_Type()
)
curStatsInMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInMpcpOctets.setStatus("current")
_CurStatsInOAMFrames_Type = Counter64
_CurStatsInOAMFrames_Object = MibTableColumn
curStatsInOAMFrames = _CurStatsInOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 20),
    _CurStatsInOAMFrames_Type()
)
curStatsInOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInOAMFrames.setStatus("current")
_CurStatsInOAMOctets_Type = Counter64
_CurStatsInOAMOctets_Object = MibTableColumn
curStatsInOAMOctets = _CurStatsInOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 21),
    _CurStatsInOAMOctets_Type()
)
curStatsInOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInOAMOctets.setStatus("current")
_CurStatsInCRCErrorPkts_Type = Counter64
_CurStatsInCRCErrorPkts_Object = MibTableColumn
curStatsInCRCErrorPkts = _CurStatsInCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 22),
    _CurStatsInCRCErrorPkts_Type()
)
curStatsInCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInCRCErrorPkts.setStatus("current")
_CurStatsInDropEvents_Type = Counter64
_CurStatsInDropEvents_Object = MibTableColumn
curStatsInDropEvents = _CurStatsInDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 23),
    _CurStatsInDropEvents_Type()
)
curStatsInDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInDropEvents.setStatus("current")
_CurStatsInJabbers_Type = Counter64
_CurStatsInJabbers_Object = MibTableColumn
curStatsInJabbers = _CurStatsInJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 24),
    _CurStatsInJabbers_Type()
)
curStatsInJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInJabbers.setStatus("current")
_CurStatsInCollision_Type = Counter64
_CurStatsInCollision_Object = MibTableColumn
curStatsInCollision = _CurStatsInCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 25),
    _CurStatsInCollision_Type()
)
curStatsInCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsInCollision.setStatus("current")
_CurStatsOutOctets_Type = Counter64
_CurStatsOutOctets_Object = MibTableColumn
curStatsOutOctets = _CurStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 26),
    _CurStatsOutOctets_Type()
)
curStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutOctets.setStatus("current")
_CurStatsOutPkts_Type = Counter64
_CurStatsOutPkts_Object = MibTableColumn
curStatsOutPkts = _CurStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 27),
    _CurStatsOutPkts_Type()
)
curStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts.setStatus("current")
_CurStatsOutBroadcastPkts_Type = Counter64
_CurStatsOutBroadcastPkts_Object = MibTableColumn
curStatsOutBroadcastPkts = _CurStatsOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 28),
    _CurStatsOutBroadcastPkts_Type()
)
curStatsOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutBroadcastPkts.setStatus("current")
_CurStatsOutMulticastPkts_Type = Counter64
_CurStatsOutMulticastPkts_Object = MibTableColumn
curStatsOutMulticastPkts = _CurStatsOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 29),
    _CurStatsOutMulticastPkts_Type()
)
curStatsOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutMulticastPkts.setStatus("current")
_CurStatsOutPkts64Octets_Type = Counter64
_CurStatsOutPkts64Octets_Object = MibTableColumn
curStatsOutPkts64Octets = _CurStatsOutPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 30),
    _CurStatsOutPkts64Octets_Type()
)
curStatsOutPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts64Octets.setStatus("current")
_CurStatsOutPkts65to127Octets_Type = Counter64
_CurStatsOutPkts65to127Octets_Object = MibTableColumn
curStatsOutPkts65to127Octets = _CurStatsOutPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 31),
    _CurStatsOutPkts65to127Octets_Type()
)
curStatsOutPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts65to127Octets.setStatus("current")
_CurStatsOutPkts128to255Octets_Type = Counter64
_CurStatsOutPkts128to255Octets_Object = MibTableColumn
curStatsOutPkts128to255Octets = _CurStatsOutPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 32),
    _CurStatsOutPkts128to255Octets_Type()
)
curStatsOutPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts128to255Octets.setStatus("current")
_CurStatsOutPkts256to511Octets_Type = Counter64
_CurStatsOutPkts256to511Octets_Object = MibTableColumn
curStatsOutPkts256to511Octets = _CurStatsOutPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 33),
    _CurStatsOutPkts256to511Octets_Type()
)
curStatsOutPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts256to511Octets.setStatus("current")
_CurStatsOutPkts512to1023Octets_Type = Counter64
_CurStatsOutPkts512to1023Octets_Object = MibTableColumn
curStatsOutPkts512to1023Octets = _CurStatsOutPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 34),
    _CurStatsOutPkts512to1023Octets_Type()
)
curStatsOutPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts512to1023Octets.setStatus("current")
_CurStatsOutPkts1024to1518Octets_Type = Counter64
_CurStatsOutPkts1024to1518Octets_Object = MibTableColumn
curStatsOutPkts1024to1518Octets = _CurStatsOutPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 35),
    _CurStatsOutPkts1024to1518Octets_Type()
)
curStatsOutPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts1024to1518Octets.setStatus("current")
_CurStatsOutPkts1519o1522Octets_Type = Counter64
_CurStatsOutPkts1519o1522Octets_Object = MibTableColumn
curStatsOutPkts1519o1522Octets = _CurStatsOutPkts1519o1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 36),
    _CurStatsOutPkts1519o1522Octets_Type()
)
curStatsOutPkts1519o1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutPkts1519o1522Octets.setStatus("current")
_CurStatsOutUndersizePkts_Type = Counter64
_CurStatsOutUndersizePkts_Object = MibTableColumn
curStatsOutUndersizePkts = _CurStatsOutUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 37),
    _CurStatsOutUndersizePkts_Type()
)
curStatsOutUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutUndersizePkts.setStatus("current")
_CurStatsOutOversizePkts_Type = Counter64
_CurStatsOutOversizePkts_Object = MibTableColumn
curStatsOutOversizePkts = _CurStatsOutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 38),
    _CurStatsOutOversizePkts_Type()
)
curStatsOutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutOversizePkts.setStatus("current")
_CurStatsOutFragments_Type = Counter64
_CurStatsOutFragments_Object = MibTableColumn
curStatsOutFragments = _CurStatsOutFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 39),
    _CurStatsOutFragments_Type()
)
curStatsOutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutFragments.setStatus("current")
_CurStatsOutMpcpFrames_Type = Counter64
_CurStatsOutMpcpFrames_Object = MibTableColumn
curStatsOutMpcpFrames = _CurStatsOutMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 40),
    _CurStatsOutMpcpFrames_Type()
)
curStatsOutMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutMpcpFrames.setStatus("current")
_CurStatsOutMpcpOctets_Type = Counter64
_CurStatsOutMpcpOctets_Object = MibTableColumn
curStatsOutMpcpOctets = _CurStatsOutMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 41),
    _CurStatsOutMpcpOctets_Type()
)
curStatsOutMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutMpcpOctets.setStatus("current")
_CurStatsOutOAMFrames_Type = Counter64
_CurStatsOutOAMFrames_Object = MibTableColumn
curStatsOutOAMFrames = _CurStatsOutOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 42),
    _CurStatsOutOAMFrames_Type()
)
curStatsOutOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutOAMFrames.setStatus("current")
_CurStatsOutOAMOctets_Type = Counter64
_CurStatsOutOAMOctets_Object = MibTableColumn
curStatsOutOAMOctets = _CurStatsOutOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 43),
    _CurStatsOutOAMOctets_Type()
)
curStatsOutOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutOAMOctets.setStatus("current")
_CurStatsOutCRCErrorPkts_Type = Counter64
_CurStatsOutCRCErrorPkts_Object = MibTableColumn
curStatsOutCRCErrorPkts = _CurStatsOutCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 44),
    _CurStatsOutCRCErrorPkts_Type()
)
curStatsOutCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutCRCErrorPkts.setStatus("current")
_CurStatsOutDropEvents_Type = Counter64
_CurStatsOutDropEvents_Object = MibTableColumn
curStatsOutDropEvents = _CurStatsOutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 45),
    _CurStatsOutDropEvents_Type()
)
curStatsOutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutDropEvents.setStatus("current")
_CurStatsOutJabbers_Type = Counter64
_CurStatsOutJabbers_Object = MibTableColumn
curStatsOutJabbers = _CurStatsOutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 46),
    _CurStatsOutJabbers_Type()
)
curStatsOutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutJabbers.setStatus("current")
_CurStatsOutCollision_Type = Counter64
_CurStatsOutCollision_Object = MibTableColumn
curStatsOutCollision = _CurStatsOutCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 47),
    _CurStatsOutCollision_Type()
)
curStatsOutCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    curStatsOutCollision.setStatus("current")


class _CurStatsStatusAndAction_Type(Integer32):
    """Custom type curStatsStatusAndAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clean", 2))
    )


_CurStatsStatusAndAction_Type.__name__ = "Integer32"
_CurStatsStatusAndAction_Object = MibTableColumn
curStatsStatusAndAction = _CurStatsStatusAndAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 1, 1, 48),
    _CurStatsStatusAndAction_Type()
)
curStatsStatusAndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    curStatsStatusAndAction.setStatus("current")
_Stats15Table_Object = MibTable
stats15Table = _Stats15Table_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2)
)
if mibBuilder.loadTexts:
    stats15Table.setStatus("current")
_Stats15Entry_Object = MibTableRow
stats15Entry = _Stats15Entry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1)
)
stats15Entry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "stats15DeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "stats15CardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "stats15PortIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "stats15Index"),
)
if mibBuilder.loadTexts:
    stats15Entry.setStatus("current")


class _Stats15DeviceIndex_Type(EponDeviceIndex):
    """Custom type stats15DeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Stats15DeviceIndex_Type.__name__ = "EponDeviceIndex"
_Stats15DeviceIndex_Object = MibTableColumn
stats15DeviceIndex = _Stats15DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 1),
    _Stats15DeviceIndex_Type()
)
stats15DeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15DeviceIndex.setStatus("current")


class _Stats15CardIndex_Type(EponCardIndex):
    """Custom type stats15CardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Stats15CardIndex_Type.__name__ = "EponCardIndex"
_Stats15CardIndex_Object = MibTableColumn
stats15CardIndex = _Stats15CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 2),
    _Stats15CardIndex_Type()
)
stats15CardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15CardIndex.setStatus("current")


class _Stats15PortIndex_Type(EponPortIndex):
    """Custom type stats15PortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Stats15PortIndex_Type.__name__ = "EponPortIndex"
_Stats15PortIndex_Object = MibTableColumn
stats15PortIndex = _Stats15PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 3),
    _Stats15PortIndex_Type()
)
stats15PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15PortIndex.setStatus("current")


class _Stats15Index_Type(EponStats15MinRecordType):
    """Custom type stats15Index based on EponStats15MinRecordType"""
    subtypeSpec = EponStats15MinRecordType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Stats15Index_Type.__name__ = "EponStats15MinRecordType"
_Stats15Index_Object = MibTableColumn
stats15Index = _Stats15Index_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 4),
    _Stats15Index_Type()
)
stats15Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats15Index.setStatus("current")
_Stats15InOctets_Type = Counter64
_Stats15InOctets_Object = MibTableColumn
stats15InOctets = _Stats15InOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 5),
    _Stats15InOctets_Type()
)
stats15InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InOctets.setStatus("current")
_Stats15InPkts_Type = Counter64
_Stats15InPkts_Object = MibTableColumn
stats15InPkts = _Stats15InPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 6),
    _Stats15InPkts_Type()
)
stats15InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts.setStatus("current")
_Stats15InBroadcastPkts_Type = Counter64
_Stats15InBroadcastPkts_Object = MibTableColumn
stats15InBroadcastPkts = _Stats15InBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 7),
    _Stats15InBroadcastPkts_Type()
)
stats15InBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InBroadcastPkts.setStatus("current")
_Stats15InMulticastPkts_Type = Counter64
_Stats15InMulticastPkts_Object = MibTableColumn
stats15InMulticastPkts = _Stats15InMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 8),
    _Stats15InMulticastPkts_Type()
)
stats15InMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InMulticastPkts.setStatus("current")
_Stats15InPkts64Octets_Type = Counter64
_Stats15InPkts64Octets_Object = MibTableColumn
stats15InPkts64Octets = _Stats15InPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 9),
    _Stats15InPkts64Octets_Type()
)
stats15InPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts64Octets.setStatus("current")
_Stats15InPkts65to127Octets_Type = Counter64
_Stats15InPkts65to127Octets_Object = MibTableColumn
stats15InPkts65to127Octets = _Stats15InPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 10),
    _Stats15InPkts65to127Octets_Type()
)
stats15InPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts65to127Octets.setStatus("current")
_Stats15InPkts128to255Octets_Type = Counter64
_Stats15InPkts128to255Octets_Object = MibTableColumn
stats15InPkts128to255Octets = _Stats15InPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 11),
    _Stats15InPkts128to255Octets_Type()
)
stats15InPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts128to255Octets.setStatus("current")
_Stats15InPkts256to511Octets_Type = Counter64
_Stats15InPkts256to511Octets_Object = MibTableColumn
stats15InPkts256to511Octets = _Stats15InPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 12),
    _Stats15InPkts256to511Octets_Type()
)
stats15InPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts256to511Octets.setStatus("current")
_Stats15InPkts512to1023Octets_Type = Counter64
_Stats15InPkts512to1023Octets_Object = MibTableColumn
stats15InPkts512to1023Octets = _Stats15InPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 13),
    _Stats15InPkts512to1023Octets_Type()
)
stats15InPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts512to1023Octets.setStatus("current")
_Stats15InPkts1024to1518Octets_Type = Counter64
_Stats15InPkts1024to1518Octets_Object = MibTableColumn
stats15InPkts1024to1518Octets = _Stats15InPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 14),
    _Stats15InPkts1024to1518Octets_Type()
)
stats15InPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts1024to1518Octets.setStatus("current")
_Stats15InPkts1519to1522Octets_Type = Counter64
_Stats15InPkts1519to1522Octets_Object = MibTableColumn
stats15InPkts1519to1522Octets = _Stats15InPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 15),
    _Stats15InPkts1519to1522Octets_Type()
)
stats15InPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InPkts1519to1522Octets.setStatus("current")
_Stats15InUndersizePkts_Type = Counter64
_Stats15InUndersizePkts_Object = MibTableColumn
stats15InUndersizePkts = _Stats15InUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 16),
    _Stats15InUndersizePkts_Type()
)
stats15InUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InUndersizePkts.setStatus("current")
_Stats15InOversizePkts_Type = Counter64
_Stats15InOversizePkts_Object = MibTableColumn
stats15InOversizePkts = _Stats15InOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 17),
    _Stats15InOversizePkts_Type()
)
stats15InOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InOversizePkts.setStatus("current")
_Stats15InFragments_Type = Counter64
_Stats15InFragments_Object = MibTableColumn
stats15InFragments = _Stats15InFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 18),
    _Stats15InFragments_Type()
)
stats15InFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InFragments.setStatus("current")
_Stats15InMpcpFrames_Type = Counter64
_Stats15InMpcpFrames_Object = MibTableColumn
stats15InMpcpFrames = _Stats15InMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 19),
    _Stats15InMpcpFrames_Type()
)
stats15InMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InMpcpFrames.setStatus("current")
_Stats15InMpcpOctets_Type = Counter64
_Stats15InMpcpOctets_Object = MibTableColumn
stats15InMpcpOctets = _Stats15InMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 20),
    _Stats15InMpcpOctets_Type()
)
stats15InMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InMpcpOctets.setStatus("current")
_Stats15InOAMFrames_Type = Counter64
_Stats15InOAMFrames_Object = MibTableColumn
stats15InOAMFrames = _Stats15InOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 21),
    _Stats15InOAMFrames_Type()
)
stats15InOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InOAMFrames.setStatus("current")
_Stats15InOAMOctets_Type = Counter64
_Stats15InOAMOctets_Object = MibTableColumn
stats15InOAMOctets = _Stats15InOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 22),
    _Stats15InOAMOctets_Type()
)
stats15InOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InOAMOctets.setStatus("current")
_Stats15InCRCErrorPkts_Type = Counter64
_Stats15InCRCErrorPkts_Object = MibTableColumn
stats15InCRCErrorPkts = _Stats15InCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 23),
    _Stats15InCRCErrorPkts_Type()
)
stats15InCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InCRCErrorPkts.setStatus("current")
_Stats15InDropEvents_Type = Counter64
_Stats15InDropEvents_Object = MibTableColumn
stats15InDropEvents = _Stats15InDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 24),
    _Stats15InDropEvents_Type()
)
stats15InDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InDropEvents.setStatus("current")
_Stats15InJabbers_Type = Counter64
_Stats15InJabbers_Object = MibTableColumn
stats15InJabbers = _Stats15InJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 25),
    _Stats15InJabbers_Type()
)
stats15InJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InJabbers.setStatus("current")
_Stats15InCollision_Type = Counter64
_Stats15InCollision_Object = MibTableColumn
stats15InCollision = _Stats15InCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 26),
    _Stats15InCollision_Type()
)
stats15InCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15InCollision.setStatus("current")
_Stats15OutOctets_Type = Counter64
_Stats15OutOctets_Object = MibTableColumn
stats15OutOctets = _Stats15OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 27),
    _Stats15OutOctets_Type()
)
stats15OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutOctets.setStatus("current")
_Stats15OutPkts_Type = Counter64
_Stats15OutPkts_Object = MibTableColumn
stats15OutPkts = _Stats15OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 28),
    _Stats15OutPkts_Type()
)
stats15OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts.setStatus("current")
_Stats15OutBroadcastPkts_Type = Counter64
_Stats15OutBroadcastPkts_Object = MibTableColumn
stats15OutBroadcastPkts = _Stats15OutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 29),
    _Stats15OutBroadcastPkts_Type()
)
stats15OutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutBroadcastPkts.setStatus("current")
_Stats15OutMulticastPkts_Type = Counter64
_Stats15OutMulticastPkts_Object = MibTableColumn
stats15OutMulticastPkts = _Stats15OutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 30),
    _Stats15OutMulticastPkts_Type()
)
stats15OutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutMulticastPkts.setStatus("current")
_Stats15OutPkts64Octets_Type = Counter64
_Stats15OutPkts64Octets_Object = MibTableColumn
stats15OutPkts64Octets = _Stats15OutPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 31),
    _Stats15OutPkts64Octets_Type()
)
stats15OutPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts64Octets.setStatus("current")
_Stats15OutPkts65to127Octets_Type = Counter64
_Stats15OutPkts65to127Octets_Object = MibTableColumn
stats15OutPkts65to127Octets = _Stats15OutPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 32),
    _Stats15OutPkts65to127Octets_Type()
)
stats15OutPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts65to127Octets.setStatus("current")
_Stats15OutPkts128to255Octets_Type = Counter64
_Stats15OutPkts128to255Octets_Object = MibTableColumn
stats15OutPkts128to255Octets = _Stats15OutPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 33),
    _Stats15OutPkts128to255Octets_Type()
)
stats15OutPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts128to255Octets.setStatus("current")
_Stats15OutPkts256to511Octets_Type = Counter64
_Stats15OutPkts256to511Octets_Object = MibTableColumn
stats15OutPkts256to511Octets = _Stats15OutPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 34),
    _Stats15OutPkts256to511Octets_Type()
)
stats15OutPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts256to511Octets.setStatus("current")
_Stats15OutPkts512to1023Octets_Type = Counter64
_Stats15OutPkts512to1023Octets_Object = MibTableColumn
stats15OutPkts512to1023Octets = _Stats15OutPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 35),
    _Stats15OutPkts512to1023Octets_Type()
)
stats15OutPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts512to1023Octets.setStatus("current")
_Stats15OutPkts1024to1518Octets_Type = Counter64
_Stats15OutPkts1024to1518Octets_Object = MibTableColumn
stats15OutPkts1024to1518Octets = _Stats15OutPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 36),
    _Stats15OutPkts1024to1518Octets_Type()
)
stats15OutPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts1024to1518Octets.setStatus("current")
_Stats15OutPkts1519o1522Octets_Type = Counter64
_Stats15OutPkts1519o1522Octets_Object = MibTableColumn
stats15OutPkts1519o1522Octets = _Stats15OutPkts1519o1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 37),
    _Stats15OutPkts1519o1522Octets_Type()
)
stats15OutPkts1519o1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutPkts1519o1522Octets.setStatus("current")
_Stats15OutUndersizePkts_Type = Counter64
_Stats15OutUndersizePkts_Object = MibTableColumn
stats15OutUndersizePkts = _Stats15OutUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 38),
    _Stats15OutUndersizePkts_Type()
)
stats15OutUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutUndersizePkts.setStatus("current")
_Stats15OutOversizePkts_Type = Counter64
_Stats15OutOversizePkts_Object = MibTableColumn
stats15OutOversizePkts = _Stats15OutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 39),
    _Stats15OutOversizePkts_Type()
)
stats15OutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutOversizePkts.setStatus("current")
_Stats15OutFragments_Type = Counter64
_Stats15OutFragments_Object = MibTableColumn
stats15OutFragments = _Stats15OutFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 40),
    _Stats15OutFragments_Type()
)
stats15OutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutFragments.setStatus("current")
_Stats15OutMpcpFrames_Type = Counter64
_Stats15OutMpcpFrames_Object = MibTableColumn
stats15OutMpcpFrames = _Stats15OutMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 41),
    _Stats15OutMpcpFrames_Type()
)
stats15OutMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutMpcpFrames.setStatus("current")
_Stats15OutMpcpOctets_Type = Counter64
_Stats15OutMpcpOctets_Object = MibTableColumn
stats15OutMpcpOctets = _Stats15OutMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 42),
    _Stats15OutMpcpOctets_Type()
)
stats15OutMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutMpcpOctets.setStatus("current")
_Stats15OutOAMFrames_Type = Counter64
_Stats15OutOAMFrames_Object = MibTableColumn
stats15OutOAMFrames = _Stats15OutOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 43),
    _Stats15OutOAMFrames_Type()
)
stats15OutOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutOAMFrames.setStatus("current")
_Stats15OutOAMOctets_Type = Counter64
_Stats15OutOAMOctets_Object = MibTableColumn
stats15OutOAMOctets = _Stats15OutOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 44),
    _Stats15OutOAMOctets_Type()
)
stats15OutOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutOAMOctets.setStatus("current")
_Stats15OutCRCErrorPkts_Type = Counter64
_Stats15OutCRCErrorPkts_Object = MibTableColumn
stats15OutCRCErrorPkts = _Stats15OutCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 45),
    _Stats15OutCRCErrorPkts_Type()
)
stats15OutCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutCRCErrorPkts.setStatus("current")
_Stats15OutDropEvents_Type = Counter64
_Stats15OutDropEvents_Object = MibTableColumn
stats15OutDropEvents = _Stats15OutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 46),
    _Stats15OutDropEvents_Type()
)
stats15OutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutDropEvents.setStatus("current")
_Stats15OutJabbers_Type = Counter64
_Stats15OutJabbers_Object = MibTableColumn
stats15OutJabbers = _Stats15OutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 47),
    _Stats15OutJabbers_Type()
)
stats15OutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutJabbers.setStatus("current")
_Stats15OutCollision_Type = Counter64
_Stats15OutCollision_Object = MibTableColumn
stats15OutCollision = _Stats15OutCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 48),
    _Stats15OutCollision_Type()
)
stats15OutCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15OutCollision.setStatus("current")


class _Stats15StatusAndAction_Type(Integer32):
    """Custom type stats15StatusAndAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clean", 2))
    )


_Stats15StatusAndAction_Type.__name__ = "Integer32"
_Stats15StatusAndAction_Object = MibTableColumn
stats15StatusAndAction = _Stats15StatusAndAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 49),
    _Stats15StatusAndAction_Type()
)
stats15StatusAndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stats15StatusAndAction.setStatus("current")
_Stats15ValidityTag_Type = TruthValue
_Stats15ValidityTag_Object = MibTableColumn
stats15ValidityTag = _Stats15ValidityTag_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 50),
    _Stats15ValidityTag_Type()
)
stats15ValidityTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15ValidityTag.setStatus("current")
_Stats15ElapsedTime_Type = Counter32
_Stats15ElapsedTime_Object = MibTableColumn
stats15ElapsedTime = _Stats15ElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 51),
    _Stats15ElapsedTime_Type()
)
stats15ElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15ElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    stats15ElapsedTime.setUnits("seconds")
_Stats15EndTime_Type = DateAndTime
_Stats15EndTime_Object = MibTableColumn
stats15EndTime = _Stats15EndTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 2, 1, 52),
    _Stats15EndTime_Type()
)
stats15EndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats15EndTime.setStatus("current")
_Stats24Table_Object = MibTable
stats24Table = _Stats24Table_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3)
)
if mibBuilder.loadTexts:
    stats24Table.setStatus("current")
_Stats24Entry_Object = MibTableRow
stats24Entry = _Stats24Entry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1)
)
stats24Entry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "stats24DeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "stats24CardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "stats24PortIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "stats24Index"),
)
if mibBuilder.loadTexts:
    stats24Entry.setStatus("current")


class _Stats24DeviceIndex_Type(EponDeviceIndex):
    """Custom type stats24DeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Stats24DeviceIndex_Type.__name__ = "EponDeviceIndex"
_Stats24DeviceIndex_Object = MibTableColumn
stats24DeviceIndex = _Stats24DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 1),
    _Stats24DeviceIndex_Type()
)
stats24DeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24DeviceIndex.setStatus("current")


class _Stats24CardIndex_Type(EponCardIndex):
    """Custom type stats24CardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Stats24CardIndex_Type.__name__ = "EponCardIndex"
_Stats24CardIndex_Object = MibTableColumn
stats24CardIndex = _Stats24CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 2),
    _Stats24CardIndex_Type()
)
stats24CardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24CardIndex.setStatus("current")


class _Stats24PortIndex_Type(EponPortIndex):
    """Custom type stats24PortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Stats24PortIndex_Type.__name__ = "EponPortIndex"
_Stats24PortIndex_Object = MibTableColumn
stats24PortIndex = _Stats24PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 3),
    _Stats24PortIndex_Type()
)
stats24PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24PortIndex.setStatus("current")


class _Stats24Index_Type(EponStats24HourRecordType):
    """Custom type stats24Index based on EponStats24HourRecordType"""
    subtypeSpec = EponStats24HourRecordType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Stats24Index_Type.__name__ = "EponStats24HourRecordType"
_Stats24Index_Object = MibTableColumn
stats24Index = _Stats24Index_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 4),
    _Stats24Index_Type()
)
stats24Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stats24Index.setStatus("current")
_Stats24InOctets_Type = Counter64
_Stats24InOctets_Object = MibTableColumn
stats24InOctets = _Stats24InOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 5),
    _Stats24InOctets_Type()
)
stats24InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InOctets.setStatus("current")
_Stats24InPkts_Type = Counter64
_Stats24InPkts_Object = MibTableColumn
stats24InPkts = _Stats24InPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 6),
    _Stats24InPkts_Type()
)
stats24InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts.setStatus("current")
_Stats24InBroadcastPkts_Type = Counter64
_Stats24InBroadcastPkts_Object = MibTableColumn
stats24InBroadcastPkts = _Stats24InBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 7),
    _Stats24InBroadcastPkts_Type()
)
stats24InBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InBroadcastPkts.setStatus("current")
_Stats24InMulticastPkts_Type = Counter64
_Stats24InMulticastPkts_Object = MibTableColumn
stats24InMulticastPkts = _Stats24InMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 8),
    _Stats24InMulticastPkts_Type()
)
stats24InMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InMulticastPkts.setStatus("current")
_Stats24InPkts64Octets_Type = Counter64
_Stats24InPkts64Octets_Object = MibTableColumn
stats24InPkts64Octets = _Stats24InPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 9),
    _Stats24InPkts64Octets_Type()
)
stats24InPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts64Octets.setStatus("current")
_Stats24InPkts65to127Octets_Type = Counter64
_Stats24InPkts65to127Octets_Object = MibTableColumn
stats24InPkts65to127Octets = _Stats24InPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 10),
    _Stats24InPkts65to127Octets_Type()
)
stats24InPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts65to127Octets.setStatus("current")
_Stats24InPkts128to255Octets_Type = Counter64
_Stats24InPkts128to255Octets_Object = MibTableColumn
stats24InPkts128to255Octets = _Stats24InPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 11),
    _Stats24InPkts128to255Octets_Type()
)
stats24InPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts128to255Octets.setStatus("current")
_Stats24InPkts256to511Octets_Type = Counter64
_Stats24InPkts256to511Octets_Object = MibTableColumn
stats24InPkts256to511Octets = _Stats24InPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 12),
    _Stats24InPkts256to511Octets_Type()
)
stats24InPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts256to511Octets.setStatus("current")
_Stats24InPkts512to1023Octets_Type = Counter64
_Stats24InPkts512to1023Octets_Object = MibTableColumn
stats24InPkts512to1023Octets = _Stats24InPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 13),
    _Stats24InPkts512to1023Octets_Type()
)
stats24InPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts512to1023Octets.setStatus("current")
_Stats24InPkts1024to1518Octets_Type = Counter64
_Stats24InPkts1024to1518Octets_Object = MibTableColumn
stats24InPkts1024to1518Octets = _Stats24InPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 14),
    _Stats24InPkts1024to1518Octets_Type()
)
stats24InPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts1024to1518Octets.setStatus("current")
_Stats24InPkts1519to1522Octets_Type = Counter64
_Stats24InPkts1519to1522Octets_Object = MibTableColumn
stats24InPkts1519to1522Octets = _Stats24InPkts1519to1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 15),
    _Stats24InPkts1519to1522Octets_Type()
)
stats24InPkts1519to1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InPkts1519to1522Octets.setStatus("current")
_Stats24InUndersizePkts_Type = Counter64
_Stats24InUndersizePkts_Object = MibTableColumn
stats24InUndersizePkts = _Stats24InUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 16),
    _Stats24InUndersizePkts_Type()
)
stats24InUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InUndersizePkts.setStatus("current")
_Stats24InOversizePkts_Type = Counter64
_Stats24InOversizePkts_Object = MibTableColumn
stats24InOversizePkts = _Stats24InOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 17),
    _Stats24InOversizePkts_Type()
)
stats24InOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InOversizePkts.setStatus("current")
_Stats24InFragments_Type = Counter64
_Stats24InFragments_Object = MibTableColumn
stats24InFragments = _Stats24InFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 18),
    _Stats24InFragments_Type()
)
stats24InFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InFragments.setStatus("current")
_Stats24InMpcpFrames_Type = Counter64
_Stats24InMpcpFrames_Object = MibTableColumn
stats24InMpcpFrames = _Stats24InMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 19),
    _Stats24InMpcpFrames_Type()
)
stats24InMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InMpcpFrames.setStatus("current")
_Stats24InMpcpOctets_Type = Counter64
_Stats24InMpcpOctets_Object = MibTableColumn
stats24InMpcpOctets = _Stats24InMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 20),
    _Stats24InMpcpOctets_Type()
)
stats24InMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InMpcpOctets.setStatus("current")
_Stats24InOAMFrames_Type = Counter64
_Stats24InOAMFrames_Object = MibTableColumn
stats24InOAMFrames = _Stats24InOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 21),
    _Stats24InOAMFrames_Type()
)
stats24InOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InOAMFrames.setStatus("current")
_Stats24InOAMOctets_Type = Counter64
_Stats24InOAMOctets_Object = MibTableColumn
stats24InOAMOctets = _Stats24InOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 22),
    _Stats24InOAMOctets_Type()
)
stats24InOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InOAMOctets.setStatus("current")
_Stats24InCRCErrorPkts_Type = Counter64
_Stats24InCRCErrorPkts_Object = MibTableColumn
stats24InCRCErrorPkts = _Stats24InCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 23),
    _Stats24InCRCErrorPkts_Type()
)
stats24InCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InCRCErrorPkts.setStatus("current")
_Stats24InDropEvents_Type = Counter64
_Stats24InDropEvents_Object = MibTableColumn
stats24InDropEvents = _Stats24InDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 24),
    _Stats24InDropEvents_Type()
)
stats24InDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InDropEvents.setStatus("current")
_Stats24InJabbers_Type = Counter64
_Stats24InJabbers_Object = MibTableColumn
stats24InJabbers = _Stats24InJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 25),
    _Stats24InJabbers_Type()
)
stats24InJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InJabbers.setStatus("current")
_Stats24InCollision_Type = Counter64
_Stats24InCollision_Object = MibTableColumn
stats24InCollision = _Stats24InCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 26),
    _Stats24InCollision_Type()
)
stats24InCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24InCollision.setStatus("current")
_Stats24OutOctets_Type = Counter64
_Stats24OutOctets_Object = MibTableColumn
stats24OutOctets = _Stats24OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 27),
    _Stats24OutOctets_Type()
)
stats24OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutOctets.setStatus("current")
_Stats24OutPkts_Type = Counter64
_Stats24OutPkts_Object = MibTableColumn
stats24OutPkts = _Stats24OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 28),
    _Stats24OutPkts_Type()
)
stats24OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts.setStatus("current")
_Stats24OutBroadcastPkts_Type = Counter64
_Stats24OutBroadcastPkts_Object = MibTableColumn
stats24OutBroadcastPkts = _Stats24OutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 29),
    _Stats24OutBroadcastPkts_Type()
)
stats24OutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutBroadcastPkts.setStatus("current")
_Stats24OutMulticastPkts_Type = Counter64
_Stats24OutMulticastPkts_Object = MibTableColumn
stats24OutMulticastPkts = _Stats24OutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 30),
    _Stats24OutMulticastPkts_Type()
)
stats24OutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutMulticastPkts.setStatus("current")
_Stats24OutPkts64Octets_Type = Counter64
_Stats24OutPkts64Octets_Object = MibTableColumn
stats24OutPkts64Octets = _Stats24OutPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 31),
    _Stats24OutPkts64Octets_Type()
)
stats24OutPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts64Octets.setStatus("current")
_Stats24OutPkts65to127Octets_Type = Counter64
_Stats24OutPkts65to127Octets_Object = MibTableColumn
stats24OutPkts65to127Octets = _Stats24OutPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 32),
    _Stats24OutPkts65to127Octets_Type()
)
stats24OutPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts65to127Octets.setStatus("current")
_Stats24OutPkts128to255Octets_Type = Counter64
_Stats24OutPkts128to255Octets_Object = MibTableColumn
stats24OutPkts128to255Octets = _Stats24OutPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 33),
    _Stats24OutPkts128to255Octets_Type()
)
stats24OutPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts128to255Octets.setStatus("current")
_Stats24OutPkts256to511Octets_Type = Counter64
_Stats24OutPkts256to511Octets_Object = MibTableColumn
stats24OutPkts256to511Octets = _Stats24OutPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 34),
    _Stats24OutPkts256to511Octets_Type()
)
stats24OutPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts256to511Octets.setStatus("current")
_Stats24OutPkts512to1023Octets_Type = Counter64
_Stats24OutPkts512to1023Octets_Object = MibTableColumn
stats24OutPkts512to1023Octets = _Stats24OutPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 35),
    _Stats24OutPkts512to1023Octets_Type()
)
stats24OutPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts512to1023Octets.setStatus("current")
_Stats24OutPkts1024to1518Octets_Type = Counter64
_Stats24OutPkts1024to1518Octets_Object = MibTableColumn
stats24OutPkts1024to1518Octets = _Stats24OutPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 36),
    _Stats24OutPkts1024to1518Octets_Type()
)
stats24OutPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts1024to1518Octets.setStatus("current")
_Stats24OutPkts1519o1522Octets_Type = Counter64
_Stats24OutPkts1519o1522Octets_Object = MibTableColumn
stats24OutPkts1519o1522Octets = _Stats24OutPkts1519o1522Octets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 37),
    _Stats24OutPkts1519o1522Octets_Type()
)
stats24OutPkts1519o1522Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutPkts1519o1522Octets.setStatus("current")
_Stats24OutUndersizePkts_Type = Counter64
_Stats24OutUndersizePkts_Object = MibTableColumn
stats24OutUndersizePkts = _Stats24OutUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 38),
    _Stats24OutUndersizePkts_Type()
)
stats24OutUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutUndersizePkts.setStatus("current")
_Stats24OutOversizePkts_Type = Counter64
_Stats24OutOversizePkts_Object = MibTableColumn
stats24OutOversizePkts = _Stats24OutOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 39),
    _Stats24OutOversizePkts_Type()
)
stats24OutOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutOversizePkts.setStatus("current")
_Stats24OutFragments_Type = Counter64
_Stats24OutFragments_Object = MibTableColumn
stats24OutFragments = _Stats24OutFragments_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 40),
    _Stats24OutFragments_Type()
)
stats24OutFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutFragments.setStatus("current")
_Stats24OutMpcpFrames_Type = Counter64
_Stats24OutMpcpFrames_Object = MibTableColumn
stats24OutMpcpFrames = _Stats24OutMpcpFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 41),
    _Stats24OutMpcpFrames_Type()
)
stats24OutMpcpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutMpcpFrames.setStatus("current")
_Stats24OutMpcpOctets_Type = Counter64
_Stats24OutMpcpOctets_Object = MibTableColumn
stats24OutMpcpOctets = _Stats24OutMpcpOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 42),
    _Stats24OutMpcpOctets_Type()
)
stats24OutMpcpOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutMpcpOctets.setStatus("current")
_Stats24OutOAMFrames_Type = Counter64
_Stats24OutOAMFrames_Object = MibTableColumn
stats24OutOAMFrames = _Stats24OutOAMFrames_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 43),
    _Stats24OutOAMFrames_Type()
)
stats24OutOAMFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutOAMFrames.setStatus("current")
_Stats24OutOAMOctets_Type = Counter64
_Stats24OutOAMOctets_Object = MibTableColumn
stats24OutOAMOctets = _Stats24OutOAMOctets_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 44),
    _Stats24OutOAMOctets_Type()
)
stats24OutOAMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutOAMOctets.setStatus("current")
_Stats24OutCRCErrorPkts_Type = Counter64
_Stats24OutCRCErrorPkts_Object = MibTableColumn
stats24OutCRCErrorPkts = _Stats24OutCRCErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 45),
    _Stats24OutCRCErrorPkts_Type()
)
stats24OutCRCErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutCRCErrorPkts.setStatus("current")
_Stats24OutDropEvents_Type = Counter64
_Stats24OutDropEvents_Object = MibTableColumn
stats24OutDropEvents = _Stats24OutDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 46),
    _Stats24OutDropEvents_Type()
)
stats24OutDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutDropEvents.setStatus("current")
_Stats24OutJabbers_Type = Counter64
_Stats24OutJabbers_Object = MibTableColumn
stats24OutJabbers = _Stats24OutJabbers_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 47),
    _Stats24OutJabbers_Type()
)
stats24OutJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutJabbers.setStatus("current")
_Stats24OutCollision_Type = Counter64
_Stats24OutCollision_Object = MibTableColumn
stats24OutCollision = _Stats24OutCollision_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 48),
    _Stats24OutCollision_Type()
)
stats24OutCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24OutCollision.setStatus("current")


class _Stats24StatusAndAction_Type(Integer32):
    """Custom type stats24StatusAndAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clear", 2))
    )


_Stats24StatusAndAction_Type.__name__ = "Integer32"
_Stats24StatusAndAction_Object = MibTableColumn
stats24StatusAndAction = _Stats24StatusAndAction_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 49),
    _Stats24StatusAndAction_Type()
)
stats24StatusAndAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stats24StatusAndAction.setStatus("current")
_Stats24ValidityTag_Type = TruthValue
_Stats24ValidityTag_Object = MibTableColumn
stats24ValidityTag = _Stats24ValidityTag_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 50),
    _Stats24ValidityTag_Type()
)
stats24ValidityTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24ValidityTag.setStatus("current")
_Stats24ElapsedTime_Type = Counter32
_Stats24ElapsedTime_Object = MibTableColumn
stats24ElapsedTime = _Stats24ElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 51),
    _Stats24ElapsedTime_Type()
)
stats24ElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24ElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    stats24ElapsedTime.setUnits("seconds")
_Stats24EndTime_Type = DateAndTime
_Stats24EndTime_Object = MibTableColumn
stats24EndTime = _Stats24EndTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 3, 1, 52),
    _Stats24EndTime_Type()
)
stats24EndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stats24EndTime.setStatus("current")
_PerfStatsGlobalSet_ObjectIdentity = ObjectIdentity
perfStatsGlobalSet = _PerfStatsGlobalSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 4)
)
if mibBuilder.loadTexts:
    perfStatsGlobalSet.setStatus("current")


class _PerfStats15MinMaxRecord_Type(EponStats15MinRecordType):
    """Custom type perfStats15MinMaxRecord based on EponStats15MinRecordType"""
    defaultValue = 96


_PerfStats15MinMaxRecord_Type.__name__ = "EponStats15MinRecordType"
_PerfStats15MinMaxRecord_Object = MibScalar
perfStats15MinMaxRecord = _PerfStats15MinMaxRecord_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 4, 1),
    _PerfStats15MinMaxRecord_Type()
)
perfStats15MinMaxRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfStats15MinMaxRecord.setStatus("current")


class _PerfStats24HourMaxRecord_Type(EponStats24HourRecordType):
    """Custom type perfStats24HourMaxRecord based on EponStats24HourRecordType"""
    defaultValue = 7


_PerfStats24HourMaxRecord_Type.__name__ = "EponStats24HourRecordType"
_PerfStats24HourMaxRecord_Object = MibScalar
perfStats24HourMaxRecord = _PerfStats24HourMaxRecord_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 4, 2),
    _PerfStats24HourMaxRecord_Type()
)
perfStats24HourMaxRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    perfStats24HourMaxRecord.setStatus("current")
_PerfStatsThresholdTable_Object = MibTable
perfStatsThresholdTable = _PerfStatsThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5)
)
if mibBuilder.loadTexts:
    perfStatsThresholdTable.setStatus("current")
_PerfStatsThresholdEntry_Object = MibTableRow
perfStatsThresholdEntry = _PerfStatsThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1)
)
perfStatsThresholdEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "perfStatsThresholdDeviceIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "perfStatsThresholdCardIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "perfStatsThresholdPortIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "perfStatsThresholdTypeIndex"),
)
if mibBuilder.loadTexts:
    perfStatsThresholdEntry.setStatus("current")


class _PerfStatsThresholdDeviceIndex_Type(EponDeviceIndex):
    """Custom type perfStatsThresholdDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PerfStatsThresholdDeviceIndex_Type.__name__ = "EponDeviceIndex"
_PerfStatsThresholdDeviceIndex_Object = MibTableColumn
perfStatsThresholdDeviceIndex = _PerfStatsThresholdDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 1),
    _PerfStatsThresholdDeviceIndex_Type()
)
perfStatsThresholdDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfStatsThresholdDeviceIndex.setStatus("current")


class _PerfStatsThresholdCardIndex_Type(EponCardIndex):
    """Custom type perfStatsThresholdCardIndex based on EponCardIndex"""
    subtypeSpec = EponCardIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PerfStatsThresholdCardIndex_Type.__name__ = "EponCardIndex"
_PerfStatsThresholdCardIndex_Object = MibTableColumn
perfStatsThresholdCardIndex = _PerfStatsThresholdCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 2),
    _PerfStatsThresholdCardIndex_Type()
)
perfStatsThresholdCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfStatsThresholdCardIndex.setStatus("current")


class _PerfStatsThresholdPortIndex_Type(EponPortIndex):
    """Custom type perfStatsThresholdPortIndex based on EponPortIndex"""
    subtypeSpec = EponPortIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PerfStatsThresholdPortIndex_Type.__name__ = "EponPortIndex"
_PerfStatsThresholdPortIndex_Object = MibTableColumn
perfStatsThresholdPortIndex = _PerfStatsThresholdPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 3),
    _PerfStatsThresholdPortIndex_Type()
)
perfStatsThresholdPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfStatsThresholdPortIndex.setStatus("current")
_PerfStatsThresholdTypeIndex_Type = EponStatsThresholdType
_PerfStatsThresholdTypeIndex_Object = MibTableColumn
perfStatsThresholdTypeIndex = _PerfStatsThresholdTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 4),
    _PerfStatsThresholdTypeIndex_Type()
)
perfStatsThresholdTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    perfStatsThresholdTypeIndex.setStatus("current")
_PerfStatsThresholdUpper_Type = Counter64
_PerfStatsThresholdUpper_Object = MibTableColumn
perfStatsThresholdUpper = _PerfStatsThresholdUpper_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 5),
    _PerfStatsThresholdUpper_Type()
)
perfStatsThresholdUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfStatsThresholdUpper.setStatus("current")
_PerfStatsThresholdLower_Type = Counter64
_PerfStatsThresholdLower_Object = MibTableColumn
perfStatsThresholdLower = _PerfStatsThresholdLower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 6),
    _PerfStatsThresholdLower_Type()
)
perfStatsThresholdLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfStatsThresholdLower.setStatus("current")
_PerfStatsThresholdRowStatus_Type = RowStatus
_PerfStatsThresholdRowStatus_Object = MibTableColumn
perfStatsThresholdRowStatus = _PerfStatsThresholdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 10, 5, 1, 7),
    _PerfStatsThresholdRowStatus_Type()
)
perfStatsThresholdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    perfStatsThresholdRowStatus.setStatus("current")
_EoCTree_ObjectIdentity = ObjectIdentity
eoCTree = _EoCTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 4)
)
_OrTree_ObjectIdentity = ObjectIdentity
orTree = _OrTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5)
)
_CatvOrObjects_ObjectIdentity = ObjectIdentity
catvOrObjects = _CatvOrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1)
)
_OnuCatvOrConfigTable_Object = MibTable
onuCatvOrConfigTable = _OnuCatvOrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    onuCatvOrConfigTable.setStatus("current")
_OnuCatvOrConfigEntry_Object = MibTableRow
onuCatvOrConfigEntry = _OnuCatvOrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1)
)
onuCatvOrConfigEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuCatvOrConfigDeviceIndex"),
)
if mibBuilder.loadTexts:
    onuCatvOrConfigEntry.setStatus("current")


class _OnuCatvOrConfigDeviceIndex_Type(EponDeviceIndex):
    """Custom type onuCatvOrConfigDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuCatvOrConfigDeviceIndex_Type.__name__ = "EponDeviceIndex"
_OnuCatvOrConfigDeviceIndex_Object = MibTableColumn
onuCatvOrConfigDeviceIndex = _OnuCatvOrConfigDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 1),
    _OnuCatvOrConfigDeviceIndex_Type()
)
onuCatvOrConfigDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuCatvOrConfigDeviceIndex.setStatus("current")


class _OnuCatvOrConfigSwitch_Type(Integer32):
    """Custom type onuCatvOrConfigSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_OnuCatvOrConfigSwitch_Type.__name__ = "Integer32"
_OnuCatvOrConfigSwitch_Object = MibTableColumn
onuCatvOrConfigSwitch = _OnuCatvOrConfigSwitch_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 2),
    _OnuCatvOrConfigSwitch_Type()
)
onuCatvOrConfigSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigSwitch.setStatus("current")
_OnuCatvOrConfigGainControlType_Type = Integer32
_OnuCatvOrConfigGainControlType_Object = MibTableColumn
onuCatvOrConfigGainControlType = _OnuCatvOrConfigGainControlType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 3),
    _OnuCatvOrConfigGainControlType_Type()
)
onuCatvOrConfigGainControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigGainControlType.setStatus("current")
_OnuCatvOrConfigAGCUpValue_Type = Integer32
_OnuCatvOrConfigAGCUpValue_Object = MibTableColumn
onuCatvOrConfigAGCUpValue = _OnuCatvOrConfigAGCUpValue_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 4),
    _OnuCatvOrConfigAGCUpValue_Type()
)
onuCatvOrConfigAGCUpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigAGCUpValue.setStatus("current")
_OnuCatvOrConfigAGCRange_Type = Integer32
_OnuCatvOrConfigAGCRange_Object = MibTableColumn
onuCatvOrConfigAGCRange = _OnuCatvOrConfigAGCRange_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 5),
    _OnuCatvOrConfigAGCRange_Type()
)
onuCatvOrConfigAGCRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigAGCRange.setStatus("current")
_OnuCatvOrConfigMGCTxAttenuation_Type = Integer32
_OnuCatvOrConfigMGCTxAttenuation_Object = MibTableColumn
onuCatvOrConfigMGCTxAttenuation = _OnuCatvOrConfigMGCTxAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 6),
    _OnuCatvOrConfigMGCTxAttenuation_Type()
)
onuCatvOrConfigMGCTxAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigMGCTxAttenuation.setStatus("current")
_OnuCatvOrConfigInputLO_Type = Integer32
_OnuCatvOrConfigInputLO_Object = MibTableColumn
onuCatvOrConfigInputLO = _OnuCatvOrConfigInputLO_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 7),
    _OnuCatvOrConfigInputLO_Type()
)
onuCatvOrConfigInputLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigInputLO.setStatus("current")
_OnuCatvOrConfigInputHI_Type = Integer32
_OnuCatvOrConfigInputHI_Object = MibTableColumn
onuCatvOrConfigInputHI = _OnuCatvOrConfigInputHI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 8),
    _OnuCatvOrConfigInputHI_Type()
)
onuCatvOrConfigInputHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigInputHI.setStatus("current")
_OnuCatvOrConfigOutputLO_Type = Integer32
_OnuCatvOrConfigOutputLO_Object = MibTableColumn
onuCatvOrConfigOutputLO = _OnuCatvOrConfigOutputLO_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 9),
    _OnuCatvOrConfigOutputLO_Type()
)
onuCatvOrConfigOutputLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigOutputLO.setStatus("current")
_OnuCatvOrConfigOutputHI_Type = Integer32
_OnuCatvOrConfigOutputHI_Object = MibTableColumn
onuCatvOrConfigOutputHI = _OnuCatvOrConfigOutputHI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 10),
    _OnuCatvOrConfigOutputHI_Type()
)
onuCatvOrConfigOutputHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigOutputHI.setStatus("current")
_OnuCatvOrConfigVoltageHI_Type = Integer32
_OnuCatvOrConfigVoltageHI_Object = MibTableColumn
onuCatvOrConfigVoltageHI = _OnuCatvOrConfigVoltageHI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 11),
    _OnuCatvOrConfigVoltageHI_Type()
)
onuCatvOrConfigVoltageHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigVoltageHI.setStatus("current")
_OnuCatvOrConfigVoltageLO_Type = Integer32
_OnuCatvOrConfigVoltageLO_Object = MibTableColumn
onuCatvOrConfigVoltageLO = _OnuCatvOrConfigVoltageLO_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 12),
    _OnuCatvOrConfigVoltageLO_Type()
)
onuCatvOrConfigVoltageLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigVoltageLO.setStatus("current")
_OnuCatvOrConfigTemperatureHI_Type = Integer32
_OnuCatvOrConfigTemperatureHI_Object = MibTableColumn
onuCatvOrConfigTemperatureHI = _OnuCatvOrConfigTemperatureHI_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 13),
    _OnuCatvOrConfigTemperatureHI_Type()
)
onuCatvOrConfigTemperatureHI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigTemperatureHI.setStatus("current")
_OnuCatvOrConfigTemperatureLO_Type = Integer32
_OnuCatvOrConfigTemperatureLO_Object = MibTableColumn
onuCatvOrConfigTemperatureLO = _OnuCatvOrConfigTemperatureLO_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 1, 1, 14),
    _OnuCatvOrConfigTemperatureLO_Type()
)
onuCatvOrConfigTemperatureLO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    onuCatvOrConfigTemperatureLO.setStatus("current")
_OnuCatvOrInfoTable_Object = MibTable
onuCatvOrInfoTable = _OnuCatvOrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    onuCatvOrInfoTable.setStatus("current")
_OnuCatvOrInfoEntry_Object = MibTableRow
onuCatvOrInfoEntry = _OnuCatvOrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 2, 1)
)
onuCatvOrInfoEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "onuCatvOrInfoDeviceIndex"),
)
if mibBuilder.loadTexts:
    onuCatvOrInfoEntry.setStatus("current")


class _OnuCatvOrInfoDeviceIndex_Type(EponDeviceIndex):
    """Custom type onuCatvOrInfoDeviceIndex based on EponDeviceIndex"""
    subtypeSpec = EponDeviceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OnuCatvOrInfoDeviceIndex_Type.__name__ = "EponDeviceIndex"
_OnuCatvOrInfoDeviceIndex_Object = MibTableColumn
onuCatvOrInfoDeviceIndex = _OnuCatvOrInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 2, 1, 1),
    _OnuCatvOrInfoDeviceIndex_Type()
)
onuCatvOrInfoDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    onuCatvOrInfoDeviceIndex.setStatus("current")
_OnuCatvOrInfoRxPower_Type = Integer32
_OnuCatvOrInfoRxPower_Object = MibTableColumn
onuCatvOrInfoRxPower = _OnuCatvOrInfoRxPower_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 2, 1, 2),
    _OnuCatvOrInfoRxPower_Type()
)
onuCatvOrInfoRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuCatvOrInfoRxPower.setStatus("current")
_OnuCatvOrInfoRfOutVoltage_Type = Integer32
_OnuCatvOrInfoRfOutVoltage_Object = MibTableColumn
onuCatvOrInfoRfOutVoltage = _OnuCatvOrInfoRfOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 2, 1, 3),
    _OnuCatvOrInfoRfOutVoltage_Type()
)
onuCatvOrInfoRfOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuCatvOrInfoRfOutVoltage.setStatus("current")
_OnuCatvOrInfoVoltage_Type = Integer32
_OnuCatvOrInfoVoltage_Object = MibTableColumn
onuCatvOrInfoVoltage = _OnuCatvOrInfoVoltage_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 2, 1, 4),
    _OnuCatvOrInfoVoltage_Type()
)
onuCatvOrInfoVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuCatvOrInfoVoltage.setStatus("current")
_OnuCatvOrInfoTemperature_Type = Integer32
_OnuCatvOrInfoTemperature_Object = MibTableColumn
onuCatvOrInfoTemperature = _OnuCatvOrInfoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 5, 1, 2, 1, 5),
    _OnuCatvOrInfoTemperature_Type()
)
onuCatvOrInfoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onuCatvOrInfoTemperature.setStatus("current")
_EponOnuWifiObject_ObjectIdentity = ObjectIdentity
eponOnuWifiObject = _EponOnuWifiObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9)
)
_EponOnuWifiGroup_ObjectIdentity = ObjectIdentity
eponOnuWifiGroup = _EponOnuWifiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1)
)
_EponOnuWifiTable_Object = MibTable
eponOnuWifiTable = _EponOnuWifiTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eponOnuWifiTable.setStatus("current")
_EponOnuWifiEntry_Object = MibTableRow
eponOnuWifiEntry = _EponOnuWifiEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1)
)
eponOnuWifiEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiIndex"),
)
if mibBuilder.loadTexts:
    eponOnuWifiEntry.setStatus("current")
_EponOnuWifiIndex_Type = EponDeviceIndex
_EponOnuWifiIndex_Object = MibTableColumn
eponOnuWifiIndex = _EponOnuWifiIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 1),
    _EponOnuWifiIndex_Type()
)
eponOnuWifiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiIndex.setStatus("current")


class _EponOnuWifiClearAllWan_Type(Integer32):
    """Custom type eponOnuWifiClearAllWan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_EponOnuWifiClearAllWan_Type.__name__ = "Integer32"
_EponOnuWifiClearAllWan_Object = MibTableColumn
eponOnuWifiClearAllWan = _EponOnuWifiClearAllWan_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 2),
    _EponOnuWifiClearAllWan_Type()
)
eponOnuWifiClearAllWan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiClearAllWan.setStatus("current")


class _EponOnuWifiCfgRestore_Type(Integer32):
    """Custom type eponOnuWifiCfgRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restore", 1)
    )


_EponOnuWifiCfgRestore_Type.__name__ = "Integer32"
_EponOnuWifiCfgRestore_Object = MibTableColumn
eponOnuWifiCfgRestore = _EponOnuWifiCfgRestore_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 3),
    _EponOnuWifiCfgRestore_Type()
)
eponOnuWifiCfgRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiCfgRestore.setStatus("current")


class _EponOnuWifiWlanEnable_Type(Integer32):
    """Custom type eponOnuWifiWlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EponOnuWifiWlanEnable_Type.__name__ = "Integer32"
_EponOnuWifiWlanEnable_Object = MibTableColumn
eponOnuWifiWlanEnable = _EponOnuWifiWlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 4),
    _EponOnuWifiWlanEnable_Type()
)
eponOnuWifiWlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiWlanEnable.setStatus("current")


class _EponOnuWifiHardwareVersion_Type(OctetString):
    """Custom type eponOnuWifiHardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EponOnuWifiHardwareVersion_Type.__name__ = "OctetString"
_EponOnuWifiHardwareVersion_Object = MibTableColumn
eponOnuWifiHardwareVersion = _EponOnuWifiHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 5),
    _EponOnuWifiHardwareVersion_Type()
)
eponOnuWifiHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiHardwareVersion.setStatus("current")


class _EponOnuWifiSoftwareVersion_Type(OctetString):
    """Custom type eponOnuWifiSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EponOnuWifiSoftwareVersion_Type.__name__ = "OctetString"
_EponOnuWifiSoftwareVersion_Object = MibTableColumn
eponOnuWifiSoftwareVersion = _EponOnuWifiSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 6),
    _EponOnuWifiSoftwareVersion_Type()
)
eponOnuWifiSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiSoftwareVersion.setStatus("current")


class _EponOnuWifiChannelID_Type(Integer32):
    """Custom type eponOnuWifiChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_EponOnuWifiChannelID_Type.__name__ = "Integer32"
_EponOnuWifiChannelID_Object = MibTableColumn
eponOnuWifiChannelID = _EponOnuWifiChannelID_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 7),
    _EponOnuWifiChannelID_Type()
)
eponOnuWifiChannelID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiChannelID.setStatus("current")


class _EponOnuWifiWlanStandard_Type(OctetString):
    """Custom type eponOnuWifiWlanStandard based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_EponOnuWifiWlanStandard_Type.__name__ = "OctetString"
_EponOnuWifiWlanStandard_Object = MibTableColumn
eponOnuWifiWlanStandard = _EponOnuWifiWlanStandard_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 8),
    _EponOnuWifiWlanStandard_Type()
)
eponOnuWifiWlanStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiWlanStandard.setStatus("current")


class _EponOnuWifiChannelBandwidth_Type(Integer32):
    """Custom type eponOnuWifiChannelBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("twenty", 1),
          ("fortyMinus", 2),
          ("fortyPlus", 3))
    )


_EponOnuWifiChannelBandwidth_Type.__name__ = "Integer32"
_EponOnuWifiChannelBandwidth_Object = MibTableColumn
eponOnuWifiChannelBandwidth = _EponOnuWifiChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 9),
    _EponOnuWifiChannelBandwidth_Type()
)
eponOnuWifiChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiChannelBandwidth.setStatus("current")


class _EponOnuWifiTxPowerMode_Type(Integer32):
    """Custom type eponOnuWifiTxPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("energy", 1),
          ("standard", 2),
          ("noclip", 3))
    )


_EponOnuWifiTxPowerMode_Type.__name__ = "Integer32"
_EponOnuWifiTxPowerMode_Object = MibTableColumn
eponOnuWifiTxPowerMode = _EponOnuWifiTxPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 1, 1, 10),
    _EponOnuWifiTxPowerMode_Type()
)
eponOnuWifiTxPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiTxPowerMode.setStatus("current")
_EponOnuWifiSsidTable_Object = MibTable
eponOnuWifiSsidTable = _EponOnuWifiSsidTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eponOnuWifiSsidTable.setStatus("current")
_EponOnuWifiSsidEntry_Object = MibTableRow
eponOnuWifiSsidEntry = _EponOnuWifiSsidEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1)
)
eponOnuWifiSsidEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiSsidOnuIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiSsidIndex"),
)
if mibBuilder.loadTexts:
    eponOnuWifiSsidEntry.setStatus("current")
_EponOnuWifiSsidOnuIndex_Type = EponDeviceIndex
_EponOnuWifiSsidOnuIndex_Object = MibTableColumn
eponOnuWifiSsidOnuIndex = _EponOnuWifiSsidOnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1, 1),
    _EponOnuWifiSsidOnuIndex_Type()
)
eponOnuWifiSsidOnuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiSsidOnuIndex.setStatus("current")
_EponOnuWifiSsidIndex_Type = Integer32
_EponOnuWifiSsidIndex_Object = MibTableColumn
eponOnuWifiSsidIndex = _EponOnuWifiSsidIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1, 2),
    _EponOnuWifiSsidIndex_Type()
)
eponOnuWifiSsidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiSsidIndex.setStatus("current")


class _EponOnuWifiSsidName_Type(OctetString):
    """Custom type eponOnuWifiSsidName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EponOnuWifiSsidName_Type.__name__ = "OctetString"
_EponOnuWifiSsidName_Object = MibTableColumn
eponOnuWifiSsidName = _EponOnuWifiSsidName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1, 3),
    _EponOnuWifiSsidName_Type()
)
eponOnuWifiSsidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiSsidName.setStatus("current")


class _EponOnuWifiSsidEncryptMode_Type(Integer32):
    """Custom type eponOnuWifiSsidEncryptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("wep", 1),
          ("wpa", 2),
          ("wpa2", 3),
          ("wpa-wap2", 4))
    )


_EponOnuWifiSsidEncryptMode_Type.__name__ = "Integer32"
_EponOnuWifiSsidEncryptMode_Object = MibTableColumn
eponOnuWifiSsidEncryptMode = _EponOnuWifiSsidEncryptMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1, 4),
    _EponOnuWifiSsidEncryptMode_Type()
)
eponOnuWifiSsidEncryptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiSsidEncryptMode.setStatus("current")


class _EponOnuWifiSsidEncryptKey_Type(OctetString):
    """Custom type eponOnuWifiSsidEncryptKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EponOnuWifiSsidEncryptKey_Type.__name__ = "OctetString"
_EponOnuWifiSsidEncryptKey_Object = MibTableColumn
eponOnuWifiSsidEncryptKey = _EponOnuWifiSsidEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1, 5),
    _EponOnuWifiSsidEncryptKey_Type()
)
eponOnuWifiSsidEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiSsidEncryptKey.setStatus("current")


class _EponOnuWifiSsidEnable_Type(Integer32):
    """Custom type eponOnuWifiSsidEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EponOnuWifiSsidEnable_Type.__name__ = "Integer32"
_EponOnuWifiSsidEnable_Object = MibTableColumn
eponOnuWifiSsidEnable = _EponOnuWifiSsidEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1, 6),
    _EponOnuWifiSsidEnable_Type()
)
eponOnuWifiSsidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiSsidEnable.setStatus("current")


class _EponOnuWifiSsidBroadcastEnable_Type(Integer32):
    """Custom type eponOnuWifiSsidBroadcastEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EponOnuWifiSsidBroadcastEnable_Type.__name__ = "Integer32"
_EponOnuWifiSsidBroadcastEnable_Object = MibTableColumn
eponOnuWifiSsidBroadcastEnable = _EponOnuWifiSsidBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1, 7),
    _EponOnuWifiSsidBroadcastEnable_Type()
)
eponOnuWifiSsidBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiSsidBroadcastEnable.setStatus("current")


class _EponOnuWifiSsidMaxUser_Type(Integer32):
    """Custom type eponOnuWifiSsidMaxUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_EponOnuWifiSsidMaxUser_Type.__name__ = "Integer32"
_EponOnuWifiSsidMaxUser_Object = MibTableColumn
eponOnuWifiSsidMaxUser = _EponOnuWifiSsidMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1, 8),
    _EponOnuWifiSsidMaxUser_Type()
)
eponOnuWifiSsidMaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiSsidMaxUser.setStatus("current")
_EponOnuWifiSsidRowStatus_Type = RowStatus
_EponOnuWifiSsidRowStatus_Object = MibTableColumn
eponOnuWifiSsidRowStatus = _EponOnuWifiSsidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 2, 1, 9),
    _EponOnuWifiSsidRowStatus_Type()
)
eponOnuWifiSsidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiSsidRowStatus.setStatus("current")
_EponOnuWifiWanTable_Object = MibTable
eponOnuWifiWanTable = _EponOnuWifiWanTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eponOnuWifiWanTable.setStatus("current")
_EponOnuWifiWanEntry_Object = MibTableRow
eponOnuWifiWanEntry = _EponOnuWifiWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1)
)
eponOnuWifiWanEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiWanOnuIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiWanIndex"),
)
if mibBuilder.loadTexts:
    eponOnuWifiWanEntry.setStatus("current")
_EponOnuWifiWanOnuIndex_Type = EponDeviceIndex
_EponOnuWifiWanOnuIndex_Object = MibTableColumn
eponOnuWifiWanOnuIndex = _EponOnuWifiWanOnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 1),
    _EponOnuWifiWanOnuIndex_Type()
)
eponOnuWifiWanOnuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiWanOnuIndex.setStatus("current")


class _EponOnuWifiWanIndex_Type(Integer32):
    """Custom type eponOnuWifiWanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EponOnuWifiWanIndex_Type.__name__ = "Integer32"
_EponOnuWifiWanIndex_Object = MibTableColumn
eponOnuWifiWanIndex = _EponOnuWifiWanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 2),
    _EponOnuWifiWanIndex_Type()
)
eponOnuWifiWanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiWanIndex.setStatus("current")


class _EponOnuWifiWanName_Type(OctetString):
    """Custom type eponOnuWifiWanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EponOnuWifiWanName_Type.__name__ = "OctetString"
_EponOnuWifiWanName_Object = MibTableColumn
eponOnuWifiWanName = _EponOnuWifiWanName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 3),
    _EponOnuWifiWanName_Type()
)
eponOnuWifiWanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanName.setStatus("current")


class _EponOnuWifiWanMtu_Type(Integer32):
    """Custom type eponOnuWifiWanMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_EponOnuWifiWanMtu_Type.__name__ = "Integer32"
_EponOnuWifiWanMtu_Object = MibTableColumn
eponOnuWifiWanMtu = _EponOnuWifiWanMtu_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 4),
    _EponOnuWifiWanMtu_Type()
)
eponOnuWifiWanMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanMtu.setStatus("current")


class _EponOnuWifiWanVid_Type(Integer32):
    """Custom type eponOnuWifiWanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_EponOnuWifiWanVid_Type.__name__ = "Integer32"
_EponOnuWifiWanVid_Object = MibTableColumn
eponOnuWifiWanVid = _EponOnuWifiWanVid_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 5),
    _EponOnuWifiWanVid_Type()
)
eponOnuWifiWanVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanVid.setStatus("current")


class _EponOnuWifiWanPrio_Type(Integer32):
    """Custom type eponOnuWifiWanPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EponOnuWifiWanPrio_Type.__name__ = "Integer32"
_EponOnuWifiWanPrio_Object = MibTableColumn
eponOnuWifiWanPrio = _EponOnuWifiWanPrio_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 6),
    _EponOnuWifiWanPrio_Type()
)
eponOnuWifiWanPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanPrio.setStatus("current")


class _EponOnuWifiWanConnectMode_Type(Integer32):
    """Custom type eponOnuWifiWanConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("route", 1),
          ("bridge", 2))
    )


_EponOnuWifiWanConnectMode_Type.__name__ = "Integer32"
_EponOnuWifiWanConnectMode_Object = MibTableColumn
eponOnuWifiWanConnectMode = _EponOnuWifiWanConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 7),
    _EponOnuWifiWanConnectMode_Type()
)
eponOnuWifiWanConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiWanConnectMode.setStatus("current")


class _EponOnuWifiWanIpMode_Type(Integer32):
    """Custom type eponOnuWifiWanIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("static", 2),
          ("pppoe", 3),
          ("other", 4))
    )


_EponOnuWifiWanIpMode_Type.__name__ = "Integer32"
_EponOnuWifiWanIpMode_Object = MibTableColumn
eponOnuWifiWanIpMode = _EponOnuWifiWanIpMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 8),
    _EponOnuWifiWanIpMode_Type()
)
eponOnuWifiWanIpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanIpMode.setStatus("current")


class _EponOnuWifiWanPppoeUser_Type(OctetString):
    """Custom type eponOnuWifiWanPppoeUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EponOnuWifiWanPppoeUser_Type.__name__ = "OctetString"
_EponOnuWifiWanPppoeUser_Object = MibTableColumn
eponOnuWifiWanPppoeUser = _EponOnuWifiWanPppoeUser_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 9),
    _EponOnuWifiWanPppoeUser_Type()
)
eponOnuWifiWanPppoeUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanPppoeUser.setStatus("current")


class _EponOnuWifiWanPppoePassword_Type(OctetString):
    """Custom type eponOnuWifiWanPppoePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EponOnuWifiWanPppoePassword_Type.__name__ = "OctetString"
_EponOnuWifiWanPppoePassword_Object = MibTableColumn
eponOnuWifiWanPppoePassword = _EponOnuWifiWanPppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 10),
    _EponOnuWifiWanPppoePassword_Type()
)
eponOnuWifiWanPppoePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanPppoePassword.setStatus("current")
_EponOnuWifiWanIpv4Addr_Type = IpAddress
_EponOnuWifiWanIpv4Addr_Object = MibTableColumn
eponOnuWifiWanIpv4Addr = _EponOnuWifiWanIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 11),
    _EponOnuWifiWanIpv4Addr_Type()
)
eponOnuWifiWanIpv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanIpv4Addr.setStatus("current")
_EponOnuWifiWanIpv4Mask_Type = IpAddress
_EponOnuWifiWanIpv4Mask_Object = MibTableColumn
eponOnuWifiWanIpv4Mask = _EponOnuWifiWanIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 12),
    _EponOnuWifiWanIpv4Mask_Type()
)
eponOnuWifiWanIpv4Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanIpv4Mask.setStatus("current")
_EponOnuWifiWanIpv4Gw_Type = IpAddress
_EponOnuWifiWanIpv4Gw_Object = MibTableColumn
eponOnuWifiWanIpv4Gw = _EponOnuWifiWanIpv4Gw_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 13),
    _EponOnuWifiWanIpv4Gw_Type()
)
eponOnuWifiWanIpv4Gw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanIpv4Gw.setStatus("current")


class _EponOnuWifiWanIpv4DnsPrimary_Type(OctetString):
    """Custom type eponOnuWifiWanIpv4DnsPrimary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_EponOnuWifiWanIpv4DnsPrimary_Type.__name__ = "OctetString"
_EponOnuWifiWanIpv4DnsPrimary_Object = MibTableColumn
eponOnuWifiWanIpv4DnsPrimary = _EponOnuWifiWanIpv4DnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 14),
    _EponOnuWifiWanIpv4DnsPrimary_Type()
)
eponOnuWifiWanIpv4DnsPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanIpv4DnsPrimary.setStatus("current")


class _EponOnuWifiWanIpv4DnsSecondary_Type(OctetString):
    """Custom type eponOnuWifiWanIpv4DnsSecondary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_EponOnuWifiWanIpv4DnsSecondary_Type.__name__ = "OctetString"
_EponOnuWifiWanIpv4DnsSecondary_Object = MibTableColumn
eponOnuWifiWanIpv4DnsSecondary = _EponOnuWifiWanIpv4DnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 15),
    _EponOnuWifiWanIpv4DnsSecondary_Type()
)
eponOnuWifiWanIpv4DnsSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanIpv4DnsSecondary.setStatus("current")
_EponOnuWifiWanRowStatus_Type = RowStatus
_EponOnuWifiWanRowStatus_Object = MibTableColumn
eponOnuWifiWanRowStatus = _EponOnuWifiWanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 3, 1, 16),
    _EponOnuWifiWanRowStatus_Type()
)
eponOnuWifiWanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eponOnuWifiWanRowStatus.setStatus("current")
_EponOnuWifiDataWanTable_Object = MibTable
eponOnuWifiDataWanTable = _EponOnuWifiDataWanTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 4)
)
if mibBuilder.loadTexts:
    eponOnuWifiDataWanTable.setStatus("current")
_EponOnuWifiDataWanEntry_Object = MibTableRow
eponOnuWifiDataWanEntry = _EponOnuWifiDataWanEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 4, 1)
)
eponOnuWifiDataWanEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiDataWanOnuIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiDataWanIndex"),
)
if mibBuilder.loadTexts:
    eponOnuWifiDataWanEntry.setStatus("current")
_EponOnuWifiDataWanOnuIndex_Type = EponDeviceIndex
_EponOnuWifiDataWanOnuIndex_Object = MibTableColumn
eponOnuWifiDataWanOnuIndex = _EponOnuWifiDataWanOnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 4, 1, 1),
    _EponOnuWifiDataWanOnuIndex_Type()
)
eponOnuWifiDataWanOnuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiDataWanOnuIndex.setStatus("current")
_EponOnuWifiDataWanIndex_Type = Integer32
_EponOnuWifiDataWanIndex_Object = MibTableColumn
eponOnuWifiDataWanIndex = _EponOnuWifiDataWanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 4, 1, 2),
    _EponOnuWifiDataWanIndex_Type()
)
eponOnuWifiDataWanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiDataWanIndex.setStatus("current")


class _EponOnuWifiDataWanConnectMode_Type(Integer32):
    """Custom type eponOnuWifiDataWanConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("route", 1),
          ("bridge", 2))
    )


_EponOnuWifiDataWanConnectMode_Type.__name__ = "Integer32"
_EponOnuWifiDataWanConnectMode_Object = MibTableColumn
eponOnuWifiDataWanConnectMode = _EponOnuWifiDataWanConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 4, 1, 3),
    _EponOnuWifiDataWanConnectMode_Type()
)
eponOnuWifiDataWanConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiDataWanConnectMode.setStatus("current")


class _EponOnuWifiDataWanServiceType_Type(Integer32):
    """Custom type eponOnuWifiDataWanServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("internet", 1),
          ("vod", 2),
          ("voip", 3),
          ("mgmt", 4),
          ("tr069", 5))
    )


_EponOnuWifiDataWanServiceType_Type.__name__ = "Integer32"
_EponOnuWifiDataWanServiceType_Object = MibTableColumn
eponOnuWifiDataWanServiceType = _EponOnuWifiDataWanServiceType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 4, 1, 4),
    _EponOnuWifiDataWanServiceType_Type()
)
eponOnuWifiDataWanServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiDataWanServiceType.setStatus("current")


class _EponOnuWifiDataWanBindIf_Type(Bits):
    """Custom type eponOnuWifiDataWanBindIf based on Bits"""
    namedValues = NamedValues(
        *(("ssid1", 0),
          ("ssid2", 1),
          ("ssid3", 2),
          ("ssid4", 3),
          ("lan1", 4),
          ("lan2", 5),
          ("lan3", 6),
          ("lan4", 7))
    )

_EponOnuWifiDataWanBindIf_Type.__name__ = "Bits"
_EponOnuWifiDataWanBindIf_Object = MibTableColumn
eponOnuWifiDataWanBindIf = _EponOnuWifiDataWanBindIf_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 4, 1, 5),
    _EponOnuWifiDataWanBindIf_Type()
)
eponOnuWifiDataWanBindIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiDataWanBindIf.setStatus("current")
_EponOnuWifiUpgradeTable_Object = MibTable
eponOnuWifiUpgradeTable = _EponOnuWifiUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5)
)
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeTable.setStatus("current")
_EponOnuWifiUpgradeEntry_Object = MibTableRow
eponOnuWifiUpgradeEntry = _EponOnuWifiUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1)
)
eponOnuWifiUpgradeEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiUpgradeOnuIndex"),
)
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeEntry.setStatus("current")
_EponOnuWifiUpgradeOnuIndex_Type = EponDeviceIndex
_EponOnuWifiUpgradeOnuIndex_Object = MibTableColumn
eponOnuWifiUpgradeOnuIndex = _EponOnuWifiUpgradeOnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 1),
    _EponOnuWifiUpgradeOnuIndex_Type()
)
eponOnuWifiUpgradeOnuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeOnuIndex.setStatus("current")


class _EponOnuWifiUpgradeFileType_Type(Integer32):
    """Custom type eponOnuWifiUpgradeFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image", 1),
          ("config", 2))
    )


_EponOnuWifiUpgradeFileType_Type.__name__ = "Integer32"
_EponOnuWifiUpgradeFileType_Object = MibTableColumn
eponOnuWifiUpgradeFileType = _EponOnuWifiUpgradeFileType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 2),
    _EponOnuWifiUpgradeFileType_Type()
)
eponOnuWifiUpgradeFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeFileType.setStatus("current")


class _EponOnuWifiUpgradeFileName_Type(OctetString):
    """Custom type eponOnuWifiUpgradeFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EponOnuWifiUpgradeFileName_Type.__name__ = "OctetString"
_EponOnuWifiUpgradeFileName_Object = MibTableColumn
eponOnuWifiUpgradeFileName = _EponOnuWifiUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 3),
    _EponOnuWifiUpgradeFileName_Type()
)
eponOnuWifiUpgradeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeFileName.setStatus("current")


class _EponOnuWifiUpgradeTransportType_Type(Integer32):
    """Custom type eponOnuWifiUpgradeTransportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ftp", 0)
    )


_EponOnuWifiUpgradeTransportType_Type.__name__ = "Integer32"
_EponOnuWifiUpgradeTransportType_Object = MibTableColumn
eponOnuWifiUpgradeTransportType = _EponOnuWifiUpgradeTransportType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 4),
    _EponOnuWifiUpgradeTransportType_Type()
)
eponOnuWifiUpgradeTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeTransportType.setStatus("current")
_EponOnuWifiUpgradeServerIpv4Addr_Type = IpAddress
_EponOnuWifiUpgradeServerIpv4Addr_Object = MibTableColumn
eponOnuWifiUpgradeServerIpv4Addr = _EponOnuWifiUpgradeServerIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 5),
    _EponOnuWifiUpgradeServerIpv4Addr_Type()
)
eponOnuWifiUpgradeServerIpv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeServerIpv4Addr.setStatus("current")
_EponOnuWifiUpgradeServerPort_Type = Integer32
_EponOnuWifiUpgradeServerPort_Object = MibTableColumn
eponOnuWifiUpgradeServerPort = _EponOnuWifiUpgradeServerPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 6),
    _EponOnuWifiUpgradeServerPort_Type()
)
eponOnuWifiUpgradeServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeServerPort.setStatus("current")


class _EponOnuWifiUpgradeUser_Type(OctetString):
    """Custom type eponOnuWifiUpgradeUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EponOnuWifiUpgradeUser_Type.__name__ = "OctetString"
_EponOnuWifiUpgradeUser_Object = MibTableColumn
eponOnuWifiUpgradeUser = _EponOnuWifiUpgradeUser_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 7),
    _EponOnuWifiUpgradeUser_Type()
)
eponOnuWifiUpgradeUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeUser.setStatus("current")


class _EponOnuWifiUpgradePassword_Type(OctetString):
    """Custom type eponOnuWifiUpgradePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EponOnuWifiUpgradePassword_Type.__name__ = "OctetString"
_EponOnuWifiUpgradePassword_Object = MibTableColumn
eponOnuWifiUpgradePassword = _EponOnuWifiUpgradePassword_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 8),
    _EponOnuWifiUpgradePassword_Type()
)
eponOnuWifiUpgradePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradePassword.setStatus("current")


class _EponOnuWifiUpgradeClearFlag_Type(Integer32):
    """Custom type eponOnuWifiUpgradeClearFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notclear", 1),
          ("clear", 2))
    )


_EponOnuWifiUpgradeClearFlag_Type.__name__ = "Integer32"
_EponOnuWifiUpgradeClearFlag_Object = MibTableColumn
eponOnuWifiUpgradeClearFlag = _EponOnuWifiUpgradeClearFlag_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 9),
    _EponOnuWifiUpgradeClearFlag_Type()
)
eponOnuWifiUpgradeClearFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeClearFlag.setStatus("current")


class _EponOnuWifiUpgradeProceed_Type(Integer32):
    """Custom type eponOnuWifiUpgradeProceed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("downloadandupgrade", 1)
    )


_EponOnuWifiUpgradeProceed_Type.__name__ = "Integer32"
_EponOnuWifiUpgradeProceed_Object = MibTableColumn
eponOnuWifiUpgradeProceed = _EponOnuWifiUpgradeProceed_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 5, 1, 10),
    _EponOnuWifiUpgradeProceed_Type()
)
eponOnuWifiUpgradeProceed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eponOnuWifiUpgradeProceed.setStatus("current")
_EponOnuWifiWanStatusTable_Object = MibTable
eponOnuWifiWanStatusTable = _EponOnuWifiWanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6)
)
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusTable.setStatus("current")
_EponOnuWifiWanStatusEntry_Object = MibTableRow
eponOnuWifiWanStatusEntry = _EponOnuWifiWanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1)
)
eponOnuWifiWanStatusEntry.setIndexNames(
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiWanStatusOnuIndex"),
    (0, "NSCRTV-FTTX-EPON-MIB", "eponOnuWifiWanStatusWanIndex"),
)
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusEntry.setStatus("current")
_EponOnuWifiWanStatusOnuIndex_Type = EponDeviceIndex
_EponOnuWifiWanStatusOnuIndex_Object = MibTableColumn
eponOnuWifiWanStatusOnuIndex = _EponOnuWifiWanStatusOnuIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 1),
    _EponOnuWifiWanStatusOnuIndex_Type()
)
eponOnuWifiWanStatusOnuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusOnuIndex.setStatus("current")
_EponOnuWifiWanStatusWanIndex_Type = Integer32
_EponOnuWifiWanStatusWanIndex_Object = MibTableColumn
eponOnuWifiWanStatusWanIndex = _EponOnuWifiWanStatusWanIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 2),
    _EponOnuWifiWanStatusWanIndex_Type()
)
eponOnuWifiWanStatusWanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusWanIndex.setStatus("current")


class _EponOnuWifiWanStatusWanName_Type(OctetString):
    """Custom type eponOnuWifiWanStatusWanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EponOnuWifiWanStatusWanName_Type.__name__ = "OctetString"
_EponOnuWifiWanStatusWanName_Object = MibTableColumn
eponOnuWifiWanStatusWanName = _EponOnuWifiWanStatusWanName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 3),
    _EponOnuWifiWanStatusWanName_Type()
)
eponOnuWifiWanStatusWanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusWanName.setStatus("current")


class _EponOnuWifiWanStatusWanIpMode_Type(Integer32):
    """Custom type eponOnuWifiWanStatusWanIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("dhcp", 2),
          ("pppoe", 3),
          ("static", 4))
    )


_EponOnuWifiWanStatusWanIpMode_Type.__name__ = "Integer32"
_EponOnuWifiWanStatusWanIpMode_Object = MibTableColumn
eponOnuWifiWanStatusWanIpMode = _EponOnuWifiWanStatusWanIpMode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 4),
    _EponOnuWifiWanStatusWanIpMode_Type()
)
eponOnuWifiWanStatusWanIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusWanIpMode.setStatus("current")


class _EponOnuWifiWanStatusConnState_Type(Integer32):
    """Custom type eponOnuWifiWanStatusConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 0),
          ("connect", 1))
    )


_EponOnuWifiWanStatusConnState_Type.__name__ = "Integer32"
_EponOnuWifiWanStatusConnState_Object = MibTableColumn
eponOnuWifiWanStatusConnState = _EponOnuWifiWanStatusConnState_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 5),
    _EponOnuWifiWanStatusConnState_Type()
)
eponOnuWifiWanStatusConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusConnState.setStatus("current")
_EponOnuWifiWanStatusErrCode_Type = Integer32
_EponOnuWifiWanStatusErrCode_Object = MibTableColumn
eponOnuWifiWanStatusErrCode = _EponOnuWifiWanStatusErrCode_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 6),
    _EponOnuWifiWanStatusErrCode_Type()
)
eponOnuWifiWanStatusErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusErrCode.setStatus("current")
_EponOnuWifiWanStatusIpv4Addr_Type = IpAddress
_EponOnuWifiWanStatusIpv4Addr_Object = MibTableColumn
eponOnuWifiWanStatusIpv4Addr = _EponOnuWifiWanStatusIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 7),
    _EponOnuWifiWanStatusIpv4Addr_Type()
)
eponOnuWifiWanStatusIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusIpv4Addr.setStatus("current")
_EponOnuWifiWanStatusIpv4Mask_Type = IpAddress
_EponOnuWifiWanStatusIpv4Mask_Object = MibTableColumn
eponOnuWifiWanStatusIpv4Mask = _EponOnuWifiWanStatusIpv4Mask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 8),
    _EponOnuWifiWanStatusIpv4Mask_Type()
)
eponOnuWifiWanStatusIpv4Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusIpv4Mask.setStatus("current")
_EponOnuWifiWanStatusIpv4Gw_Type = IpAddress
_EponOnuWifiWanStatusIpv4Gw_Object = MibTableColumn
eponOnuWifiWanStatusIpv4Gw = _EponOnuWifiWanStatusIpv4Gw_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 9),
    _EponOnuWifiWanStatusIpv4Gw_Type()
)
eponOnuWifiWanStatusIpv4Gw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusIpv4Gw.setStatus("current")


class _EponOnuWifiWanStatusIpv4DnsPrimary_Type(OctetString):
    """Custom type eponOnuWifiWanStatusIpv4DnsPrimary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EponOnuWifiWanStatusIpv4DnsPrimary_Type.__name__ = "OctetString"
_EponOnuWifiWanStatusIpv4DnsPrimary_Object = MibTableColumn
eponOnuWifiWanStatusIpv4DnsPrimary = _EponOnuWifiWanStatusIpv4DnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 10),
    _EponOnuWifiWanStatusIpv4DnsPrimary_Type()
)
eponOnuWifiWanStatusIpv4DnsPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusIpv4DnsPrimary.setStatus("current")


class _EponOnuWifiWanStatusIpv4DnsSecondary_Type(OctetString):
    """Custom type eponOnuWifiWanStatusIpv4DnsSecondary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EponOnuWifiWanStatusIpv4DnsSecondary_Type.__name__ = "OctetString"
_EponOnuWifiWanStatusIpv4DnsSecondary_Object = MibTableColumn
eponOnuWifiWanStatusIpv4DnsSecondary = _EponOnuWifiWanStatusIpv4DnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 9, 1, 1, 6, 1, 11),
    _EponOnuWifiWanStatusIpv4DnsSecondary_Type()
)
eponOnuWifiWanStatusIpv4DnsSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eponOnuWifiWanStatusIpv4DnsSecondary.setStatus("current")

# Managed Objects groups


# Notification objects

eponAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 1, 1)
)
eponAlarmNotification.setObjects(
      *(("NSCRTV-FTTX-EPON-MIB", "eponTrapSequenceNumber"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapOccurTime"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapCode"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapInstance"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapSeverity"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapCorrelationId"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapAdditionalText"))
)
if mibBuilder.loadTexts:
    eponAlarmNotification.setStatus(
        "current"
    )

eponEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 17409, 2, 2, 11, 1, 1, 2)
)
eponEventNotification.setObjects(
      *(("NSCRTV-FTTX-EPON-MIB", "eponTrapSequenceNumber"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapOccurTime"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapCode"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapInstance"),
        ("NSCRTV-FTTX-EPON-MIB", "eponTrapAdditionalText"))
)
if mibBuilder.loadTexts:
    eponEventNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-FTTX-EPON-MIB",
    **{"EponAlarmInstance": EponAlarmInstance,
       "EponAlarmCode": EponAlarmCode,
       "EponSeverityType": EponSeverityType,
       "TAddress": TAddress,
       "EponCardIndex": EponCardIndex,
       "EponPortIndex": EponPortIndex,
       "EponDeviceIndex": EponDeviceIndex,
       "AutoNegotiationTechAbility": AutoNegotiationTechAbility,
       "EponStats15MinRecordType": EponStats15MinRecordType,
       "EponStats24HourRecordType": EponStats24HourRecordType,
       "EponStatsThresholdType": EponStatsThresholdType,
       "nscrtvRoot": nscrtvRoot,
       "nscrtvHFCemsTree": nscrtvHFCemsTree,
       "nscrtvEponEocTree": nscrtvEponEocTree,
       "propertyIdent": propertyIdent,
       "alarmsIdent": alarmsIdent,
       "eponAlarmTree": eponAlarmTree,
       "eponTrapObjectGroup": eponTrapObjectGroup,
       "eponNotifications": eponNotifications,
       "eponAlarmNotification": eponAlarmNotification,
       "eponEventNotification": eponEventNotification,
       "eponTrapObjects": eponTrapObjects,
       "eponTrapInstance": eponTrapInstance,
       "eponTrapCorrelationId": eponTrapCorrelationId,
       "eponTrapAdditionalText": eponTrapAdditionalText,
       "eponTrapCode": eponTrapCode,
       "eponTrapSeverity": eponTrapSeverity,
       "eponTrapOccurTime": eponTrapOccurTime,
       "eponTrapSequenceNumber": eponTrapSequenceNumber,
       "eponAlarmObjGroup": eponAlarmObjGroup,
       "activeAlarmTable": activeAlarmTable,
       "activeAlarmEntry": activeAlarmEntry,
       "activeAlarmSeqNum": activeAlarmSeqNum,
       "activeAlarmCode": activeAlarmCode,
       "activeAlarmInstance": activeAlarmInstance,
       "activeAlarmSeverity": activeAlarmSeverity,
       "activeAlarmRaisingNumber": activeAlarmRaisingNumber,
       "activeAlarmFirstOccurTime": activeAlarmFirstOccurTime,
       "activeAlarmLastOccurTime": activeAlarmLastOccurTime,
       "activeAlarmRepeats": activeAlarmRepeats,
       "activeAlarmConfirm": activeAlarmConfirm,
       "activeAlarmAdditionalText": activeAlarmAdditionalText,
       "historyAlarmTable": historyAlarmTable,
       "historyAlarmEntry": historyAlarmEntry,
       "historyAlarmSeqNum": historyAlarmSeqNum,
       "historyAlarmCode": historyAlarmCode,
       "historyAlarmInstance": historyAlarmInstance,
       "historyAlarmSeverity": historyAlarmSeverity,
       "historyAlarmRaisingNumber": historyAlarmRaisingNumber,
       "historyAlarmFirstOccurTime": historyAlarmFirstOccurTime,
       "historyAlarmLastOccurTime": historyAlarmLastOccurTime,
       "historyAlarmRepeats": historyAlarmRepeats,
       "historyAlarmCorrelationId": historyAlarmCorrelationId,
       "historyAlarmAdditionalText": historyAlarmAdditionalText,
       "historyAlarmClearTime": historyAlarmClearTime,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventSeqNum": eventSeqNum,
       "eventCode": eventCode,
       "eventInstance": eventInstance,
       "eventOccurTime": eventOccurTime,
       "eventAdditionalText": eventAdditionalText,
       "eponManagementObjGroup": eponManagementObjGroup,
       "eponManagementAddrTable": eponManagementAddrTable,
       "eponManagementAddrEntry": eponManagementAddrEntry,
       "eponManagementAddrName": eponManagementAddrName,
       "eponManagementAddrTAddress": eponManagementAddrTAddress,
       "eponManagementAddrCommunity": eponManagementAddrCommunity,
       "eponManagementAddrRowStatus": eponManagementAddrRowStatus,
       "eponTree": eponTree,
       "systemObjects": systemObjects,
       "systemGlobalObjects": systemGlobalObjects,
       "systemTime": systemTime,
       "inbandIpAddress": inbandIpAddress,
       "inbandIpSubnetMask": inbandIpSubnetMask,
       "inbandIpGateway": inbandIpGateway,
       "inbandVlanId": inbandVlanId,
       "inbandMacAddress": inbandMacAddress,
       "outbandIpAddress": outbandIpAddress,
       "outbandIpSubnetMask": outbandIpSubnetMask,
       "outbandIpGateway": outbandIpGateway,
       "outbandMacAddress": outbandMacAddress,
       "systemOUI": systemOUI,
       "vendorName": vendorName,
       "devSn": devSn,
       "saveConfig": saveConfig,
       "saveConfigStatus": saveConfigStatus,
       "oltObjects": oltObjects,
       "oltPropertyTable": oltPropertyTable,
       "oltPropertyEntry": oltPropertyEntry,
       "oltDeviceIndex": oltDeviceIndex,
       "oltName": oltName,
       "oltType": oltType,
       "oltAdminStatus": oltAdminStatus,
       "oltDeviceUpTime": oltDeviceUpTime,
       "oltDeviceNumOfTotalServiceSlot": oltDeviceNumOfTotalServiceSlot,
       "oltDeviceNumOfTotalPowerSlot": oltDeviceNumOfTotalPowerSlot,
       "oltDeviceNumOfTotalFanSlot": oltDeviceNumOfTotalFanSlot,
       "oltDeviceStyle": oltDeviceStyle,
       "boardObjects": boardObjects,
       "boardTable": boardTable,
       "boardEntry": boardEntry,
       "bDeviceIndex": bDeviceIndex,
       "bCardIndex": bCardIndex,
       "bType": bType,
       "bAttribute": bAttribute,
       "bOperationStatus": bOperationStatus,
       "bAdminStatus": bAdminStatus,
       "bHardwareVersion": bHardwareVersion,
       "bFirmwareVersion": bFirmwareVersion,
       "bSoftwareVersion": bSoftwareVersion,
       "bUpTime": bUpTime,
       "bAlarmStatus": bAlarmStatus,
       "bSerialNumber": bSerialNumber,
       "bAction": bAction,
       "bName": bName,
       "bPresenceStatus": bPresenceStatus,
       "powerObjects": powerObjects,
       "powerPropertyTable": powerPropertyTable,
       "powerPropertyEntry": powerPropertyEntry,
       "powerDeviceIndex": powerDeviceIndex,
       "powerCardIndex": powerCardIndex,
       "powerCardOperationStatus": powerCardOperationStatus,
       "powerCardAlarmStatus": powerCardAlarmStatus,
       "powerCardAction": powerCardAction,
       "powerCardName": powerCardName,
       "powerCardPresenceStatus": powerCardPresenceStatus,
       "powerCardRedundancyStatus": powerCardRedundancyStatus,
       "fanObjects": fanObjects,
       "fanPropertyTable": fanPropertyTable,
       "fanPropertyEntry": fanPropertyEntry,
       "fanDeviceIndex": fanDeviceIndex,
       "fanCardIndex": fanCardIndex,
       "fanCardOperationStatus": fanCardOperationStatus,
       "fanCardAlarmStatus": fanCardAlarmStatus,
       "fanCardName": fanCardName,
       "fanCardPresenceStatus": fanCardPresenceStatus,
       "fileTransferManagement": fileTransferManagement,
       "fileTransferTable": fileTransferTable,
       "fileTransferEntry": fileTransferEntry,
       "fileTransferIndex": fileTransferIndex,
       "fileTransferProtocolType": fileTransferProtocolType,
       "serverIpAddress": serverIpAddress,
       "ftpUserName": ftpUserName,
       "ftpUserPassword": ftpUserPassword,
       "transferFileSrcNamePath": transferFileSrcNamePath,
       "transferFileDstNamePath": transferFileDstNamePath,
       "transferAction": transferAction,
       "transferStatus": transferStatus,
       "fileInfoManagementTable": fileInfoManagementTable,
       "fileInfoManagementEntry": fileInfoManagementEntry,
       "filePath": filePath,
       "fileName": fileName,
       "fileSize": fileSize,
       "fileModifyTime": fileModifyTime,
       "fileManagementAction": fileManagementAction,
       "fileAttribute": fileAttribute,
       "onuBatchUpgradeTable": onuBatchUpgradeTable,
       "onuBatchUpgradeEntry": onuBatchUpgradeEntry,
       "onuBatchUpgradeIndex": onuBatchUpgradeIndex,
       "onuBatchUpgradeOnuList": onuBatchUpgradeOnuList,
       "onuBatchUpgradeAction": onuBatchUpgradeAction,
       "onuBatchUpgradeStatus": onuBatchUpgradeStatus,
       "onuBatchUpgradeImageName": onuBatchUpgradeImageName,
       "sniObjects": sniObjects,
       "sniAttributeTable": sniAttributeTable,
       "sniAttributeEntry": sniAttributeEntry,
       "sniAttributeDeviceIndex": sniAttributeDeviceIndex,
       "sniAttributeCardIndex": sniAttributeCardIndex,
       "sniAttributePortIndex": sniAttributePortIndex,
       "sniPortName": sniPortName,
       "sniAdminStatus": sniAdminStatus,
       "sniOperationStatus": sniOperationStatus,
       "sniMediaType": sniMediaType,
       "sniAutoNegotiationStatus": sniAutoNegotiationStatus,
       "sniAutoNegotiationMode": sniAutoNegotiationMode,
       "sniPerfStats15minuteEnable": sniPerfStats15minuteEnable,
       "sniPerfStats24hourEnable": sniPerfStats24hourEnable,
       "sniLastStatusChangeTime": sniLastStatusChangeTime,
       "sniMacAddrLearnMaxNum": sniMacAddrLearnMaxNum,
       "sniIsolationEnable": sniIsolationEnable,
       "sniPortType": sniPortType,
       "sniTrunkManagement": sniTrunkManagement,
       "sniTrunkGroupConfigTable": sniTrunkGroupConfigTable,
       "sniTrunkGroupConfigEntry": sniTrunkGroupConfigEntry,
       "sniTrunkGroupConfigIndex": sniTrunkGroupConfigIndex,
       "sniTrunkGroupConfigName": sniTrunkGroupConfigName,
       "sniTrunkGroupConfigMember": sniTrunkGroupConfigMember,
       "sniTrunkGroupConfigPolicy": sniTrunkGroupConfigPolicy,
       "sniTrunkGroupConfigRowstatus": sniTrunkGroupConfigRowstatus,
       "sniTrunkGroupTable": sniTrunkGroupTable,
       "sniTrunkGroupEntry": sniTrunkGroupEntry,
       "sniTrunkGroupIndex": sniTrunkGroupIndex,
       "sniTrunkGroupOperationStatus": sniTrunkGroupOperationStatus,
       "sniTrunkGroupActualSpeed": sniTrunkGroupActualSpeed,
       "sniTrunkGroupAdminStatus": sniTrunkGroupAdminStatus,
       "sniMirrorTable": sniMirrorTable,
       "sniMirrorEntry": sniMirrorEntry,
       "sniMirrorGroupIndex": sniMirrorGroupIndex,
       "sniMirrorGroupName": sniMirrorGroupName,
       "sniMirrorGroupDstPortList": sniMirrorGroupDstPortList,
       "sniMirrorGroupSrcInPortList": sniMirrorGroupSrcInPortList,
       "sniMirrorGroupSrcOutPortList": sniMirrorGroupSrcOutPortList,
       "sniMirrorGroupRowstatus": sniMirrorGroupRowstatus,
       "sniMacAddressManagement": sniMacAddressManagement,
       "sniMacAddressManagementTable": sniMacAddressManagementTable,
       "sniMacAddressManagementEntry": sniMacAddressManagementEntry,
       "sniMacAddressManagementDeviceIndex": sniMacAddressManagementDeviceIndex,
       "sniMacAddrTableAgingTime": sniMacAddrTableAgingTime,
       "sniMacAddrTableClear": sniMacAddrTableClear,
       "sniMacAddressTable": sniMacAddressTable,
       "sniMacAddressEntry": sniMacAddressEntry,
       "sniMacAddrIndex": sniMacAddrIndex,
       "sniMacAddrVlanIdIndex": sniMacAddrVlanIdIndex,
       "sniMacAddrType": sniMacAddrType,
       "sniMacAddrPortId": sniMacAddrPortId,
       "sniMacAddrRowStatus": sniMacAddrRowStatus,
       "sniBroadcastStormSuppressionTable": sniBroadcastStormSuppressionTable,
       "sniBroadcastStormSuppressionEntry": sniBroadcastStormSuppressionEntry,
       "sniBroadcastStormSuppressionDeviceIndex": sniBroadcastStormSuppressionDeviceIndex,
       "sniBroadcastStormSuppressionCardIndex": sniBroadcastStormSuppressionCardIndex,
       "sniBroadcastStormSuppressionPortIndex": sniBroadcastStormSuppressionPortIndex,
       "sniUnicastStormEnable": sniUnicastStormEnable,
       "sniUnicastStormInPacketRate": sniUnicastStormInPacketRate,
       "sniUnicastStormOutPacketRate": sniUnicastStormOutPacketRate,
       "sniMulticastStormEnable": sniMulticastStormEnable,
       "sniMulticastStormInPacketRate": sniMulticastStormInPacketRate,
       "sniMulticastStormOutPacketRate": sniMulticastStormOutPacketRate,
       "sniBroadcastStormEnable": sniBroadcastStormEnable,
       "sniBroadcastStormInPacketRate": sniBroadcastStormInPacketRate,
       "sniBroadcastStormOutPacketRate": sniBroadcastStormOutPacketRate,
       "ponPortObjects": ponPortObjects,
       "ponPortInfoTable": ponPortInfoTable,
       "ponPortInfoEntry": ponPortInfoEntry,
       "ponDeviceIndex": ponDeviceIndex,
       "ponCardIndex": ponCardIndex,
       "ponPortIndex": ponPortIndex,
       "ponPortType": ponPortType,
       "ponOperationStatus": ponOperationStatus,
       "ponPortAdminStatus": ponPortAdminStatus,
       "ponPortMaxOnuNumSupport": ponPortMaxOnuNumSupport,
       "ponPortUpOnuNum": ponPortUpOnuNum,
       "ponPortEncryptMode": ponPortEncryptMode,
       "ponPortEncryptKeyExchangeTime": ponPortEncryptKeyExchangeTime,
       "ponPortIsolationEnable": ponPortIsolationEnable,
       "maxDsBandwidth": maxDsBandwidth,
       "actualDsBandwidthInUse": actualDsBandwidthInUse,
       "remainDsBandwidth": remainDsBandwidth,
       "perfStats15minuteEnable": perfStats15minuteEnable,
       "perfStats24hourEnable": perfStats24hourEnable,
       "ponPortMacAddrLearnMaxNum": ponPortMacAddrLearnMaxNum,
       "maxUsBandwidth": maxUsBandwidth,
       "actualUsBandwidthInUse": actualUsBandwidthInUse,
       "remainUsBandwidth": remainUsBandwidth,
       "ponPortName": ponPortName,
       "onuLongEmitDetectEnable": onuLongEmitDetectEnable,
       "aclManagementGroup": aclManagementGroup,
       "aclListTable": aclListTable,
       "aclListEntry": aclListEntry,
       "aclListIndex": aclListIndex,
       "aclDescription": aclDescription,
       "ruleRowStatus": ruleRowStatus,
       "aclRuleTable": aclRuleTable,
       "aclRuleEntry": aclRuleEntry,
       "aclRuleListIndex": aclRuleListIndex,
       "aclRuleIndex": aclRuleIndex,
       "matchedSourseMac": matchedSourseMac,
       "matchedDestinationMac": matchedDestinationMac,
       "matchedVlanId": matchedVlanId,
       "matchedEthernetType": matchedEthernetType,
       "matchedSourseIP": matchedSourseIP,
       "matchedDestinationIP": matchedDestinationIP,
       "matchedIpMessageType": matchedIpMessageType,
       "matchedDscp": matchedDscp,
       "matchedSoursePort": matchedSoursePort,
       "matchedDestinationPort": matchedDestinationPort,
       "aclRuleRowStatus": aclRuleRowStatus,
       "matchedFieldSelection": matchedFieldSelection,
       "aclAction": aclAction,
       "aclActionParameter": aclActionParameter,
       "matchedSourseMacMask": matchedSourseMacMask,
       "matchedDestinationMacMask": matchedDestinationMacMask,
       "matchedSourseIPMask": matchedSourseIPMask,
       "matchedDestinationIPMask": matchedDestinationIPMask,
       "portACLListTable": portACLListTable,
       "portACLListEntry": portACLListEntry,
       "aclDeviceIndex": aclDeviceIndex,
       "aclCardIndex": aclCardIndex,
       "aclPortIndex": aclPortIndex,
       "portAclListIndex": portAclListIndex,
       "aclPortDirection": aclPortDirection,
       "aclRowStatus": aclRowStatus,
       "ponBroadcastStormSuppressionTable": ponBroadcastStormSuppressionTable,
       "ponBroadcastStormSuppressionEntry": ponBroadcastStormSuppressionEntry,
       "bsDeviceIndex": bsDeviceIndex,
       "bsCardIndex": bsCardIndex,
       "bsPortIndex": bsPortIndex,
       "unicastStormEnable": unicastStormEnable,
       "unicastStormInPacketRate": unicastStormInPacketRate,
       "unicastStormOutPacketRate": unicastStormOutPacketRate,
       "multicastStormEnable": multicastStormEnable,
       "multicastStormInPacketRate": multicastStormInPacketRate,
       "multicastStormOutPacketRate": multicastStormOutPacketRate,
       "broadcastStormEnable": broadcastStormEnable,
       "broadcastStormInPacketRate": broadcastStormInPacketRate,
       "broadcastStormOutPacketRate": broadcastStormOutPacketRate,
       "ponOnuAuthenticationModeTable": ponOnuAuthenticationModeTable,
       "ponOnuAuthenticationModeEntry": ponOnuAuthenticationModeEntry,
       "ponAuthenDeviceIndex": ponAuthenDeviceIndex,
       "ponAuthenCardIndex": ponAuthenCardIndex,
       "ponAuthenPortIndex": ponAuthenPortIndex,
       "ponOnuAuthenMode": ponOnuAuthenMode,
       "onuAuthenModeRowStatus": onuAuthenModeRowStatus,
       "ponPortOpticalTransmissionPropertyTable": ponPortOpticalTransmissionPropertyTable,
       "ponPortOpticalTransmissionPropertyEntry": ponPortOpticalTransmissionPropertyEntry,
       "ponOpDeviceIndex": ponOpDeviceIndex,
       "ponOpCardIndex": ponOpCardIndex,
       "ponOpPortIndex": ponOpPortIndex,
       "ponOpVcc": ponOpVcc,
       "ponOpBias": ponOpBias,
       "ponOpTxPower": ponOpTxPower,
       "ponOpRxPower": ponOpRxPower,
       "ponPortOpticalRxPowerTable": ponPortOpticalRxPowerTable,
       "ponPortOpticalRxPowerEntry": ponPortOpticalRxPowerEntry,
       "ponOpRxOfOnuDeviceIndex": ponOpRxOfOnuDeviceIndex,
       "ponOpRxPowerOfOnu": ponOpRxPowerOfOnu,
       "onuObjects": onuObjects,
       "onuInfoTable": onuInfoTable,
       "onuInfoEntry": onuInfoEntry,
       "onuDeviceIndex": onuDeviceIndex,
       "onuName": onuName,
       "onuType": onuType,
       "onuIpAddress": onuIpAddress,
       "onuIpSubnetMask": onuIpSubnetMask,
       "onuIpGateway": onuIpGateway,
       "onuMacAddress": onuMacAddress,
       "onuOperationStatus": onuOperationStatus,
       "onuAdminStatus": onuAdminStatus,
       "onuChipVendor": onuChipVendor,
       "onuChipType": onuChipType,
       "onuChipVersion": onuChipVersion,
       "onuSoftwareVersion": onuSoftwareVersion,
       "onuFirmwareVersion": onuFirmwareVersion,
       "onuTestDistance": onuTestDistance,
       "onuLlidId": onuLlidId,
       "resetONU": resetONU,
       "onuTimeSinceLastRegister": onuTimeSinceLastRegister,
       "onuMgmtCvlan": onuMgmtCvlan,
       "onuMgmtSvlan": onuMgmtSvlan,
       "onuMgmtPriority": onuMgmtPriority,
       "onuMgmtSnmpTrapHost": onuMgmtSnmpTrapHost,
       "onuMgmtSnmpCommunityForRead": onuMgmtSnmpCommunityForRead,
       "onuMgmtSnmpCommunityForWrite": onuMgmtSnmpCommunityForWrite,
       "onuVendorId": onuVendorId,
       "onuModelId": onuModelId,
       "onuHardwareVersion": onuHardwareVersion,
       "onuSn": onuSn,
       "onuTimeLastRegister": onuTimeLastRegister,
       "onuPonPortOpticalTransmissionPropertyTable": onuPonPortOpticalTransmissionPropertyTable,
       "onuPonPortOpticalTransmissionPropertyEntry": onuPonPortOpticalTransmissionPropertyEntry,
       "onuPonPortOpticalTransmissionPropertyDeviceIndex": onuPonPortOpticalTransmissionPropertyDeviceIndex,
       "onuPonPortOpticalTransmissionPropertyCardIndex": onuPonPortOpticalTransmissionPropertyCardIndex,
       "onuPonPortOpticalTransmissionPropertyPortIndex": onuPonPortOpticalTransmissionPropertyPortIndex,
       "onuReceivedOpticalPower": onuReceivedOpticalPower,
       "onuTramsmittedOpticalPower": onuTramsmittedOpticalPower,
       "onuBiasCurrent": onuBiasCurrent,
       "onuWorkingVoltage": onuWorkingVoltage,
       "onuWorkingTemperature": onuWorkingTemperature,
       "onuCapabilityTable": onuCapabilityTable,
       "onuCapabilityEntry": onuCapabilityEntry,
       "onuCapabilityDeviceIndex": onuCapabilityDeviceIndex,
       "onuGePortNum": onuGePortNum,
       "onuGePortBitmap": onuGePortBitmap,
       "onuFePortNum": onuFePortNum,
       "onuFePortBitmap": onuFePortBitmap,
       "onuQueueNumUplink": onuQueueNumUplink,
       "onuMaxQueueNumUplink": onuMaxQueueNumUplink,
       "onuQueueNumDownlink": onuQueueNumDownlink,
       "onuMaxQueueNumDownlink": onuMaxQueueNumDownlink,
       "onuFecEnable": onuFecEnable,
       "onuEncryptMode": onuEncryptMode,
       "onuEncryptKeyExchangeTime": onuEncryptKeyExchangeTime,
       "onuIsolationEnable": onuIsolationEnable,
       "slaTable": slaTable,
       "slaEntry": slaEntry,
       "slaIndex": slaIndex,
       "slaDsFixedBW": slaDsFixedBW,
       "slaDsPeakBW": slaDsPeakBW,
       "slaDsCommittedBW": slaDsCommittedBW,
       "slaUsFixedBW": slaUsFixedBW,
       "slaUsPeakBW": slaUsPeakBW,
       "slaUsCommittedBW": slaUsCommittedBW,
       "onuAuthenticationManagement": onuAuthenticationManagement,
       "onuAuthenticationPolicy": onuAuthenticationPolicy,
       "onuAuthenticationPreConfigTable": onuAuthenticationPreConfigTable,
       "onuAuthenticationPreConfigEntry": onuAuthenticationPreConfigEntry,
       "onuAuthenOnuId": onuAuthenOnuId,
       "onuAuthenMacAddress": onuAuthenMacAddress,
       "onuAuthenAction": onuAuthenAction,
       "onuAuthenRowStatus": onuAuthenRowStatus,
       "onuAuthenticationBlockTable": onuAuthenticationBlockTable,
       "onuAuthenticationBlockEntry": onuAuthenticationBlockEntry,
       "onuAuthenBlockOnuId": onuAuthenBlockOnuId,
       "onuAuthenBlockMacAddress": onuAuthenBlockMacAddress,
       "authenBlockTime": authenBlockTime,
       "onuAuthenBlockRowStatus": onuAuthenBlockRowStatus,
       "onuLoidAuthenticationConfigTable": onuLoidAuthenticationConfigTable,
       "onuLoidAuthenticationConfigEntry": onuLoidAuthenticationConfigEntry,
       "onuLoidAuthenOnuId": onuLoidAuthenOnuId,
       "onuLoidAuthenLOID": onuLoidAuthenLOID,
       "onuLoidAuthenPassword": onuLoidAuthenPassword,
       "onuLoidAuthenRowStatus": onuLoidAuthenRowStatus,
       "onuAutoFindTable": onuAutoFindTable,
       "onuAutoFindEntry": onuAutoFindEntry,
       "onuAutoFindOnuIndex": onuAutoFindOnuIndex,
       "onuAutoFindMacAddress": onuAutoFindMacAddress,
       "onuAutoFindTime": onuAutoFindTime,
       "onuAutoFindAuthenLOID": onuAutoFindAuthenLOID,
       "onuAutoFindAuthenPassword": onuAutoFindAuthenPassword,
       "uniObjects": uniObjects,
       "uniAttributeTable": uniAttributeTable,
       "uniAttributeEntry": uniAttributeEntry,
       "uniAttributeDeviceIndex": uniAttributeDeviceIndex,
       "uniAttributeCardIndex": uniAttributeCardIndex,
       "uniAttributePortIndex": uniAttributePortIndex,
       "uniAdminStatus": uniAdminStatus,
       "uniOperationStatus": uniOperationStatus,
       "uniAutoNegotiationEnable": uniAutoNegotiationEnable,
       "uniAutoNegotiationLocalTechAbility": uniAutoNegotiationLocalTechAbility,
       "uniAutoNegotiationRestart": uniAutoNegotiationRestart,
       "uniMacAddrLearnMaxNum": uniMacAddrLearnMaxNum,
       "uniCurrentPerfStatsEnable": uniCurrentPerfStatsEnable,
       "uniMacAddressManagement": uniMacAddressManagement,
       "uniMacAddressManagementTable": uniMacAddressManagementTable,
       "uniMacAddressManagementEntry": uniMacAddressManagementEntry,
       "uniMacAddrONUIndex": uniMacAddrONUIndex,
       "uniMacAddrAgingTime": uniMacAddrAgingTime,
       "uniMacAddrClear": uniMacAddrClear,
       "uniMacAddressTable": uniMacAddressTable,
       "uniMacAddressEntry": uniMacAddressEntry,
       "uniMacAddrIndex": uniMacAddrIndex,
       "uniMacAddrVlanIdIndex": uniMacAddrVlanIdIndex,
       "uniMacAddrType": uniMacAddrType,
       "uniMacAddrPortId": uniMacAddrPortId,
       "uniMacAddrRowStatus": uniMacAddrRowStatus,
       "uniTrunkManagement": uniTrunkManagement,
       "uniTrunkGroupConfigTable": uniTrunkGroupConfigTable,
       "uniTrunkGroupConfigEntry": uniTrunkGroupConfigEntry,
       "uniTrunkGroupConfigIndex": uniTrunkGroupConfigIndex,
       "uniTrunkGroupConfigName": uniTrunkGroupConfigName,
       "uniTrunkGroupConfigMember": uniTrunkGroupConfigMember,
       "uniTrunkGroupConfigPolicy": uniTrunkGroupConfigPolicy,
       "uniTrunkGroupConfigRowstatus": uniTrunkGroupConfigRowstatus,
       "uniTrunkGroupTable": uniTrunkGroupTable,
       "uniTrunkGroupEntry": uniTrunkGroupEntry,
       "uniTrunkGroupIndex": uniTrunkGroupIndex,
       "uniTrunkGroupOperationStatus": uniTrunkGroupOperationStatus,
       "uniTrunkGroupActualSpeed": uniTrunkGroupActualSpeed,
       "uniTrunkGroupAdminStatus": uniTrunkGroupAdminStatus,
       "uniPortRateLimitTable": uniPortRateLimitTable,
       "uniPortRateLimitEntry": uniPortRateLimitEntry,
       "uniPortRateLimitDeviceIndex": uniPortRateLimitDeviceIndex,
       "uniPortRateLimitCardIndex": uniPortRateLimitCardIndex,
       "uniPortRateLimitPortIndex": uniPortRateLimitPortIndex,
       "uniPortInCIR": uniPortInCIR,
       "uniPortInCBS": uniPortInCBS,
       "uniPortInEBS": uniPortInEBS,
       "uniPortOutCIR": uniPortOutCIR,
       "uniPortOutPIR": uniPortOutPIR,
       "uniPortInRateLimitEnable": uniPortInRateLimitEnable,
       "uniPortOutRateLimitEnable": uniPortOutRateLimitEnable,
       "uniMirrorTable": uniMirrorTable,
       "uniMirrorEntry": uniMirrorEntry,
       "uniMirrorGroupIndex": uniMirrorGroupIndex,
       "uniMirrorGroupName": uniMirrorGroupName,
       "uniMirrorGroupDstPortList": uniMirrorGroupDstPortList,
       "uniMirrorGroupSrcInPortList": uniMirrorGroupSrcInPortList,
       "uniMirrorGroupSrcOutPortList": uniMirrorGroupSrcOutPortList,
       "uniMirrorGroupRowstatus": uniMirrorGroupRowstatus,
       "uniBroadcastStormSuppressionTable": uniBroadcastStormSuppressionTable,
       "uniBroadcastStormSuppressionEntry": uniBroadcastStormSuppressionEntry,
       "uniBroadcastStormSuppressionCardIndex": uniBroadcastStormSuppressionCardIndex,
       "uniBroadcastStormSuppressionPortIndex": uniBroadcastStormSuppressionPortIndex,
       "uniUnicastStormEnable": uniUnicastStormEnable,
       "uniUnicastStormInPacketRate": uniUnicastStormInPacketRate,
       "uniUnicastStormOutPacketRate": uniUnicastStormOutPacketRate,
       "uniMulticastStormEnable": uniMulticastStormEnable,
       "uniMulticastStormInPacketRate": uniMulticastStormInPacketRate,
       "uniMulticastStormOutPacketRate": uniMulticastStormOutPacketRate,
       "uniBroadcastStormEnable": uniBroadcastStormEnable,
       "uniBroadcastStormInPacketRate": uniBroadcastStormInPacketRate,
       "uniBroadcastStormOutPacketRate": uniBroadcastStormOutPacketRate,
       "uniExtAttributeTable": uniExtAttributeTable,
       "uniExtAttributeEntry": uniExtAttributeEntry,
       "uniExtAttributeCardIndex": uniExtAttributeCardIndex,
       "uniExtAttributePortIndex": uniExtAttributePortIndex,
       "uniPerfStats15minuteEnable": uniPerfStats15minuteEnable,
       "uniPerfStats24hourEnable": uniPerfStats24hourEnable,
       "uniLastChangeTime": uniLastChangeTime,
       "uniIsolationEnable": uniIsolationEnable,
       "uniExMacAddrLearnMaxNum": uniExMacAddrLearnMaxNum,
       "uniAutoNegotiationAdvertisedTechAbility": uniAutoNegotiationAdvertisedTechAbility,
       "uniMacAddrClearByPort": uniMacAddrClearByPort,
       "igmpManagementObjects": igmpManagementObjects,
       "igmpEntityTable": igmpEntityTable,
       "igmpEntityEntry": igmpEntityEntry,
       "igmpDeviceIndex": igmpDeviceIndex,
       "igmpMode": igmpMode,
       "maxQueryResponseTime": maxQueryResponseTime,
       "robustVariable": robustVariable,
       "queryInterval": queryInterval,
       "lastMemberQueryInterval": lastMemberQueryInterval,
       "lastMemberQueryCount": lastMemberQueryCount,
       "igmpVersion": igmpVersion,
       "igmpProxyParaTable": igmpProxyParaTable,
       "igmpProxyParaEntry": igmpProxyParaEntry,
       "proxyIndex": proxyIndex,
       "proxyName": proxyName,
       "proxySrcIPAddress": proxySrcIPAddress,
       "proxyMulticastVID": proxyMulticastVID,
       "proxyMulticastIPAddress": proxyMulticastIPAddress,
       "multicastAssuredBW": multicastAssuredBW,
       "multicastMaxBW": multicastMaxBW,
       "proxyRowStatus": proxyRowStatus,
       "igmpForwardingTable": igmpForwardingTable,
       "igmpForwardingEntry": igmpForwardingEntry,
       "groupDeviceIndex": groupDeviceIndex,
       "groupVlanIndex": groupVlanIndex,
       "groupIPAddress": groupIPAddress,
       "groupPortList": groupPortList,
       "controllededMulticastTable": controllededMulticastTable,
       "controlledMulticastUserAuthorityTable": controlledMulticastUserAuthorityTable,
       "controlledMulticastUserAuthorityEntry": controlledMulticastUserAuthorityEntry,
       "cmDeviceIndex": cmDeviceIndex,
       "cmCardIndex": cmCardIndex,
       "cmPortIndex": cmPortIndex,
       "multicastPackageList": multicastPackageList,
       "igmpGlobalBW": igmpGlobalBW,
       "igmpGlobalBWUsed": igmpGlobalBWUsed,
       "cmUserAuthorityRowStatus": cmUserAuthorityRowStatus,
       "controlledMulticastPackageTable": controlledMulticastPackageTable,
       "controlledMulticastPackageEntry": controlledMulticastPackageEntry,
       "cmIndex": cmIndex,
       "cmName": cmName,
       "cmProxyList": cmProxyList,
       "multicastUserAuthority": multicastUserAuthority,
       "maxRequestChannelNum": maxRequestChannelNum,
       "singlePreviewTime": singlePreviewTime,
       "totalPreviewTime": totalPreviewTime,
       "previewResetTime": previewResetTime,
       "previewCount": previewCount,
       "cmRowStatus": cmRowStatus,
       "igmpOnuUniTable": igmpOnuUniTable,
       "igmpOnuUniEntry": igmpOnuUniEntry,
       "uniMvlanDeviceIndex": uniMvlanDeviceIndex,
       "uniMvlanCardIndex": uniMvlanCardIndex,
       "uniMvlanPortIndex": uniMvlanPortIndex,
       "uniMvlanVid": uniMvlanVid,
       "uniMaxMultiNum": uniMaxMultiNum,
       "uniMvlanTag": uniMvlanTag,
       "uniMvlanRowstatus": uniMvlanRowstatus,
       "igmpOltMulticastVlanTable": igmpOltMulticastVlanTable,
       "igmpOltMulticastVlanEntry": igmpOltMulticastVlanEntry,
       "igmpOltMulticastVlanDeviceIndex": igmpOltMulticastVlanDeviceIndex,
       "multicastVlanId": multicastVlanId,
       "mVlanMaxQueryResponseTime": mVlanMaxQueryResponseTime,
       "mVlanRobustVariable": mVlanRobustVariable,
       "mVlanQueryInterval": mVlanQueryInterval,
       "mVlanLastMemberQueryInterval": mVlanLastMemberQueryInterval,
       "mVlanLastMemberQueryCount": mVlanLastMemberQueryCount,
       "mvlanRowstatus": mvlanRowstatus,
       "igmpSniMulticastVlanTable": igmpSniMulticastVlanTable,
       "igmpSniMulticastVlanEntry": igmpSniMulticastVlanEntry,
       "sniMultiVlanVid": sniMultiVlanVid,
       "sniMultiVlanDeviceIndex": sniMultiVlanDeviceIndex,
       "sniMultiVlanRowstatus": sniMultiVlanRowstatus,
       "onuIgmpModeTable": onuIgmpModeTable,
       "onuIgmpModeEntry": onuIgmpModeEntry,
       "onuIgmpModeDeviceIndex": onuIgmpModeDeviceIndex,
       "onuIgmpMode": onuIgmpMode,
       "vlanManagementObjects": vlanManagementObjects,
       "vlanGlobalInfoTable": vlanGlobalInfoTable,
       "vlanGlobalInfoEntry": vlanGlobalInfoEntry,
       "vlanDeviceIndex": vlanDeviceIndex,
       "maxVlanId": maxVlanId,
       "maxSupportVlans": maxSupportVlans,
       "createdVlanNumber": createdVlanNumber,
       "vlanConfigGroup": vlanConfigGroup,
       "oltVlanConfigTable": oltVlanConfigTable,
       "oltVlanConfigEntry": oltVlanConfigEntry,
       "oltVlanIndex": oltVlanIndex,
       "oltVlanDeviceIndex": oltVlanDeviceIndex,
       "oltVlanName": oltVlanName,
       "taggedPort": taggedPort,
       "untaggedPort": untaggedPort,
       "oltVlanRowStatus": oltVlanRowStatus,
       "onuVlanConfigTable": onuVlanConfigTable,
       "onuVlanConfigEntry": onuVlanConfigEntry,
       "onuVlanIndex": onuVlanIndex,
       "onuVlanDeviceIndex": onuVlanDeviceIndex,
       "onuVlanName": onuVlanName,
       "onuVlanTaggedPort": onuVlanTaggedPort,
       "onuVlanUntaggedPort": onuVlanUntaggedPort,
       "onuVlanRowStatus": onuVlanRowStatus,
       "portVlanGroup": portVlanGroup,
       "onuPortortVlanTable": onuPortortVlanTable,
       "onuPortVlanEntry": onuPortVlanEntry,
       "pvlanDeviceIndex": pvlanDeviceIndex,
       "pvlanCardIndex": pvlanCardIndex,
       "pvlanPortIndex": pvlanPortIndex,
       "vlanTagTpid": vlanTagTpid,
       "vlanTagCfi": vlanTagCfi,
       "vlanTagPriority": vlanTagPriority,
       "vlanPVid": vlanPVid,
       "vlanMode": vlanMode,
       "portVlanTranslationTable": portVlanTranslationTable,
       "portVlanTranslationEntry": portVlanTranslationEntry,
       "pvtDeviceIndex": pvtDeviceIndex,
       "pvtCardIndex": pvtCardIndex,
       "pvtPortIndex": pvtPortIndex,
       "portVidIndex": portVidIndex,
       "translationNewVid": translationNewVid,
       "translationRowStatus": translationRowStatus,
       "portVlanAggregationManagement": portVlanAggregationManagement,
       "portVlanAggregationConfigTable": portVlanAggregationConfigTable,
       "portVlanAggregationConfigEntry": portVlanAggregationConfigEntry,
       "pvaDeviceIndex": pvaDeviceIndex,
       "pvaCardIndex": pvaCardIndex,
       "pvaPortIndex": pvaPortIndex,
       "portAggregationVidIndex": portAggregationVidIndex,
       "aggregationVidList": aggregationVidList,
       "aggregationRowStatus": aggregationRowStatus,
       "portVlanTrunkTable": portVlanTrunkTable,
       "portVlanTrunkEntry": portVlanTrunkEntry,
       "trunkDeviceIndex": trunkDeviceIndex,
       "trunkCardIndex": trunkCardIndex,
       "trunkPortIndex": trunkPortIndex,
       "trunkVidList": trunkVidList,
       "portVlanTrunkRowStatus": portVlanTrunkRowStatus,
       "oltPortVlanTable": oltPortVlanTable,
       "oltPortVlanEntry": oltPortVlanEntry,
       "oltPortVlanDeviceIndex": oltPortVlanDeviceIndex,
       "oltPortVlanTagPriority": oltPortVlanTagPriority,
       "oltPortVlanPVid": oltPortVlanPVid,
       "oltPortVlanMode": oltPortVlanMode,
       "qinQConfigGroup": qinQConfigGroup,
       "portQinQConfigTable": portQinQConfigTable,
       "portQinQConfigEntry": portQinQConfigEntry,
       "pqDeviceIndex": pqDeviceIndex,
       "pqCardIndex": pqCardIndex,
       "pqPortIndex": pqPortIndex,
       "pqStartVlanId": pqStartVlanId,
       "pqEndVlanId": pqEndVlanId,
       "pqSVlanId": pqSVlanId,
       "pqSTagCosDetermine": pqSTagCosDetermine,
       "pqSTagCosNewValue": pqSTagCosNewValue,
       "pqRowStatus": pqRowStatus,
       "qosManagementObjects": qosManagementObjects,
       "qosGlobalSetTable": qosGlobalSetTable,
       "qosGlobalSetEntry": qosGlobalSetEntry,
       "qosGlobalSetDeviceIndex": qosGlobalSetDeviceIndex,
       "qosGlobalSetMaxQueueCount": qosGlobalSetMaxQueueCount,
       "qosGlobalSetMode": qosGlobalSetMode,
       "deviceBaseQosMapTable": deviceBaseQosMapTable,
       "deviceBaseQosMapEntry": deviceBaseQosMapEntry,
       "deviceBaseQosMapDeviceIndex": deviceBaseQosMapDeviceIndex,
       "deviceBaseQosMapRuleIndex": deviceBaseQosMapRuleIndex,
       "deviceBaseQosMapOctet": deviceBaseQosMapOctet,
       "deviceBaseQosPolicyTable": deviceBaseQosPolicyTable,
       "deviceBaseQosPolicyEntry": deviceBaseQosPolicyEntry,
       "deviceBaseQosPolicyDeviceIndex": deviceBaseQosPolicyDeviceIndex,
       "deviceBaseQosPolicyMode": deviceBaseQosPolicyMode,
       "deviceBaseQosPolicyWeightOctet": deviceBaseQosPolicyWeightOctet,
       "deviceBaseQosPolicySpBandwidthRange": deviceBaseQosPolicySpBandwidthRange,
       "portBaseQosMapTable": portBaseQosMapTable,
       "portBaseQosMapEntry": portBaseQosMapEntry,
       "portBaseQosMapDeviceIndex": portBaseQosMapDeviceIndex,
       "portBaseQosMapCardIndex": portBaseQosMapCardIndex,
       "portBaseQosMapPortIndex": portBaseQosMapPortIndex,
       "portBaseQosMapRuleIndex": portBaseQosMapRuleIndex,
       "portBaseQosMapOctet": portBaseQosMapOctet,
       "portBaseQosPolicyTable": portBaseQosPolicyTable,
       "portBaseQosPolicyEntry": portBaseQosPolicyEntry,
       "portBaseQosPolicyDeviceIndex": portBaseQosPolicyDeviceIndex,
       "portBaseQosPolicyCardIndex": portBaseQosPolicyCardIndex,
       "portBaseQosPolicyPortIndex": portBaseQosPolicyPortIndex,
       "portBaseQosPolicyMode": portBaseQosPolicyMode,
       "portBaseQosPolicyWeightOctet": portBaseQosPolicyWeightOctet,
       "portBaseQosPolicySpBandwidthRange": portBaseQosPolicySpBandwidthRange,
       "stpManagementObjects": stpManagementObjects,
       "stpGlobalSetTable": stpGlobalSetTable,
       "stpGlobalSetEntry": stpGlobalSetEntry,
       "stpGlobalSetIndex": stpGlobalSetIndex,
       "stpGlobalSetVersion": stpGlobalSetVersion,
       "stpGlobalSetPriority": stpGlobalSetPriority,
       "stpGlobalSetTimeSinceTopologyChange": stpGlobalSetTimeSinceTopologyChange,
       "stpGlobalSetTopChanges": stpGlobalSetTopChanges,
       "stpGlobalSetDesignatedRoot": stpGlobalSetDesignatedRoot,
       "stpGlobalSetRootCost": stpGlobalSetRootCost,
       "stpGlobalSetRootPort": stpGlobalSetRootPort,
       "stpGlobalSetMaxAge": stpGlobalSetMaxAge,
       "stpGlobalSetHelloTime": stpGlobalSetHelloTime,
       "stpGlobalSetHoldTime": stpGlobalSetHoldTime,
       "stpGlobalSetForwardDelay": stpGlobalSetForwardDelay,
       "stpGlobalSetBridgeMaxAge": stpGlobalSetBridgeMaxAge,
       "stpGlobalSetBridgeHelloTime": stpGlobalSetBridgeHelloTime,
       "stpGlobalSetBridgeForwardDelay": stpGlobalSetBridgeForwardDelay,
       "stpGlobalSetRstpTxHoldCount": stpGlobalSetRstpTxHoldCount,
       "stpGlobalSetEnable": stpGlobalSetEnable,
       "stpPortTable": stpPortTable,
       "stpPortEntry": stpPortEntry,
       "stpPortStpIndex": stpPortStpIndex,
       "stpPortCardIndex": stpPortCardIndex,
       "stpPortIndex": stpPortIndex,
       "stpPortStatus": stpPortStatus,
       "stpPortPriority": stpPortPriority,
       "stpPortPathCost": stpPortPathCost,
       "stpPortDesignatedRoot": stpPortDesignatedRoot,
       "stpPortDesignatedCost": stpPortDesignatedCost,
       "stpPortDesignatedBridge": stpPortDesignatedBridge,
       "stpPortDesignatedPort": stpPortDesignatedPort,
       "stpPortForwardTransitions": stpPortForwardTransitions,
       "stpPortRstpProtocolMigration": stpPortRstpProtocolMigration,
       "stpPortRstpAdminEdgePort": stpPortRstpAdminEdgePort,
       "stpPortRstpOperEdgePort": stpPortRstpOperEdgePort,
       "stpPortPointToPointAdminStatus": stpPortPointToPointAdminStatus,
       "stpPortPointToPointOperStatus": stpPortPointToPointOperStatus,
       "stpPortEnabled": stpPortEnabled,
       "performanceStatisticObjects": performanceStatisticObjects,
       "curStatsTable": curStatsTable,
       "curStatsEntry": curStatsEntry,
       "curStatsDeviceIndex": curStatsDeviceIndex,
       "curStatsCardIndex": curStatsCardIndex,
       "curStatsPortIndex": curStatsPortIndex,
       "curStatsInOctets": curStatsInOctets,
       "curStatsInPkts": curStatsInPkts,
       "curStatsInBroadcastPkts": curStatsInBroadcastPkts,
       "curStatsInMulticastPkts": curStatsInMulticastPkts,
       "curStatsInPkts64Octets": curStatsInPkts64Octets,
       "curStatsInPkts65to127Octets": curStatsInPkts65to127Octets,
       "curStatsInPkts128to255Octets": curStatsInPkts128to255Octets,
       "curStatsInPkts256to511Octets": curStatsInPkts256to511Octets,
       "curStatsInPkts512to1023Octets": curStatsInPkts512to1023Octets,
       "curStatsInPkts1024to1518Octets": curStatsInPkts1024to1518Octets,
       "curStatsInPkts1519to1522Octets": curStatsInPkts1519to1522Octets,
       "curStatsInUndersizePkts": curStatsInUndersizePkts,
       "curStatsInOversizePkts": curStatsInOversizePkts,
       "curStatsInFragments": curStatsInFragments,
       "curStatsInMpcpFrames": curStatsInMpcpFrames,
       "curStatsInMpcpOctets": curStatsInMpcpOctets,
       "curStatsInOAMFrames": curStatsInOAMFrames,
       "curStatsInOAMOctets": curStatsInOAMOctets,
       "curStatsInCRCErrorPkts": curStatsInCRCErrorPkts,
       "curStatsInDropEvents": curStatsInDropEvents,
       "curStatsInJabbers": curStatsInJabbers,
       "curStatsInCollision": curStatsInCollision,
       "curStatsOutOctets": curStatsOutOctets,
       "curStatsOutPkts": curStatsOutPkts,
       "curStatsOutBroadcastPkts": curStatsOutBroadcastPkts,
       "curStatsOutMulticastPkts": curStatsOutMulticastPkts,
       "curStatsOutPkts64Octets": curStatsOutPkts64Octets,
       "curStatsOutPkts65to127Octets": curStatsOutPkts65to127Octets,
       "curStatsOutPkts128to255Octets": curStatsOutPkts128to255Octets,
       "curStatsOutPkts256to511Octets": curStatsOutPkts256to511Octets,
       "curStatsOutPkts512to1023Octets": curStatsOutPkts512to1023Octets,
       "curStatsOutPkts1024to1518Octets": curStatsOutPkts1024to1518Octets,
       "curStatsOutPkts1519o1522Octets": curStatsOutPkts1519o1522Octets,
       "curStatsOutUndersizePkts": curStatsOutUndersizePkts,
       "curStatsOutOversizePkts": curStatsOutOversizePkts,
       "curStatsOutFragments": curStatsOutFragments,
       "curStatsOutMpcpFrames": curStatsOutMpcpFrames,
       "curStatsOutMpcpOctets": curStatsOutMpcpOctets,
       "curStatsOutOAMFrames": curStatsOutOAMFrames,
       "curStatsOutOAMOctets": curStatsOutOAMOctets,
       "curStatsOutCRCErrorPkts": curStatsOutCRCErrorPkts,
       "curStatsOutDropEvents": curStatsOutDropEvents,
       "curStatsOutJabbers": curStatsOutJabbers,
       "curStatsOutCollision": curStatsOutCollision,
       "curStatsStatusAndAction": curStatsStatusAndAction,
       "stats15Table": stats15Table,
       "stats15Entry": stats15Entry,
       "stats15DeviceIndex": stats15DeviceIndex,
       "stats15CardIndex": stats15CardIndex,
       "stats15PortIndex": stats15PortIndex,
       "stats15Index": stats15Index,
       "stats15InOctets": stats15InOctets,
       "stats15InPkts": stats15InPkts,
       "stats15InBroadcastPkts": stats15InBroadcastPkts,
       "stats15InMulticastPkts": stats15InMulticastPkts,
       "stats15InPkts64Octets": stats15InPkts64Octets,
       "stats15InPkts65to127Octets": stats15InPkts65to127Octets,
       "stats15InPkts128to255Octets": stats15InPkts128to255Octets,
       "stats15InPkts256to511Octets": stats15InPkts256to511Octets,
       "stats15InPkts512to1023Octets": stats15InPkts512to1023Octets,
       "stats15InPkts1024to1518Octets": stats15InPkts1024to1518Octets,
       "stats15InPkts1519to1522Octets": stats15InPkts1519to1522Octets,
       "stats15InUndersizePkts": stats15InUndersizePkts,
       "stats15InOversizePkts": stats15InOversizePkts,
       "stats15InFragments": stats15InFragments,
       "stats15InMpcpFrames": stats15InMpcpFrames,
       "stats15InMpcpOctets": stats15InMpcpOctets,
       "stats15InOAMFrames": stats15InOAMFrames,
       "stats15InOAMOctets": stats15InOAMOctets,
       "stats15InCRCErrorPkts": stats15InCRCErrorPkts,
       "stats15InDropEvents": stats15InDropEvents,
       "stats15InJabbers": stats15InJabbers,
       "stats15InCollision": stats15InCollision,
       "stats15OutOctets": stats15OutOctets,
       "stats15OutPkts": stats15OutPkts,
       "stats15OutBroadcastPkts": stats15OutBroadcastPkts,
       "stats15OutMulticastPkts": stats15OutMulticastPkts,
       "stats15OutPkts64Octets": stats15OutPkts64Octets,
       "stats15OutPkts65to127Octets": stats15OutPkts65to127Octets,
       "stats15OutPkts128to255Octets": stats15OutPkts128to255Octets,
       "stats15OutPkts256to511Octets": stats15OutPkts256to511Octets,
       "stats15OutPkts512to1023Octets": stats15OutPkts512to1023Octets,
       "stats15OutPkts1024to1518Octets": stats15OutPkts1024to1518Octets,
       "stats15OutPkts1519o1522Octets": stats15OutPkts1519o1522Octets,
       "stats15OutUndersizePkts": stats15OutUndersizePkts,
       "stats15OutOversizePkts": stats15OutOversizePkts,
       "stats15OutFragments": stats15OutFragments,
       "stats15OutMpcpFrames": stats15OutMpcpFrames,
       "stats15OutMpcpOctets": stats15OutMpcpOctets,
       "stats15OutOAMFrames": stats15OutOAMFrames,
       "stats15OutOAMOctets": stats15OutOAMOctets,
       "stats15OutCRCErrorPkts": stats15OutCRCErrorPkts,
       "stats15OutDropEvents": stats15OutDropEvents,
       "stats15OutJabbers": stats15OutJabbers,
       "stats15OutCollision": stats15OutCollision,
       "stats15StatusAndAction": stats15StatusAndAction,
       "stats15ValidityTag": stats15ValidityTag,
       "stats15ElapsedTime": stats15ElapsedTime,
       "stats15EndTime": stats15EndTime,
       "stats24Table": stats24Table,
       "stats24Entry": stats24Entry,
       "stats24DeviceIndex": stats24DeviceIndex,
       "stats24CardIndex": stats24CardIndex,
       "stats24PortIndex": stats24PortIndex,
       "stats24Index": stats24Index,
       "stats24InOctets": stats24InOctets,
       "stats24InPkts": stats24InPkts,
       "stats24InBroadcastPkts": stats24InBroadcastPkts,
       "stats24InMulticastPkts": stats24InMulticastPkts,
       "stats24InPkts64Octets": stats24InPkts64Octets,
       "stats24InPkts65to127Octets": stats24InPkts65to127Octets,
       "stats24InPkts128to255Octets": stats24InPkts128to255Octets,
       "stats24InPkts256to511Octets": stats24InPkts256to511Octets,
       "stats24InPkts512to1023Octets": stats24InPkts512to1023Octets,
       "stats24InPkts1024to1518Octets": stats24InPkts1024to1518Octets,
       "stats24InPkts1519to1522Octets": stats24InPkts1519to1522Octets,
       "stats24InUndersizePkts": stats24InUndersizePkts,
       "stats24InOversizePkts": stats24InOversizePkts,
       "stats24InFragments": stats24InFragments,
       "stats24InMpcpFrames": stats24InMpcpFrames,
       "stats24InMpcpOctets": stats24InMpcpOctets,
       "stats24InOAMFrames": stats24InOAMFrames,
       "stats24InOAMOctets": stats24InOAMOctets,
       "stats24InCRCErrorPkts": stats24InCRCErrorPkts,
       "stats24InDropEvents": stats24InDropEvents,
       "stats24InJabbers": stats24InJabbers,
       "stats24InCollision": stats24InCollision,
       "stats24OutOctets": stats24OutOctets,
       "stats24OutPkts": stats24OutPkts,
       "stats24OutBroadcastPkts": stats24OutBroadcastPkts,
       "stats24OutMulticastPkts": stats24OutMulticastPkts,
       "stats24OutPkts64Octets": stats24OutPkts64Octets,
       "stats24OutPkts65to127Octets": stats24OutPkts65to127Octets,
       "stats24OutPkts128to255Octets": stats24OutPkts128to255Octets,
       "stats24OutPkts256to511Octets": stats24OutPkts256to511Octets,
       "stats24OutPkts512to1023Octets": stats24OutPkts512to1023Octets,
       "stats24OutPkts1024to1518Octets": stats24OutPkts1024to1518Octets,
       "stats24OutPkts1519o1522Octets": stats24OutPkts1519o1522Octets,
       "stats24OutUndersizePkts": stats24OutUndersizePkts,
       "stats24OutOversizePkts": stats24OutOversizePkts,
       "stats24OutFragments": stats24OutFragments,
       "stats24OutMpcpFrames": stats24OutMpcpFrames,
       "stats24OutMpcpOctets": stats24OutMpcpOctets,
       "stats24OutOAMFrames": stats24OutOAMFrames,
       "stats24OutOAMOctets": stats24OutOAMOctets,
       "stats24OutCRCErrorPkts": stats24OutCRCErrorPkts,
       "stats24OutDropEvents": stats24OutDropEvents,
       "stats24OutJabbers": stats24OutJabbers,
       "stats24OutCollision": stats24OutCollision,
       "stats24StatusAndAction": stats24StatusAndAction,
       "stats24ValidityTag": stats24ValidityTag,
       "stats24ElapsedTime": stats24ElapsedTime,
       "stats24EndTime": stats24EndTime,
       "perfStatsGlobalSet": perfStatsGlobalSet,
       "perfStats15MinMaxRecord": perfStats15MinMaxRecord,
       "perfStats24HourMaxRecord": perfStats24HourMaxRecord,
       "perfStatsThresholdTable": perfStatsThresholdTable,
       "perfStatsThresholdEntry": perfStatsThresholdEntry,
       "perfStatsThresholdDeviceIndex": perfStatsThresholdDeviceIndex,
       "perfStatsThresholdCardIndex": perfStatsThresholdCardIndex,
       "perfStatsThresholdPortIndex": perfStatsThresholdPortIndex,
       "perfStatsThresholdTypeIndex": perfStatsThresholdTypeIndex,
       "perfStatsThresholdUpper": perfStatsThresholdUpper,
       "perfStatsThresholdLower": perfStatsThresholdLower,
       "perfStatsThresholdRowStatus": perfStatsThresholdRowStatus,
       "eoCTree": eoCTree,
       "orTree": orTree,
       "catvOrObjects": catvOrObjects,
       "onuCatvOrConfigTable": onuCatvOrConfigTable,
       "onuCatvOrConfigEntry": onuCatvOrConfigEntry,
       "onuCatvOrConfigDeviceIndex": onuCatvOrConfigDeviceIndex,
       "onuCatvOrConfigSwitch": onuCatvOrConfigSwitch,
       "onuCatvOrConfigGainControlType": onuCatvOrConfigGainControlType,
       "onuCatvOrConfigAGCUpValue": onuCatvOrConfigAGCUpValue,
       "onuCatvOrConfigAGCRange": onuCatvOrConfigAGCRange,
       "onuCatvOrConfigMGCTxAttenuation": onuCatvOrConfigMGCTxAttenuation,
       "onuCatvOrConfigInputLO": onuCatvOrConfigInputLO,
       "onuCatvOrConfigInputHI": onuCatvOrConfigInputHI,
       "onuCatvOrConfigOutputLO": onuCatvOrConfigOutputLO,
       "onuCatvOrConfigOutputHI": onuCatvOrConfigOutputHI,
       "onuCatvOrConfigVoltageHI": onuCatvOrConfigVoltageHI,
       "onuCatvOrConfigVoltageLO": onuCatvOrConfigVoltageLO,
       "onuCatvOrConfigTemperatureHI": onuCatvOrConfigTemperatureHI,
       "onuCatvOrConfigTemperatureLO": onuCatvOrConfigTemperatureLO,
       "onuCatvOrInfoTable": onuCatvOrInfoTable,
       "onuCatvOrInfoEntry": onuCatvOrInfoEntry,
       "onuCatvOrInfoDeviceIndex": onuCatvOrInfoDeviceIndex,
       "onuCatvOrInfoRxPower": onuCatvOrInfoRxPower,
       "onuCatvOrInfoRfOutVoltage": onuCatvOrInfoRfOutVoltage,
       "onuCatvOrInfoVoltage": onuCatvOrInfoVoltage,
       "onuCatvOrInfoTemperature": onuCatvOrInfoTemperature,
       "eponOnuWifiObject": eponOnuWifiObject,
       "eponWifiGroup": eponWifiGroup,
       "eponOnuWifiGroup": eponOnuWifiGroup,
       "eponOnuWifiTable": eponOnuWifiTable,
       "eponOnuWifiEntry": eponOnuWifiEntry,
       "eponOnuWifiIndex": eponOnuWifiIndex,
       "eponOnuWifiClearAllWan": eponOnuWifiClearAllWan,
       "eponOnuWifiCfgRestore": eponOnuWifiCfgRestore,
       "eponOnuWifiWlanEnable": eponOnuWifiWlanEnable,
       "eponOnuWifiHardwareVersion": eponOnuWifiHardwareVersion,
       "eponOnuWifiSoftwareVersion": eponOnuWifiSoftwareVersion,
       "eponOnuWifiChannelID": eponOnuWifiChannelID,
       "eponOnuWifiWlanStandard": eponOnuWifiWlanStandard,
       "eponOnuWifiChannelBandwidth": eponOnuWifiChannelBandwidth,
       "eponOnuWifiTxPowerMode": eponOnuWifiTxPowerMode,
       "eponOnuWifiSsidTable": eponOnuWifiSsidTable,
       "eponOnuWifiSsidEntry": eponOnuWifiSsidEntry,
       "eponOnuWifiSsidOnuIndex": eponOnuWifiSsidOnuIndex,
       "eponOnuWifiSsidIndex": eponOnuWifiSsidIndex,
       "eponOnuWifiSsidName": eponOnuWifiSsidName,
       "eponOnuWifiSsidEncryptMode": eponOnuWifiSsidEncryptMode,
       "eponOnuWifiSsidEncryptKey": eponOnuWifiSsidEncryptKey,
       "eponOnuWifiSsidEnable": eponOnuWifiSsidEnable,
       "eponOnuWifiSsidBroadcastEnable": eponOnuWifiSsidBroadcastEnable,
       "eponOnuWifiSsidMaxUser": eponOnuWifiSsidMaxUser,
       "eponOnuWifiSsidRowStatus": eponOnuWifiSsidRowStatus,
       "eponOnuWifiWanTable": eponOnuWifiWanTable,
       "eponOnuWifiWanEntry": eponOnuWifiWanEntry,
       "eponOnuWifiWanOnuIndex": eponOnuWifiWanOnuIndex,
       "eponOnuWifiWanIndex": eponOnuWifiWanIndex,
       "eponOnuWifiWanName": eponOnuWifiWanName,
       "eponOnuWifiWanMtu": eponOnuWifiWanMtu,
       "eponOnuWifiWanVid": eponOnuWifiWanVid,
       "eponOnuWifiWanPrio": eponOnuWifiWanPrio,
       "eponOnuWifiWanConnectMode": eponOnuWifiWanConnectMode,
       "eponOnuWifiWanIpMode": eponOnuWifiWanIpMode,
       "eponOnuWifiWanPppoeUser": eponOnuWifiWanPppoeUser,
       "eponOnuWifiWanPppoePassword": eponOnuWifiWanPppoePassword,
       "eponOnuWifiWanIpv4Addr": eponOnuWifiWanIpv4Addr,
       "eponOnuWifiWanIpv4Mask": eponOnuWifiWanIpv4Mask,
       "eponOnuWifiWanIpv4Gw": eponOnuWifiWanIpv4Gw,
       "eponOnuWifiWanIpv4DnsPrimary": eponOnuWifiWanIpv4DnsPrimary,
       "eponOnuWifiWanIpv4DnsSecondary": eponOnuWifiWanIpv4DnsSecondary,
       "eponOnuWifiWanRowStatus": eponOnuWifiWanRowStatus,
       "eponOnuWifiDataWanTable": eponOnuWifiDataWanTable,
       "eponOnuWifiDataWanEntry": eponOnuWifiDataWanEntry,
       "eponOnuWifiDataWanOnuIndex": eponOnuWifiDataWanOnuIndex,
       "eponOnuWifiDataWanIndex": eponOnuWifiDataWanIndex,
       "eponOnuWifiDataWanConnectMode": eponOnuWifiDataWanConnectMode,
       "eponOnuWifiDataWanServiceType": eponOnuWifiDataWanServiceType,
       "eponOnuWifiDataWanBindIf": eponOnuWifiDataWanBindIf,
       "eponOnuWifiUpgradeTable": eponOnuWifiUpgradeTable,
       "eponOnuWifiUpgradeEntry": eponOnuWifiUpgradeEntry,
       "eponOnuWifiUpgradeOnuIndex": eponOnuWifiUpgradeOnuIndex,
       "eponOnuWifiUpgradeFileType": eponOnuWifiUpgradeFileType,
       "eponOnuWifiUpgradeFileName": eponOnuWifiUpgradeFileName,
       "eponOnuWifiUpgradeTransportType": eponOnuWifiUpgradeTransportType,
       "eponOnuWifiUpgradeServerIpv4Addr": eponOnuWifiUpgradeServerIpv4Addr,
       "eponOnuWifiUpgradeServerPort": eponOnuWifiUpgradeServerPort,
       "eponOnuWifiUpgradeUser": eponOnuWifiUpgradeUser,
       "eponOnuWifiUpgradePassword": eponOnuWifiUpgradePassword,
       "eponOnuWifiUpgradeClearFlag": eponOnuWifiUpgradeClearFlag,
       "eponOnuWifiUpgradeProceed": eponOnuWifiUpgradeProceed,
       "eponOnuWifiWanStatusTable": eponOnuWifiWanStatusTable,
       "eponOnuWifiWanStatusEntry": eponOnuWifiWanStatusEntry,
       "eponOnuWifiWanStatusOnuIndex": eponOnuWifiWanStatusOnuIndex,
       "eponOnuWifiWanStatusWanIndex": eponOnuWifiWanStatusWanIndex,
       "eponOnuWifiWanStatusWanName": eponOnuWifiWanStatusWanName,
       "eponOnuWifiWanStatusWanIpMode": eponOnuWifiWanStatusWanIpMode,
       "eponOnuWifiWanStatusConnState": eponOnuWifiWanStatusConnState,
       "eponOnuWifiWanStatusErrCode": eponOnuWifiWanStatusErrCode,
       "eponOnuWifiWanStatusIpv4Addr": eponOnuWifiWanStatusIpv4Addr,
       "eponOnuWifiWanStatusIpv4Mask": eponOnuWifiWanStatusIpv4Mask,
       "eponOnuWifiWanStatusIpv4Gw": eponOnuWifiWanStatusIpv4Gw,
       "eponOnuWifiWanStatusIpv4DnsPrimary": eponOnuWifiWanStatusIpv4DnsPrimary,
       "eponOnuWifiWanStatusIpv4DnsSecondary": eponOnuWifiWanStatusIpv4DnsSecondary}
)
