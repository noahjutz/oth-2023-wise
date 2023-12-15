# a

1. Richtig, da man keine Teilmenge der Berechtigungen zurücknehmen kann.
2. Falsch, RESTRICT beeinflusst, **ob** REVOKE ausgeführt wird.
3. Falsch, da für Mehrbenutzeranomalien mehrere TAs notwendig sind
4. Falsch, da Lost Update **nie** auftreten kann.
5. Richtig, da das Phantomproblem auftritt, wenn die gleiche Query verschiedene Anzahlen an Rows gibt.

# b

6. Falsch

![[aufgabe 1b bild.png]]

# c

7. Richtig

|TA1|TA2|TA3|Sperren|
|-|-|-|-|
|$w_1(x)$|||$X_1(x)$|
||==wait ($w_2(x)$)==||$X_1(x)$|
||wait ($r_2(y)$)||$X_1(x)$|
|$r_1(y)$|||$X_1(x),S_1(y)$|
|||wait ($w_3(y)$)|$X_1(x),S_1(y)$|
|$c_1$||||
||$w_2(x)$||$X_2(x)$|
||$r_2(y)$||$X_2(x), S_2(y)$|
||$c_2$|||
|||$w_3(y)$|$X_3(y)$|
|||$c_3$||

