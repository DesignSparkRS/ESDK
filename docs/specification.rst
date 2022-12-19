ESDK Module Specification
=========================

The ESDK module specification is as follows.

Physical
--------

Two board sizes are currently in use within the ESDK ecosystem, comprising of a "1U" and "2U" variant. A 1U module is 35x70mm and a 2U module is double the width at 70x70mm.

Four corner mounting holes are to be provided, spaced 6mm from each edge. The hole should be 3.2mm diameter, which allows suitable clearance for M3 fastening hardware.

Each corner of the board should be chamfered at a 45° angle, such that the length parallel to the chamfer equates to 2.121mm.

A 3mm keep-out should be present around the edge of the board where no components should be placed — this allows room for the case to sandwich the PCBA. Tracks & vias can however be placed within this zone, being mindful of any PCB fabrication rules specified by a board house.


Connectors
----------

Each ESDK module typically features a male and female 12-pin header. Typically Samtec parts TSW-106-08-G-D-RA and SSW-106-02-G-D-RA are used which form a mating pair. These should be centred on the vertical edge of the PCB with the male header facing left and female facing right. The male header should be positioned such that the pins align with the board edge (but should not protrude over) and the mating face of the female header should protrude 5.53mm beyond the PCB edge.

Connector positioning is somewhat critical to ensure that a solid connection is made, but the parts do not bottom out completely within each other which would increase the risk of damage resulting from knocks and bumps


Power
-----

Two power rails are currently present on the ESDK ecosystem connector — 3.3Vdc and 5Vdc. The 3.3Vdc rail is provided by an LD1117S33 regulator located on ESDK-MAIN and is fused with a 200mA polyfuse. The 5Vdc rail is provided directly from the USB-C power input on ESDK-MAIN and is fused with a 750mA polyfuse. Each supply rail features a TVS diode for additional protection.

Current draw should be kept as low as possible on both 3.3V and 5V rails. Boards that require more current should utilise the 5V rail and add their own local regulation — an example of this is the ESDK-CO2 board that features another LD1117S33 regulator connected to the 5V supply.

A power indicator LED should be present and connected to the module primary supply rail through some form of removable link. Either a Kingbright KPA-3010CGCK right angle green SMD LED for the 3.3V rail, or a Kingbright KPA-3010YC right angle orange SMD LED for the 5V rail.

The power indicator should be positioned at the top of the board with a small gap from the 3mm component setback. The indicator should be horizontally centred on the board.

I/O
---

I/O is usually provided via the I2C bus present that connects to Raspberry Pi I2C1. This bus utilises the pull-ups located on the Raspberry Pi and features a small TVS diode for additional ESD protection.

Two GPIO lines are extended from the Raspberry Pi - GPIO 20 which becomes ESDK GPIO 1 and GPIO 21 which becomes ESDK GPIO 2. These lines are protected by another TVS diode but are otherwise unbuffered and completely at the mercy of software written by a user, so care should be taken when designing a module to provide an adequate interface.

An example of a board that can utilise one of the ESDK GPIO lines is the ESDK-NRD which features an event output connected via a 1K ohm resistor to GPIO 1. The resistor offers some level of protection should the Pi GPIO be configured as a current source and the module GPIO configured as a current sink.


Addressing
----------

All modules with I2C should use unique device addresses. See :doc:`modules/index` for details of those currently in use. If any modules are developed that have address conflicts consider the use of an I2C address translator such as the Analog Devices LTC4316.

.. note::
	I2C address translators have not been tested but should work. Test and verify before designing in!