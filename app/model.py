import os
import wandb
from loadotenv import load_env 
load_env()

# Local folder and filename for the downloaded model
MODELS_DIR = "../models"
MODEL_FILENAME = "best_model.pth"

os.makedirs(MODELS_DIR, exist_ok=True)


#TODO: wrap all this in a function

wandb_org = os.environ.get("WANDB_ORG")
wandb_project = os.environ.get("WANDB_PROJECT")
wandb_model_name = os.environ.get("WANDB_MODEL_NAME")
wandb_model_version = os.environ.get("WANDB_MODEL_VERSION")


wandb_api_key = os.getenv("WANDB_API_KEY")
wandb.login(key=wandb_api_key)
api = wandb.Api()

#artifact_path = "username/project_name/artifact_name:version"
# TODO: ensemble the artifact path from environment variables
#artifact_path = "antonios-org/mlops_dsr_batch_44/resnet18:v0"
artifact_path = f"{wandb_org}/{wandb_project}/{wandb_model_name}:{wandb_model_version}"
artifact = api.artifact(artifact_path, type="model")
artifact.download(root=MODELS_DIR)
