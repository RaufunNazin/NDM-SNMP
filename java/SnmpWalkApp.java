//package com.maestro.snmp4j;

import java.io.IOException;
//import com.micmiu.snmp4j.demo1x.*;
import org.snmp4j.CommunityTarget;
import org.snmp4j.PDU;
import org.snmp4j.Snmp;
import org.snmp4j.TransportMapping;
import org.snmp4j.event.ResponseEvent;
import org.snmp4j.mp.SnmpConstants;
import org.snmp4j.smi.Address;
import org.snmp4j.smi.GenericAddress;
import org.snmp4j.smi.Integer32;
import org.snmp4j.smi.Null;
import org.snmp4j.smi.OID;
import org.snmp4j.smi.OctetString;
import org.snmp4j.smi.VariableBinding;
import org.snmp4j.transport.DefaultUdpTransportMapping;
import java.net.*;
import java.util.*;
import java.io.*;
import java.sql.*;

/**
 *
 * blog http://www.micmiu.com
 *
 * @author Michael

	javac -classpath ..\lib\ojdbc7.jar;..\lib\snmp4j-2.8.12.jar;. SnmpWalkApp.java

 */
public class SnmpWalkApp {

	public static final int DEFAULT_VERSION = SnmpConstants.version2c;
	public static final String DEFAULT_PROTOCOL = "udp";
	public static final int DEFAULT_PORT = 161;
	public static final long DEFAULT_TIMEOUT = 3 * 1000L;
	public static final int DEFAULT_RETRY = 3;

	static ConnectTest con = null;
	static java.sql.Statement  stmt = null;
	static Hashtable portHash = new Hashtable();

	public SnmpWalkApp(){
		add2index = 0;
	}
	/**
	 *
	 * @param ip
	 * @param community
	 * @return CommunityTarget
	 */
	public static CommunityTarget createDefault(String ip, String community, int sport) {
		Address address = GenericAddress.parse(DEFAULT_PROTOCOL + ":" + ip
				+ "/" + ""+(sport>0?sport:DEFAULT_PORT));
		CommunityTarget target = new CommunityTarget();
		target.setCommunity(new OctetString(community));
		target.setAddress(address);
		target.setVersion(DEFAULT_VERSION);
		target.setTimeout(DEFAULT_TIMEOUT); // milliseconds
		target.setRetries(DEFAULT_RETRY);
		return target;
	}

	/**
	 * @param ip
	 * @param community
	 * @param targetOid
	 */
	public static void snmpWalk_ifIndex(String ip, String community, String targetOid, int sw_id,String model) {

		CommunityTarget target = SnmpUtil.createDefault(ip, community);
		TransportMapping transport = null;
		Snmp snmp = null;
		try {
			transport = new DefaultUdpTransportMapping();
			snmp = new Snmp(transport);
			transport.listen();

			PDU pdu = new PDU();
			OID targetOID = new OID(targetOid);
			pdu.add(new VariableBinding(targetOID));
			//pdu.add(new VariableBinding(new OID(".1.3.6.1.2.1.1")));

			boolean finished = false;
			System.out.println("----> demo start <----");
			while (!finished) {
				VariableBinding vb = null;
				ResponseEvent respEvent = snmp.getNext(pdu, target);

				PDU response = respEvent.getResponse();

				if (null == response) {
					System.out.println("responsePDU == null");
					finished = true;
					break;
				} else {
					vb = response.get(0);
				}
				// check finish
				finished = checkWalkFinished(targetOID, pdu, vb);
				if (!finished) {

					System.out.println("==== walk each vlaue :");
					String value = vb.getVariable().toString();

					if(value.indexOf("Hex-STRING")>0){
						System.out.println(vb.getOid() + " ==  " + HexStrConver.testHex2Str(value));
					}else{
					System.out.println(vb.getOid() + " = " + vb.getVariable());

						if(vb.getOid().toString().indexOf(".")>0) {
							String dd[] = vb.getOid().toString().split("\\.");
							System.out.println(vb.getOid().toString() + " " +dd.length);
							String index = dd[dd.length-1];
							if(model.equals("BDCOM") && vb.getVariable().toString().indexOf(":")>0) {

							}
							else{
								String ins = "insert into switch_snmp_ports (id,sw_id,ifname,ifindex) values(switch_snmp_ports_sq.nextval,"+sw_id+",'"+vb.getVariable()+"',"+index+")";
								System.out.println(ins);
								try{
									stmt.executeUpdate(ins);
								}catch(Exception ert){
									System.out.println(ert.getMessage()+" "+vb.getVariable()+" "+index);
								}
							}
						}

					}

					// Set up the variable binding for the next entry.
					pdu.setRequestID(new Integer32(0));
					pdu.set(0, vb);
				} else {
					System.out.println("SNMP walk OID has finished.");
					snmp.close();
				}
			}
			System.out.println("----> demo end <----");
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("SNMP walk Exception: " + e);
		} finally {
			if (snmp != null) {
				try {
					snmp.close();
				} catch (IOException ex1) {
					snmp = null;
				}
			}
		}

	}


