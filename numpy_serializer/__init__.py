__version__ = "0.1.3"
__doc__ = """
This is a small package that provides 4 high-level APIs to serialize/deserialize numpy arrays to an object/file, namely:

    - to_bytes
    - to_file
    - from_bytes
    - from_file

It is fast and preserves the shape and type information.
"""

import msgpack
import msgpack_numpy as m
import numpy as np

def to_bytes(payload: np.array)->bytes:
    return msgpack.packb(payload, default=m.encode)
to_bytes.__doc__= """
to_bytes takes a numpy.array as a single argument and serializes it to bytes.
"""


def to_file(payload:np.array,path:str) -> int:
    with open(path, mode="wb") as f:
       return f.write(to_bytes(payload)) 
to_file.__doc__= """
to_file takes a numpy.array and a file path as arguments and persists the serialized bytes to the file.
"""

def from_bytes(payload:bytes) -> np.array:
    return msgpack.unpackb(payload, object_hook=m.decode)
from_bytes.__doc__= """
from_bytes recovers a numpy.array from a bytes array that was produced via numpy_serializer.to_bytes.
"""


def from_file(path:str) -> np.array:
    with open(path, mode="rb") as f:
        return from_bytes(f.read())
from_file.__doc__= """
from_file recovers a numpy.array from a file that that was produced via numpy_serializer.to_file.
"""


