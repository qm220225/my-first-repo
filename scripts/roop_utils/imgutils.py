from PIL import Image
import cv2
import numpy as np
from math import isqrt, ceil
import torch
from ifnude import detect
from scripts.roop_globals import SD_CONVERT_SCORE

def convert_to_sd(img):
    shapes = []
    chunks = detect(img)
    for chunk in chunks:
        shapes.append(chunk["score"] > SD_CONVERT_SCORE)
    return any(shapes)

def pil_to_cv2(pil_img):
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)


def cv2_to_pil(cv2_img):
    return Image.fromarray(cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB))

def torch_to_pil(images):
    """
    Convert a numpy image or a batch of images to a PIL image.
    """
    images = images.cpu().permute(0, 2, 3, 1).numpy()
    if images.ndim == 3:
        images = images[None, ...]
    images = (images * 255).round().astype("uint8")
    pil_images = [Image.fromarray(image) for image in images]
    return pil_images


def pil_to_torch(pil_images):
    """
    Convert a PIL image or a list of PIL images to a torch tensor or a batch of torch tensors.
    """
    if isinstance(pil_images, list):
        numpy_images = [np.array(image) for image in pil_images]
        torch_images = torch.from_numpy(np.stack(numpy_images)).permute(0, 3, 1, 2)
        return torch_images

    numpy_image = np.array(pil_images)
    torch_image = torch.from_numpy(numpy_image).permute(2, 0, 1)
    return torch_image

from collections import Counter
def create_square_image(image_list):
    """
    Creates a square image by combining multiple images in a grid pattern.
    
    Args:
        image_list (list): List of PIL Image objects to be combined.
        
    Returns:
        PIL Image object: The resulting square image.
        None: If the image_list is empty or contains only one image.
    """
    
    # Count the occurrences of each image size in the image_list
    size_counter = Counter(image.size for image in image_list)
    
    # Get the most common image size (size with the highest count)
    common_size = size_counter.most_common(1)[0][0]
    
    # Filter the image_list to include only images with the common size
    image_list = [image for image in image_list if image.size == common_size]
    
    # Get the dimensions (width and height) of the common size
    size = common_size
    
    # If there are more than one image in the image_list
    if len(image_list) > 1:
        num_images = len(image_list)
        
        # Calculate the number of rows and columns for the grid
        rows = isqrt(num_images)
        cols = ceil(num_images / rows)

        # Calculate the size of the square image
        square_size = (cols * size[0], rows * size[1])

        # Create a new RGB image with the square size
        square_image = Image.new("RGB", square_size)

        # Paste each image onto the square image at the appropriate position
        for i, image in enumerate(image_list):
            row = i // cols
            col = i % cols

            square_image.paste(image, (col * size[0], row * size[1]))

        # Return the resulting square image
        return square_image
    
    # Return None if there are no images or only one image in the image_list
    return None

def create_mask(image, box_coords):
    width, height = image.size
    mask = Image.new("L", (width, height), 255)
    x1, y1, x2, y2 = box_coords
    for x in range(width):
        for y in range(height):
            if x1 <= x <= x2 and y1 <= y <= y2:
                mask.putpixel((x, y), 255)
            else:
                mask.putpixel((x, y), 0)
    return mask