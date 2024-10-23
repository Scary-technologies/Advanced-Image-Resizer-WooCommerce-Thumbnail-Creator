# Advanced Image Resizer & WooCommerce Thumbnail Creator

## Overview
The **Advanced Image Resizer & WooCommerce Thumbnail Creator** is a versatile desktop application that allows users to resize and crop images for use in WooCommerce, as well as for other purposes. The application provides options to create different size thumbnails commonly used in WooCommerce product galleries, including standard and custom dimensions. The application also includes an option to convert images to the WebP format, providing optimized image sizes suitable for web usage.

## Features
- **Select Input Image**: Users can select an image file (JPEG, PNG) as input for resizing and cropping.
- **Choose Output Folder**: Select a directory to save the processed images.
- **Crop Sizes**: Several common crop sizes are provided, such as thumbnails, medium, large, and WooCommerce gallery sizes. Users can select one or more sizes.
- **Select All Sizes**: Easily select or deselect all crop sizes.
- **Convert to WebP**: Convert images to WebP format to reduce file size and improve web performance.
- **Progress Tracking**: Progress bar to visualize the current progress while processing multiple images.
- **Logs Table**: Displays details of processed images, showing the filename and status of completion.
- **Responsive UI**: The user interface adjusts dynamically for better user experience.
- **GitHub Repository**: Quick link to the GitHub repository for further exploration.

## Prerequisites
- Python 3.x
- The following Python libraries are required:
  - `tkinter`
  - `Pillow`
  - `os`
  - `threading`
  - `cv2` (OpenCV, optional)

You can install the required libraries using:
```sh
pip install Pillow opencv-python
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Scary-technologies/Advanced-Image-Resizer-WooCommerce-Thumbnail-Creator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Advanced-Image-Resizer-WooCommerce-Thumbnail-Creator
   ```
3. Make sure all dependencies are installed.

## Usage
1. Run the script:
   ```sh
   python script.py
   ```
2. Use the interface to:
   - **Select an input image**.
   - **Choose an output folder** to save resized images.
   - **Select crop sizes** (or click "Select All Sizes").
   - **Convert to WebP** if desired.
3. Click the **Process** button to start resizing and cropping.
4. Monitor the **Progress Bar** and check the **Log Table** to track the process.


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## GitHub Repository
For more details, source code, and contributions, visit the GitHub repository:  
[Advanced Image Resizer & WooCommerce Thumbnail Creator](https://github.com/Scary-technologies/Advanced-Image-Resizer-WooCommerce-Thumbnail-Creator)

## Credits
- Developed by Scary Technologies.
- Icons used in the application: `Logo.ico` (included in the project directory).

Feel free to contribute or report any issues via the GitHub repository.

