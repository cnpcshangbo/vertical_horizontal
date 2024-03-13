# Classify the crack mask into three masks according to the crack direction
[![image](https://github.com/cnpcshangbo/vertical_horizontal/assets/4831029/0bf08188-a2ad-4d30-b59e-139c782c9a5d)](https://www.youtube.com/watch?v=I67dWD0_tIc)

## Input files:
- Input mask file generated from InspectionNet:
`S1078754.png`
- Raw image:
`raw/S1078754.JPG`

## Output files:
- `3masks/vertical_crack_mask.png`
- `3masks/horizontal_crack_mask.png`
- `3masks/diagonal_crack_mask.png`

## Usages:
- Create a new `conda` environment if necessary;
- Install necessary libraries according to the what are imported in `red23connected_components.py`;
- Run `red23connected_components.py`;
- Check result files in `3masks` folder;
- (Optional) Serve your project folder and visit the `index.html` to interactively change colors for the cracks.
