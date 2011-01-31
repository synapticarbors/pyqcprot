from distutils.core import setup
from distutils.extension import Extension

ext_modules = [Extension("pyqcprot", ["pyqcprot.c"],
                extra_compile_args=["-O3","-ffast-math"])]

setup(
  name = 'Python qcprot module',
  ext_modules = ext_modules
)