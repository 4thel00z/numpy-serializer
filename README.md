# numpy-serializer

![numpy-serializer Logo](https://raw.githubusercontent.com/4thel00z/numpy-serializer/master/logo.png)

## Motivation

I couldn't find a nice high-level package that is fast enough to serialize and deserialize numpy arrays while preserving the type
and shape informations.

## Installation

```
pip install numpy-serializer
```

## How to use

```python3
import numpy_serializer as ns
import numpy as np

a = np.random.normal(size=(50,120,150))
b = ns.to_bytes(a)
c = ns.from_bytes(b)
assert np.array_equal(a,c)
```

## License

This project is licensed under the GPL-3 license.
