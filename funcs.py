from fritzconnection import FritzConnection
from cred import USER, PASS


def get_ip_data():
    fc = FritzConnection(address="192.168.178.1", user=USER, password=PASS)
    status = fc.call_action("WANIPConn1", "GetStatusInfo")["NewConnectionStatus"]
    uptime = fc.call_action("WANIPConn1", "GetStatusInfo")["NewUptime"]
    try:
        address = fc.call_action("WANIPConn1", "GetExternalIPAddress")["NewExternalIPAddress"]
    except IndexError:
        address = "0.0.0.0"
    upstream = fc.call_action("WANCommonInterfaceConfig", "GetCommonLinkProperties")[
        "NewX_AVM-DE_UpstreamCurrentUtilization"].split(",")[0]
    downstream = fc.call_action("WANCommonInterfaceConfig", "GetCommonLinkProperties")[
        "NewX_AVM-DE_DownstreamCurrentUtilization"].split(",")[0]
    ip_dict = {"status": status, "uptime": uptime, "address": address, "upstream": upstream, "downstream": downstream}
    return ip_dict
