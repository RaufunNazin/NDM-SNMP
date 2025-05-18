# snmp_session.py
from pysnmp.hlapi.v3arch.asyncio import *
from typing import Tuple

# Global cache for session components
_session_cache = {}

async def get_snmp_session(ip: str, port: int, community: str, version: int, timeout: int, retries: int) -> Tuple[SnmpEngine, CommunityData, UdpTransportTarget, ContextData]:
    key = f"{ip}:{port}:{community}:{version}"
    
    if key not in _session_cache:
        snmp_engine = SnmpEngine()
        community_data = CommunityData(community, mpModel=version)
        transport = await UdpTransportTarget.create((ip, port), timeout=timeout, retries=retries)
        context = ContextData()
        
        _session_cache[key] = (snmp_engine, community_data, transport, context)

    return _session_cache[key]
