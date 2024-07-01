import numpy as np
import cv2
from scipy.io import wavfile
from PIL import Image

FILE_PATH = "./chall_stega.png"

class StegaPng:

    def __init__(self, image_path):
        self.image_path = image_path
        self.audio = None

    
    def extract_lsb_to_stereo(self, output_file):
        # Read the PNG image
        img = cv2.imread(self.image_path, cv2.IMREAD_UNCHANGED)
        
        # Extract all channels (RGBA)
        channels = [img[:, :, i] for i in range(4)]
        
        # Combine all channels into one array
        all_samples = np.vstack(channels)
        print("all samples: ", all_samples)
        
        # Extract LSBs from all channels
        lsb_samples = np.unpackbits(all_samples.flatten() & 1)
        print("all samples: ", lsb_samples)
        
        # Split the LSB samples into left and right channels
        left_channel = lsb_samples[::2]
        right_channel = lsb_samples[1::2]
        
        # Convert binary audio samples to int16
        left_channel_samples = np.packbits(left_channel).astype(np.int16)
        right_channel_samples = np.packbits(right_channel).astype(np.int16)
        
        # Write stereo audio to a WAV file
        stereo_samples = np.column_stack((left_channel_samples, right_channel_samples))
        wavfile.write(output_file, 44100, stereo_samples)

        print("Stereo audio file created successfully.")


    def extract_LSB(self):
        # Open the PNG image
        img = Image.open(self.image_path)
        
        # Convert the image to RGBA mode if it's not already in that mode
        img = img.convert('RGBA')
        
        # Get the image data
        data = img.getdata()
        
        # Extract the LSB of each color channel for each pixel
        lsb_data = []
        for pixel in data:
            r, g, b, a = pixel
            lsb_r = r   # Extract LSB of red channel
            lsb_g = r   # Extract LSB of green channel
            lsb_b = r   # Extract LSB of blue channel
            lsb_a = r   # Extract LSB of alpha channel
            lsb_data.append((lsb_r, lsb_g, lsb_b, lsb_a))
        
        # Create a new image using the LSBs extracted
        new_img = Image.new('RGBA', img.size)
        new_img.putdata(lsb_data)
        
        # Save the new image
        new_image_path = self.image_path.replace('.png', '_lsb_extracted.png')
        new_img.save(new_image_path)
        
        print("New image with LSB extracted saved as:", new_image_path)

if __name__ == '__main__':
    stegano = StegaPng(FILE_PATH)

    stegano.extract_LSB()