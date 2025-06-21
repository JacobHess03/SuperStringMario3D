from solid import scad_render_to_file, import_scad, translate
from solid.utils import union

# Paths to your SCAD modules
letters = import_scad('SuperMarioSTD/SuperMarioLetters.scad')
brim    = import_scad('SuperMarioSTD/SuperMarioBrim.scad')

# Define spacing between letters module and brim module (in mm)
distance = 10

# Combine the two modules with an offset on the X axis
distanced_letters = translate([-distance/0.1, 0, 0])(letters.letters_main())
distanced_brim    = translate([ distance/0.1, 0, 0])(brim.brim_main())

model = union()(distanced_letters, distanced_brim)

# Export to a single SCAD file
scad_render_to_file(model, 'SuperMarioSTD/CombinedModel.scad', file_header='$fn = 100;')