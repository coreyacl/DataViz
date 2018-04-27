import matplotlib.pyplot as plt
import matplotlib.mathtext as mathtext
import matplotlib.patches as patches
import matplotlib
import numpy as np
import pandas as pd
import plotly.plotly as py
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states
from PIL import Image, ImageDraw, ImageFont


data = pd.read_excel("files/OES_Report(1).xlsx")
df = pd.DataFrame(data)

"""
This is the information to input----
    For the profession:
        0 - Accountant
        1 - Software Developer
        2 - Mech E
        3 - Physicist
        4 - Surgeon
        5 - Farmers
        6 - Plumber
    For the data you want :
        #information by column
        employment = 1
        hourly_mean_wage = 3
        annual_mean_wage = 4
        hourly_median_wage = 8
        annual_median_wage = 13
"""

def get_profession_data(dataframe, profession, info_needed):
    """
    This code will take a string that exactly matches one in the file and
    one of the variables from above. It returns the specific value asked for."""
    output = dataframe.iloc[profession, info_needed]
    return output

def get_all_data(dataframe, profession, data_wanted):
    """This is the same as the previous one, except it takes all the data that you
    want (in list form) and returns a new list with the outputs."""
    final_list = []
    for i in data_wanted:
        final_list.append(get_profession_data(dataframe, profession, i))
    return final_list

def create_worktime(free_time, work_time, sleep):
    labels = 'Free Time', 'Work Time', 'Sleep'

    sizes = [free_time, work_time, sleep]
    explode = (0, 0.1, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels,
            autopct='%.0f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Ideal Daily Schedule')
    plt.show()
    fig1.savefig('Pie Chart.png')

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
    ax.set_title('Income for Engineer')
    plt.show()
    fig.savefig('income.png')

def create_population(population):
    pop = population //1000000
    W, H = (400, 400)
    image = Image.new('RGB', (W, H))
    msg = 'Population Circle Diagram'
    msg1 = 'U.S. Population'
    msg2 = 'Doctors'
    font = ImageFont.truetype('DejaVuSans.ttf', 15)
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(msg, font = font)
    w1, h1 = draw.textsize(msg1, font = font)
    w2, h2 = draw.textsize(msg2, font = font)
    draw.ellipse((40, 40, 360, 360), fill = 'blue', outline ='blue')
    draw.text(((W-w)/2, 20), msg, (255, 255, 0), font = font)
    draw.text(((W-w1)/2, (H-h1)/4), msg1, (255, 255, 0), font = font)
    #draw.text((100, 100), msg, (255, 255, 0), font = font)
    #draw.text((10,10), "Hello world", font=font, fill=(255, 255, 0))
    draw.ellipse((200 - 160 * pop //2.3 ,200 - 160 * pop //2.3,
                200 + 160 * pop //2.3 , 200 + 160 * pop //2.3), 'red')
    draw.text(((W-w2)/2, (H-h2)/2), msg2, (255, 255, 0), font = font)
    image.show()
    image.save('Population circle diagram.png')
def create_map():

    del states["HI"]
    del states["AK"]

    EXCLUDED = ("ak", "hi", "pr", "gu", "vi", "mp", "as")

    state_xs = [states[code]["lons"] for code in states]
    state_ys = [states[code]["lats"] for code in states]

    colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

    state_colors = []
    for state_id in states:
        #if states[state_id]["state"] in EXCLUDED:
        #    continue
        try:
            rate = 30
            idx = int(rate/6)
            state_colors.append(colors[idx])
        except KeyError:
            state_colors.append("black")

    p = figure(title="US Number of People with Occupation", toolbar_location="left",
               plot_width=1100, plot_height=700)

    p.patches(state_xs, state_ys, fill_color = state_colors,fill_alpha=0.7,
              line_color="#884444", line_width=2, line_alpha=0.3)

    output_file("choropleth.html", title="choropleth.py example")

    show(p)


def create_happiness(a, b):
    fig, ax = plt.subplots()
    index = np.arange(2)
    bar_width = 0.3
    opacity = 0.8
    rects1 = plt.bar(index, [a,b], bar_width,
                 alpha=opacity,
                 color='r')
    plt.ylabel('Suicide Rate (per 100000 people)')
    plt.title('Suicide Rate of Particular Job')
    plt.xticks(index, ('Average Job', 'Particular Job'))
    plt.tight_layout()
    plt.show()
    fig.savefig('Suicide Rate.png')
#create_population(get_profession_data(df,0,1))
#create_worktime(8, 4, 12)
#create_income(get_profession_data(df,2,4))
#create_happiness(5, 7)
create_map()
#print(get_profession_data(df,0,1))