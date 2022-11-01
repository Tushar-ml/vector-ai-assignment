# Classification

This section contains the instructions of the file structure and flow of the code. Code in this section will be used further in different sections as well.

## File Structure

- <b>preprocessing.py</b> : This file contains utility class which helps you to load dataset in the Image Generator form from any directory, or array.

- <b>model.py:</b> This file contains the architecture and model prediction code.

- <b>train.py</b>: This file contains a general training flow which can provide you different configs to train your model. By `python3 train.py` will by default train faishon_mnist and stores the model in `models` folder.

## How to train a custom Model

1. First, setup config in train.py

   - target_size => Size of input you want in the model. eg : Fashion MNIST (28,28,1) or Cat v/s Dog (224,224,3)

   - classes => No of Classes in your dataset. Eg: Fashion MNIST: 10
   - data_type:

     - "array" - if you choose this data_type, you need to assign trainX, trainy, testX (optional), testY(optional) in array format

     - "directory" - if you choose this data_type, you need to assign train_dir, val_dir value in train.py

       - file structure of this directories must be like
         - train_dir /
           - class_1 /
           - class_2 /
         - test_dir /
           - class_1 /
           - class_2 /

   - epochs, batch_size => Setup these parameters for training
   - model_name => When model is saved it will be saved in models/{model_name}.h5. This will help you to distinguish

2. Run the code by `python3 train.py`

## How to test the code

Using the `predict_model` function in `model.py` you can get the predictions.

- loaded_model is required
- data with proper shape of format eg:(length_data, 224,224,3)
- n_classes : No of Classes

See example in part3 section
