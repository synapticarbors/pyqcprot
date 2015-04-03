=====================
  PyQCPROT README
=====================

* Author:   Joshua L. Adelman, University of Pittsburgh 
* Contact:  jla65@pitt.edu

PyQCPROT is a python/cython implementation of Douglas Theobald's `QCP
method`_ for calculating the minimum RMSD between two structures and
determining the optimal least-squares rotation matrix.

A full description of the method, along with the original C implementation can 
be found at http://theobald.brandeis.edu/qcp/

If you use this QCP rotation calculation method in a publication,
please reference [Theobald2005]_ and [Liu2010]_:

.. [Theobald2005]  Douglas L. Theobald (2005)
      "Rapid calculation of RMSD using a quaternion-based characteristic polynomial."
      Acta Crystallographica A 61(4):478-480.

.. [Liu2010] Pu Liu, Dmitris K. Agrafiotis, and Douglas L. Theobald (2010)
      "Fast determination of the optimal rotational matrix for macromolecular superpositions."
      J. Comput. Chem. 31, 1561-1563. 


.. _`QCP method`: http://theobald.brandeis.edu/qcp/


License
======= 
This code code is released under the BSD 3-clause license as noted in the .pyx source code 
or LICENSE file. 

The original C code is copyright:
2009-2010, Pu Liu and Douglas L. Theobald

This implementation is copyright
2011, Joshua L. Adelman

Installation
============

This module requires:

- numpy_
- cython_ (optional)
- gcc_

.. _numpy: http://numpy.scipy.org/
.. _cython: http://cython.org/
.. _gcc: http://gcc.gnu.org/


Method 1:
~~~~~~~~~

To compile the extension in the directory in which ``qcprot.pyx``
resides::

   python setup.py build_ext --inplace

Further information on `compiling cython extensions`_ is available in 
the cython_ docs.

.. _`compiling cython extensions`:
   http://docs.cython.org/src/userguide/source_files_and_compilation.html


Method 2
~~~~~~~~

If you do not have `cython`_ installed, you can build the extension
directly from the cython generated ``pyqcprot.c``. This is handled
automatically by ``setup.py``.


Example Usage
=============

See ``example.py`` for a simple example.

For an example using the `MDAnalysis`_ package see
``mdanalysis_example.py``.

.. _MDAnalysis: https://MDAnalysis.github.io
 
