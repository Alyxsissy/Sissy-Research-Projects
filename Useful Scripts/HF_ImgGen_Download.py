# Install required libraries
#pip install huggingface_hub
#pip install joblib

# Import necessary libraries
from huggingface_hub import hf_hub_download
import joblib

# Define repository ID and filename
REPO_ID = "stabilityai/stable-diffusion-xl-base-1.0"  # replace with target repo ID
FILENAME = "sd_xl_base_1.0.safetensors"  # replace with target filename

# Download and load the model
model = joblib.load(hf_hub_download(repo_id=REPO_ID, filename=FILENAME))

# When run on Windows, model files will be located in C:\Users\<username>\.cache\huggingface\hub