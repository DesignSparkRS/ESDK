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

The ESDK hardware designs are entered using `DesignSpark PCB`_. 

The original design files and manufacturing outputs may be found in the GitHub repository:

https://github.com/DesignSparkRS/ESDK

Project Documentation
---------------------

Documentation is available on `docs.designspark.io`_.

Licensing
=========

Hardware
--------

Copyright 2021-2022 RS Components Ltd
SPDX-License-Identifier: Apache-2.0 WITH SHL-2.1

Licensed under the Solderpad Hardware License v 2.1 (the “License”); you may not
use this file except in compliance with the License, or, at your option, the
Apache License version 2.0. You may obtain a copy of the License at

https://solderpad.org/licenses/SHL-2.1/

Unless required by applicable law or agreed to in writing, any work distributed
under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

Software
--------

Copyright 2021 RS Components Ltd and provided under the MIT License.

Documentation
-------------

Copyright 2021-2022 RS Components Ltd and provide under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

.. _DesignSpark PCB: https://www.rs-online.com/designspark/pcb-software
.. _docs.designspark.io: https://docs.designspark.io/projects/esdk-hardware/en/latest/