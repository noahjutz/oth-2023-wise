# 1
$$
|\pi_{\text{vnr}}\text{(Schlagworte)}| = 50.000.000
$$

# 2
$$
\begin{align*}
	|\sigma_{\text{genre='Musik'}\vee\text{genre='Musikvideo'}}\text{(Videos)}|
	
	&= \frac{2}{20} \cdot |\text{Videos}| \\

	&= \frac{1}{10} \cdot 100.000.000 \\

	&= 10.000.000
\end{align*}
$$

# 3
$$
\begin{align*}
	|
		\sigma_{
			\text{genre='Musik'}\wedge\text{sprache='Deutsch'}}\text{(Videos)
		}
	|

	&= \frac{1}{20} \cdot \frac{1}{25} \cdot |\text{Videos}| \\

	&= \frac{1}{500} \cdot 100.000.000 \\

	&= 200.000
\end{align*}
$$

# 4
$$
\begin{align*}
	|
		\text{Videos}\bowtie_\text{
			Videos.vnr=Schlagworte.vnr
		}
		\text{Schlagworte}
	|

	&= |\text{Schlagworte}| \\
 
	&= 400.000.000
\end{align*}
$$

# 5
$$
\begin{align*}
	&|
		\pi_\text{
			vnr, titel
		} \sigma_\text{
			Schlagworte.schlagwort='lusting'
		} (
			\text{Videos} \bowtie_\text{
				Videos.vnr=Schlagworte.vnr
			}
			\text{Schlagworte}
		)
	| \\

	&\stackrel{4}{=} |
		\pi_\text{
			vnr, titel
		} \sigma_\text{
			Schlagworte.schlagwort='lusting'
		} (
			\underbrace{V'}_{
				|V'| = |\text{Schlagworte}|
			}
		)
	| \\

	&= |
		\pi_\text{vnr, titel} (
			\underbrace{V''}_{
				|V''| = \frac{1}{400} \cdot |\text{Schlagworte}|
			}
		)
	| \\

	&= |
		\pi_\text{vnr} (
			V''
		)
	| \\

	&= |V''| \\

	&= \frac{1}{400} \cdot |\text{Schlagworte}| \\

	&= \frac{1}{400} \cdot 400.000.000 \\

	&= 1.000.000
\end{align*}
$$


