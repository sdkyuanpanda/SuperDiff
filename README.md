# SuperDiff: Diffusion Models for Conditional Generation of Hypothetical New Families of Superconductors

## Authors: Samuel Yuan and S.V. Dordevic

## [Paper on arXiv](https://arxiv.org/abs/2402.00198)

This is the implementation of SuperDiff, a state-of-the-art method for computationally generating new hypothetical superconductors. SuperDiff is a new method for generating hypothetical superconductors using Diffusion Models and is the first computational superconductor generation method to generate hypothetical new families of superconductors and also the first to have support for conditioning on reference compounds. This repository contains the code, instructions, and model weights necessary to train or directly run a version of SuperDiff. SuperDiff was created by Samuel Yuan and Sasa Dordevic, you may reach us at [sdkyuan@gmail.com](mailto:sdkyuan@gmail.com) and [dsasa@uakron.edu](mailto:dsasa@uakron.edu).

<p align="center">
  <img src="https://github.com/sdkyuanpanda/SuperDiff/assets/49769610/fdf28dd9-4fdc-406b-bd3e-d4d67932ddc8" width="75%">
</p>

Pre-trained UNet(s) used for SuperDiff are available in `SuperDiff/checkpoints`, and `outputs` contain sample raw output data from one experiment with conditional SuperDiff and one experiment with unconditional SuperDiff.

<p align="center">
  <img src="https://github.com/sdkyuanpanda/SuperDiff/assets/49769610/66eefc6a-ca3a-41a4-a557-93fc49b9b08f" width="75%">
</p>

If you find this work useful, please cite it as

`@misc{yuan2024superdiff,
      title={SuperDiff: Diffusion Models for Conditional Generation of Hypothetical New Families of Superconductors}, 
      author={Samuel Yuan and S. V. Dordevic},
      year={2024},
      eprint={2402.00198},
      archivePrefix={arXiv},
      primaryClass={cond-mat.supr-con}
}`
