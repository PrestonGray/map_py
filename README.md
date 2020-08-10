<img
align="right"
src="https://user-images.githubusercontent.com/32917068/80525225-816fc500-8956-11ea-9035-8a9387daf5f1.png"
alt="logo"
height="400px"
width="550px"
/>
# Mappy
> A simple random walk map generator.

## Table of Contents
- [About](#about)
- [Usage](#usage)
- [Customization](#customization)

## About
Mappy is a small proof of concept project designed to create a two dimensional side view map using the random walk algorithm. It allows for custom made materials with name, color, and rarity. These are interspersed randomly throughout the map at a specified number of cluster centers based on their rarity. They are then randomly diffused outward from the center with an area also determined by the material's rarity.

## Usage
To install, clone the repository where you want via the terminal.

```sh
git clone https://github.com/PrestonGray/map_py.git
cd map_py
```

In order to randomly generate a map, simply run the titular `map_py.py` file using python.

```sh
python3 map_py.py
```

## Customization
To customize the possible materials to populate the map, simply edit the colors and materials data structures found in `map_py/constants.py`.
