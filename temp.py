import os
import requests


def download_image(url, folder_path):
    # Send a GET request to the image URL
    response = requests.get(url)

    # Extract the file name from the URL
    file_name = os.path.basename(url)

    # Create the folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # Save the image to the specified folder
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'wb') as file:
        file.write(response.content)

    print(f"Image downloaded and saved as: {file_path}")


# Example usage
image_url = 'https://replicate.delivery/pbxt/3FUFYumIgvooPBtzCqn68mvFFsI5RCM8MNxsDVfhDjw6J7eQA/output.png'
save_folder = 'static/output'

download_image(image_url, save_folder)
