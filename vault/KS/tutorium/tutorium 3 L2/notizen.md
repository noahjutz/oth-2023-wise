# Scapy

https://scapy.net/

![[scapy.png]]

## Ethernet-Parameter anzeigen

```
ls(Ether)
```

## Ethernet-II-Paket erstellen

```
a=Ether()
a.src="00:02:03:04:05:06"
a.dst="01:02:03:04:05:06"
a.type=0x8888
data="Diese Payload ist 46 Buchstaben bzw Bytes lang"
```

## Paket anschauen

```
>>> a
<Ether  dst=01:02:03:04:05:06 src=01:02:03:04:05:06 type=0x8888 |>
```

## Paket senden

```
sendp(a/data)
```
