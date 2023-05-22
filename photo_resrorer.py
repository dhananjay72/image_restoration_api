import matplotlib.pyplot as plt
from PIL import Image
import replicate
from dotenv import load_dotenv
import os
import requests
import random
load_dotenv()
api_token = os.getenv("REPLICATE_API_TOKEN")
print("11111")
# model = replicate.models.get("tencentarc/gfpgan")
# version = model.versions.get("9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3")

# def predict_image(filename):
#     inputs = {
#         # Input
#         'img': open(filename, "rb"),
#         'version': "v1.4",
#         'scale' : 2,
#     }

#     output = version.predict(**inputs)
#     print(output)
#     return output
# def predict_image(filename):
#     output = replicate.run(
#         "tencentarc/gfpgan:9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856a3",
#         input={"img": open(filename, "rb")}
#     )
#     print(output)
#     return output

# img = 'E:\API_restore\static\imagesGT_p28.jpg'
# res = predict_image(img)
# plt.show(res)
selected_feature = ["Image Deblurring (GoPro)", "Image Denoising",
                    "Image Dehazing (Outdoor)", "Image Deraining (Rain drop)"]


def predict_image(filename, selected):
    print(selected)
    print(selected_feature[int(selected)-1])
    client = replicate.Client(
        api_token='r8_9SDYuPbLlGN6793l50I4LT9Si2plc4725SKDA')  # api_token)
    output = replicate.run(
        "google-research/maxim:494ca4d578293b4b93945115601b6a38190519da18467556ca223d219c3af9f9",
        input={
            "model": selected_feature[int(selected)-1],
            "image": open(filename, "rb")}
    )
    print(output)
    save_folder = 'static/output'

    download_image(output, save_folder)
    return output


# def save_image_from_url(image_url, folder_path, custom_name=None):
#     # Send a GET request to the image URL
#     response = requests.get(image_url)

#     # Extract the filename from the URL or use the custom name
#     if custom_name:
#         filename = str(custom_name)
#     else:
#         filename = os.path.basename(image_url)

#     # Construct the file path to save the image
#     file_path = os.path.join(folder_path, filename)

#     # Save the image to the specified folder
#     with open(file_path, 'wb') as f:
#         f.write(response.content)

#     print(f"Image saved successfully at {file_path}")

# def save_image_from_url(image_url, folder_path, custom_name=None):
#     # Send a GET request to the image URL
#     response = requests.get(image_url)

#     # Extract the filename from the URL or use the custom name
#     if custom_name:
#         filename = str(custom_name)
#     else:
#         filename = os.path.basename(image_url)

#     # Remove invalid characters from the filename
#     filename = "".join(c for c in filename if c.isalnum() or c in "_-.")

#     # Construct the file path to save the image
#     file_path = os.path.join(folder_path, filename)

#     # Save the image to the specified folder
#     with open(file_path, 'wb') as f:
#         f.write(response.content)

#     print(f"Image saved successfully at {file_path}")


# img_path = 'E:\API_restore\static\imagesGT_p28.jpg'
# res = predict_image(img_path)

# # Save the output image to a file
# with open('output.png', 'wb') as f:
#     f.write(res['output'].read())

# # Open the output image using PIL and display it
# output_img = Image.open('output.png')
# output_img.show()


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