	//1.3.6.1.4.1.2011.6.128.1.1.2.43.1.3
	public static void snmpWalk_MAC(String ip, String community, String ifindex, int sw_id) {

		String targetOid = "1.3.6.1.4.1.2011.6.128.1.1.2.43.1.3."+ifindex;
		CommunityTarget target = SnmpUtil.createDefault(ip, community);
		TransportMapping transport = null;
		Snmp snmp = null;
		try {
			transport = new DefaultUdpTransportMapping();
			snmp = new Snmp(transport);
			transport.listen();

			PDU pdu = new PDU();
			OID targetOID = new OID(targetOid);
			pdu.add(new VariableBinding(targetOID));
			//pdu.add(new VariableBinding(new OID(".1.3.6.1.2.1.1")));

			boolean finished = false;
			System.out.println("----> demo start <----");
			while (!finished) {

				VariableBinding vb = null;
				ResponseEvent respEvent = snmp.getNext(pdu, target);

				PDU response = respEvent.getResponse();

				if (null == response) {
					System.out.println("responsePDU == null");
					finished = true;
					break;
				} else {
					vb = response.get(0);
				}

				System.out.println("vb = "+vb.toString());

				// check finish
				finished = checkWalkFinished(targetOID, pdu, vb);
				if (!finished) {
					boolean ismac = false;
					System.out.println("==== walk each vlaue :");
					String value = vb.getVariable().toString();
					System.out.println("value = "+value);
					if(value !=null){
						String dd[] = value.split(":");
						if(dd.length==8) ismac = true;
					}
					if(ismac || value.indexOf("Hex-STRING")>0){
						String mac = value;
						if(ismac==false) mac = HexStrConver.testHex2Str(value);
						//System.out.println("Hex-STRING>> "+vb.getOid() + " ==  " + mac + " = "+mac.length());
						if(mac != null && mac.length()==18){
							String ins = "insert into SWITCH_SNMP_ONU_PORTS (id,sw_id,mac) values(SWITCH_SNMP_ONU_PORTS_sq.nextval,"+sw_id+",'"+mac+"')";
							System.out.println(ins);
						}
					}else{
					System.out.println(vb.getOid() + " := " + vb.getVariable());
						if(vb.getOid().toString().indexOf(".")>0) {
							String dd[] = vb.getOid().toString().split("\\.");
							System.out.println(vb.getOid().toString() + " " +dd.length);
							String index = dd[dd.length-1];

						}

					}

					// Set up the variable binding for the next entry.
					pdu.setRequestID(new Integer32(0));
					pdu.set(0, vb);
				} else {
					System.out.println("SNMP walk OID has finished.");
					snmp.close();
				}
			}
			System.out.println("----> demo end <----");
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("SNMP walk Exception: " + e);
		} finally {
			if (snmp != null) {
				try {
					snmp.close();
				} catch (IOException ex1) {
					snmp = null;
				}
			}
		}

	}

