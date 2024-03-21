# Latent Truth Detector in LLMs

## Description

This project is made in the context of the course IFT714 - Natural Language Processing at the University of Sherbrooke. The goal of this project is to implement a classifier that is able to predict when a LLM is lying based on the internal state of the model.

![Schéma entrées-sortie de notre modèle](<reports/figures/Schéma entrée sortie.jpg>)

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
This project use the [transformers](https://huggingface.co/transformers/) library to load the LLMs. The model currently used is the Llama-2-7b-hf model. If you want to try another model you should change the name in this [file](model/get_model.py). The model can then be downloaded with the following command.

**Download the model :**
```python
make model
```
You can generate yourself the activations of the model [here](notebooks/main.ipynb). Or you can download the activations that we generated from [huggingface](https://huggingface.co/datasets/Louzii/activations-weights-truth-dataset) and put it in /activations folder. You can also use this command to download it in the right folder.

**Download the activations :**
```python
make act
```