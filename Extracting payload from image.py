# EXTRACTING PAYLOAD FROM AN IMAGE

from PIL import Image

def extract_payload(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())
    
    binary_data = ''
    for pixel in pixels:
        for value in pixel[:3]:  # RGB channels only
            binary_data += bin(value)[-1]  # Extract LSB

    payload = int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder='big').decode('utf-8', errors='ignore')
    return payload

# Usage
payload = extract_payload('payload_image.png')
print(payload)
