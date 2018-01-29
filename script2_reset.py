import paramiko
import time

ip_address = "198.18.134.140"
username = "admin"
password = "C1sco12345"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("no int loop 0\n")
remote_connection.send("no int loop 1\n")
remote_connection.send("cdp timer 60\n")
remote_connection.send("no vlan 2-10\n")
remote_connection.send("hostname nxosv-1\n")

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close
