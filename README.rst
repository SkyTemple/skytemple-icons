|logo|

|icon1| |icon2| |icon3| |icon5| |icon6| |icon7|

SkyTemple Icons
===============

|build| |pypi-version| |pypi-downloads| |discord|

.. |logo| image:: https://raw.githubusercontent.com/SkyTemple/skytemple/master/skytemple/data/icons/hicolor/256x256/apps/skytemple.png

.. |icon1| image:: https://raw.githubusercontent.com/SkyTemple/skytemple-icons/main/example/skytemple-e-actor-symbolic.png
.. |icon2| image:: https://raw.githubusercontent.com/SkyTemple/skytemple-icons/main/example/skytemple-e-dungeon-floor-symbolic.png
.. |icon3| image:: https://raw.githubusercontent.com/SkyTemple/skytemple-icons/main/example/skytemple-e-dungeon-symbolic.png
.. |icon5| image:: https://raw.githubusercontent.com/SkyTemple/skytemple-icons/main/example/skytemple-e-graphics-symbolic.png
.. |icon6| image:: https://raw.githubusercontent.com/SkyTemple/skytemple-icons/main/example/skytemple-e-ground-symbolic.png
.. |icon7| image:: https://raw.githubusercontent.com/SkyTemple/skytemple-icons/main/example/skytemple-e-monster-base-symbolic.png

.. |build| image:: https://img.shields.io/github/workflow/status/SkyTemple/skytemple-icons/Build,%20test%20and%20publish
    :target: https://pypi.org/project/skytemple-icons/
    :alt: Build Status

.. |pypi-version| image:: https://img.shields.io/pypi/v/skytemple-icons
    :target: https://pypi.org/project/skytemple-icons/
    :alt: Version

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/skytemple-icons
    :target: https://pypi.org/project/skytemple-icons/
    :alt: Downloads

.. |discord| image:: https://img.shields.io/discord/710190644152369162?label=Discord
    :target: https://discord.gg/4e3X36f
    :alt: Discord

.. |kofi| image:: https://www.ko-fi.com/img/githubbutton_sm.svg
    :target: https://ko-fi.com/I2I81E5KH
    :alt: Ko-Fi

.. _Aviivix: https://twitter.com/Aviivix

Pixelated symbolic icons for SkyTemple and the SkyTemple Script Engine Debugger.

These great icons were created by Aviivix_!

The ``source`` directory contains the original icons (designed for background color #383c4a).
``skytemple_icons`` contains the GTK+ 3 icon resource (symbolic PNGs, taking theme colors).
``example`` contains some scaled icons for this README.

License
-------
The icons directly stored in this Git repository are dual-licensed:

- GNU General Public License Version 3 (GPLv3+) - See LICENSE_GPLv3
- Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) - See LICENSE_CC

Choose whatever license is more convenient for you.

Building
--------
To convert the icons in ``source`` into the format GTK needs (for auto-converting the colors
based on theme color) and also all the different sizes, run ``./convert_icons.py``

|kofi|