	private static int add2index=0;

/*
SNMPv2-SMI::enterprises.37950.1.1.5.12.2.1.8.1.7.1.20 = STRING: "0.03 mW (-15.93 dBm)"
SNMPv2-SMI::enterprises.37950.1.1.5.12.2.1.8.1.7.1.21 = STRING: "0.03 mW (-15.23 dBm)"
SNMPv2-SMI::enterprises.37950.1.1.5.12.2.1.8.1.7.1.22 = STRING: "0.03 mW (-15.93 dBm)"
SNMPv2-SMI::enterprises.37950.1.1.5.12.2.1.8.1.7.1.23 = STRING: "0.02 mW (-16.50 dBm)"
SNMPv2-SMI::enterprises.37950.1.1.5.12.2.1.8.1.7.2.1 = STRING: "0.03 mW (-14.62 dBm)"
SNMPv2-SMI::enterprises.37950.1.1.5.12.2.1.8.1.7.2.2 = STRING: "0.03 mW (-14.70 dBm)"
SNMPv2-SMI::enterprises.37950.1.1.5.12.2.1.8.1.7.2.3 = STRING: "0.02 mW (-17.17 dBm)"

*/

	//.1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9
	public static boolean  snmpWalk_onu_detail(String ip, String community, String ifindex, int sw_id, String targetOid,String col_name, String model, int sport) {

		System.out.println("1 targetOid = "+targetOid);
		double max_index = 0;
		boolean vsol_epon_rxpower = false;
		if(targetOid.equals("1.3.6.1.4.1.37950.1.1.5.12.2.1.8.1.7")) vsol_epon_rxpower = true;
		/*String col_name = "";
		if( targetOid.equals(".1.3.6.1.4.1.2011.6.128.1.1.2.46.1.15")) col_name = "status";
		else if( targetOid.equals(".1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9")) col_name = "IFDESCR";
		else if( targetOid.equals(".1.3.6.1.4.1.2011.6.128.1.1.2.51.1.4")) col_name = "POWER";
		*/

		//IF-MIB::ifOperStatus.276 = INTEGER: up(1)
		//IF-MIB::ifOperStatus.284 = INTEGER: down(2)

		//targetOid = targetOid + "."+ifindex; // ".1.3.6.1.4.1.2011.6.128.1.1.2.43.1.9."+ifindex;
		if(ifindex.length()>0) targetOid = targetOid + "."+ifindex;

		CommunityTarget target = SnmpUtil.createDefault(ip,community);
		if(sport>0) target = SnmpUtil.createDefault(ip, ""+sport,community);
		TransportMapping transport = null;
		Snmp snmp = null;
		try {
			transport = new DefaultUdpTransportMapping();
			snmp = new Snmp(transport);
			transport.listen();

			PDU pdu = new PDU();
			OID targetOID = new OID(targetOid);
			pdu.add(new VariableBinding(targetOID));
			//pdu.add(new VariableBinding(new OID(".1.3.6.1.2.1.1")));

			boolean finished = false;
			System.out.println("----> demo start <---- "+col_name);
			while (!finished) {
				String portName="";
				VariableBinding vb = null;
				ResponseEvent respEvent = snmp.getNext(pdu, target);

				PDU response = respEvent.getResponse();
				System.out.println("1 response = "+response);

				if (null == response) {
					System.out.println("responsePDU == null "+ip+" "+sport+" "+community);
					finished = true;
					return false;
				} else {
					vb = response.get(0);
				}

				System.out.println("2 vb = "+vb.toString());

				// check finish
				finished = checkWalkFinished(targetOID, pdu, vb);
				if (!finished) {
					boolean ismac = false;
					System.out.println("==== walk each vlaue 1 :");
					String value = vb.getVariable().toString();
					if(value.indexOf("Hex-STRING")>0) ismac = true;
					System.out.println("value = "+value);
					if(value !=null){
						String dd[] = value.split(":");
						if(dd.length==6) ismac = true;
						else{
							dd = value.split(" ");
							if(dd.length==6) ismac = true;
						}
					}
					System.out.println("==== ismac :"+ismac+" "+value);
					if(ismac || value.indexOf("Hex-STRING")>0){
						String mac = value;
						if(ismac==false) mac = HexStrConver.testHex2Str(value);
						System.out.println("Hex-STRING>> "+vb.getOid() + " ==  " + mac + " = "+mac.length());
						mac = mac.toUpperCase();
						if(mac != null && mac.length()==17){



							String dd[] = vb.getOid().toString().split("\\.");
							System.out.println(vb.getOid().toString() + " " +dd.length);
							String index1 = dd[dd.length-1];
							int index = Integer.parseInt(index1);

							System.out.println("index="+index);

							if( (model.equals("VSOL")||model.equals("DBC") )  && col_name.equals("MAC") ) {
								System.out.println("1 add2index index="+index);
								index = index + add2index;
								System.out.println("2 add2index index="+index);
							}

							try{
								String ins = "insert into SWITCH_SNMP_ONU_PORTS (id,sw_id,ifindex,"+col_name+",udate) values(SWITCH_SNMP_ONU_PORTS_sq.nextval,"+sw_id+","+index+",'"+mac+"',sysdate)";
								System.out.println(ins);
								stmt.executeUpdate(ins);
							}
							catch(Exception ert){
								String emsg = ""+ert.getMessage();
								if(emsg.indexOf("unique constraint")>0){
									String up = "update SWITCH_SNMP_ONU_PORTS set "+col_name+"='"+mac+"', udate=sysdate where sw_id="+sw_id+" and ifindex="+index;
									System.out.println(up);
									stmt.executeUpdate(up);
								}
							}
						}

					}else{
						System.out.println("==== walk each vlaue else :");
						System.out.println(vb.getOid() + " := " + vb.getVariable());
						if(vb.getOid().toString().indexOf(".")>0) {
							String dd[] = vb.getOid().toString().split("\\.");
							System.out.println(vb.getOid().toString() + " " +dd.length);
							String index = dd[dd.length-1];
							System.out.println("index="+index);

							if(model.equals("VSOL-GPON")) {
								String index_0 = dd[dd.length-2];
								index = index_0+"."+index;
							}
							System.out.println(model+" index="+index);

							if(vsol_epon_rxpower){

								String index_0 = dd[dd.length-2];
								portName = index_0+":"+index;
							}

							//2147483647
							String myvalue = vb.getVariable().toString();

							if(model.equals("BDCOM") && col_name.equals("STATUS") ) {
								try {
									myvalue = ""+ (Integer.parseInt(myvalue)-2);
								}catch(Exception etry){}
							}
							else if((model.equals("VSOL")||model.equals("DBC")) && col_name.equals("MAC") ) {
								System.out.println("1 index="+index);
								index = index + add2index;
								System.out.println("2 index="+index);
							}
							else if((model.equals("VSOL")||model.equals("DBC")) && col_name.equals("IFDESCR") ) {
								if(add2index==0){
									add2index = Integer.parseInt(index);
									System.out.println("add2index="+add2index);
								}
								try {
									if(myvalue != null && myvalue.indexOf(" ")>0)
									myvalue = myvalue.substring(0,myvalue.indexOf(" "));
									if(myvalue.indexOf("ONU")>0){
										myvalue = myvalue.replace("ONU",":");
										if(myvalue.indexOf("EPON0")==0) myvalue = myvalue.replace("EPON0","EPON0/");
										else if(myvalue.indexOf("EPON1")==0) myvalue = myvalue.replace("EPON1","EPON1/");
										else if(myvalue.indexOf("EPON2")==0) myvalue = myvalue.replace("EPON2","EPON2/");
										else if(myvalue.indexOf("EPON3")==0) myvalue = myvalue.replace("EPON3","EPON3/");

									}
								}catch(Exception etry){}

										System.out.println(" -- > "+myvalue+" , "+index);
										portHash.put(myvalue,index);
							}
							else if( model.equals("VSOL-GPON") && col_name.equals("IFDESCR") ) {
								//SNMPv2-SMI::enterprises.37950.1.1.6.1.1.4.1.24.1.1 = STRING: "GPON0/1:1"
								System.out.println(" -- > "+myvalue+" , "+index);
								try {
									if(myvalue != null && myvalue.indexOf(" ")>0)
									myvalue = myvalue.substring(0,myvalue.indexOf(" "));
									if(myvalue.indexOf("ONU")>0){
										myvalue = myvalue.replace("ONU",":");
										if(myvalue.indexOf("EPON0")==0) myvalue = myvalue.replace("EPON0","EPON0/");
										else if(myvalue.indexOf("EPON1")==0) myvalue = myvalue.replace("EPON1","EPON1/");
										else if(myvalue.indexOf("EPON2")==0) myvalue = myvalue.replace("EPON2","EPON2/");
										else if(myvalue.indexOf("EPON3")==0) myvalue = myvalue.replace("EPON3","EPON3/");

									}
								}catch(Exception etry){}

										System.out.println(" -- > "+myvalue+" , "+index);
										portHash.put(myvalue,index);
							}

							if(col_name.equals("POWER") && (myvalue.equals("2147483647") ||  myvalue.equals("65535") )) myvalue="0";
							else if(col_name.equals("POWER") && model.equals("BDCOM")) {
								try {
									myvalue = ""+ (Long.parseLong(myvalue)/10.0);
								}catch(Exception etry){}
							}
							else if(vsol_epon_rxpower && col_name.equals("POWER") ){
								//SNMPv2-SMI::enterprises.37950.1.1.5.12.2.1.8.1.7.1.23 = STRING: "0.02 mW (-16.50 dBm)"
								//SNMPv2-SMI::enterprises.37950.1.1.5.12.2.1.8.1.7.2.4 = ""
								String pdata[] = myvalue.split(" ");
								String pow1 = "0";
								if(pdata.length>=3){
									pow1 = pdata[2];
									pow1 = pow1.replace("(","");
								}
								myvalue = pow1;



								//EPON0/8:32 -- index
								String port1 = "EPON0/"+portName;
								String act_index = "";
								try{ act_index = (String)portHash.get(port1); }catch(Exception ertyu){}
								System.out.println("--> pdata ="+port1+" = "+act_index+" = "+pow1);
								index = act_index;

							}


							if(  col_name.equals("STATUS") && Integer.parseInt(index) < max_index ) break;
							//else if( Integer.parseInt(index) > max_index && col_name.equals("STATUS") ) max_index = Integer.parseInt(index);
							else if( Double.parseDouble(index) > max_index && col_name.equals("STATUS") ) max_index = Double.parseDouble(index) ;

							try{
								String ins = "insert into SWITCH_SNMP_ONU_PORTS (id,sw_id,ifindex,"+col_name+",udate) values(SWITCH_SNMP_ONU_PORTS_sq.nextval,"+sw_id+","+index+",'"+myvalue+"',sysdate)";
								System.out.println(ins);
								stmt.executeUpdate(ins);
							}
							catch(Exception ert){
								String emsg = ""+ert.getMessage();
								if(emsg.indexOf("unique constraint")>0){
									String up = "update SWITCH_SNMP_ONU_PORTS set "+col_name+"='"+myvalue+"', udate=sysdate where sw_id="+sw_id+" and ifindex="+index;
									System.out.println(up);
									try{ stmt.executeUpdate(up); } catch(Exception ert2){}
								}
							}

						}

					}

					// Set up the variable binding for the next entry.
					pdu.setRequestID(new Integer32(0));
					pdu.set(0, vb);

				} else {
					System.out.println("SNMP walk OID has finished.");
					snmp.close();
				}
			}
			System.out.println("----> demo end <----");
			return true;
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("SNMP walk Exception: " + e);
		} finally {
			if (snmp != null) {
				try {
					snmp.close();
				} catch (IOException ex1) {
					snmp = null;
				}
			}
		}
		return true;

	}


