# SNMP MIB module (RFC1155-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/RFC1155-SMI
# Produced by pysmi-1.6.1 at Tue May  6 18:12:45 2025
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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class ObjectName(ObjectIdentifier):
    """Custom type ObjectName based on ObjectIdentifier"""




class IpAddress(OctetString):
    """Custom type IpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4





class Counter(Integer32):
    """Custom type Counter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class Gauge(Integer32):
    """Custom type Gauge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class TimeTicks(Integer32):
    """Custom type TimeTicks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )





class Opaque(OctetString):
    """Custom type Opaque based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1155-SMI",
    **{"ObjectName": ObjectName,
       "IpAddress": IpAddress,
       "Counter": Counter,
       "Gauge": Gauge,
       "TimeTicks": TimeTicks,
       "Opaque": Opaque,
       "internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises}
)
