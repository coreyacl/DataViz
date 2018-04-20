import matplotlib.pyplot as plt
import matplotlib.mathtext as mathtext
import matplotlib.patches as patches
import matplotlib
import numpy as np
import pandas as pd
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
    income = income // 10000
    for i in range(0,income):
        x = [0.2,0.7,.8,.3]
        y = [0.15 + i*0.05,0.15+i*0.05,0.25+i*0.05,0.25+i*0.05]
        ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=True, edgecolor = (0, 0, 0), facecolor = 'green'))
        ax.set_xticks([])
        ax.set_yticks([])
    ax.set_xlabel('Income (1 sheet = $10000)')
    plt.show()
    fig.savefig('income.png')

def create_population(population):
    pop = population //1000000
    image = Image.new('RGB', (400, 400))
    msg = 'Population Circle Diagram'
    font = ImageFont.truetype('DejaVuSans.ttf', 15)
    draw = ImageDraw.Draw(image)
    draw.ellipse((20, 20, 380, 380), fill = 'blue', outline ='blue')
    draw.text((0, 10), msg, (255, 255, 0), font = font)
    #draw.text((100, 100), msg, (255, 255, 0), font = font)
    #draw.text((10,10), "Hello world", font=font, fill=(255, 255, 0))
    draw.ellipse((200 - 180 * pop //320 ,200 - 180 * pop //320,
                200 + 180 * pop //320 , 200 + 180 * pop //320 ), 'red')
    image.show()
    image.save('Population circle diagram.png')
def create_table():
    vis = vincent.Map(width=1000, height=800)
    #Add the US county data and a new line color
    vis.geo_data(projection='albersUsa', scale=1000, counties=county_geo)
    vis + ('2B4ECF', 'marks', 0, 'properties', 'enter', 'stroke', 'value')

    #Add the state data, remove the fill, write Vega spec output to JSON
    vis.geo_data(states=state_geo)
    vis - ('fill', 'marks', 1, 'properties', 'enter')
    vis.to_json(path)
def create_happiness(a, b):
    fig, ax = plt.subplots()
    index = np.arange(2)
    bar_width = 0.3
    opacity = 0.8
    rects1 = plt.bar(index, [a,b], bar_width,
                 alpha=opacity,
                 color='r')
    plt.ylabel('Happiness Value')
    plt.title('Happiness Factor')
    plt.xticks(index, ('Average Job', 'Particular Job'))
    plt.tight_layout()
    plt.show()
    fig.savefig('Happiness_Factor.png')
create_population(65000000)
#create_income(65000)
#create_happiness(5, 7)
#create_table()
