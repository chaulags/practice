import wmi
def check():
    pass


def ip():
    print("Its Static")
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration()
    # First network adaptor
    nic = nic_configs[2]
    print(nic)
    ip = u'192.168.6.5' # Chanage the ip you want in your adapter
    subnetmask = u'255.255.255.248' # Chanage the subnet you want in your adapter
    gateway = u'192.168.6.1' # Chanage the ip gateway you want in your adapter
    nic.EnableStatic(IPAddress=[ip], SubnetMask=[subnetmask])
    nic.SetGateways(DefaultIPGateway=[gateway])
def dhcp():
    print("Its DHCP")
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration()
    nic = nic_configs[2]
    print(nic)
    changed = nic.EnableDHCP()
    print(changed)

input = int(input("Enable Static or DHCP ? 1/2 >> "))
if input == 1:
    ip()
elif input == 2:
    dhcp()
else:
    print("Invalid Options")