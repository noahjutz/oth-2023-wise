# a

Auf **L2** ist ein Ethernet-Frame, das im Datenblock den IP-Header (**L3**) enthält. Der IP-Header enthält in seinem Datenblock ein UDP Datagram bzw. ein TCP Segment (**L4**).

Das Internet Protokoll auf **L3** fragmentiert Daten aus **L4**, sodass die MTU (Maximum Transmission Unit) auf **L2** eingehalten werden kann. 

Es führt auch IP-Addressen ein, welche durch die IANA (IANA $\to$ RIRs $\to$ ISPs $\to$ Kunde) vergeben werden. Dadurch können Hosts addressiert werden.

# b

| OSI | TCIP/IP | Name | Protokolle |
| ---- | ---- | ---- | ---- |
| 7 | Application<br>Anwendung | Application Layer<br>Anwendungsschicht | HTTP, SMTP, SSH |
| 6 | Application<br>Anwendung | Presentation Layer<br>Darstellungsschicht |  |
| 5 | Application<br>Anwendung | Session Layer<br>Sitzungsschicht |  |
| 4 | Transport | Transport Layer<br>Transportschicht | UDP/TCP |
| 3 | Internet | Network Layer<br>Vermittlungsschicht | IP |
| 2 | Network Access<br>Netzzugriff | Data Link Layer<br>Sicherungsschicht | IEEE 802.3 |
| 1 | Network Access<br>Netzzugriff | Physical Layer<br>Bitübertragungsschicht |  |

# c

Segment 1 (PC $\to$ Switch)

| Device | Ethernet-Frame | IP-Header | Device |
| ---- | ---- | ---- | ---- |
| Src (PC) | 00:50:56:8A:76:0D | 192.168.1.3 | Src (PC) |
| Dst (Router) | 00:40:5F:8A:76:1E | 10.1.1.3 | Dst (Server) |

Segment 2 (Switch $\to$ Router)

| Device | Ethernet-Frame | IP-Header | Device |
| ---- | ---- | ---- | ---- |
| Src (PC) | 00:50:56:8A:76:0D | 192.168.1.3 | Src (PC) |
| Dst (Router) | 00:40:5F:8A:76:1E | 10.1.1.3 | Dst (Server) |

Segment 3 (Router $\to$ Server)

| Device | Ethernet-Frame | IP-Header | Device |
| ---- | ---- | ---- | ---- |
| Src (Router) | 02:43:AF:89:56:2D | 192.168.1.3 | Src (PC) |
| Dst (Server) | 1E:2A:11:A0:43:A1 | 10.1.1.3 | Dst (Server) |

Die IP-Addressen bleiben immer gleich. Die MAC-Addressen bleiben in einem Subnetz gleich.