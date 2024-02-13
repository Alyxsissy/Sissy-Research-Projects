# Install required libraries
#pip install huggingface_hub
#pip install transformers
#pip install joblib

# Import libraries
from transformers import AutoModelForCausalLM, AutoTokenizer

# Define the model name or path on the Hugging Face Hub
MODEL_NAME = "username/LLaMA-2-7b"  # Replace "username/LLaMA-2-7b" with the actual model path

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)