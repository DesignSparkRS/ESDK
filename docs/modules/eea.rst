ESDK Ecosystem Adapter (EEA)
============================

.. image:: /images/ESDK-EEA.jpg
   :alt: ESDK EEA board

Introduction
------------

The ESDK-to-ecosystem adapter board is designed to be used at the end of a sensor chain and transitions from the ESDK system connector to:

* Pmod I2C
* Grove I2C
* Grove GPIO
* Qwiic (I2C)

As such it enables convenient interfacing of third party modules.

Schematic diagram
-----------------

.. image:: /images/ESDK-EEA-Schematic.svg
   :alt: ESDK EEA schematic diagram

Theory of operation
-------------------

The ESDK-EEA provides a buffered I2C interface that can support hot-plugging without corruption of the I2C bus. An NXP PCA9508DP is utilised to effect this, combined with a dual TVS diode for additional ESD protection. The two ESDK GPIO lines are also buffered by a bidirectional voltage translator that allows for both input and output with a selectable IO voltage of 3.3V or 5V. An additional TVS diode offers additional protection for the GPIO lines.

Board layout
------------

.. image:: /images/ESDK-EEA-Layout.png
   :alt: ESDK EEA board layout