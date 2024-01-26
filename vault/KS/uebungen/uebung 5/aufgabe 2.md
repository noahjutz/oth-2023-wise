# a

- TCP ist verbindungsorientiert, völlig zuverlässig, Point-to-Point und gewährleistet Flow-Control und Congestion-Avoidance.
- UDP ist verbindungslos, best-effort, Multicast-fähig, und stellt keine Flow-Control oder Congestion-Avoidance bereit.

# b

| Use-Case | Protokoll | Begründung |
| ---- | ---- | ---- |
| File Transfer | TCP | Die Datei soll intakt ankommen. |
| Real-time streaming | UDP | Einzelne frames dürfen verloren gehen, dafür ist es schneller. |
| Web browsing | TCP | HTTP baut auf TCP (bzw. QUIC) auf, da Webseiten korrekt angezeigt werden. |
| VoIP | UDP | Wie bei streaming, teile der Konversation dürfen, um Echtzeitkommunikation zu gewährleisten, verloren gehen. |

# c

Portnummern (16 bit unsigned integer) identifizieren Endgerätanwendungen wie Mail (IMAP, SMTP) oder Web-Browsing (HTTP). So können auf dem gleichen Gerät mehrere Dienste laufen. TCP und UDP bündeln so alle darüber liegende Anwendungen (L5) in eine Schicht (L4).
