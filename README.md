# Example Code

This repository will contain code examples for the projects covered described in the new [RAREblog](https://rareblog.substack.com).

The code is MIT licensed.

The first project will have code for creating simple plots on the Raspberry Pi Pico and Pico 2.

I'll be showing my work as I go.

For now, I'm still building scaffolding, mocks for testing, and unit tests.
The next step will be to create visible plot using guizero's canvas.

I'm doing the development using strict TDD.

I'm using Alistair Cockburn's [hexagonal architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)), also known as ports and adapters architecture. The abstract Display class defines the interface to adapters.

There will be adapters for testing, for guizero, and for a variety of OLED and TFT displays that the Pico can drive.

The Display interface borrows heavily from Pimoroni's [Micropyhon PicoGraphics Library](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/picographics), so it should be easy to use this package with products like the Pimoroni Pico Explorer, mono OLED, GFX pack and friends.