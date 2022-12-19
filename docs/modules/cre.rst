Cabled Range Extender (CRE)
===========================

.. image:: /images/ESDK-CRE.jpg
   :alt: ESDK CRE board set

Introduction
------------

The CRE board set is comprised of an *A* end plus a *B* end. The former is connected to the end of the local sensor chain and provides an RJ45 connector for extending the chain via twisted pair (CAT5/CAT6) cabling. 

The *B* board connects to the other end of the twisted pair cabling and enables sensor modules to be connected remotely.

The boards transition from single-ended I2C to differential signalling, and then back again. In addition to which the CRE-A boosts the power supply voltage so as to account for any cable losses, with the CRE-B board providing voltage regulation for the remotely connected sensors. 

.. warning:: 
   Sensors which use plain GPIO for interfacing may not be used at the remote end.

CRE-A schematic diagram
-----------------------

.. image:: /images/ESDK-CRE-A-schematic.jpg
   :alt: ESDK CRE-A schematic diagram

CRE-A theory of operation
-------------------------

*TBD*

CRE-A board layout
------------------

.. image:: /images/ESDK-CRE-A-layout.jpg
   :alt: ESDK CRE-A board layout

CRE-B schematic diagram
-----------------------

.. image:: /images/ESDK-CRE-B-schematic.jpg
   :alt: ESDK CRE-B schematic diagram

CRE-B theory of operation
-------------------------

*TBD*

CRE-B board layout
------------------

.. image:: /images/ESDK-CRE-B-layout.jpg
   :alt: ESDK CRE-B board layout