#!/usr/bin/python
#!/usr/bin/python
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi
def topology(remote_controller):
 "Create a network."
 net = Mininet_wifi()
  
 info("*** Adding stations/hosts\n")
 h1a = net.addHost("h1a", ip="192.0.2.1/24")
 h2a = net.addHost("h2a", ip="192.0.2.2/24")
 h1b = net.addHost("h1b", ip="203.0.113.1/24")
 h2b = net.addHost("h2b", ip="203.0.113.2/24")
 h1c = net.addHost("h1c", ip="198.51.100.1/24")
 h2c = net.addHost("h2c", ip="198.51.100.2/24")
 h1d = net.addHost("h1d", ip="192.168.10.1/24")
 h2d = net.addHost("h2d", ip="192.168.10.2/24")

 roteador1 = net.addHost("roteador1")
 roteador2 = net.addHost("roteador2")
 roteador3 = net.addHost("roteador3")
 roteador4 = net.addHost("roteador4")
 roteador5 = net.addHost("roteador5")
 roteador6 = net.addHost("roteador6")
 roteador7 = net.addHost("roteador7")
 roteador8 = net.addHost("roteador8")
 roteador9 = net.addHost("roteador9")
 roteador10 = net.addHost("roteador10")
 roteador11 = net.addHost("roteador11")
  
 info("*** Adding P4Switches (core)\n")
 switch1 = net.addSwitch("switch1")
 switch2 = net.addSwitch("switch2")
 switch3 = net.addSwitch("switch3")
 switch4 = net.addSwitch("switch4")

 info("*** Creating links\n")
 info("*** Switch Roteador 1\n")
 net.addLink(h1a, switch1, bw=1000)
 net.addLink(h2a, switch1, bw=1000)

 info("*** Switch Roteador 2\n")
 net.addLink(h1b, switch2, bw=1000)
 net.addLink(h2b, switch2, bw=1000)

 info("*** Switch Roteador 3\n")
 net.addLink(h1c, switch3, bw=1000)
 net.addLink(h2c, switch3, bw=1000)

 info("*** Switch Roteador 4\n")
 net.addLink(h1d, switch4, bw=1000)
 net.addLink(h2d, switch4, bw=1000)
  
 net.addLink(roteador1, switch1, bw=1000) #r1 eth0
 net.addLink(roteador11, switch2, bw=1000) #r11 eth0
 net.addLink(roteador7, switch3, bw=1000) #r7 eth0
 net.addLink(roteador7, switch4, bw=1000) #r7 eth1
 net.addLink(roteador1, roteador2, bw=1000) #r1 eth1 e r2 eth0
 net.addLink(roteador1, roteador3, bw=1000) #r1 eth2 e r3 eth0
 net.addLink(roteador2, roteador4, bw=1000) #r2 eth1 e r4 eth0
 net.addLink(roteador3, roteador4, bw=1000) #r3 eth1 e r4 eth1
 net.addLink(roteador5, roteador4, bw=1000) #r5 eth0 e r4 eth2
 net.addLink(roteador5, roteador6, bw=1000) #r5 eth1 e r6 eth0
 net.addLink(roteador5, roteador8, bw=1000) #r5 eth2 e r8 eth0
 net.addLink(roteador6, roteador11, bw=1000) #r6 eth1 e r11 eth1
 net.addLink(roteador6, roteador9, bw=1000) #r6 eth2 e r9 eth0
 net.addLink(roteador7, roteador8, bw=1000) #r7 eth2 e r8 eth1
 net.addLink(roteador8, roteador10, bw=1000) #r8 eth2 e r10 eth0
 net.addLink(roteador8, roteador9, bw=1000) #r8 eth3 e r9 eth1
 net.addLink(roteador9, roteador10, bw=1000) #r9 eth2 e r10 eth1
 net.addLink(roteador10, roteador11, bw=1000) #r10 eth2 e r11 eth2
  
 info("*** Starting network\n")
 net.start()
 net.staticArp()

 info("*** Applying switches configurations\n")
 switch1.cmd(
 'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switch1.name))
 switch2.cmd(
 'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switch2.name))
 switch3.cmd(
 'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switch3.name))
 switch4.cmd(
 'ovs-ofctl add-flow {} "actions=output:NORMAL"'.format(switch4.name))
  
 info("*** Applying hosts and routers configurations\n")
 roteador1.cmd("ifconfig roteador1-eth0 192.0.2.254/24")
 roteador1.cmd("ifconfig roteador1-eth1 10.10.100.1/30")
 roteador1.cmd("ifconfig roteador1-eth2 10.10.100.13/30")
 roteador2.cmd("ifconfig roteador2-eth0 10.10.100.2/30")
 roteador2.cmd("ifconfig roteador2-eth1 10.10.100.5/30")
 roteador3.cmd("ifconfig roteador3-eth0 10.10.100.14/30")
 roteador3.cmd("ifconfig roteador3-eth1 10.10.100.9/30")
 roteador4.cmd("ifconfig roteador4-eth0 10.10.100.6/30")
 roteador4.cmd("ifconfig roteador4-eth1 10.10.100.10/30")
 roteador4.cmd("ifconfig roteador4-eth2 10.10.100.17/30")
 roteador5.cmd("ifconfig roteador5-eth0 10.10.100.18/30")
 roteador5.cmd("ifconfig roteador5-eth1 10.10.200.5/30")
 roteador5.cmd("ifconfig roteador5-eth2 10.10.200.1/30")
 roteador6.cmd("ifconfig roteador6-eth0 10.10.200.6/30")
 roteador6.cmd("ifconfig roteador6-eth1 10.10.201.1/30")
 roteador6.cmd("ifconfig roteador6-eth2 10.10.202.9/30")
 roteador7.cmd("ifconfig roteador7-eth0 198.51.100.254/24")
 roteador7.cmd("ifconfig roteador7-eth1 192.168.10.254/24")
 roteador7.cmd("ifconfig roteador7-eth2 10.10.200.9/30")
 roteador8.cmd("ifconfig roteador8-eth0 10.10.200.2/30")
 roteador8.cmd("ifconfig roteador8-eth1 10.10.200.10/30")
 roteador8.cmd("ifconfig roteador8-eth2 10.10.206.1/30")
 roteador8.cmd("ifconfig roteador8-eth3 10.10.202.5/30")
 roteador9.cmd("ifconfig roteador9-eth0 10.10.202.10/30")
 roteador9.cmd("ifconfig roteador9-eth1 10.10.202.6/30")
 roteador9.cmd("ifconfig roteador9-eth2 10.10.201.9/30")
 roteador10.cmd("ifconfig roteador10-eth0 10.10.206.2/30")
 roteador10.cmd("ifconfig roteador10-eth1 10.10.201.10/30")
 roteador10.cmd("ifconfig roteador10-eth2 10.10.201.5/30")
 roteador11.cmd("ifconfig roteador11-eth0 203.0.113.254/24")
 roteador11.cmd("ifconfig roteador11-eth1 10.10.201.2/30")
 roteador11.cmd("ifconfig roteador11-eth2 10.10.201.6/30")
 h1a.cmd("ip route add default via 192.0.2.254")
 h2a.cmd("ip route add default via 192.0.2.254")
 h1b.cmd("ip route add default via 203.0.113.254")
 h2b.cmd("ip route add default via 203.0.113.254")
 h1c.cmd("ip route add default via 198.51.100.254")
 h2c.cmd("ip route add default via 198.51.100.254")
 h1d.cmd("ip route add default via 192.168.10.254")
 h2d.cmd("ip route add default via 192.168.10.254")
 roteador1.cmd("ip route add 203.0.113.0/24 via 10.10.100.2")
 roteador1.cmd("ip route add 198.51.100.0/24 via 10.10.100.14")
 roteador1.cmd("ip route add 192.168.10.0/24 via 10.10.100.14")
 roteador2.cmd("ip route add 192.0.2.0/24 via 10.10.100.1")
 roteador2.cmd("ip route add 203.0.113.0/24 via 10.10.100.6")
 roteador2.cmd("ip route add 198.51.100.0/24 via 10.10.100.6")
 roteador2.cmd("ip route add 192.168.10.0/24 via 10.10.100.6")
 roteador3.cmd("ip route add 192.0.2.0/24 via 10.10.100.13")
 roteador3.cmd("ip route add 203.0.113.0/24 via 10.10.100.10")
 roteador3.cmd("ip route add 198.51.100.0/24 via 10.10.100.10")
 roteador3.cmd("ip route add 192.168.10.0/24 via 10.10.100.10")
 roteador4.cmd("ip route add 192.0.2.0/24 via 10.10.100.5")
 roteador4.cmd("ip route add 203.0.113.0/24 via 10.10.100.18")
 roteador4.cmd("ip route add 198.51.100.0/24 via 10.10.100.18")
 roteador4.cmd("ip route add 192.168.10.0/24 via 10.10.100.18")
 roteador5.cmd("ip route add 192.0.2.0/24 via 10.10.100.17")
 roteador5.cmd("ip route add 203.0.113.0/24 via 10.10.200.6")
 roteador5.cmd("ip route add 198.51.100.0/24 via 10.10.200.2")
 roteador5.cmd("ip route add 192.168.10.0/24 via 10.10.200.2")
 roteador6.cmd("ip route add 192.0.2.0/24 via 10.10.200.5")
 roteador6.cmd("ip route add 203.0.113.0/24 via 10.10.201.2")
 roteador6.cmd("ip route add 198.51.100.0/24 via 10.10.202.10")
 roteador6.cmd("ip route add 192.168.10.0/24 via 10.10.202.10")
 roteador7.cmd("ip route add 192.0.2.0/24 via 10.10.200.10")
 roteador7.cmd("ip route add 203.0.113.0/24 via 10.10.200.10")
 roteador8.cmd("ip route add 192.0.2.0/24 via 10.10.200.1")
 roteador8.cmd("ip route add 203.0.113.0/24 via 10.10.202.6")
 roteador8.cmd("ip route add 198.51.100.0/24 via 10.10.200.9")
 roteador8.cmd("ip route add 192.168.10.0/24 via 10.10.200.9")
 roteador9.cmd("ip route add 192.0.2.0/24 via 10.10.202.9")
 roteador9.cmd("ip route add 203.0.113.0/24 via 10.10.202.9")
 roteador9.cmd("ip route add 198.51.100.0/24 via 10.10.202.5")
 roteador9.cmd("ip route add 192.168.10.0/24 via 10.10.202.5")
 roteador10.cmd("ip route add 192.0.2.0/24 via 10.10.201.9")
 roteador10.cmd("ip route add 203.0.113.0/24 via 10.10.201.6")
 roteador10.cmd("ip route add 198.51.100.0/24 via 10.10.206.1")
 roteador10.cmd("ip route add 192.168.10.0/24 via 10.10.206.1")
 roteador11.cmd("ip route add 192.0.2.0/24 via 10.10.201.1")
 roteador11.cmd("ip route add 198.51.100.0/24 via 10.10.201.5")
 roteador11.cmd("ip route add 192.168.10.0/24 via 10.10.201.5")
 info("*** Running CLI\n")
 CLI(net)
 info("*** Stopping network\n")
 net.stop()
if __name__ == "__main__":
 setLogLevel("info")
 remote_controller = False
 topology(remote_controller)
