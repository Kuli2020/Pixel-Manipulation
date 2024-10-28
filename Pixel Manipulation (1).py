pip install pillow

from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Apply a basic mathematical operation to each pixel
    encrypted_pixels = (pixels + key) % 256

    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Reverse the mathematical operation
    decrypted_pixels = (pixels - key) % 256

    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    key = 50  # Shift value for encryption/decryption
    encrypt_image("input_image.png", "encrypted_image.png", key)
    decrypt_image("encrypted_image.png", "decrypted_image.png", key)
