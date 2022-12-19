Nitrogen Dioxide Sensor (NO2)
=============================

.. image:: /images/ESDK-NO2.jpg
   :alt: ESDK NO2 board

Introduction
------------

The ESDK-NO2 board measures atmospheric nitrogen dioxide levels using an electrochemical cell that produces a current from a redox reaction.

Schematic diagram
-----------------

.. image:: /images/ESDK-NO2-Schematic.svg
   :alt: ESDK NO2 schematic diagram

Theory of operation
-------------------

A SPEC Sensors ULPSM-NO2 module provides an interface to the electrochemical cell that converts the current output into a linear voltage output. As this signal from the ULPSM module is high impedance, a unity-gain amplifier configuration buffers the signal before being fed into an ADS1119 16-bit, four channel ADC that is polled over the I2C bus.

Board layout
------------

.. image:: /images/ESDK-NO2-Layout.png
   :alt: ESDK NO2 board layout