$$
\forall x \in \left[
	0; \frac{\pi}{2}
\right] : \sin(x) + \cos(x) \le \sqrt 2
$$

# Beweis

Finde das globale Minimum in $f(x) = \sin x + \cos x$  mit $D = \left[0;\frac{\pi}{2}\right]$.

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
