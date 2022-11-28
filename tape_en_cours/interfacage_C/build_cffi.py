import pathlib
import cffi
import re

print("Building CFFI Module")
ffi = cffi.FFI()

this_dir = pathlib.Path().resolve()
h_file_name = this_dir / "cmult.h"
with open(h_file_name) as h_file:
    # cffi does not like our preprocessor directives, so we remove them
    lns = h_file.read().splitlines()
    flt = filter(lambda ln: not re.match(r" *#", ln), lns)
    flt = map(lambda ln: ln.replace("EXPORT_SYMBOL ", ""), flt)
    ffi.cdef(str("\n").join(flt))

ffi.set_source(
    "cffi_example",
    # Since we are calling a fully built library directly no custom source
    # is necessary. We need to include the .h files, though, because behind
    # the scenes cffi generates a .c file which contains a Python-friendly
    # wrapper around each of the functions.
    '#include "cmult.h"',
    # The important thing is to include the pre-built lib in the list of
    # libraries we are linking against:
    libraries=["cmult"],
    library_dirs=[this_dir.as_posix()],
    extra_link_args=["-Wl,-rpath,."],
)

ffi.compile()
print("* Complete")
