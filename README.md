<img
align="right"
src="https://user-images.githubusercontent.com/32917068/80525225-816fc500-8956-11ea-9035-8a9387daf5f1.png"
alt="logo"
height="400px"
width="550px"
/>
# Mappy
> A simple random walk map generator.

<br />

<br />

## Table of Contents
- [About](#about)
- [Usage](#usage)
- [Customization](#customization)

<br />

<br />

## About
Mappy is a small proof of concept project designed to create a two dimensional side view map using the random walk algorithm. It allows for custom made materials with name, color, and rarity. These are interspersed randomly throughout the map at a specified number of cluster centers based on their rarity. They are then randomly diffused outward from the center with an area also determined by the material's rarity.

## Usage
To install, clone the repository where you want via the terminal.

```sh
git clone https://github.com/PrestonGray/map_py.git
cd map_py
```

## Customization
To customize the all aspects of the map including possible materials to populate the map, simply edit the provided variables found in `map_py/constants.py`.
