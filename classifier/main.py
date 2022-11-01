from concurrent.futures import process
from preprocessing import Preprocess_Image
from model import generate_model
from keras.datasets import fashion_mnist

(trainX, trainy), (testX, testy) = fashion_mnist.load_data()
# ----------- Config -------------------------
target_size = [28, 28, 1]
classes = 10
data_type = "array"  # possible values are 'directory', 'array'
epochs = 30
batch_size = 32
model_name = 'fashion_model'  # Name with which it will save

assert (data_type in ['array', 'directory'],
        "possible values are 'directory', 'array'")

train_dir, valid_dir = None, None

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
model.save(f"{model_name}.h5")
