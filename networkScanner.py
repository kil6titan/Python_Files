import nmap
ns = nmap.PortScanner()

print(ns.nmap_version())
ns.scan("192.168.1.1","22-445",'-v --version-all')
#print(ns.scaninfo())
#print(ns.csv())
hostlist = ns.all_hosts()
print(hostlist)

i = 0
for host in hostlist:
    i += 1
    protocols = ns[host].all_protocols()
    print(str(i) + "." + str(host) + "-----\t" + ns[host].state() + "-----\t" + str(protocols) + '\n')
    for protocol in protocols:
        showServices = ns[host][protocol].keys()
        print(showServices)



