# Aufgabe
Warum ist die CRC am Ende (Trailer) und nicht am Anfang (Header)?

# Antwort A
Die CRC kann somit vom Empfänger schon während dem Empfang des Pakets berechnet werden.
> [!danger] Nicht ganz richtig
> Dafür müsste die CRC am Anfang sein. Sowieso wäre der Vorteil unerheblich, weil die Prüfsumme des empfangenen Pakets berechnet werden muss. Dafür muss man in jedem Fall auf das gesamte Paket warten.

# Antwort B
Die CRC kann auch vom Sender schon während dem Senden berechnet werden. $\checkmark$
> [!success] Richtig
