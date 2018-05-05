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
def get_gender(a, b):
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
    print(a, b)
def get_race(a, b, c, d):
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
    print(a, b, c, d)
def create_worktime(work_time):
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
    pop = int(population) //420000
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
    create_population(dt.get_specfic_value(OES_df, a, 'employment'))
    create_income(dt.get_specfic_value(OES_df, a, 'annual mean wage'))
    create_happiness(dt.get_average(suiciderate_df, 'total'), 953)
    get_gender(dt.get_specfic_value(gender_df, a, 'Men'), dt.get_specfic_value(gender_df, a, 'Wmn'))
    get_race(dt.get_specfic_value(race_df, a, 'White'), dt.get_specfic_value(race_df, a, 'black'), dt.get_specfic_value(race_df, a, 'asian'), dt.get_specfic_value(race_df, a, 'hispanic'))
    create_worktime(dt.get_time_row(timework_df, a))
    #create_map(dt.get_state_data('mech_eng'))
#create_worktime(dt.get_hoursworked('plumber', 10))
#create_income(get_profession_data(df,6,4))
#create_happiness(dt.get_average(suiciderate_df, 'total'), 103)
#print(create_map(dt.get_state_data('surgeon')))
#print(get_profession_data(df,6,1))
#print(dt.get_state_data('mech_eng'))
#print(dt.get_average(suiciderate_df, 'total'))
#print(dt.get_specfic_value(suiciderate_df, 'installation', 'total'))
#get_gender(dt.get_specfic_value(gender_df, 'accountant', 'Men'), dt.get_specfic_value(gender_df, 'accountant', 'Wmn'))
#create_map(dt.get_state_data('software'))
#get_race(dt.get_specfic_value(race_df, 'surgeon', 'white'), dt.get_specfic_value(race_df, 'surgeon', 'black'), dt.get_specfic_value(race_df, 'surgeon', 'asian'), dt.get_specfic_value(race_df, 'surgeon', 'Hispanic'))

#create_map(dt.get_state_data('physicist'))
#create_population(dt.get_specfic_value(OES_df, 'physicist', 'employment'))
create_graphs('plumber')
modify_image('population.png')
