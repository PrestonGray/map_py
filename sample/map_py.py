from sample import rmap
from sample import mapgen
from sample import diffuser
from sample import constants as c

import matplotlib as mpl
from matplotlib import pyplot


def generate():
    # Create the map
    mapping = rmap.RMap(c.map_width, c.map_height)
    # Create the generator and generate the map
    generator = mapgen.MapGen(c.num_tunnels, c.max_length, c.max_depth, c.max_diag, c.min_width, c.max_width)
    generator.generate(mapping)
    # Add materials
    diffuse = diffuser.Diffuser(c.num_centers, c.max_radius)
    diffuse.generate(mapping)
    # Color map
    cmap = mpl.colors.ListedColormap(list(c.colors.keys()))
    bounds = list(c.colors.values())
    # Plot
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    img = pyplot.imshow(mapping.get_colors(), interpolation='nearest', cmap=cmap, norm=norm)
    pyplot.show()


if __name__ == "__main__":
    generate()
