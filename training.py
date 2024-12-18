from ultralytics import YOLO
from helper import split_dataset
from modelling import train_model

# Set dataset directories and split the dataset into train, val, test

# image_directory = 'data/annotated/images'
# label_directory = 'data/annotated/labels'
# output_directory = 'split_test'
# split_dataset(image_directory, label_directory, output_directory)

# Load a model
model = YOLO("best.pt")  # load a pretrained model (recommended for training)

if __name__ == '__main__':

    # Train the model
    train_model(model, epochs=300, save_period=30)

    # Select best model checkpoint for model evaluation on validation or test set
    # and run model on validation or test set to get test results
    # To switch between validation or test set, modify the split argument with 'val' or 'test'

    # test_model = YOLO('best.pt')
    # test_results = test_model.val(split='test', plots=True, conf=0.25, batch=16, iou=0.6, device="0")

