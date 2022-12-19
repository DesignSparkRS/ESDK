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
     - N/A
     - N/A
   * - :doc:`PEA <pea>`
     - Sensor chain start
     - N/A 
     - N/A 
   * - :doc:`THV <thv>`
     - Temperature, humidity and VOCs sensor
     - ?
     - ?
   * - :doc:`CO2 <co2>`
     - Carbon dioxide sensor
     - ?
     - ?
   * - :doc:`PM2 <pm2>`
     - Particulate matter sensor
     - ?
     - ?
   * - :doc:`NO2 <no2>`
     - Nitrogen dioxide sensor
     - ?
     - ?
   * - :doc:`FDH <fdh>`
     - Formaldehyde sensor
     - ?
     - ?
   * - :doc:`NRD <nrd>`
     - Nuclear radiation detector
     - ?
     - ?
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

