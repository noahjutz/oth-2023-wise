[[2_layer2.pdf#page=30|Stop and Wait]]

# Definitionen
## Bitrate
[[1_layer1.pdf#page=32]]
$$
R := \frac{N}{t}
$$

## Auslastung
$$
r := \frac{R_\text{eff}}{R} \checkmark \ge \frac{1}{2} = \frac{2\text{kbps}}{4\text{kbps}}
$$

# Zahlen
Bitrate $R = 4 \text{kbps}$
Latenz $l = 20 \text{ms}$
Auslastung $r \ge \frac{1}{2}$
Bestätigungsgröße: Vernachlässigbar (1bit)
Framegröße $N = \ ?$

# Bearbeitung
$$
\fbox{Sender}
\left.
\begin{gather*}
\xrightarrow[\text{20ms}]{N_f\ \text{bit}}\\

\xleftarrow[\text{20ms}]{1\ \text{bit}}
\end{gather*}
\right.
\fbox{Empfänger}
$$

## Wenn $r = 1$
$$
\begin{align*}
	N &= R \cdot
		\underbrace{\frac{1}{2}}_{\text{Hälfte für Acks}} \cdot
		\frac{l}{1000}\text{ms} \\
	  
	&= 4\text{kbps} \cdot
		\frac{1}{2} \cdot
		\frac{20}{1000}\text{ms} \\
	
	&= 0.04 \ \text{kbit}
\end{align*}
$$

## Allgemein ($r \ge \frac{1}{2}$)
$$
\begin{align*}
	N &= r \cdot
		R \cdot
		\frac{1}{2} \cdot
		\frac{l}{1000}\text{ms} \\
  
	&\ge \frac{1}{2} \cdot
		4\text{kbps} \cdot
		\frac{1}{2} \cdot
		\frac{20}{1000}\text{ms} \\

	&= \underline{0.2\text{kbit}}
\end{align*}
$$

> [!danger] Falsch

# Lösung
- Framegröße $N =: x$
- Auslastung $r =: E = 0.5$
- Latenz $l = 20\text{ms}$
- Bitrate $R = 4\text{kbps}$
$$
\fbox{Sender}
\left.
\begin{gather*}
	t_1\xrightarrow[t_2-t_1]{N_f\ \text{bit}} \\
	
	t_3 \xleftarrow[t_3-t_2]{1\ \text{bit}}
\end{gather*}
\right.
t_2 \ \fbox{Empfänger}
$$
- Gesamtzeit $t = t_3 - t_1$
- Verzögerungszeit $l = 20\text{ms}$
- $t_2-t_1 = l + \frac{x}{R} = 20\text{ms} + \frac{x\text{ kb}}{4\text{ kbps}}$
- $t_3-t_2 = l = 20\text{ms}$ (Annahme: Sendezeit Ack vernachlässigbar)
- $t_3-t_1 = (t_3-t_2) + (t_2-t_1) = 20\text{ms} + 20\text{ms} + \frac{x}{4\text{kbps}}$
- $R_\text{eff} = \frac{x}{t_3-t_1}$
- $E = \frac{R_\text{eff}}{R} = \frac{\frac{x}{t_3-t_1}}{4\text{kbps}}$

$$
\begin{align*}
	&&E &= 0.5 \\
 
	&\iff& \frac{R_\text{eff}}{R} &= 0.5 \\
 
	&\iff& \frac{\frac{x}{t_3-t_1}}{4\text{kbps}} &= 0.5 \\
 
	&\iff& \frac{
		\frac{x}{40\text{ms}+\frac{x}{4\text{kbps}}}
	}{
		4\text{kbps}
	} &= 0.5 \\

	&\iff& \frac{
		x
	}{
		4\text{kbps} \cdot (
			40\text{ms} + \frac{x}{4\text{kbps}}
		)
	} &= 0.5 \\

	&\iff& \frac{
		x
	}{
		4\text{kbps} \cdot 40\text{ms} + x
	} &= 0.5 \\

	&\iff& x &= 0.5 \cdot (
		4\text{kbps} \cdot 40\text{ms} + x
	) \\
 
	&\iff& 2x &= 4\text{kbps} \cdot 40\text{ms} + x \\
 
	&\iff& x &= 4\text{kbps} \cdot 40\text{ms} \\

	&&&=160 \left[ \text{kbps} \cdot \text{ms} \right] \\

	&&&= 160 \left[\text{bps} \cdot \text{s} \right] \\

	&&&= 160 \left[ \frac{\text{bit}}{\text{s}} \cdot \text{s} \right] \\

	&&&= \underline{160 \text{bit}}
\end{align*}
$$
