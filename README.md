# Super Mario Text

This repository provides two OpenSCAD scripts to generate 3D-printable text with an interlocking brim or two separated objects:

- **SuperMarioLetters.scad**: Creates the hollow letter shapes, designed to fit seamlessly into the brim.
- **SuperMarioBrim.scad**: Generates the border (brim) around each letter for added strength and decorative effect.

## Usage

1. **Clone the repo**
   ```bash
   git clone https://github.com/<your-username>/SuperStringMario3D.git
   cd SuperStringMario3D

## Customize words

In SuperMarioLetters.scad, set word1 and word2 (uppercase) at the top.

Brim parameters (thickness, radius) can be adjusted in SuperMarioBrim.scad.

## Render

Open each .scad file in OpenSCAD.

## Compile 
(F6) and verify the interlocking fit.

## Export STL

In the OpenSCAD GUI: Design → Compile and Render (F6)

Then File → Export → Export as STL for each script.

## Requirements

OpenSCAD 2021.01 or newer