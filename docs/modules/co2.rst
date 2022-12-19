Carbon Dioxide Sensor (CO2)
===========================

.. image:: /images/ESDK-CO2.jpg
   :alt: ESDK CO2 board

Introduction
------------

The ESDK-CO2 board provides CO\ :sub:`2` measuring capability to the ESDK platform, utilising a Sensirion SCD41 sensor.

Schematic diagram
-----------------

.. image:: /images/ESDK-CO2-Schematic.svg
   :alt: ESDK CO2 schematic diagram

Theory of operation
-------------------

This board features a single sensor, the Sensirion SCD41, that utilises NDIR technology to measure atmospheric CO\ :sub:`2` levels with a specified range of 400-5000ppm and a quoted accuracy of ±40ppm + 5%. On the ESDK-CO2 board, an additional 3.3V regulator is present due to the high current peaks of up to 205mA that the sensor can require during measurements.

Board layout
------------

.. image:: /images/ESDK-CO2-Layout.png
   :alt: ESDK CO2 board layout
