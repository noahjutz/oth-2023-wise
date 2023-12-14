$$
a_{n+1} := \frac{1}{2}\big(
	a_n+\frac{x_0}{a_n}
\big), n \in \mathbb{N}, x_0 \ge 0
$$

$$
a_1 > \sqrt{x_0}
$$

# Behauptung
$$
\text{z.z.: } \forall n \in \mathbb{N}: a_n > \sqrt{x_0}
$$

# Beweis
## IA ($n = 1$)
$$
a_1 \stackrel{\text{Def.}}{>} \sqrt{x_0} \ \checkmark
$$

## IS ($n \to n+1$)
$$
\text{z.z.: } a_n > \sqrt{x_0} \implies a_{n+1} > \sqrt{x_0}
$$

$$
\begin{alignat*}{3}
	&\quad&a_{n+1} &> \sqrt{x_0} &\quad& \\
 
	\stackrel{\text{Def.}}{\iff} &&
	\frac{1}{2} \Big(
		a_n+\frac{x_0}{a_n}
	\Big) &>
	\sqrt{x_0} \\

	\iff &&
	\frac{1}{2} \Big(
		a_n+\frac{x_0}{a_n}
	\Big) &>
	\underbrace{
		\sqrt{
			a_n \cdot \frac{x_0}{a_n}
		}
	}_{=\sqrt{x_0}} \\

	\stackrel{\text{1.9}}{\impliedby} &\quad \rlap{
		\frac{1}{2}(a+b) \ge \sqrt{ab} \quad \wedge \quad
		\text{LS} \neq \text{RS, da } a_n \neq \frac{x_0}{a_n} \text{, da }
	} \\

	&\quad \rlap{
		a_n = \frac{x_0}{a_n}
		\iff a_n^2 = x_0
		\iff a_n = \sqrt{x_0} \ \unicode{x21af} \ \text{(IV)}
		\ \blacksquare
	}
\end{alignat*}
$$

# Latex align testing
## split
$$
\begin{split}
a = b &= c \\
&=d = b \\
c = a = z
\end{split}
\begin{split}
x = c &= b \\
&= a \\
a
\end{split}
$$

## multiline
$$
\begin{multline}
a = b + c + d + e + f + g + h + i + b + c + d + e + f + g + h + i \\ + b + c + d + e + f + g + h + i + b + c + d + e + f + g + h + i
\end{multline}
$$

$$
\begin{multline}
	a = a + b \\
	\shoveleft{b = c} \\
	\shoveright{c = d} \\
	d = e
\end{multline}
$$

## gather & split
$$
\begin{gather*}
	\text{first} = \text{equation} \\
	\begin{split}
		\text{second} &= \text{equation} \\
		&= \text{on two lines}
	\end{split}
	\\
	\text{third} = \text{equation}
\end{gather*}
$$

## align
$$
\begin{align*}
x&=y & X&=Y & a&=b+c\\
x’&=y’ & X’&=Y’ & a’&=b\\
x+x’&=y+y’ & X+X’&=Y+Y’ & a’b&=c’b
\end{align*}
$$

$$
\begin{align*}
x& = y_1-y_2+y_3-y_5+y_8-\dots
&& \text{by \eqref{eq:C}}\\
& = y’\circ y^* && \text{by \eqref{eq:D}}\\
& = y(0) y’ && \text {by Axiom 1.}
\end{align*}
$$

## alignat
$$
\begin{alignat*}{2}
x& = y_1-y_2+y_3-y_5+y_8-\dots
&& \text{by \eqref{eq:C}}\\
& = y’\circ y^* && \text{by \eqref{eq:D}}\\
& = y(0) y’ && \text {by Axiom 1.}
\end{alignat*}
$$

## flalign
$$
\begin{flalign}
x&=y & X&=Y\\
x’&=y’ & X’&=Y’\\
x+x’&=y+y’ & X+X’&=Y+Y’
\end{flalign}
$$

## examples
$$
\begin{equation}
	\left.
	\begin{aligned}
		B’&=-\partial\times E,\\
		E’&=\partial\times B - 4\pi j,
	\end{aligned}
	\right\}
	\ \text{Maxwell’s equations}
\end{equation}
$$

$$
\left\|
\begin{gather*}
asd \\
def \\
bcd
\end{gather*}
\right\}
$$

[Further Reading](https://www.ams.org/arc/tex/amsmath/amsldoc.pdf)