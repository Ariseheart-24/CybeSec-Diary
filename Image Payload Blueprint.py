#ENCODING PAYLOAD INTO AN IMAGE

from PIL import Image

def encode_image(image_path, data, output_path):
    image = Image.open(image_path)
    binary_data = ''.join(format(ord(char), '08b') for char in data)
    binary_data += '1111111111111110'  # End of data delimiter

    data_index = 0
    pixels = list(image.getdata())
    
    new_pixels = []
    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):
            if data_index < len(binary_data):
                new_pixel[i] = new_pixel[i] & 254 | int(binary_data[data_index])
                data_index += 1
        new_pixels.append(tuple(new_pixel))

    new_image = Image.new(image.mode, image.size)
    new_image.putdata(new_pixels)
    new_image.save(output_path)

def decode_image(image_path):
    image = Image.open(image_path)
    pixels = list(image.getdata())

    binary_data = ''
    for pixel in pixels:
        for i in range(3):
            binary_data += str(pixel[i] & 1)

    binary_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    data = ''.join([chr(int(byte, 2)) for byte in binary_data])
    return data.split('1111111111111110')[0]

# Usage
encode_image('input.png', 'Secret Message', 'encoded.png')
decoded_message = decode_image('encoded.png')
print(decoded_message)
