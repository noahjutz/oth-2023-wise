# Zu zeigen

$$
\forall x \in \left[
	0; \frac{\pi}{2}
\right] : \sin(x) + \cos(x) \le \sqrt 2
$$

# Beweis

Finde das globale Maximum in $f(x) = \sin x + \cos x$  mit $D = \left[0;\frac{\pi}{2}\right]$.

![[aufgabe 2 funktion.svg|300]]

## 1 Funktion bestimmen

gegeben.

## 2 Variablen eliminieren

gegeben.

## 3 Definitionsbereich angeben

gegeben.

## 4 Funktion ableiten

$$
f'(x) = \cos x - \sin x
$$

## 5 Nullstellen der Ableitung

$$
\begin{align*}
	f'(x) &= 0 \\

	\cos x - \sin x &= 0 \\

	\cos x &= \sin x \\

	\cos x &= \cos(x-\frac{\pi}{2}) \\

	x &= x - \frac{\pi}{2} \\

	0 &= -\frac{\pi}{2} \text{⚡}
\end{align*}
$$
$\implies f'$  hat keine Nullstellen

> [!fail] Falsch

$$
\begin{align*}
	f'(x) &= 0 \\
	\cos x - \sin x &= 0 \\
	\cos x &= \sin x \\
	\frac{\cos x}{\cos x} &=  \frac{\sin x}{\cos x} \\
	1 &= \tan x \\

	\arctan 1 &= x \\

	\underline{\frac{\pi}{4}} &= x
\end{align*}
$$

$\implies$ es gibt einen Extrempunkt oder Terassenpunkt in $x = \frac{\pi}{4}$.

> [!check] Richtig

## 6 Liegt im Definitionsbereich?

$$
\frac{\pi}{4} \in D = \left[0;\frac{\pi}{2}\right] \ \checkmark
$$

## 7 Bestimmung des globalen Maximums

es kommen in frage:

- $x_0 = \frac{\pi}{4}$
- $x_0 = 0$
- $x_0 = \frac{\pi}{2}$

$$
f\left(\frac{\pi}{4}\right) = \sin \frac{\pi}{4} + \cos \frac{\pi}{4} = \sqrt 2
$$

$$
f\left(\frac{\pi}{2}\right) = \sin \frac{\pi}{2} + \cos \frac{\pi}{2} = 1
$$

$$
f(0) = \sin 0 + \cos 0 = 1
$$

$\implies$ $x_0 = \frac{\pi}{4}$ ist ein globales strenges Maximum in $D$.

> [!info] 4.21, 4.22 Extrema
> - **Relativ/Lokal:** $\forall x \in \mathcal{U}_\delta$
> 	- **Generell:** $f(x_0) \ge f(x)$
> 	- **Streng/Isoliert:** $f(x_0) > f(x)$
> - **Global/Isoliert**: $\forall x \in D$
> 	- **Generell:** $f(x_0) \ge f(x)$
> 	- **Streng/Isoliert:** Gibt es das?

# 8 Antwortsatz

da $x_0 = \frac{\pi}{2}$ das globale Maximum in $D$ ist, gibt es kein $x \in D$, das größer als $x_0$ ist. Es gilt also für alle $x \in D$, dass $f(x) \le x_0 = \sqrt 2$. $\blacksquare$
