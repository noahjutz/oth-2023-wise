# Pseudocode

- `lo`: lower bound index of (sub)list, inclusive
- `hi`: upper bound index of (sub)list, inclusive
```
quicksort(items, lo, hi):
	if lo >= hi:
		return items

	pivot_index = partition(items, lo, hi)
	quicksort(items, lo, pivot_index - 1)
	quicksort(items, pivot_index + 1, hi)
```
```
partition(items, lo, hi):
	pivot_index = hi
	pivot = items[pivot_index]
	j = -1
	for i in lo until hi:
		if items[i] <= pivot:
			j += 1
			swap items[i] with items[j]

	new_pivot_index = j + 1
	swap items[new_pivot_index] with items[pivot_index]
	return new_pivot_index
```
