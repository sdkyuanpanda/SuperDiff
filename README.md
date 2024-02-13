# SuperDiff: Diffusion Models for Conditional Generation of Hypothetical New Families of Superconductors

## [Paper on arXiv](https://arxiv.org/abs/2402.00198)

This is the implementation of SuperDiff, a state-of-the-art method for computationally generating new hypothetical superconductors. SuperDiff is a new method for generating hypothetical superconductors using Diffusion Models and is the first computational superconductor generation method to generate hypothetical new families of superconductors and also the first to have support for conditioning on reference compounds. This repository contains the code, instructions, and model weights necessary to train or directly run a version of SuperDiff. SuperDiff was created by Samuel Yuan and Sasa Dordevic, you may reach us at [sdkyuan@gmail.com](mailto:sdkyuan@gmail.com) and [dsasa@uakron.edu](mailto:dsasa@uakron.edu).

<p align="center">
  <img src="https://github.com/sdkyuanpanda/SuperDiff/assets/49769610/fdf28dd9-4fdc-406b-bd3e-d4d67932ddc8" width="75%">
</p>

This repository also contains all the LaTeX code for the figures in the paper, which may be found in `paper/figures`.

<p align="center">
  <img src="https://github.com/sdkyuanpanda/SuperDiff/assets/49769610/66eefc6a-ca3a-41a4-a557-93fc49b9b08f" width="75%">
</p>




# Usage


# Training

For loading the pre-trained UNet for SuperDiff, which are located in `SuperDiff/checkpoints`
```python
from denoising_diffusion_pytorch import Unet1D
unet = Unet1D(
    dim = 48,
    dim_mults = (1, 2, 3, 6),
    channels = 1
)
unet.to(device)
unet.load_state_dict(torch.load(("cuprate5_unet_param_69.pth")))
```
The above is to load the `cuprate` model. Alternatively, the models for `others`, `pnictides`, or `everything` can be loaded as well, and the files for which are located in the same folder as well.
