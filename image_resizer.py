# Import pillow
# Open the image we want to resize using python
# Print the current size of that image
# Specify the size we wanna change it to
# Save the new resized image

from PIL import Image

# Take two integers to resize the image selected


def resize_image(size1, size2):
    image = Image.open('test.jpg')

    print(f'Current size : {image.size}')

    resized_image = image.resize((size1, size2))

    resized_image.save('resizedimage' + str(size1) + '.jpg')


while True:
    # Input for the size desired
    resize = input('Enter the dimensions you desire (EX 100x100):  ').lower()
    # Split the input in a list of two numbers (str)
    re = resize.split('x')
    # If the input is empty or not numxnum we ask for new input
    if resize == '':
        print('\nNOT VALID INPUT\n')
    else:
        try:
            int(re[0])
            try:
                int(re[1])
                break
            except:
                print('\nNOT VALID INPUT\n')
        except:
            print('\nNOT VALID INPUT\n')

print()
# Call the function with int arguments
resize_image(int(re[0]), int(re[1]))
