# SNMP MIB module (SNMP-FRAMEWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///home/user/Documents/snmptest/mibs/SNMP-FRAMEWORK-MIB
# Produced by pysmi-1.6.1 at Tue May  6 16:38:15 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpFrameworkMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 10)
)
if mibBuilder.loadTexts:
    snmpFrameworkMIB.setRevisions(
        ("2002-10-14 00:00",
         "1999-01-19 00:00",
         "1997-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpEngineID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 32),
    )



class SnmpSecurityModel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class SnmpMessageProcessingModel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class SnmpSecurityLevel(TextualConvention, Integer32):
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
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )



class SnmpAdminString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SnmpFrameworkAdmin_ObjectIdentity = ObjectIdentity
snmpFrameworkAdmin = _SnmpFrameworkAdmin_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1)
)
_SnmpAuthProtocols_ObjectIdentity = ObjectIdentity
snmpAuthProtocols = _SnmpAuthProtocols_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 1)
)
if mibBuilder.loadTexts:
    snmpAuthProtocols.setStatus("current")
_SnmpPrivProtocols_ObjectIdentity = ObjectIdentity
snmpPrivProtocols = _SnmpPrivProtocols_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 1, 2)
)
if mibBuilder.loadTexts:
    snmpPrivProtocols.setStatus("current")
_SnmpFrameworkMIBObjects_ObjectIdentity = ObjectIdentity
snmpFrameworkMIBObjects = _SnmpFrameworkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 2)
)
_SnmpEngine_ObjectIdentity = ObjectIdentity
snmpEngine = _SnmpEngine_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 2, 1)
)
_SnmpEngineID_Type = SnmpEngineID
_SnmpEngineID_Object = MibScalar
snmpEngineID = _SnmpEngineID_Object(
    (1, 3, 6, 1, 6, 3, 10, 2, 1, 1),
    _SnmpEngineID_Type()
)
snmpEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineID.setStatus("current")


class _SnmpEngineBoots_Type(Integer32):
    """Custom type snmpEngineBoots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnmpEngineBoots_Type.__name__ = "Integer32"
_SnmpEngineBoots_Object = MibScalar
snmpEngineBoots = _SnmpEngineBoots_Object(
    (1, 3, 6, 1, 6, 3, 10, 2, 1, 2),
    _SnmpEngineBoots_Type()
)
snmpEngineBoots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineBoots.setStatus("current")


class _SnmpEngineTime_Type(Integer32):
    """Custom type snmpEngineTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SnmpEngineTime_Type.__name__ = "Integer32"
_SnmpEngineTime_Object = MibScalar
snmpEngineTime = _SnmpEngineTime_Object(
    (1, 3, 6, 1, 6, 3, 10, 2, 1, 3),
    _SnmpEngineTime_Type()
)
snmpEngineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineTime.setStatus("current")
if mibBuilder.loadTexts:
    snmpEngineTime.setUnits("seconds")


class _SnmpEngineMaxMessageSize_Type(Integer32):
    """Custom type snmpEngineMaxMessageSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 2147483647),
    )


_SnmpEngineMaxMessageSize_Type.__name__ = "Integer32"
_SnmpEngineMaxMessageSize_Object = MibScalar
snmpEngineMaxMessageSize = _SnmpEngineMaxMessageSize_Object(
    (1, 3, 6, 1, 6, 3, 10, 2, 1, 4),
    _SnmpEngineMaxMessageSize_Type()
)
snmpEngineMaxMessageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpEngineMaxMessageSize.setStatus("current")
_SnmpFrameworkMIBConformance_ObjectIdentity = ObjectIdentity
snmpFrameworkMIBConformance = _SnmpFrameworkMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 3)
)
_SnmpFrameworkMIBCompliances_ObjectIdentity = ObjectIdentity
snmpFrameworkMIBCompliances = _SnmpFrameworkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 3, 1)
)
_SnmpFrameworkMIBGroups_ObjectIdentity = ObjectIdentity
snmpFrameworkMIBGroups = _SnmpFrameworkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 6, 3, 10, 3, 2)
)

# Managed Objects groups

snmpEngineGroup = ObjectGroup(
    (1, 3, 6, 1, 6, 3, 10, 3, 2, 1)
)
snmpEngineGroup.setObjects(
      *(("SNMP-FRAMEWORK-MIB", "snmpEngineID"),
        ("SNMP-FRAMEWORK-MIB", "snmpEngineBoots"),
        ("SNMP-FRAMEWORK-MIB", "snmpEngineTime"),
        ("SNMP-FRAMEWORK-MIB", "snmpEngineMaxMessageSize"))
)
if mibBuilder.loadTexts:
    snmpEngineGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpFrameworkMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 10, 3, 1, 1)
)
snmpFrameworkMIBCompliance.setObjects(
    ("SNMP-FRAMEWORK-MIB", "snmpEngineGroup")
)
if mibBuilder.loadTexts:
    snmpFrameworkMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-FRAMEWORK-MIB",
    **{"SnmpEngineID": SnmpEngineID,
       "SnmpSecurityModel": SnmpSecurityModel,
       "SnmpMessageProcessingModel": SnmpMessageProcessingModel,
       "SnmpSecurityLevel": SnmpSecurityLevel,
       "SnmpAdminString": SnmpAdminString,
       "snmpFrameworkMIB": snmpFrameworkMIB,
       "snmpFrameworkAdmin": snmpFrameworkAdmin,
       "snmpAuthProtocols": snmpAuthProtocols,
       "snmpPrivProtocols": snmpPrivProtocols,
       "snmpFrameworkMIBObjects": snmpFrameworkMIBObjects,
       "snmpEngine": snmpEngine,
       "snmpEngineID": snmpEngineID,
       "snmpEngineBoots": snmpEngineBoots,
       "snmpEngineTime": snmpEngineTime,
       "snmpEngineMaxMessageSize": snmpEngineMaxMessageSize,
       "snmpFrameworkMIBConformance": snmpFrameworkMIBConformance,
       "snmpFrameworkMIBCompliances": snmpFrameworkMIBCompliances,
       "snmpFrameworkMIBCompliance": snmpFrameworkMIBCompliance,
       "snmpFrameworkMIBGroups": snmpFrameworkMIBGroups,
       "snmpEngineGroup": snmpEngineGroup}
)
