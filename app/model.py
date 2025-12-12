import os
import wandb
from loadotenv import load_env 
load_env()

# Local folder and filename for the downloaded model
MODELS_DIR = "../models"
MODEL_FILENAME = "best_model.pth"

os.makedirs(MODELS_DIR, exist_ok=True)


<<<<<<< HEAD
def download_model():
    """
    Download a model artifact from Weights & Biases.
    
    Retrieves W&B configuration from environment variables and downloads
    the specified model artifact to the local models directory.
    
    Environment variables required:
        WANDB_ORG: W&B organization name
        WANDB_PROJECT: W&B project name
        WANDB_MODEL_NAME: Name of the model artifact
        WANDB_MODEL_VERSION: Version of the model artifact
        WANDB_API_KEY: W&B API key for authentication
    
    Returns:
        wandb.Artifact: The downloaded artifact object
    """
=======
def download_artifact():
    # this will raise an assertion error if the variable is not found
    assert 'WANDB_API_KEY' in os.environ, "WANDB_API_KEY not found in environment variables"
>>>>>>> 01d1a7a (adding changes to hello.py and model.py)
    wandb_org = os.environ.get("WANDB_ORG")
    wandb_project = os.environ.get("WANDB_PROJECT")
    wandb_model_name = os.environ.get("WANDB_MODEL_NAME")
    wandb_model_version = os.environ.get("WANDB_MODEL_VERSION")
<<<<<<< HEAD
    
    wandb_api_key = os.getenv("WANDB_API_KEY")
    wandb.login(key=wandb_api_key)
    api = wandb.Api()
    
    artifact_path = f"{wandb_org}/{wandb_project}/{wandb_model_name}:{wandb_model_version}"
    artifact = api.artifact(artifact_path, type="model")
    artifact.download(root=MODELS_DIR)
    
    return artifact


if __name__ == "__main__":
    download_model()
=======


    wandb_api_key = os.getenv("WANDB_API_KEY")
    wandb.login(key=wandb_api_key)
    api = wandb.Api()

    #artifact_path = "username/project_name/artifact_name:version"
    # TODO: ensemble the artifact path from environment variables
    #artifact_path = "antonios-org/mlops_dsr_batch_44/resnet18:v0"
    artifact_path = f"{wandb_org}/{wandb_project}/{wandb_model_name}:{wandb_model_version}"
    artifact = api.artifact(artifact_path, type="model")
    print(f"Downloading artifact from {artifact_path}")

    artifact.download(root=MODELS_DIR)


download_artifact()
>>>>>>> 01d1a7a (adding changes to hello.py and model.py)
