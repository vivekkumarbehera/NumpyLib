import numpy as np
rng = np.random.default_rng(seed=142)
a = rng.integers(10, 100, size=(3, 4))
print(a)
#choice
b = rng.choice(a.flatten(), size=5, replace=False)
print(b)
#shuffle
rng.shuffle(a, axis=0)  # Shuffle rows
print(a)
rng.shuffle(a, axis=1)  # Shuffle columns
print(a)
#permutation
c = rng.permutation(a.flatten())
print(c)
#random
d = rng.random((2, 3))
print(d)
#normal
e = rng.normal(loc=0.0, scale=1.0, size=(2, 3))
print(e)
#uniform
f = rng.uniform(low=0.0, high=1.0, size=(2, 3))
print(f)
