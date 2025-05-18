from enums import MAC, OPERATION_STATUS, ADMIN_STATUS, DISTANCE, UP_SINCE, VENDOR, MODEL, SERIAL_NO, POWER, CDATA_EPON, CDATA_GPON

oid_dictionary = {
    MAC: {
        CDATA_EPON: '1.3.6.1.4.1.17409.2.3.4.1.1.7',
        CDATA_GPON: '1.3.6.1.4.1.17409.2.8.4.6.1.1.2'
    },
    OPERATION_STATUS: {
        CDATA_EPON: '1.3.6.1.4.1.17409.2.3.4.1.1.8',
        CDATA_GPON: '1.3.6.1.4.1.17409.2.8.4.1.1.7'
    },
    ADMIN_STATUS: {
        CDATA_EPON: '1.3.6.1.4.1.17409.2.3.4.1.1.9',
        CDATA_GPON: '1.3.6.1.4.1.17409.2.8.4.1.1.8'
    },
    DISTANCE: {
        CDATA_EPON: '1.3.6.1.4.1.17409.2.3.4.1.1.15',
        CDATA_GPON: '1.3.6.1.4.1.17409.2.8.4.1.1.9.16779546'
    },
    UP_SINCE: {
        CDATA_EPON: '1.3.6.1.4.1.17409.2.3.4.1.1.18',
        CDATA_GPON: '1.3.6.1.4.1.17409.2.8.4.1.1.12'
    },
    VENDOR: {
        CDATA_EPON: '1.3.6.1.4.1.17409.2.3.4.1.1.25',
        CDATA_GPON: '1.3.6.1.4.1.17409.2.8.4.1.1.5'
    },
    MODEL: {
        CDATA_EPON: '1.3.6.1.4.1.17409.2.3.4.1.1.26',
        CDATA_GPON: '1.3.6.1.4.1.17409.2.8.4.1.1.6'
    },
    SERIAL_NO: {
        CDATA_EPON: '1.3.6.1.4.1.17409.2.3.4.1.1.28',
        CDATA_GPON: '1.3.6.1.4.1.17409.2.8.4.1.1.3'
    },
    POWER: {
        CDATA_EPON: '1.3.6.1.4.1.17409.2.3.4.2.1.4',
        CDATA_GPON: '1.3.6.1.4.1.17409.2.8.4.4.1.4'
    } 
}

IFDESCR = '1.3.6.1.2.1.2.2.1.2'