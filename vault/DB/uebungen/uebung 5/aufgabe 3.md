# 1
Die Videos (id und name), die das Schlagwort 'lustig' haben.

# 2
Die Schlagworte, die zu videos gehören, welche vom Genre entweder 'Musik' oder 'Musikvideo sind'.
In eigenen Worten: Alle Schlagworte, die in Musikvideos erwähnt werden

# 3
```
s = pi schlagworte (
	sigma vnr=3517 (
		videos join schlagworte
	)
)

v = pi titel (
	videos join s
)

v \ (
	pi titel (
		sigma vnr=3517 (videos)
	)
)
```
Zusammen:
```
pi titel (
	videos join (
		pi schlagworte (
			sigma vnr=3517 (
				videos join schlagworte
			)
		)
	)
) \ (
	pi titel (
		sigma vnr=3517 (
			videos
		)
	)
)
```
