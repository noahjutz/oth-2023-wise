# Gegeben
## Zugewiesener Adressbereich
```
137.23.0.0/21
```

## Anzahl Rechner
|Abteilung|Rechner|
|-|-|
|A|100|
|B|50|
|C|100|
|D|300|
|E|1000|

# Bearbeitung
## Adressbereich in Binär
```
10001111.00010111.00000000.00000000
^^^^^^^^ ^^^^^^^^ ^^^^^
```

## Subnetze
### A
$$
\begin{gather*}
	\left\lceil \log_2 100\right\rceil = 7 \\

	\implies \mathtt{
			\underbrace{
				10001111.00010111.00000
				\textcolor{red}{XXX}
				.
				\textcolor{red}{X}
			}_{
				\text{Netz-ID}
			}
			\underbrace{
				0000000
			}_\text{
				Host-ID
			}
		}
\end{gather*}
$$

### B
$$
\begin{gather*}
	\left\lceil \log_2 50\right\rceil = 6 \\

	\implies \mathtt{
			\underbrace{
				10001111.00010111.00000
				\textcolor{red}{XXX}
				.
				\textcolor{red}{XX}
			}_{
				\text{Netz-ID}
			}
			\underbrace{
				000000
			}_\text{
				Host-ID
			}
		}
\end{gather*}
$$


### C
$$
\begin{gather*}
	\left\lceil \log_2 100\right\rceil = 7 \\

	\implies \mathtt{
			\underbrace{
				10001111.00010111.00000
				\textcolor{red}{XXX}
				.
				\textcolor{red}{X}
			}_{
				\text{Netz-ID}
			}
			\underbrace{
				0000000
			}_\text{
				Host-ID
			}
		}
\end{gather*}
$$

### D
$$
\begin{gather*}
	\left\lceil \log_2 300\right\rceil = 9 \\
 
	\implies \mathtt{
			\underbrace{
				10001111.00010111.00000
				\textcolor{red}{XX}
			}_{
				\text{Netz-ID}
			}
			\underbrace{
				0.00000000
			}_\text{
				Host-ID
			}
		}
	\end{gather*}
$$

### E
$$
\begin{gather*}
	\left\lceil \log_2 1000 \right\rceil = 10 \\
 
	\implies \mathtt{
		\underbrace{
			10001111.00010111.00000
			\textcolor{red}{X}
		}_{
			\text{Netz-ID}
		}
		\underbrace{
			00.00000000
		}_\text{
			Host-ID
		}
	}
\end{gather*}
$$

> [!NOTE] Zusammenfassung
> $$
> \begin{align*}
> 	A&&\mathtt{
> 		10001111.00010111.00000
> 		\textcolor{red}{XXX}
> 		.\!
> 		\textcolor{red}{X}
> 		0000000
> 	} \\
> 
> 	B&&\mathtt{
> 		10001111.00010111.00000
> 		\textcolor{red}{XXX}
> 		.\!
> 		\textcolor{red}{XX}
> 		000000
> 	} \\
> 
> 	C&&\mathtt{
> 		10001111.00010111.00000
> 		\textcolor{red}{XXX}
> 		.\!
> 		\textcolor{red}{X}
> 		0000000
> 	} \\
> 
> 	D&&\mathtt{
> 		10001111.00010111.00000
> 		\textcolor{red}{XX}
> 		0.00000000
> 	} \\
> 
> 	E&&\mathtt{
> 		10001111.00010111.00000
> 		\textcolor{red}{X}
> 		00.00000000
> 	}
> \end{align*}
> $$

## Auswahl
$$
\begin{align*}
	A&&\mathtt{
		\textcolor{grey}{10001111.00010111.00000}
		\textcolor{red}{000}
		\textcolor{grey}{.}\!
		\textcolor{red}{1}
		\textcolor{grey}{0000000}
	} \\

	B&&\mathtt{
		\textcolor{grey}{10001111.00010111.00000}
		\textcolor{red}{000}
		\textcolor{grey}{.}\!
		\textcolor{red}{01}
		\textcolor{grey}{000000}
	} \\

	C&&\mathtt{
		\textcolor{grey}{10001111.00010111.00000}
		\textcolor{red}{001}
		\textcolor{grey}{.}\!
		\textcolor{red}{0}
		\textcolor{grey}{0000000}
	} \\

	D&&\mathtt{
		\textcolor{grey}{10001111.00010111.00000}
		\textcolor{red}{01}
		\textcolor{grey}{0.00000000}
	} \\

	E&&\mathtt{
		\textcolor{grey}{10001111.00010111.00000}
		\textcolor{red}{0}
		\textcolor{grey}{00.00000000}
	} \\

	\\

	\text{Übrig}&&\mathtt{
		\textcolor{grey}{10001111.00010111.00000}
		1
		\textcolor{grey}{XX.\!XXXXXXXX}
	} \\

	&&\mathtt{
		\textcolor{grey}{10001111.00010111.00000}
		011
		\textcolor{grey}{.\!XXXXXXXX}
	} \\

	&&\mathtt{
		\textcolor{grey}{10001111.00010111.00000}
		010
		\textcolor{grey}{.}\!
		1
		\textcolor{grey}{XXXXXXX}
	} \\

	&&\mathtt{...}
\end{align*}
$$

# Antwort
|Subnetz|Netz-ID|Interface-IDs|Broadcast|
|-|-|-|-|
|A|137.32.0.128/25|137.32.0.129 - 137.32.0.254|137.32.0.255|
|B|137.32.0.64/26|137.32.0.65 - 137.32.0.126|137.32.0.127|
|C|137.32.1.0/25|137.32.1.1 - 137.32.1.126|137.32.1.127|
|D|137.32.2.0/23|137.32.2.1 - 137.32.3.254|137.32.3.255|
|E|137.32.0.0/22|137.32.0.1 - 137.32.3.254|137.32.3.255|

# Netzwerk-Plan
```mermaid
graph TD
X((X))
A((A))
B((B))
C((C))
D((D))
E((E))
  
A---|137.32.0.128|X
B---|137.32.0.64|X
  
X---|137.32.1.0|C
X---|137.32.2.0|D
X---|137.32.0.0|E
```
