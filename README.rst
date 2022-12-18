Environmental Sensor Development Kit (ESDK)
===========================================

.. image:: https://raw.githubusercontent.com/DesignSparkRS/ESDK/main/docs/images/ESDK_chain.jpg
   :alt: ESDK System

The Environmental Sensor Development Kit (ESDK) is an open source hardware
platform that is designed to make it as easy as possible to prototype custom
sensor solutions. It has been created to support the engineer activism Air
Quality project, but could easily be put to use in other sensing projects — and
for that matter, potentially a great many more IoT and wider applications that
have a need for a small Linux computer with integrated touchscreen and GPS etc.

Components
----------

The system is based upon a Raspberry Pi SBC fitted with the ESDK-Main board, which provides a touch screen, physical buttons, RTC, buzzer and sensor power supply. This is then connected to a sensor chain, with sensors interfaced via I2C and/or plain GPIO. 

Hardware Designs 
----------------

This repository contains the ESDK hardware designs — which are entered using `DesignSpark PCB`_ — together with the manufacturing outputs.

Documentation
-------------

Documentation is available on `docs.designspark.io`_.

.. _DesignSpark PCB: https://www.rs-online.com/designspark/pcb-software
.. _docs.designspark.io: https://docs.designspark.io/projects/esdk-hardware/en/latest/
