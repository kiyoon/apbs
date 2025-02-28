.. _mgdummy:

mg-dummy
========

.. currentmodule::  apbs.input_file.calculate.finite_difference

.. note::
   
   This command has been ported to the *new APBS syntax* (see :ref:`new_input_format`); see :func:`FiniteDifference.noop` for more information.


Not a Poisson-Boltzmann calculation.
Many calculations of surface and charge distribution properties which do not require solution of the PBE.

This type of calculation allows users to write out dielectric, ion-accessibility, and charge distribution, and other types of maps that depend solely on biomolecular geometry.
Since these maps depend only on geometry, they can be written out without actually solving the PB equation. 

.. toctree::
   :maxdepth: 2
   :caption: ELEC mg-auto keywords:

   bcfl
   chgm
   dime
   gcent
   glen
   ../generic/grid
   ion
   lpbe
   lrpbe
   ../generic/mol
   npbe
   pdie
   ../generic/sdens
   sdie
   ../generic/srad
   srfm
   ../generic/swin
   ../generic/temp
   write
