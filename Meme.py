from PIL import Image, ImageDraw, ImageFont

print('Генератор мемов запущен!')

top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")

print(top_text, bottom_text)

print("Список картинок")
print("1.Кот в ресторане")
print("2.Кот в очках")
print("3.Sisyphus")
print("4.Чел нет, да")

picture = int(input("Введите номер картинки: "))

if picture == 1:
    picture_file = "Кот в ресторане.png"
elif picture == 4:
    picture_file = "Man no yes.jpg"
elif picture == 3:
    picture_file = "Sisyphus.jpg"
elif picture == 2:
    picture_file = "Кот в очках.png"
else:
    print("Неверный номер картинки")
    exit()

image = Image.open(picture_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0, 0), top_text)
text_width = text[2]

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill='blue')

text = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - text[2]) / 2, height - text[3] - 10), bottom_text, font=font, fill="blue")
image.save("new_meme.jpg")