import paramiko
import time

ip_address = "198.18.134.140"
username = "admin"
password = "C1sco12345"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Resetting Configuration on", ip_address

remote_connection = ssh_client.invoke_shell()

reset_config = ["configure terminal",
                "no interface loopback 0",
                "no interface loopback 1",
                "cdp timer 60",
                "no vlan 2-10",
                "hostname nxosv-1",
                "end"]

for line in reset_config:
    line=line.strip()
    print line
    remote_connection.send(line + "\n")
    time.sleep(0.5)

output = remote_connection.recv(65535)
ssh_client.close
