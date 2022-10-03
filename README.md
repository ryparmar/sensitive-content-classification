# A simple training pipeline for sensitive-content article classification

By sensitive-content is meant child-abuse, rap

This pipeline is intended to be run on the [Paperspace Gradient platform](https://www.paperspace.com/gradient) 
(or any notebok-like environment with GPU access). 


## Pipeline steps

0. *00_prepare_environment.ipynb* - install packages and download data
1. *10_prepare_data.ipynb* - get the data and process them
2. *11_data_augmentation.ipynb* - due to the lack of data, this step augments them to increase the amount and improve robustnes of the classifier
3. *20_train_model.ipynb* - train the model using HuggingFace transformers library and log the model into MLflow
4. *30_predict.ipynb* - load the trained model and try it on some examples


## Data

Obviously, the data are not accessible in the repository, so the pipeline won't run.