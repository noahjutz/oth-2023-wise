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
