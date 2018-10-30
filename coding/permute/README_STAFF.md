# Staff

Solution: stari_otn!ptgni

```Python
import itertools as iter

gen = iter.permutations("starting_point!")

for i, x in enumerate(gen):
    print(i, "".join(x))
```
