          # GRADIO AUTHENTICATION SETUP

          # Add these snippets to your app.py file to require a username and password.

import os
import gradio as gr

          # Define your Gradio app's interface and functions here

          # Environment variables for username and password
username = os.environ.get("MY_APP_USERNAME")
password = os.environ.get("MY_APP_PASSWORD")

          # Launch the Gradio app with basic authentication
app.launch(auth=(username, password))




                      # SET ENVIRONMENT VARIABLES
# MY_APP_USERNAME = "your_username"
# MY_APP_PASSWORD = "your_password"