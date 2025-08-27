from funcs import get_ip_data
import psycopg2
from cred import *

ip_data = get_ip_data()

db_conn = psycopg2.connect(host="192.168.178.117", user=DB_USER, password=DB_PASS, database="network")
cursor = db_conn.cursor()
statement = f"INSERT INTO {TABLE} (status, uptime, ipaddr, upstream, downstream) VALUES ('{ip_data['status']}', {ip_data['uptime']}, '{ip_data['address']}', {ip_data['upstream']}, {ip_data['downstream']})"
cursor.execute(statement)
db_conn.commit()