# Certificate extractor for eduroam

> [!WARNING]
> Meta Horizon OS currently (at v72) has a bug where selecting a certificate manually does not actually install it! Currently, you will need to set up the headset with a regular WPA2-PSK network (such as a mobile hotspot) and sideload the geteduroam app. You will then need to set up the network in the geteduroam app (which will only install the certificate, and not actually connect) and then manually finish the network setup in WiFi settings, making sure to select the installed certificate in the dropdown.

Primarily intended for Meta Quest headsets, but should also be useful for other Android devices that can't use geteduroam.

Python script that uses only standard dependencies. 

Run it with a path to the ChromeOS setup file as the argument, or without arguments to receive the prompt.

