Temperature, humidity and VOCs Sensor (THV)
===========================================

.. image:: /images/ESDK-THV.jpg
   :alt: ESDK THV board

Introduction
------------

The ESDK-THV board provides two sensors that report a total of three metrics including

* Temperature
* Relative humidity
* Volatile Organic Compounds (VOCs)

Schematic diagram
-----------------

.. image:: /images/ESDK-THV-Schematic.svg
   :alt: ESDK THV schematic diagram

Theory of operation
-------------------

The ESDK-THV utilises a Sensirion SHT31 to provide temperature and relative humidity measurements accurate to 2% RH and 0.2°C. A Sensirion SGP40 provides a processed sensor output with an "VOC Index" unit from 0-500, with an ethanol equivalent measuring range of 0-1000ppm. Further reading about the Sensirion "VOC Index" measurement can be found here_.

To help reduce thermal influence from the PCB, the SHT31 is mounted on a tab routed out of the board with only small traces connecting 3.3V/GND/I2C.

Both sensors appear on the I2C bus with separate addresses of 0x41 for the SHT31 and 0x59 for the SGP40.

Board layout
------------

.. image:: /images/ESDK-THV-Layout.png
   :alt: ESDK THV board layout

.. _here: https://sensirion.com/media/documents/02232963/6294E043/Info_Note_VOC_Index.pdf