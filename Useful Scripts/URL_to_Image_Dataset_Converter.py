# A Python script for converting URL-based datasets into image datasets. It downloads images from provided URLs, saves them locally, and allows for optional upload to the Hugging Face hub.

# REQUIREMENTS

# datasets==2.16.1
# pandas==2.1.4
# Requests==2.31.0
# tqdm==4.66.1

from datasets import load_dataset
import requests
import os
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

def download_image(url, folder_name, image_id, progress):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        image_path = os.path.join(folder_name, f"{image_id}.jpg")
        with open(image_path, 'wb') as file:
            file.write(response.content)
        progress.update(1)
        return image_path
    except Exception:
        progress.update(1)
        return None

def download_images(entries, folder_name, url_col):
    progress = tqdm(total=len(entries), desc="Downloading images")
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(download_image, entry[url_col], folder_name, i, progress) for i, entry in enumerate(entries)]
        for future in futures:
            future.result()
    progress.close()

def main():
    dataset_name = input("Name of dataset to convert: ")
    url_col = input("URL column: ")
    caption_col = input("Caption column: ")
    push_to_hub = input("Push dataset to hub? (y/n): ").lower().strip() == "y"

    if push_to_hub:
        hf_repo_id = input("HuggingFace repo ID: ")
        hf_token = input("HuggingFace token (write access): ")

    dataset = load_dataset(dataset_name)
    train_dataset = dataset['train']

    folder_name = f"{dataset_name.split('/')[1]}_images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    download_images(train_dataset, folder_name, url_col)

    metadata = []
    for i, entry in tqdm(enumerate(train_dataset), total=len(train_dataset), desc="Collecting metadata"):
        image_path = os.path.join(folder_name, f"{i}.jpg")
        if os.path.exists(image_path):
            metadata.append({'file_name': f'{i}.jpg', 'caption': entry[caption_col]})

    metadata_df = pd.DataFrame(metadata)
    metadata_csv_path = os.path.join(folder_name, "metadata.csv")
    metadata_df.to_csv(metadata_csv_path, index=False)

    if push_to_hub:
        converted_dataset = load_dataset('imagefolder', data_dir=folder_name)
        converted_dataset.push_to_hub(hf_repo_id, token=hf_token)
        print(f'Successfully uploaded dataset to hub https://huggingface.co/datasets/{hf_repo_id}.')

    print("Dataset processing complete.")

if __name__ == "__main__":
    main()