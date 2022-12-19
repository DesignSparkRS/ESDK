ESDK System
===========

The ESDK Main board plugs into the P1 header of a Raspberry Pi 3, 3+ or 4 Model B. However, it is not technically a 'HAT', since its proportions are such that it is too large to confirm to the official specification.

The sensor chain starts with the PEA board and this is cabled to the Main board. This board exists so as to permit the sensor chain to be positioned at the same Z-height as the Raspberry Pi SBC, rather than the ESDK-Main board.

The sensor chain may optionally be extended over longer distances using the Cabled Range Extender (CRE) board set.

Modules
-------

.. list-table:: ESDK Modules
   :header-rows: 1
   :widths: 5 30 10 10

   * - Name
     - Description
     - I2C
     - GPIO
   * - :doc:`Main <main>`
     - Main board
     - 0x38 for LCD touchscreen, 0x68 for RTC
     - Multiple, see documentation for main board
   * - :doc:`PEA <pea>`
     - Sensor chain start
     - N/A 
     - N/A 
   * - :doc:`THV <thv>`
     - Temperature, humidity and VOCs sensor
     - 0x41 for SHT31 temperature & humidity, 0x59 for SGP40 VOC
     - N/A
   * - :doc:`CO2 <co2>`
     - Carbon dioxide sensor
     - 0x62
     - N/A
   * - :doc:`PM2 <pm2>`
     - Particulate matter sensor
     - 0x69
     - N/A
   * - :doc:`NO2 <no2>`
     - Nitrogen dioxide sensor
     - 0x40
     - N/A
   * - :doc:`FDH <fdh>`
     - Formaldehyde sensor
     - 0x5D
     - N/A
   * - :doc:`NRD <nrd>`
     - Nuclear radiation detector
     - 0x60
     - ESDK GPIO 1 (Raspberry Pi GPIO 20) — optional, enabled and disabled through software
   * - :doc:`CRE <cre>`
     - Cabled range extenders
     - N/A 
     - N/A 
   * - :doc:`EEA <eea>`
     - Ecosystem adapter board
     - N/A 
     - N/A 

.. toctree::
   :hidden:

   main
   pea
   thv
   co2
   pm2
   no2
   fdh
   nrd
   cre
   eea

