# Latent Truth Detector in LLMs

## Description

This project is made in the context of the course IFT714 - Natural Language Processing at the University of Sherbrooke. The goal of this project is to implement a classifier that is able to predict when a LLM is lying based on the internal state of the model.

## Installation

Install the requirements in a virtual environment using the following command:
```python
make requirements
```

## Usage

This project uses the data published in the paper "The Geometry of Truth: Emergent Linear Structure in Large Language Model Representations of True/False Datasets", Marks, S., & Tegmark, M. (2023). [ArXiv, abs/2310.06824](https://api.semanticscholar.org/CorpusID:263831277)

The data can be downloaded from their [github](https://github.com/saprmarks/geometry-of-truth). Further information on how the datasets were made are in the paper and the github.

The data can be directly downloaded and put in the right folder with the following command.

**Download the data and put it in the data folder :**

```python
make data
```

**Clean your data folder :**
```python
make clean
```
