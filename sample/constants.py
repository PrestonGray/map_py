from . import material

map_width = 500
map_height = 500

num_tunnels = 250
max_length = 100
max_depth = 50
max_diag = 35
min_width = 5
max_width = 25

num_centers = 500
max_radius = 50

colors = {'brown': 0,
          'white': 1,
          'gray': 2,
          'gold': 3,
          'blue': 4}

materials = [material.Material('Dirt', 'brown', 0.7),
             material.Material('Iron', 'gray', 0.2),
             material.Material('Gold', 'gold', .08),
             material.Material('Diamond', 'blue', .02)]
