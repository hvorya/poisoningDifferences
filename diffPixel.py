from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def compute_pixel_difference(image1_path, image2_path):
    # Load the two images
    img1 = Image.open(image1_path).convert('RGB')  # Convert to RGB to ensure consistent channels
    img2 = Image.open(image2_path).convert('RGB')
    
    # Ensure both images are the same size
    if img1.size != img2.size:
        raise ValueError("The images must be the same size for pixel-by-pixel comparison.")

    # Convert images to numpy arrays
    img1_np = np.array(img1)
    img2_np = np.array(img2)

    # Compute absolute difference
    difference_np = np.abs(img1_np - img2_np)

    # Convert the result to an image
    difference_img = Image.fromarray(difference_np.astype(np.uint8))

    # Display the original images and the difference image
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(img1)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title("Stego Image")
    plt.imshow(img2)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title("Difference Image")
    plt.imshow(difference_img)
    plt.axis('off')

    plt.show()

    return difference_img

# Example usage:
# Replace 'image1.png' and 'image2.png' with the file paths to your clear and stego images
difference_image = compute_pixel_difference('image1.png', 'image2.png')

