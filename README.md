<img src="thumbnail.png" alt="thumbnail" width="300"/>

# Advanced Visualization Cookbook

[![nightly-build](https://github.com/ProjectPythia/advanced-viz-cookbook-template/actions/workflows/nightly-build.yaml/badge.svg)](https://github.com/ProjectPythia/advanced-viz-cookbook/actions/workflows/nightly-build.yaml)
[![Binder](https://binder.projectpythia.org/badge_logo.svg)](https://binder.projectpythia.org/v2/gh/ProjectPythia/advanced-viz-cookbook/main?labpath=notebooks)
[![DOI](https://zenodo.org/badge/671205314.svg)](https://zenodo.org/badge/latestdoi/671205314)

This Project Pythia Cookbook covers advanced visualization techniques building upon and combining various Python packages.

## Motivation

The possibilities of data visualization in Python are almost endless. Already using `matplotlib` the workhorse behind many visualization packages, the user has a lot of customization options available to them. `cartopy`,  `metpy`, `seaborn`, `geocat-viz`, and `datashader` are all also great packages that can offer unique additions to you Python visualization toolbox.

This Cookbook will house various visualization workflow examples that use different visualization packages, highlight the differences in functionality between the packages, any noteable syntax distinctions, and demonstrate combining tools to achieve a specific image. 

## Authors

[Julia Kent](@jukent)

### Contributors

<a href="https://github.com/ProjectPythia/advanced-viz-cookbook/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ProjectPythia/advanced-viz-cookbook" />
</a>

## Structure

This cookbook is broken up into two main sections - an "Overview" that compares different visualization packages and an "Example Workflows" section that houses a growing collection of advanced visualization applications.

### Overview

The overview contains foundational content for Python visualization and a compare contrast chart of different visualization packages available to the Scientific Python programmer. 

### Example Workflows

Example Worklfows demonstrate visualization applications that combine or use these packages in novel ways.

## Running the Notebooks

You can either run the notebook using [Binder](https://binder.projectpythia.org/) or on your local machine.

### Running on Binder

The simplest way to interact with a Jupyter Notebook is through
[Binder](https://binder.projectpythia.org/), which enables the execution of a
[Jupyter Book](https://jupyterbook.org) in the cloud. The details of how this works are not
important for now. All you need to know is how to launch a Pythia
Cookbooks chapter via Binder. Simply navigate your mouse to
the top right corner of the book chapter you are viewing and click
on the rocket ship icon, (see figure below), and be sure to select
“launch Binder”. After a moment you should be presented with a
notebook that you can interact with. I.e. you’ll be able to execute
and even change the example programs. You’ll see that the code cells
have no output at first, until you execute them by pressing
{kbd}`Shift`\+{kbd}`Enter`. Complete details on how to interact with
a live Jupyter notebook are described in [Getting Started with
Jupyter](https://foundations.projectpythia.org/foundations/getting-started-jupyter.html).

### Running on Your Own Machine

If you are interested in running this material locally on your com

1. Clone the `https://github.com/ProjectPythia/advanced-viz-cookbook` repository:

   ```bash
    git clone https://github.com/ProjectPythia/advanced-viz-cookbook.git
   ```

1. Move into the `advanced-viz-cookbook` directory
   ```bash
   cd advanced-viz-cookbook
   ```
1. Create and activate your conda environment from the `environment.yml` file
   ```bash
   conda env create -f environment.yml
   conda activate advanced-viz-cookbook
   ```
1. Move into the `notebooks` directory and start up Jupyterlab
   ```bash
   cd notebooks/
   jupyter lab
   ```
