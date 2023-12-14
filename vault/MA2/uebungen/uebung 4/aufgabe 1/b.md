$$
\frac{p}{q} = 0.1230\overline{443}
$$

# Bearbeitung
$$
\begin{align*}
	0.1230\overline{443} &= 0.123 +
		0.\colorbox{lightblue}{$0000$}\colorbox{pink}{$443$} +
		0.\colorbox{lightblue}{$0000$}\colorbox{lightgray}{$000$}\colorbox{pink}{$443$} +
		0.\colorbox{lightblue}{$0000$}\colorbox{lightgray}{$000$}\colorbox{lightgray}{$000$}\colorbox{pink}{$443$} +
		\cdots \\

	&= 0.123 + \sum_{k=0}^{\infty} \colorbox{lightblue}{$0.0001$} \cdot
		\colorbox{lightgray}{$0.001^k$} \cdot
		\colorbox{pink}{$0.443$} \\

	&= 0.123 + 0.0001 \cdot 0.443 \cdot \sum_{k=0}^{\infty} 0.001^k \\

	&= 0.123 + 0.0000443 \cdot \frac{1}{1-0.001} \\

	&= 0.123 + \frac{0.0000443}{0.999} \\

	&= \frac{123}{1000} + \frac{443}{9990000} \\

	&= \frac{1228770}{9990000} + \frac{443}{9990000} \\

	&= \frac{1229213}{9990000} \\

	&\implies p=1229213,\ q=9990000
\end{align*}
$$
