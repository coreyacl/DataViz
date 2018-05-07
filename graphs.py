import matplotlib.pyplot as plt
import matplotlib.mathtext as mathtext
import matplotlib.patches as patches
import matplotlib
import numpy as np
import pandas as pd
import bokeh
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_states import data as states
from PIL import Image, ImageDraw, ImageFont
import datacollection as dt

"""
These are the datasets used to generate graphs.
"""
data = pd.read_excel("files/OES_Report(1).xlsx")
df = pd.DataFrame(data)

OES = pd.read_excel("files/OES_Report(1).xlsx")
OES_df = pd.DataFrame(OES)

timework = pd.read_csv("files/tabula-timework.csv")
timework_df = pd.DataFrame(timework)

suiciderate = pd.read_csv("files/suiciderate.csv")
suiciderate_df = pd.DataFrame(suiciderate)

divorcerate  = pd.read_csv('files/tabula-divorce.csv')
divorcerate_df = pd.DataFrame(divorcerate)

gender = pd.read_csv('files/tabula-gender.csv')
gender_df = pd.DataFrame(gender)

spending = pd.read_csv('files/tabula-spending.csv')
spending_df = pd.DataFrame(spending)

race = pd.read_excel("files/race.xlsx")
race_df = pd.DataFrame(race)


