.. _termcombine:

termcombine
===========

.. todo::  This command has not yet been ported to the *new APBS syntax* (see :ref:`new_input_format`).

Combine multiple PB-(S)AM Brownian dynamics trajectory termination conditions (see :doc:`term`) via logic operators

.. code-block:: bash
   
   termcombine {op}

where ``op`` is either the string ``or`` or ``and``.
If  ``and`` is selected, all listed termination conditions must be fulfilled before the simulation ends.
If ``or`` is selected, only one needs to be satisfied to complete the simulation.
