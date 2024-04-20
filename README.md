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
This project use the [transformers](https://huggingface.co/transformers/) library to load the LLMs. The model currently used is the Qwen/Qwen1.5-0.5B model. If you want to try another model you should change the name in this [file](model/get_model.py). The model can then be downloaded with the following command.

**Download the model :**
```python
make model
```
You can generate yourself the activations of the model [here](notebooks/main.ipynb). Or you can download the activations that we generated from [huggingface](https://huggingface.co/datasets/Louzii/activations-weights-truth-dataset) and put it in /activations folder. You can also use this command to download it in the right folder.

**Download the activations :**
```python
make act
```

## Notebooks

The notebooks folder contains the notebooks that we used to generate the activations and to train the classifier. The main notebook is [main.ipynb](notebooks/main.ipynb). It contains the code to generate the activations. 

Other important notebooks are [visualize.ipynb](notebooks/visualize.ipynb) that contains the code to visualize the PCA of the activations and [classification.ipynb](notebooks/classification.ipynb) that contains the code to train the classifier and visualize the neurons importance.

[generate_answers.ipynb](notebooks/generate_answers.ipynb) is a notebook that were we used models to generate answers to the questions of the dataset. We used the [Qwen/Qwen1.5-0.5B](https://huggingface.co/Qwen/Qwen1.5-0.5B) in order to see if the change of the activation of neurons during inference would change the answer. But the results were not conclusive and we didn't spend much time on this.

We created a datasets of assertions using geopardy and the Qwen/Qwen1.5-0.5B model. The notebook [jeopardy_parsing.ipynb](notebooks/jeopardy_parsing.ipynb) contains the code to generate the dataset.

[baseline.ipynb](notebooks/baseline.ipynb) contains the code to train Bert classifier on the dataset to compare the results with our model.

Finaly [classification_cities.ipynb](notebooks/classification_cities.ipynb) contains the code to compare the accuracy of the models (Qwen, Qwen-chat using prompt template and Qwen-chat) trained on variaus datasets (cities, cities_new, counterfact_cities, cities_augm) that are variations of the cities dataset.

## Find the data 

The activations data can be found in Huggingface datasets [here](https://huggingface.co/datasets/Louzii/activations-weights-truth-dataset)

And our created datasets can be found [here](https://huggingface.co/datasets/Louzii/cities-variants)

The Bert model trained on the cities dataset can be found [here](https://huggingface.co/Louzii/bert-models-truth)