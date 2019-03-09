import os, sys

# Library: pip install Pillow
from PIL import Image

# Python Version: 3.4
from pathlib import Path


def resize(image, size):
    return image.resize((size, size))


while True:
    inputFile = input("Please choose the image to resize to square size: ")
    currentPath = Path(os.path.abspath(os.path.dirname(__file__)))
    filePath = Path(inputFile)

    if filePath == Path(filePath.name):
        filePath = currentPath.joinpath(filePath)

    if not filePath.is_file():
        print("File not found.\n\n")
        continue

    outputPath = Path(os.path.split(filePath.absolute())[0])
    fileName, extension = os.path.splitext(filePath.name)
    outputFile = outputPath.joinpath(fileName + "_resized" + extension)
    count = 0
    while outputFile.is_file():
        outputFile = outputPath.joinpath(fileName + "_resized_" + str(count) + extension)
        count += 1

    try:
        image = Image.open(inputFile)
        size = min(image.size)
        newImage = resize(image, size)
        newImage.save(outputFile, image.format)
        image.close()
        newImage.close()
        print("Image output: {}\n\n".format(outputFile.absolute()))
    except:
        print("Unable to parse the file.\n\n")
