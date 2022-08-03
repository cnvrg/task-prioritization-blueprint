#Task Prioritization Train
Task prioritization is a machine learning technique that assigns a set of predefined categories to open-ended text. Text classifiers can be used to organize, structure, and categorize pretty much any kind of text.

[![N|Solid](https://cnvrg.io/wp-content/uploads/2018/12/logo-dark.png)](https://nodesource.com/products/nsolid)

# Retrain
This library is used to retrain the neural network on a custom dataset.
As a result, we get a model file that can be used to classify texts by their topics and sentiment. 
### Flow
- The user has to upload the training dataset which is a collection of possible messages mapped to their intent. The dataset should be in the format of a csv file containing two columns; the first is the intent and the second is the text. 
- The model is trained on the extended dataset and a model file is produced. The model can then be used for personalized text classification.

### Inputs
- `--data` refers to the base training dataset.
 
## How to run
```
python3 text_classification_train/retrain_intents_model.py --data <name of data file> --additional_data <name of additional data file>
```
Example:
```
python3 text_classification_train/retrain_intents_model.py --data 'data.csv' --additional_data 'additional_data.csv'
```