	/**
	 * 1)responsePDU == null<br>
	 * 2)responsePDU.getErrorStatus() != 0<br>
	 * 3)responsePDU.get(0).getOid() == null<br>
	 * 4)responsePDU.get(0).getOid().size() < targetOID.size()<br>
	 * 5)targetOID.leftMostCompare(targetOID.size(),responsePDU.get(0).getOid())
	 * !=0<br>
	 * 6)Null.isExceptionSyntax(responsePDU.get(0).getVariable().getSyntax())<br>
	 * 7)responsePDU.get(0).getOid().compareTo(targetOID) <= 0<br>
	 *
	 * @param targetOID
	 * @param pdu
	 * @param vb
	 * @return
	 */
	private static boolean checkWalkFinished(OID targetOID, PDU pdu,
			VariableBinding vb) {
		boolean finished = false;
		if (pdu.getErrorStatus() != 0) {
			System.out.println("[true] responsePDU.getErrorStatus() != 0 ");
			System.out.println(pdu.getErrorStatusText());
			finished = true;
		} else if (vb.getOid() == null) {
			System.out.println("[true] vb.getOid() == null");
			finished = true;
		} else if (vb.getOid().size() < targetOID.size()) {
			System.out.println("[true] vb.getOid().size() < targetOID.size()");
			finished = true;
		} else if (targetOID.leftMostCompare(targetOID.size(), vb.getOid()) != 0) {
			System.out.println("[true] targetOID.leftMostCompare() != 0");
			finished = true;
		} else if (Null.isExceptionSyntax(vb.getVariable().getSyntax())) {
			System.out
					.println("[true] Null.isExceptionSyntax(vb.getVariable().getSyntax())");
			finished = true;
		} else if (vb.getOid().compareTo(targetOID) <= 0) {
			System.out.println("[true] Variable received is not "
					+ "lexicographic successor of requested " + "one:");
			System.out.println(vb.toString() + " <= " + targetOID);
			finished = true;
		}
		return finished;

	}

