# AMPILIGHT

A DIY Philips Ambilight-a-like built on a Rapsberry Pi 3 (I think), a 20 Euro capture card, a HDMI splitter, two extra HDMI cables, and a strip or two of Neopixel LEDs (depending on the size of your TV).

## How does it work?

Taking the image from the capture card every few tenths of a second, reducing the scale to something a bit more manageable, *something I haven't thought about here*, run website see what the machine is currently doing with websockets, output to lights.

## Notes

This was built on a scale suitable for my home system - a 43" TCL 4K - which has a length measured on three sides of almost exactly 2m. Three side because I didn't see a reason to have lights across the bottom. NeoPixel strips come in three flavours, 30, 60, and 144 LEDs per metre. I opted for the 144 LED variant which also requires me to have a slightly beefier external 5v 10a supply to drive them all at full brightness if necessary. My screen is 54cm tall, there are 144 LEDs per metre, which makes for an average of 1.44 LED/CM or 77/78 per vertical screen size. Making the width in LEDs 136/134. So our target resolution is 136x77/134x78 - ish.