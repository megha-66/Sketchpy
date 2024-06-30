from sketchpy import canvas 
one = canvas.sketch_from_image(r"C:\Users\prach\OneDrive\Documents\Desktop\megha_resized.jpg")
one.draw(threshold = 30) # Here, you can try various threshold values as per you!

# Here I have used a resized image. Resizing is essential sometimes, so that 
# the sketch of full image is obtained!!