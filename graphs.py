import matplotlib.pyplot as plt
import matplotlib.mathtext as mathtext
import matplotlib.patches as patches
import matplotlib
from PIL import Image, ImageDraw, ImageFont

def create_worktime(free_time, work_time, sleep):
    labels = 'Free Time', 'Work Time', 'Sleep'
    sizes = [50, 50, 63]
    explode = (0, 0.1, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

def create_income(income):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    income = income // 5000
    for i in range(0,income):
        x = [0.1,0.6,.7,.2]
        y = [0.15 + i*0.05,0.15+i*0.05,0.25+i*0.05,0.25+i*0.05]
        ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False))
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()

def create_population(population):

    image = Image.new('RGB', (200, 200))
    fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 20)
    draw = ImageDraw.Draw(image)
    draw.ellipse((20, 20, 180, 180), fill = 'blue', outline ='blue')
    draw.ellipse((90, 90, 110, 110), 'red', 'red')
    draw.text((50,60), "World", font=fnt, fill=(255,255,255,255))
    image.show()