	/**
	 *
	 * @param args
	 */
	public static void main(String[] args) {

		int sport = 4145;
		ServerSocket serverSocket = null;
		try {
		  	serverSocket = new ServerSocket(sport,1,InetAddress.getByName("localhost"));
		} catch (IOException localIOException) {
			//System.out.println("Could not listen on port: "+sport);
			System.exit(-1);
		}

		Runtime.getRuntime().addShutdownHook(new Thread() {
			public void run() {
				con.close();
				System.out.println("Shutdown-Hook");
			}
		});

		String ip_or_name=null;
		if(args.length>0) ip_or_name = args[0];

		con  = new ConnectTest();
		stmt = con.connect();

		try{


			String sqry = "select * from switches where sw_type='OLT' and snmp is not null and brand in ('BDCOM','VSOL','DBC','VSOL-GPON')";
			//String sqry = "select * from switches where sw_type='OLT' and snmp is not null and brand in ('VSOL') ";//and id=45102";
			if(ip_or_name != null) sqry = "select * from switches where sw_type='OLT' and snmp is not null and brand in ('BDCOM','VSOL','DBC','VSOL-GPON') "+
				" and (ip='"+ip_or_name+"' or name='"+ip_or_name+"')";
			ResultSet rs = stmt.executeQuery(sqry);
			Vector v = new Vector();
			while(rs.next()){
				v.add(new String[]{rs.getString("id"),rs.getString("ip"),rs.getString("brand"),rs.getString("snmp"),rs.getString("snmp_port")});
			}


			SnmpWalkApp app = new SnmpWalkApp();
			for(int i=0; i<v.size();i++){

				String[] dd = (String[])v.elementAt(i);
				String ip = dd[1]; //"10.233.254.2";//"10.234.254.6";
				InetAddress inet = InetAddress.getByName(ip);

				System.out.println("Sending Ping Request to " + ip);
				if(inet.isReachable(5000)==false){
					System.out.println(ip+" is NOT reachable");
					continue;
				}


				String model = dd[2]; //model = "BDCOM";
				String community = dd[3]; //"InFObd2019";

				int swid = Integer.parseInt(dd[0]);//15026;
				int snmpport = Integer.parseInt(dd[4]);//15026;

				portHash = new Hashtable();
				//boolean bbb = app.snmpWalk_onu_detail(ip, community, "",swid,SnmpOID.getIfName(model),"IFDESCR",model,snmpport );
				boolean bbb = app.snmpWalk_onu_detail(ip, community, "",swid,SnmpOID.getIfDescr(model),"IFDESCR",model,snmpport );

				if(bbb)
				{
					app.snmpWalk_onu_detail(ip, community, "",swid,SnmpOID.getRxPower(model),"POWER",model,snmpport );
					app.snmpWalk_onu_detail(ip, community, "",swid,SnmpOID.getOnuMac(model),"MAC",model,snmpport );
					app.snmpWalk_onu_detail(ip, community, "",swid,SnmpOID.getIfStatus(model),"STATUS",model,snmpport );
					String up1 ="update switches set SNMP_SYSOBJECTID=null where id= "+swid;
					stmt.executeUpdate(up1);
				}
				else{
					String up1 ="update switches set SNMP_SYSOBJECTID='SNMP: no response' where id= "+swid;
					stmt.executeUpdate(up1);
				}
				app = new SnmpWalkApp();

			}

		} catch(Exception e) {
			System.out.println("ERROR: public class RuntimeCheck :"+e.getMessage());
			e.printStackTrace();
		} finally {
			con.close();
		}

		//System.out.println(""+HexStrConver.hexStringToBytes("07 B2 01 05 02 1E 2B 02 2B 06 00"));
	}



}
