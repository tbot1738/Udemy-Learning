from PIL import Image

img = Image.open("astro.jpg")

crop = img.resize((300, 300))
crop.save("reduced_astro.png", "png")

# Alternate Method for Creating a thumbnail

img.thumbnail((400, 400))
img.show()
