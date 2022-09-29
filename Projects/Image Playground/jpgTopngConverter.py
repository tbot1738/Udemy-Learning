import os
import PIL.Image as image
import sys

path = sys.argv[1]
directory = sys.argv[2]
if not os.path.exists(directory):
    os.makedirs(directory)
# images = ["bulbasaur.jpg", "charmander.jpg", "pikachu.jpg", "squirtle.jpg"]
images = os.listdir(path)
for name in images:
    img = image.open(os.path.join(path, name))
    print(img)
    name_simple = name.split(".")
    img.save(f"{directory}{name_simple[0]}.png","png")
print(images)
