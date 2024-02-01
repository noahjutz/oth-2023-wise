# Formeln/Gesetze
## Binomische Formeln

$$
(a+b)(a-b) = a^2 - b^2
$$

$$
\begin{align*}
	(a+b)^2 &= a^2 + 2ab + b^2 \\
	(a-b)^2 &= a^2 - 2ab + b^2 \\
	
	(a+b)^3 &= a^3 + 3a^2b + 3ab^2 + b^3 \\
	(a-b)^3 &= a^3 - 3a^2b + 3ab^2 - b^3 \\
	
	(a+b)^4 &= a^4 + 4a^3b + 6a^2b^2 + 4ab^3 + b^4 \\
	(a-b)^4 &= a^4 - 4a^3b + 6a^2b^2 - 4ab^3 + b^4 \\
	
	(a+b)^5 &= a^5 + 5a^4b + 10a^3b^2 + 10a^2b^3 + 5ab^4 + b^5 \\
	(a-b)^5 &= a^5 - 5a^4b + 10a^3b^2 - 10a^2b^3 + 5ab^4 - b^5 \\
	
	(a+b)^6 &= a^6 + 6a^5b + 15a^4b^2 + 20a^3b^3 + 15a^2b^4 + 6ab^5 + b^6 \\
	(a-b)^6 &= a^6 - 6a^5b + 15a^4b^2 - 20a^3b^3 + 15a^2b^4 - 6ab^5 + b^6
\end{align*}
$$

## Mitternachtsformel

$$
x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2a}
$$

## Potenzgesetze

$$
\begin{gather*}
	\frac{x^a}{x^b} = x^{a-b} \\
	x^a \cdot x^b = x^{a+b} \\
	x^{-\frac{m}{n}} = \frac{1}{\sqrt[n]{x^m}} \\
	(x^a)^b = x^{a \cdot b}
\end{gather*}
$$

# Wertetabelle

| $x$ | $x!$ | $2^x$ |
| ---- | ---- | ---- |
| 0 | 1 | 1 |
| 1 | 1 | 2 |
| 2 | 2 | 4 |
| 3 | 6 | 8 |
| 4 | 24 | 16 |
| 5 | 120 | 32 |
| 6 | 720 | 64 |
| 7 | 5 040 | 128 |
| 8 | 40 320 | 256 |
| 9 | 362 880 | 512 |
| 10 | 3 628 800 | 1024 |
| 11 | 39 916 800 | 2048 |
| 12 | 479 001 600 | 4096 |
| 13 | 6 227 020 800 | 8192 |

# Injektiv, Surjektiv, Bijektiv

|Eigenschaft|Folgerung|
|-|-|
|Injektiv|$\forall f(x)=y:y$ hat höchstens einen Wert|
|Surjektiv|$\forall f(x)=y:y$ hat mindestens einen Wert|
|Bijektiv |$\forall f(x)=y:y$ hat genau einen Wert|

# Ableitungen

$$
\textcolor{blue}{x^x}
\to x^x \cdot (\ln x + 1)
\to x^x \cdot \left(\frac{1}{x} + (\ln x + 1)^2\right)
$$

$$
x \ln x
\to \ln x + 1 
\to \textcolor{blue}{\frac{1}{x}}
\to -x^{-2}
\to 2 x^{-3}
\to -6 x^{-4}
$$

$$
\frac{8}{105} x^\frac{7}{2}
\to \frac{4}{15} x^\frac{5}{2}
\to \frac{2}{3} x^\frac{3}{2}
\to \textcolor{blue}{\sqrt x}
\to \frac{1}{2} x^{-\frac{1}{2}}
\to -\frac{1}{4} x^{-\frac{3}{2}}
\to \frac{3}{8} x^{-\frac{5}{2}}
\to \frac{15}{16} x^{-\frac{7}{2}}
$$

$$
\frac{1}{720} x^6
\to \frac{1}{120} x^5
\to \frac{1}{24} x^4
\to \frac{1}{6} x^3
\to \frac{1}{2} x^2
\to \textcolor{blue}{x}
\to 1
\to 0
$$

$$
\textcolor{blue}{e^{-x}} \to -e^{-x} \to e^{-x} \to \ldots
$$

$$
\frac{1}{k^3} e^{kx}
\to \frac{1}{k^2} e^{kx} 
\to \frac{1}{k} e^{kx} 
\to e^{kx}
\to ke^{kx}
\to k^2e^{kx}
\to k^3e^{kx}
$$

# Geradengleichung

$$
y = m \cdot (x-\Delta x) + \Delta y
$$

# Geometrie

| Figur | Fläche A | Umfang U |
| ---- | ---- | ---- |
| Kreis | $\pi r^2$ | $2 \pi r$ |
| Kreisring | $\pi (R^2-r^2)$ | $2 \pi (R+r)$ |

| Körper | Volumen V | Oberfläche O |
| ---- | ---- | ---- |
| Kugel | $\frac{4}{3} \pi r^3$ | $4 \pi r^2$ |
| Zylinder | $\pi r^2 h$ | $2 \pi r \cdot (r+h)$ |
| Hohlzylinder | $\pi R^2 h - \pi r^2 h$ | $2 \pi ((R+r)h+R^2-r^2)$ |

# Arithm. und Geom. Mittel

Allgemeines arithmetisches Mittel:

$$
\overline X = \frac{1}{n} \cdot \sum_{k=0}^n a_k
$$

Allgemeines geometrisches Mittel:

$$
\overline X = \sqrt[n]{\prod_{k=0}^n a_k}
$$

# Dreieckszahl

$$
\sum_{k=1}^n k = \frac{n(n+1)}{2}
$$

# Logarithmische Integration

$$
\int \frac{f'(x)}{f(x)} \,dx = \ln |f(x)| +C
$$

# Gauß-Verfahren

1. Die am weitesten links stehende von 0 verschiedene Spalte ist die Pivot-Spalte
2. Pivot-Element in dieser Spalte wählen und nach oben **vertauschen**
3. **Ersetze** Zahlen unter Pivot-Element mit Nullen
4. Decke oberste Zeile zu, führe Schritt 1-3 mit übriger Matrix durch
5. Pivot-Elemente von rechts nach links durch **skalieren** auf 1 bringen
6. Erzeuge Nullen über den Pivot-Elementen

- Ersetzen: Die Zeile wird mit einem Vielfachen einer anderen Zeile summiert.
- Skalieren: Die Zeile wird mit einem Faktor multipliziert
- Vertauschen: Zwei Zeilen werden vertauscht