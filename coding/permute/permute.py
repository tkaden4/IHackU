import itertools as iter

SOL = "4882268 stari_otn!ptgni"

gen = iter.permutations("starting_point!")

for i, x in enumerate(gen):
    print(i, "".join(x))
