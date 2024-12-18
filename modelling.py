import wandb
from wandb.integration.ultralytics import add_wandb_callback
from ultralytics import YOLO

def train_model(model, data='datasets/dataset.yaml', epochs=100, imgsz=640, batch=16, workers=0, project='yolov8_mbs', device=0, save_period=10):

    # Initialize a Weights & Biases run
    wandb.init(project="yolov8_mbs", job_type="training")

    # Add W&B Callback for Ultralytics
    add_wandb_callback(model, enable_model_checkpointing=False)

    # Train model
    model.train(data=data, epochs=epochs, imgsz=imgsz, batch=batch, workers=workers, project=project, device=device, save_period=save_period)

    # Finish the W&B run
    wandb.finish()
