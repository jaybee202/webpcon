import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QRadioButton, QCheckBox, QMessageBox, QLabel
from PIL import Image

class WebpConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("WebpCon")
        self.resize(550, 200)  # Increase window size
        
        layout = QVBoxLayout()
        
        title = QLabel("WebpCon", self)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)
        
        description = QLabel("This program converts .webp images to .png or .jpg formats individually, by folder, or by repository.\n")
        layout.addWidget(description)
        
        step1 = QLabel("Step 1: Choose whether to convert to PNG or JPG.")
        layout.addWidget(step1)
        
        self.radioPng = QRadioButton('Convert to PNG')
        self.radioPng.setChecked(True)
        layout.addWidget(self.radioPng)
        
        self.radioJpg = QRadioButton('Convert to JPG')
        layout.addWidget(self.radioJpg)
        
        step2 = QLabel("Step 2: If selecting a folder, choose whether to include subfolders.")
        layout.addWidget(step2)
        
        self.checkSubfolders = QCheckBox('Include Subfolders')
        layout.addWidget(self.checkSubfolders)
        
        step3 = QLabel("Step 3: Select a file or a folder containing .webp images.")
        layout.addWidget(step3)

        step4 = QLabel("Step 4: The program will process the images and notify you when done.")
        layout.addWidget(step4)
        
        self.selectFileButton = QPushButton('Select File', self)
        self.selectFileButton.clicked.connect(self.selectFile)
        layout.addWidget(self.selectFileButton)
        
        self.selectFolderButton = QPushButton('Select Folder', self)
        self.selectFolderButton.clicked.connect(self.selectFolder)
        layout.addWidget(self.selectFolderButton)
        
        self.setLayout(layout)
    
    def selectFile(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select WebP File', '', 'WebP Files (*.webp);;All Files (*)', options=options)
        if file_path:
            self.convertFile(file_path)
    
    def selectFolder(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder', options=options)
        if folder_path:
            self.convertFolder(folder_path)
    
    def convertFile(self, file_path):
        if file_path.lower().endswith('.webp'):
            output_format = 'PNG' if self.radioPng.isChecked() else 'JPEG'
            output_extension = 'png' if self.radioPng.isChecked() else 'jpg'
            output_path = os.path.splitext(file_path)[0] + f'.{output_extension}'
            
            with Image.open(file_path) as img:
                img = img.convert('RGB')
                img.save(output_path, output_format, quality=95)
            
            self.showDoneMessage()
    
    def convertFolder(self, folder_path):
        include_subfolders = self.checkSubfolders.isChecked()
        output_format = 'PNG' if self.radioPng.isChecked() else 'JPEG'
        output_extension = 'png' if self.radioPng.isChecked() else 'jpg'
        
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith('.webp'):
                    file_path = os.path.join(root, file)
                    output_path = os.path.splitext(file_path)[0] + f'.{output_extension}'
                    
                    with Image.open(file_path) as img:
                        img = img.convert('RGB')
                        img.save(output_path, output_format, quality=95)
            
            if not include_subfolders:
                break
        
        self.showDoneMessage()
    
    def showDoneMessage(self):
        msgBox = QMessageBox()
        msgBox.setText("All done!")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = WebpConverter()
    converter.show()
    sys.exit(app.exec_())