# WebpCon

## Inspiration
A friend told me to try OpenAI's updated image generation. After noticing that Spotify allows you to add your own custom playlist icons, I had the perfect use case. After quickly generating a few great images, I realized that ChatGPT's images are in .webp format, which is not compatible with Spotify (which requires .png or .jpg). Since I was already using ChatGPT, used it to create this program, README.txt, and requirements.txt in just seven prompts.

If you ever find yourself with a bunch of .webp files, you can use this program to convert them to .png or .jpg—individually, by folder, or for an entire repository.

Please enjoy!

## Description
WebpCon is a simple GUI application built using PyQt5 that allows users to convert `.webp` images to `.png` or `.jpg` formats. Users can select either a single file or an entire folder for conversion, with an option to include subfolders.

## Features
- Convert `.webp` images to `.png` or `.jpg`
- Select a single file or an entire folder
- Option to include subfolders during batch conversion
- User-friendly graphical interface

## Installation
### Prerequisites
Ensure you have Python installed (version 3.6 or higher).

### Install Required Dependencies
Run the following command to install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
1. Launch the application by running:
   ```
   python webp_converter.py
   ```
2. Follow these steps within the GUI:
   - **Step 1**: Choose whether to convert to PNG or JPG.
   - **Step 2**: If selecting a folder, decide whether to include subfolders.
   - **Step 3**: Select a file or folder to process.
   - **Step 4**: The program will process the images and notify you when done.

## License
This project is licensed under the MIT License.

