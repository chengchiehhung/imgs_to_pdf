import os
from PIL import Image

def convert_to_pdf(directory, output_filename):
    images = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.png')]
    images.sort()  # sort in alphabetical order

    converted_images = []

    # Open the first image and convert it to RGB mode
    image_1 = Image.open(images[0])
    image_1 = image_1.convert('RGB')

    # Get the dimensions of the first image
    width, height = image_1.size

    # Loop through the remaining images, resize them to match the dimensions of the first image, and convert them to RGB mode
    for image in images[1:]:
        image_o = Image.open(image)
        if image_o.size != (width, height):
            image_o = image_o.resize((width, height))
        image_o = image_o.convert('RGB')
        converted_images.append(image_o)
    
    # Save all the images, including the first one, to a PDF file using the save method of the first image object, with the save_all and append_images parameters
    image_1.save(rf'{output_filename}', save_all=True, append_images=converted_images, dpi=(1200, 1200))

if __name__ == '__main__':
    convert_to_pdf('images/', 'output.pdf')
