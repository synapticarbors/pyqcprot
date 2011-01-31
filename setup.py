from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("pyqcprot", ["pyqcprot.pyx"],
                extra_compile_args=["-O3","-ffast-math"])]

setup(
  name = 'Python qcprot module',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)