def get_gender(a, b):
    """
    This function generates a pie chart for gender ratio in particular occupation.
    The first argument is male percentage, the second argument is female percentage.
    """
    new_labels = 'Male', 'Female'
    new_sizes = [a, b]
    explode = (0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(new_sizes, explode=explode, labels=new_labels,
            autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Gender Ratio')
    plt.show()
    fig1.savefig('gender.png', transparent = True)

def get_race(a, b, c, d):
    """
    This function generates a pie chart for ethnicity ratio in particular occupation.
    The order of argument is White, Black or African American, Asian, and Hispanic or Latino.
    """
    new_labels = 'White', 'Black or African American', 'Asian', 'Hispanic or Latino'
    new_sizes = [a, b, c, d]
    explode = (0, 0, 0.2, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(new_sizes, explode=explode, labels=new_labels,
            autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')
    plt.title('Ethnicity Ratio')

    plt.show()
    fig1.savefig('race.png', transparent = True)

def create_worktime(work_time):
    """
    This function creates a histogram that shows the percentage of workers
    working throughout the 24 hour period.
    """
    fig, ax = plt.subplots()
    time_list = work_time[0].index.tolist() + work_time[1].index.tolist()
    percent_list = work_time[0].tolist() + work_time[1].tolist()
    percent_list = [x for x in percent_list if "plumber" not in x]
    time_list = [x for x in time_list if "occupation" not in x]
    percent_list = list(map(float, percent_list))
    for i in range(12, 24):
        string = time_list[i]
        if i == 12:
            string = str(i) + ' pm'
        else:
            string = str(i-12) + ' pm'
        time_list[i] = string
    y_pos = np.arange(len(time_list))
    bar = plt.bar(y_pos, percent_list, align='center', alpha=0.5)
    plt.xticks(y_pos, time_list, rotation = 'vertical')
    plt.ylabel('Percent of People at Work')
    plt.title('When do they work?')
    plt.show()
    fig.savefig('time.png', transparent = True)
    return time_list
def create_income(income):
    """
    This function creates a diagram that represents income using stack
    of "paper bills", which are green parallelograms. Each bill represents
    $10000.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    income = int(income) // 10000
    for i in range(0,income):
        x = [0.2,0.7,.8,.3]
        y = [0.15 + i*0.05,0.15+i*0.05,0.25+i*0.05,0.25+i*0.05]
        ax.add_patch(patches.Polygon(xy=list(zip(x,y)), fill=True, edgecolor = (0, 0, 0), facecolor = 'green'))
        ax.set_xticks([])
        ax.set_yticks([])
    ax.set_xlabel('Income (1 sheet = $10000)')
    ax.set_title('Annual Income')
    plt.show()
    fig.savefig('income.png', transparent = True)

def create_population(population):
    """
    This function creates a circle diagram that represents population holding
    particular occupation in the U.S.
    """
    pop = int(population) // 1.1*int(population)
    W, H = (400, 400)
    image = Image.new('RGBA', (W, H))
    msg = 'Population Circle Diagram'
    msg1 = 'U.S. Population'
    msg2 = 'Plumbers'
    font = ImageFont.truetype('DejaVuSans.ttf', 15)
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(msg, font = font)
    w1, h1 = draw.textsize(msg1, font = font)
    w2, h2 = draw.textsize(msg2, font = font)
    w3, h3 = draw.textsize(str(population), font = font)
    draw.ellipse((40, 40, 360, 360), fill = 'blue', outline ='blue')
    draw.text(((W-w)/2, 20), msg, (255, 255, 0), font = font)
    draw.text(((W-w1)/2, (H-h1)/4), msg1, (255, 255, 0), font = font)
    #draw.text((100, 100), msg, (255, 255, 0), font = font)
    #draw.text((10,10), "Hello world", font=font, fill=(255, 255, 0))
    draw.ellipse((200 - 160 * pop /2.3 ,200 - 160 * pop /2.3,
                200 + 160 * pop /2.3 , 200 + 160 * pop /2.3), 'red')
    draw.text(((W-w2)/2, (H-h2)/2), msg2, (255, 255, 0), font = font)
    draw.text(((W-w3)/2, (H-h3)/2+15), str(population), (255, 255, 0), font = font)
    image.show()
    image.save('population.png', transparent = True)
def modify_image(a):
    """
    This function modifies the image from create_population so that the
    background is transparent.
    """
    img = Image.open(a)
    imga = img.convert("RGBA")
    datas = imga.getdata()

    newData = list()
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append([255, 255, 255, 0])
        else:
            newData.append(item)

    imgb = Image.frombuffer("RGBA", imga.size, newData, "raw", "RGBA", 0, 1)
    imgb.save(a, "PNG")
def create_map(data):
    """
    This function creates a choropleth U.S. map, where the shade of colors
    in each state represents the density of people holding the occupation in
    each state.
    """
    dataset = []
    states_list = data[0]
    data_list = data[1]
    states_list.pop(states_list.index('HI'))
    data_list.pop(states_list.index('ID'))
    states_list.pop(states_list.index('AK'))
    data_list.pop(states_list.index('AZ'))

    sum_data = data[2]

    EXCLUDED = ("pr", "gu", "vi", "mp", "as")

    state_xs = [states[code]["lons"] for code in states_list]
    state_ys = [states[code]["lats"] for code in states_list]

    colors = ["#F1EEF6", "#D4B9DA", "#C994C7", "#DF65B0", "#DD1C77", "#980043"]

    state_colors = []
    for state in states_list:
        #if states[state_id]["state"] in EXCLUDED:
        #    continue
        dataset.append(data_list[states_list.index(state)]/sum_data)
        highest = max(dataset)
        try:
            rate = data_list[states_list.index(state)]/sum_data
            idx = int(rate*6-1)
            state_colors.append(colors[idx])
        except KeyError:
            state_colors.append("black")

    p = figure(title="Where are they in the U.S.?", toolbar_location="left",
               plot_width=1100, plot_height=700)

    p.patches(state_xs, state_ys, fill_color = state_colors,fill_alpha=0.7,
              line_color="#884444", line_width=2, line_alpha=0.3)
    p.background_fill_alpha = 0
    #output_file("State Map for Accountants.html", title="choropleth.py example")

    show(p)
    export_png(p, filename="map.png")
def create_happiness(a, b):
    """
    This competition shows a bar graph that compares the average suicide rate
    of U.S. workers with the suicide rate of people holding partiular job.
    """
    fig, ax = plt.subplots()
    index = np.arange(2)
    bar_width = 0.3
    opacity = 0.8
    rects1 = plt.bar(index, [a,b], bar_width,
                 alpha=opacity,
                 color='r')
    plt.ylabel('Suicide Rate (per 100000 people)')
    plt.title('Suicide Rate')
    plt.xticks(index, ('Average Job', 'Plumbers'))
    plt.tight_layout()
    plt.show()
    fig.savefig('mort.png')

def create_graphs(a):
    """
    This function generates all the necessary graphs at once. You simply type
    the occupation name.
    """
    create_population(dt.get_specfic_value(OES_df, a, 'employment'))
    create_income(dt.get_specfic_value(OES_df, a, 'annual mean wage'))
    create_happiness(dt.get_average(suiciderate_df, 'total'), dt.get_specfic_value(suiciderate_df, a, 'total'))
    get_gender(dt.get_specfic_value(gender_df, a, 'Men'), dt.get_specfic_value(gender_df, a, 'Wmn'))
    get_race(dt.get_specfic_value(race_df, a, 'White'), dt.get_specfic_value(race_df, a, 'black'), dt.get_specfic_value(race_df, a, 'asian'), dt.get_specfic_value(race_df, a, 'hispanic'))
    create_worktime(dt.get_time_row(timework_df, a))
    if a == 'physicist' or 'plumber':
        break
    if a == 'mechanical engineer':
        create_map(dt.get_state_data('mech_eng'))
    elif a == 'farmer':
        create_map(dt.get_state_data('farm'))
    else:
        create_map(dt.get_state_data(a))
