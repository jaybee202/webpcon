# WebpCon

## Inspiration
A friend told me to try OpenAI's updated image generation.  After noticing that spotify allows you to add your own custom playlist icons, I had a perfect use case.  After quickly getting a few great artifacts I realized that ChatGPTs images are .webp and that as not compatable with Spotify (required .png/.jpg).  I was already in ChatGPT so it helped me create this program, readme.txt, and requirements.txt in seven prompts.

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

