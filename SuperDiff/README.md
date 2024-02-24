
# 
# Use Instructions and What's In This Folder

## Use Instructions

Pre-trained UNETs are available in `SuperDiff/checkpoints` and training dataset is available in `Datasets`. You may easily load the pre-trained UNet to recreate our results.

## What's in this Folder?

This folder `SuperDiff` contains sample unconditional and conditional SuperDiff versions: `diffusion_1d_v3` is the unconditional version of SuperDiff and `diffusion_1d_v4` is the conditional version.

Here, `diffusion1d-v3-[VERSION]-SAMPLE.ipynb` are the unconditional SuperDiff versions (name corresponds to class—cuprates, pnictides, etc.) and `diffusion1d_v4_ilvr_YBa1.4Sr0.6Cu3O6Se0.51.ipynb` is conditional SuperDiff trained on cuprates conditioned on YBa1.4Sr0.6Cu3O6Se0.51. Code for the other versions of conditional SuperDiff conditioned on various other compounds is available upon reasonable request to the corresponding author at [sdkyuan@gmail.com](mailto:sdkyuan@gmail.com).

The example versions are trained on cuprates, but you can load the models trained on Pnictides, Others, or "Everything" to run the other versions if you wish.

You may also change the conditioning compound in `diffusion_1d_v4` to try conditioning conditional SuperDiff on different reference compounds.

The code used to create the formation energy distributions and visualize clustering data are also available. The file `ElemNet_formation_energy_prediction_cuprates.ipynb` was adapted and modified for our use (added filtering to remove compounds containing elements with atomic number > 86) from https://www.nature.com/articles/s41598-018-35934-y.

The code for the superconductor Tc prediction, classification, and clustering models are available at reasonable request (as they are from another work), and code for the other versions of SuperDiff run for experiments are also available upon reasonable request as well.
