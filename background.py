from PIL import Image, ImageDraw, ImageFont

# Cria uma imagem em branco
width, height = 800, 600
image = Image.new('RGB', (width, height), color = (73, 109, 137))

# Cria um objeto ImageDraw
draw = ImageDraw.Draw(image)

# Define a fonte
font = ImageFont.load_default()

# Texto de exemplo (código Python)
text = """def hello_world():
    print("Hello, World!")

for i in range(10):
    print(i)
"""

# Desenha o texto na imagem
draw.text((10, 10), text, font=font, fill=(255, 255, 255))



# Salva a imagem
image.save("python_background.png")