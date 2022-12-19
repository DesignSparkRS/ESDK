Particulate Matter Sensor (PM2)
===============================

.. image:: /images/ESDK-PM2.jpg
   :alt: ESDK PM2 board

Introduction
------------

The ESDK-PM2 features a Sensirion SPS30 particulate matter sensor that can count four different particulate sizes and reports these over an I2C interface.

Schematic diagram
-----------------

.. image:: /images/ESDK-PM2-Schematic.svg
   :alt: ESDK PM2 schematic diagram

Theory of operation
-------------------

The ESDK-PM2 board is primarily a passive board that only serves to convert the connector on the SPS30 sensor module into the ESDK ecosystem connector. The Sensirion SPS30 is capable of measuring PM1.0, PM2.5, PM4.0 and PM10 in densities ranging from 0-1000μg/m\ :sup:`3` with an accuracy up to ±10μg/m\ :sup:`3`.

This utilises a small fan to pull air and particulates through a measurement chamber that takes advantage of laser scattering to be able to count particles. The sensor can report both mass and number concentration, as well as the typical particle size over an I2C interface.

Board layout
------------

.. image:: /images/ESDK-PM2-Layout.png
   :alt: ESDK PM2 board layout

