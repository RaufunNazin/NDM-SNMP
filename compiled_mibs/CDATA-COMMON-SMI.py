# SNMP MIB module (CDATA-COMMON-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/CDATA-COMMON-SMI
# Produced by pysmi-1.6.1 at Thu May  8 16:38:34 2025
# On host user-HP platform Linux version 6.11.0-25-generic by user user
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

vendor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592)
)
if mibBuilder.loadTexts:
    vendor.setRevisions(
        ("2016-03-02 14:47",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DataDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2))
    )



class DeviceOperation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("default", 3),
          ("saveConfig", 4),
          ("restore", 5),
          ("delete", 6))
    )



class DeviceStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("notPresent", 1),
          ("offline", 2),
          ("online", 3),
          ("normal", 4),
          ("abnormal", 5))
    )



class DeviceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            67174657
        )
    )
    namedValues = NamedValues(
        ("fd1508gs", 67174657)
    )



class LedStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("blink", 3))
    )



class OperSwitch(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_IpProduct_ObjectIdentity = ObjectIdentity
ipProduct = _IpProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1)
)
if mibBuilder.loadTexts:
    ipProduct.setStatus("current")
_MediaConverter_ObjectIdentity = ObjectIdentity
mediaConverter = _MediaConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1)
)
if mibBuilder.loadTexts:
    mediaConverter.setStatus("current")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 2)
)
if mibBuilder.loadTexts:
    switch.setStatus("current")
_Epon_ObjectIdentity = ObjectIdentity
epon = _Epon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 3)
)
if mibBuilder.loadTexts:
    epon.setStatus("current")
_Eoc_ObjectIdentity = ObjectIdentity
eoc = _Eoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 4)
)
if mibBuilder.loadTexts:
    eoc.setStatus("current")
_Gpon_ObjectIdentity = ObjectIdentity
gpon = _Gpon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5)
)
if mibBuilder.loadTexts:
    gpon.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CDATA-COMMON-SMI",
    **{"DataDirection": DataDirection,
       "DeviceOperation": DeviceOperation,
       "DeviceStatus": DeviceStatus,
       "DeviceType": DeviceType,
       "LedStatus": LedStatus,
       "OperSwitch": OperSwitch,
       "vendor": vendor,
       "ipProduct": ipProduct,
       "mediaConverter": mediaConverter,
       "switch": switch,
       "epon": epon,
       "eoc": eoc,
       "gpon": gpon}
)
