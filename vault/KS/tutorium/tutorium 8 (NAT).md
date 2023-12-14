# 4

- DLink: Host -> Router  (Intranet)
- IntelPro: Router -> Internet (Internet)

## ping 194.95.109.166

|Device|IP|
|-|-|
|NAT Gateway|194.95.109.71|
|NAT Host|192.168.3.100|
|Default Gateway (Host)(?)|192.168.3.1|
|Ping target|194.95.109.166|

- ping id: 0x04B9 BE (0xB904 LE)
- ping sequence: 0x0044 BE (0x4400 LE)
	- decimal: 68
 
### Request (ID: 0x34ef)
- Request 192.168.3.100 -> 194.95.109.166 ==(DLink, Intranet)==
- Request 194.95.109.71 -> 194.95.109.166 ==(IntelPro, Internet)==

### Reply (ID: 0x5896)
- Reply 194.95.109.166 -> 194.95.109.71
- Reply 194.95.109.166 -> 192.168.3.100

## Display filter
```
(arp || icmp) && (ip.id == 0x34ef || ip.id == 0x5896)
```

## Kontrollfragen
Todo
