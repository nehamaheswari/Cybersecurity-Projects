from PIL import Image
import os

def encrypt_image(image_path, encryption_key):
    try:
        image = Image.open(image_path)
        width, height = image.size
        pixels = image.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                
                pixels[x, y] = (r + encryption_key, g + encryption_key, b + encryption_key)

        encrypted_image_path = os.path.splitext(image_path)[0] + "_encrypted" + os.path.splitext(image_path)[1]
        image.save(encrypted_image_path)
        print(f"Image encrypted and saved as {encrypted_image_path}")
        return encrypted_image_path
    except Exception as e:
        print(f"Error encrypting image: {e}")

def decrypt_image(encrypted_image_path, encryption_key):
    try:
        encrypted_image = Image.open(encrypted_image_path)
        width, height = encrypted_image.size
        encrypted_pixels = encrypted_image.load()

        for x in range(width):
            for y in range(height):
                r, g, b = encrypted_pixels[x, y]
                
                encrypted_pixels[x, y] = (r - encryption_key, g - encryption_key, b - encryption_key)

        decrypted_image_path = os.path.splitext(encrypted_image_path)[0] + "_decrypted" + os.path.splitext(encrypted_image_path)[1]
        encrypted_image.save(decrypted_image_path)
        print(f"Image decrypted and saved as {decrypted_image_path}")
        return decrypted_image_path
    except Exception as e:
        print(f"Error decrypting image: {e}")

def main():
    print("Welcome to the Image Encryption Tool")
    print("------------------------------------")
    image_path = input("Enter the path to the image file: ")
    encryption_key = int(input("Enter the encryption key (an integer value): "))

    encrypted_image_path = encrypt_image(image_path, encryption_key)

    decrypt_choice = input("Decrypt image? (y/n): ").lower()
    if decrypt_choice == 'y':
        decrypted_image_path = decrypt_image(encrypted_image_path, encryption_key)

        preview_choice = input("Preview original and decrypted images? (y/n): ").lower()
        if preview_choice == 'y':
            try:
                Image.open(image_path).show()
                Image.open(decrypted_image_path).show()
            except Exception as e:
                print(f"Error previewing images: {e}")

if __name__ == "__main__":
    main()
