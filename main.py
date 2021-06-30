import numpy as np
print('\n100 EXERCISE NUMPY')
print('\n\tExercise 30')

def generate():
    for x in range(10):
        yield x
Z = np.fromiter(generate(),dtype=float,count=-1)
print('\t',Z)

print('\n\tExercise 32')
A=np.random.random(10)
A.sort()
print('\t',A)

print('\n\tExercise 54')
class ArrayFuntion (np.ndarray) :
    def __new__(cls, array, name="no name"):
        obj = np.asarray(array).view(cls)
        obj.name = name
        return obj
    def __array_finalize__ (self, obj):
        if obj is None: return
        self.info = getattr(obj, 'name', "no name")
W = ArrayFuntion(np.arange(10),"range_10")
print(W.name)

print('\n\tExercise 58')
B=np.random.randint(0,10,(3,4,3,4))
sum=B.reshape(B.shape[:-2]+(-1,)).sum(axis=-1)
print(sum)

import numpy as np
print('\n\tExercise 87')
Z = np.random.randint(0,2,(6,3))
T = np.ascontiguousarray(Z).view(np.dtype((np.void,Z.dtype.itemsize*Z.shape[1])))
_, idx=np.unique(T, return_index=True)
uZ=Z[idx]
print(uZ)