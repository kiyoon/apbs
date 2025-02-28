.. _domainLength:

domainLength
============

.. currentmodule:: apbs.input_file.calculate.finite_element

.. note::  This command has been ported to the *new APBS syntax* (see :func:`FiniteElement.domain_length`).

Specify the rectangular finite element mesh domain lengths for :ref:`femanual` finite element calculations.
This length may be different in each direction.
If the :ref:`usemesh` keyword is included, then this command is ignored.
The syntax is:

.. code-block:: bash

   domainLength {xlen ylen zlen}

where the parameters ``xlen ylen zlen`` are floating point numbers that specify the mesh lengths in the x-, y-, and z-directions (respectively) in units of Å.

