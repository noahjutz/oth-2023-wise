
> [!info] Slow Start
> ![[slow start.png|400]]

- Rundreisezeit: l = 10ms
- Empfangsfenster: S = 24KB
- MSS: s = 2KB

# Round-Trip-Anzahl

| Round-Trip | Segmente | KB |
| ---- | ---- | ---- |
| 0 | $2^0$ | 2 |
| 1 | $2^1$ | 4 |
| 2 | $2^2$ | 8 |
| 3 | $2^3$ | 16 |

$$
\begin{align*}
	\sum_{k=0}^n 2^k \cdot s &\ge S \\
	s \cdot \frac{1-2^{n+1}}{1-2} &\ge S \\
	-1+2^{n+1} &\ge \frac{S}{s} \\
	2^{n+1} &\ge \frac{S}{s} + 1 \\
	2^n &\ge \frac{1}{2} \cdot \left( \frac{S}{s} + 1 \right) \\
	n &\ge \log_2 \left(
		\frac{1}{2} \cdot \frac{S}{s} + \frac{1}{2} 
	\right) \\
	n &\ge \log_2 6.5 \\
	n &\ge 2.7
\end{align*}
$$

n ist mindestens 3, also sind die Round-Trips 0, 1, 2 und 3 notwendig.

# Zeit

$$
t = l \cdot (\lceil n \rceil + 1) = 4 \cdot 10 \text{ms} = 40 \text{ms}
$$