# Plotting Library
A simple Python library for graphics and plotting operations with color manipulation support.

## Overview

This project will provide a lightweight library for creating and manipulating graphical elements.
The project is in an early stage of development.

It will include:
- A colour manipulation utility (HSV to RGB)
- Display abstraction for drawing operations
- Mock implementations for testing

I'm using Alistair Cockburn's [hexagonal architecture](https://en.wikipedia.org/wiki/Hexagonal_architecture_(software)),
also known as ports and adapters architecture.

The abstract Display class defines the interface to adapters.

The Display interface borrows heavily from Pimoroni's [Micropyhon PicoGraphics Library](https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/picographics),
so it should be easy to use this code with products like the Pimoroni Pico Explorer, mono OLED, GFX pack and friends.

There will be adapters for testing, for guizero, and for several of the OLED and TFT displays that the Pico can drive.

