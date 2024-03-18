# Latent Truth Detector in LLMs

## Description

This project is made in the context of the course IFT714 - Natural Language Processing at the University of Sherbrooke. The goal of this project is to implement a classifier that is able to predict when a LLM is lying based on the internal state of the model.

## Installation

Install the requirements in a virtual environment using the following command:
```python
make requirements
```

## Usage

This project uses the data published in the paper "The Internal State of an LLM Knows When It's Lying" by Amos Azaria and Tom Mitchell. [Doi: 10.48550/arXiv.2304.13734](https://doi.org/10.48550/arXiv.2304.13734)

The data can be downloaded from the link : [azariaa.com/Content/Datasets/true-false-dataset.zip](http://azariaa.com/Content/Datasets/true-false-dataset.zip). Or use the following command.

**Download the data and put it in the data folder :**

```python
make data
```

**Clean your data folder :**
```python
make clean
```
