
# 
# Use Instructions and What's In This Repo

## Use Instructions

Pre-trained UNETs are available in `SuperDiff/checkpoints` and training dataset is available in `Datasets`. 

## What's in this repo?

This folder `SuperDiff` contains a sample unconditional and conditional SuperDiff version: `diffusion_1d_v3` is the unconditional version of SuperDiff and `diffusion_1d_v4` is the conditional version. 

The example versions are trained on cuprates, but you can load the models trained on Pnictides, Others, or "Everything" to run the other versions if you wish.

You may also change the conditioning compound in `diffusion_1d_v4` to try conditioning conditional SuperDiff on different reference compounds.

The code used to create the formation energy distributions and visualize clustering data are also available.

The code for the superconductor Tc prediction, classification, and clustering models are available at reasonable request (as they are from another work), and code for the other versions of SuperDiff run for experiments are also available upon reasonable request as well.
