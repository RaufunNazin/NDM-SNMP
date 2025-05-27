public class SnmpOID
{
	private static String ifName = "1.3.6.1.2.1.31.1.1.1.1";


	public static String getIfName(String vendor){
		if(vendor.equals("VSOL")) return "1.3.6.1.4.1.37950.1.1.5.12.2.1.14.1.2";
		if(vendor.equals("DBC")) return "1.3.6.1.4.1.37950.1.1.5.12.2.1.14.1.2";
		else return ifName;
	}
	public static String getIfStatus(String vendor){
		if(vendor.equals("Huwaei")) return ".1.3.6.1.4.1.2011.6.128.1.1.2.46.1.15";
		else if(vendor.equals("BDCOM")) return ".1.3.6.1.4.1.3320.101.10.1.1.26";//"IF-MIB::ifOperStatus";
		else if(vendor.equals("CDATA"))  return "1.3.6.1.4.1.34592.1.5.1.1.2.19.5.1.1"; //gponOnuEthPortStatusInfo
		else if(vendor.equals("VSOL-GPON")) return "1.3.6.1.4.1.37950.1.1.6.1.1.1.1.4"; // 1 = OK, 2 = disable/off
		else return "";
	}

/*
SNMPv2-SMI::enterprises.37950.1.1.6.1.1.1.1.4.1.1 = INTEGER: 1
SNMPv2-SMI::enterprises.37950.1.1.6.1.1.1.1.4.1.2 = INTEGER: 2
SNMPv2-SMI::enterprises.37950.1.1.6.1.1.1.1.4.1.3 = INTEGER: 1
SNMPv2-SMI::enterprises.37950.1.1.6.1.1.1.1.4.1.4 = INTEGER: 2
SNMPv2-SMI::enterprises.37950.1.1.6.1.1.1.1.4.1.5 = INTEGER: 1
*/
	public static String getIfAdminStatus(String vendor){
		if(vendor.equals("Huwaei")) return ".1.3.6.1.4.1.2011.6.128.1.1.2.46.1.15";
		else if(vendor.equals("BDCOM")) return "IF-MIB::ifAdminStatus";
		else return "";
	}

	public static String getRxPower(String vendor){
		if(vendor.equals("Huwaei")) return ".1.3.6.1.4.1.2011.6.128.1.1.2.51.1.4";
		else if(vendor.equals("BDCOM")) return ".1.3.6.1.4.1.3320.101.10.5.1.5";
		else if(vendor.equals("DBC")) return "1.3.6.1.4.1.37950.1.1.5.12.2.1.14.1.3"; /* High Speed VSOL midel 1600D ...  RxPower */
		else if(vendor.equals("VSOL")) return "1.3.6.1.4.1.37950.1.1.5.12.2.1.8.1.7";
		else if(vendor.equals("CDATA")) return "1.3.6.1.4.1.34592.1.5.1.1.2.18.6.1.4";
		else if(vendor.equals("VSOL-GPON")) return "1.3.6.1.4.1.37950.1.1.6.1.1.3.1.7"; //37950.1.1.6.1.1.3.1.7.1.1 = STRING: "-14.41"
		else return "";
	}

	public static String getTxPower(String vendor){
		if(vendor.equals("Huwaei")) return ".1.3.6.1.4.1.2011.6.128.1.1.2.51.1.4";
		else if(vendor.equals("BDCOM")) return ".1.3.6.1.4.1.3320.101.10.5.1.6";
		else return "";
	}

	public static String getOnuMac(String vendor){

		if(vendor.equals("BDCOM")) return " 1.3.6.1.4.1.3320.101.10.1.1.3";
		else if(vendor.equals("DBC")) return "1.3.6.1.4.1.37950.1.1.5.12.1.12.1.6";
		else if(vendor.equals("VSOL")) return "1.3.6.1.4.1.37950.1.1.5.10.3.2.1.3";
		else if(vendor.equals("VSOL-GPON")) return "1.3.6.1.4.1.37950.1.1.5.12.1.12.1.6";
		else if(vendor.equals("CDATA")) return "1.3.6.1.4.1.34592.1.5.1.1.2.19.3.1.2";
		//if(vendor.equals("Huwaei")) return ".1.3.6.1.4.1.2011.6.128.1.1.2.51.1.4";
		else return "";
	}

	public static String getIfDescr(String vendor){
		if(vendor.equals("Huwaei")) return ".1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9";
		else if(vendor.equals("BDCOM")) return "1.3.6.1.2.1.31.1.1.1.1"; //"IF-MIB::ifAlias";
		else if(vendor.equals("VSOL")) return "1.3.6.1.4.1.37950.1.1.5.12.2.1.14.1.2";
		else if(vendor.equals("VSOL-GPON")) return "1.3.6.1.4.1.37950.1.1.6.1.1.4.1.24";
		else if(vendor.equals("DBC")) return "1.3.6.1.4.1.37950.1.1.5.12.2.1.14.1.2";
		else if(vendor.equals("CDATA")) return "";
		else return "";
	}

}