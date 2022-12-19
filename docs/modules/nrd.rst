Nuclear Radiation Detector (NRD)
================================

.. image:: /images/ESDK-NRD.jpg
   :alt: ESDK NRD board

Introduction
------------

The ESDK-NRD board enables detection of nuclear radiation events, utilising a solid-state sensor that reduces the risk of using a sensing element that requires high voltage.

Schematic diagram
-----------------

.. image:: /images/ESDK-NRD-Schematic.svg
   :alt: ESDK NRD schematic diagram

Theory of operation
-------------------

The ESDK-NRD utilises a Teviso BG51 radiation sensor that is capable of detecting Beta and Gamma radiation. This sensor utilises an array of PIN photodiodes in a housing combined with circuitry to interface with the diodes to produce a TTL level pulse output. To bridge the gap between TTL pulse and I2C bus, a Raspberry Pi RP2040 microcontroller runs a MicroPython application that keeps track of accumulated pulses and exposes a number of registers containing counts per second, per minute and total counts.

A GPIO pin is connected from the RP2040 to an on-board LED that can be software enabled/disabled to provide an indication of a count event. An additional GPIO is connected through a 1K ohm resistor to the ESDK GPIO 1 line allowing for custom triggering to be set up should a user wish to modify the MicroPython application. A USB-C connector provides a USB connection to the RP2040 to allow for easy reprogramming, plus the ability to run the device standalone using a USB virtual com port. A four layer PCB is used to make routing easier and to achieve the required USB differential impedance of 90 ohms.

Board layout
------------

.. image:: /images/ESDK-NRD-Layout.png
   :alt: ESDK NRD board layout
