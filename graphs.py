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
    income = income // 5000
    for i in range(0,income):
        x = [0.2,0.7,.8,.3]
        y = [0.15 + i*0.05,0.15+i*0.05,0.25+i*0.05,0.25+i*0.05]
        ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=False, color = 'green'))
        ax.set_xticks([])
        ax.set_yticks([])
    ax.set_xlabel('Income (1 sheet = $5000)')
    plt.show()

def create_population(population):
    image = Image.new('RGB', (200, 200))
    draw = ImageDraw.Draw(image)
    draw.ellipse((20, 20, 180, 180), fill = 'blue', outline ='blue')
    draw.ellipse((70, 70, 110, 110), 'red')
    image.show()

def create_table():
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
            'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
            'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
            'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    df = pd.DataFrame(np.random.randn(1,len(states)), columns = states)
    ax.table(cellText=df.values,colLabels=df.columns,loc = 'center')
    plt.show()
def create_happiness():
    fig, ax = plt.subplots()
    index = np.arange(1)
    bar_width = 0.15
    opacity = 0.8
    rects1 = plt.bar(index+bar_width, 5, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Averge Job')
    rects2 = plt.bar(index + 2*bar_width, 7, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Particular Job')
    plt.ylabel('Happiness Value')
    plt.title('Happiness Factor')
    plt.xticks(index + 3*bar_width, ('Average Job', 'Particular Job'))
    plt.legend()
    plt.tight_layout()
    plt.show()
#create_population(10)
#create_income(65000)
#create_happiness()
#create_table()
