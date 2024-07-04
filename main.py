from PIL import Image

# ascii conversion (light --> dark)
ASCII = "`^\”,:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

img_path = "./charmander.jpg"
output_path = "output.txt"

def calcBrightness(pixel):
    '''
    brightness calculated using this formula: (0.2126*R + 0.7152*G + 0.0722*B)
    0-255
    '''
    return 0.2126*pixel[0] + 0.7152*pixel[1] + 0.0722*pixel[2]

def convertToAscii(brightness):
    '''
    
    '''
    ascii_index = int((len(ASCII) - 1) * (brightness/255))
    return ASCII[ascii_index]


def main():
    # load image
    im = Image.open(img_path)
    width, height = im.size

    pixels = im.load() # get pixel data of img in (r, g, b, a) format
    output = '' # ascii output

    compression = 25

    # convert each pixel to an ASCII character based on brightness
    for y in range(0, height, compression):
        for x in range(0, width, compression):
            avg_brightness = 0

            for yExtra in range(compression):
                for xExtra in range(compression):
                    if x+xExtra >= width or y+yExtra >= height:
                        pixel_data = pixels[x, y]
                    else:
                        pixel_data = pixels[x+xExtra, y+yExtra]

                    avg_brightness += calcBrightness(pixel_data)
    
            avg_brightness = avg_brightness / (compression*compression)
            output += convertToAscii(avg_brightness)
        output += '\n'


    # save to text file
    f = open(output_path, "w")
    f.write(output)
    f.close()

    print('done!')


if __name__ == '__main__':
    main()