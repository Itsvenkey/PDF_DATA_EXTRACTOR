# PDF_DATA_EXTRACTOR

This repository contains the source code and files for the [Project Name] web application.

## Contents

- [Web App](./pdf) : The web app files are located in the `pdf` folder.
- [Scripts](./script) : The scripts for the project can be found in the `script` folder.

## Web App

The web application is designed to take image or pdf using radio button and process the file and extract the key value pairs from the pdf or image taken by the user and give a response with a table of fields and values extracted from the file.



## Scripts

This Python script is designed to extract key-value pairs from a PDF invoice document. The extracted data will be saved into a CSV file in csv_files folder for further analysis or processing  

the csv files created by extracted from images are named as image_output.csv

the csv files created by extracted from images are named as pdf_output.csv



## Getting Started

1. Clone the repository:

   ```bash
    https://github.com/Itsvenkey/PDF_DATA_EXTRACTOR.git

2. run the following command in your terminal in the present directory in pdf/pdf folder

    ```bash

    pipenv shell



3. go to the pdf/pdf directory and install the requirements:

    ```terminal
    pip install -r requirements.txt

4. then install the Tesseract OCR from the following link:

    ```browser
    https://tesseract-ocr.github.io/tessdoc/Downloads.html

5. go to views.py file and scrpt's task.py file look for the following line (usually its the same location in most cases if you dont change the installation location then you dont need to follow  this step)

    ```
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    ```


    and replace the following location 'C:\Program Files\Tesseract-OCR\tesseract' with the location of your installed tesseract-ocr\tesseract


6. then in the terminal run the following commands:

    ```
    py manage.py migrate

    py manage.py makemigrations

    py manage.py runserver

    ```

    and the website will run perfectly fine


7. to run the scripts exit from the virtual environment.
