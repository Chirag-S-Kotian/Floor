import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path):
    """Load an image from the specified path."""
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found at {image_path}")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def convert_to_grayscale(image):
    """Convert the image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_gaussian_blur(image, kernel_size=(5, 5)):
    """Apply Gaussian blur to the image."""
    return cv2.GaussianBlur(image, kernel_size, 0)

def detect_edges(image, low_threshold=50, high_threshold=150):
    """Detect edges using the Canny edge detection algorithm."""
    return cv2.Canny(image, low_threshold, high_threshold)

def find_contours(image):
    """Find contours in the image."""
    contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def draw_contours(image, contours):
    """Draw contours on the image."""
    contour_image = image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
    return contour_image

def display_images(images, titles):
    """Display multiple images side by side."""
    plt.figure(figsize=(15, 5))
    for i in range(len(images)):
        plt.subplot(1, len(images), i + 1)
        if len(images[i].shape) == 2:
            plt.imshow(images[i], cmap='gray')
        else:
            plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

def process_image(image_path):
    """Process the image to detect edges and contours."""
    # Load the image
    image = load_image(image_path)
    if image is None:
        return

    # Convert to grayscale
    gray_image = convert_to_grayscale(image)

    # Apply Gaussian blur
    blurred_image = apply_gaussian_blur(gray_image)

    # Perform Canny edge detection
    edges = detect_edges(blurred_image)

    # Find contours
    contours = find_contours(edges)

    # Draw contours on the original image
    contour_image = draw_contours(image, contours)

    # Display results
    display_images([image, edges, contour_image], ['Original Image', 'Edge Detection', 'Contours'])

if __name__ == "__main__":
    # Provide the path to the image
    image_path = 'image.jpg'  

    # Process the image
    process_image(image_path)