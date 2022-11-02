from classifier.preprocessing import Preprocess_Image
from classifier.model import generate_model
from keras.datasets import fashion_mnist
import os

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


# ----------- Config -------------------------
target_size = [28, 28, 1]
classes = 10
data_type = "array"  # possible values are 'directory', 'array'
epochs = 30
batch_size = 32
model_name = 'fashion_model'  # Name with which it will save

assert (data_type in ['array', 'directory'],
        "possible values are 'directory', 'array'")

train_dir, valid_dir = None, None  # Only needed when data_type = "directory"

# Only needed when data_type = "array"
(trainX, trainy), (testX, testy) = fashion_mnist.load_data()

# ----------- Data Preprocess --------------------------
processor = Preprocess_Image(
    num_classes=classes, batch_size=batch_size, target_image_size=target_size)

if data_type == 'array':
    train_gen, valid_gen = processor.Get_Data_from_Array(
        trainX, trainy, testX, testy)

else:
    train_gen, valid_gen = processor.Get_Images_from_Directory(
        training_images_directory=train_dir, validation_images_directory=valid_dir)


# ---------------- Training Model ----------------------
model = generate_model(target_size, classes)

history = model.fit(train_gen, epochs=epochs, validation_data=valid_gen)
model.save(f"{ROOT_DIR}/models/{model_name}.h5")
print("Model has been saved")
