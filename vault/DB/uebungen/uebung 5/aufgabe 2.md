# Heuristiken zur Anfrageoptimierung
- Frühstmögliche Selektion
- Frühstmögliche Projektion
- Join statt Kreuzprodukt
- Join Reihenfolge

# Loesung

$$
\begin{align*}
	R &= \boxed{
		 \begin{gather*}
			\big(
				\pi_\text{schlagwort}
				\sigma_\text{genre='Musik'}
				\underbrace{
					\sigma_\text{Videos.vnr=Schlagworte.vnr} (
						\text{Videos} \times \text{Schlagworte}
					)
				}_\text{Join statt Kreuzprodukt}
			\big)
			\\\cup 
			\\\big(
				\pi_\text{schlagwort}
				\sigma_\text{genre='Musikvideo'}
				\underbrace{
					\sigma_\text{Videos.vnr=Schlagworte.vnr} (
						\text{Videos} \times \text{Schlagworte}
					)
				}_\text{Join statt Kreuzprodukt}
			\big)
	   \end{gather*}
	}

	\\ &= \boxed{
		\begin{gather*}
			\big(
				\pi_\text{schlagwort}
				\sigma_\text{genre='Musik'}
				\text{Videos} \bowtie_\text{Videos.vnr=Schlagworte.vnr} (
					\text{Schlagworte}
				)
			\big)
			\\\underbrace{\cup}_\text{Selektionen statt Mengenoperationen}
			\\\big(
				\pi_\text{schlagwort}
				\sigma_\text{genre='Musikvideo'}
				\text{Videos} \bowtie_\text{Videos.vnr=Schlagworte.vnr} (
					 \text{Schlagworte}
				)
			\big)
		\end{gather*}
	}

	\\ &= \boxed{
		\underbrace{
			\pi_\text{schlagwort}
			\sigma_{\text{genre='Musik'} \vee \text{genre='Musikvideo'}}
		}_\text{Fruehstmoegliche Selektion und Projektion} \big(
			\text{Videos} \bowtie_\text{Videos.vnr=Schlagworte.vnr} (
				\text{Schlagworte}
			)
		\big)
	}

	\\ &= \boxed{
		(
			\colorbox{pink} {$
				\pi_\text{vnr}
			$}
			\colorbox{yellow} {$
				\sigma_{\text{genre='Musik'} \wedge \text{genre='Musikvideo'}}
			$} \text{Videos}
		)
		\bowtie_\text{Videos.vnr=Schlagworte.vnr} (
			\colorbox{yellow} {$
				\pi_\text{schlagwort}
			$}
			\text{Schlagworte}
		)
	}
 
\end{align*}
$$

