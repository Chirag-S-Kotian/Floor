# Image Processing with OpenCV

This Python program processes an image to detect edges and contours using OpenCV and displays the results using Matplotlib.

## Features

- Load an image from a specified path.
- Convert the image to grayscale.
- Apply Gaussian blur to the image.
- Detect edges using the Canny edge detection algorithm.
- Find and draw contours on the image.
- Display the original image, edge-detected image, and contour-drawn image side by side.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- Matplotlib

## Installation

1. Clone this repository or download the script.
2. Install the required libraries using pip:

```bash
pip install opencv-python numpy matplotlib
```

## Usage

1. Place the image you want to process in the same directory as the script or provide the path to the image.
2. Update the `image_path` variable in the `process_image` function call within the `__main__` section to the path of your image file.
3. Run the script:

```bash
python image_processing.py
```

## Code Explanation

### Functions

- `load_image(image_path)`: Loads an image from the specified path.
- `convert_to_grayscale(image)`: Converts the image to grayscale.
- `apply_gaussian_blur(image, kernel_size=(5, 5))`: Applies Gaussian blur to the image.
- `detect_edges(image, low_threshold=50, high_threshold=150)`: Detects edges using the Canny edge detection algorithm.
- `find_contours(image)`: Finds contours in the image.
- `draw_contours(image, contours)`: Draws contours on the image.
- `display_images(images, titles)`: Displays multiple images side by side using Matplotlib.
- `process_image(image_path)`: Processes the image to detect edges and contours and displays the results.

### Example

```python
if __name__ == "__main__":
    # Provide the path to the image
    image_path = 'image.jpg'  

    # Process the image
    process_image(image_path)
```

In this example, replace `'image.jpg'` with the path to your image file. The script will process the image and display the original image, edge-detected image, and image with contours.

## License

This project is licensed under the MIT License.

---
