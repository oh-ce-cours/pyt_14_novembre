#!/usr/bin/env python3
# IDE might complain with "no module found" here, even when it exists
import cffi_example
from cffi import FFI
import numpy
import matplotlib.pyplot as plt

# Sample data for our call:
x, y = 6, 2.3
ffi = FFI()

# appel d'une fonction simple
# answer = cffi_example.lib.cmult(x, y)
# print(f"    In Python: int: {x} float {y:.1f} return val {answer:.1f}")

# # appel d'une fonction modifiant des tableaux 1d
array_in = numpy.arange(10, dtype=numpy.float32)
ptr_array_in = ffi.cast("float *", ffi.from_buffer(array_in))
array_out = numpy.zeros_like(array_in)
ptr_array_out = ffi.cast("float *", ffi.from_buffer(array_out))
answer = cffi_example.lib.square_numpy(ptr_array_in, ptr_array_out, len(array_in))
print(f"On met au carré les nombres 0 - 10 en C : {array_out}, {type(array_out)}")

# création d'un tableau en C
data = cffi_example.lib.demo_2d_array(7, 5)
buf = ffi.buffer(data, ffi.sizeof("float") * 5 * 7)
np_arr2 = numpy.frombuffer(buf, dtype=numpy.float32)
array_2d = np_arr2.reshape(7, 5)
plt.imshow(array_2d)
plt.show()

# import ipdb

# ipdb.set_trace()
