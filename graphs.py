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

#spending = pd.read_csv('files/tabula-spending.csv')
#spending_df = pd.DataFrame(spending)

race = pd.read_excel("files/race.xlsx")
race_df = pd.DataFrame(race)


def get_gender(job):
    """
    This function generates a pie chart for gender ratio in particular occupation.
    Simply type the job name.
    """
    new_labels = 'Male', 'Female'
    new_sizes = [dt.get_specfic_value(gender_df, job, 'Men'), dt.get_specfic_value(gender_df, job, 'Wmn')]
    explode = (0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(new_sizes, explode=explode, labels=new_labels,
            autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Gender Ratio')
    plt.show()
    fig1.savefig('gender.png', transparent = True)

def get_race(job):
    """
    This function generates a pie chart for ethnicity ratio in particular occupation.
    It takes the occupation name as an argument.
    """
    new_labels = 'White', 'Black or African American', 'Asian', 'Hispanic or Latino'
    new_sizes = [dt.get_specfic_value(race_df, job, 'White'), dt.get_specfic_value(race_df, job, 'black'), dt.get_specfic_value(race_df, job, 'asian'), dt.get_specfic_value(race_df, job, 'hispanic')]
    explode = (0, 0, 0.2, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(new_sizes, explode=explode, labels=new_labels,
            autopct='%1.1f%%',
            shadow=True, startangle=0)
    ax1.axis('equal')
    plt.title('Ethnicity Ratio')

    plt.show()
    fig1.savefig('race.png', transparent = True)

def create_worktime(job):
    """
    This function creates a histogram that shows the percentage of workers
    working throughout the 24 hour period.
    """
    work_time = dt.get_time_row(timework_df, job)
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
def create_income(job):
    """
    This function creates a diagram that represents income using stack
    of "paper bills", which are green parallelograms. Each bill represents
    $10000.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    income = int(dt.get_specfic_value(OES_df, job, 'annual mean wage')) // 10000
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

def create_population(job):
    """
    This function creates a circle diagram that represents population holding
    particular occupation in the U.S.
    """
    pop = int(dt.get_specfic_value(OES_df, job, 'employment'))
    pop1 = pop/1000000
    W, H = (500, 500)
    r = 50
    if pop < 10000:
        r = 5
    if pop < 100000:
        r = 10
    image = Image.new('RGBA', (W, H))
    msg = 'Population Circle Diagram'
    msg1 = 'U.S. Adult Population'
    msg2 = job
    font = ImageFont.truetype('DejaVuSans.ttf', 15)
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(msg, font = font)
    w1, h1 = draw.textsize(msg1, font = font)
    w2, h2 = draw.textsize(msg2, font = font)
    w3, h3 = draw.textsize(str(pop), font = font)
    draw.ellipse((40, 40, 460, 460), fill = 'blue', outline ='blue')
    draw.text(((W-w)/2, 20), msg, font = font, fill = 'black')
    draw.text(((W-w1)/2, (H-h1)/4), msg1, (255, 255, 0), font = font)
    #draw.text((100, 100), msg, (255, 255, 0), font = font)
    #draw.text((10,10), "Hello world", font=font, fill=(255, 255, 0))
    draw.ellipse((250 - 210 * pop1/r , 250 - 210 * pop1 /r,
                250 + 210 * pop1 /r , 250 + 210 * pop1 /r), 'red')
    draw.text(((W-w2)/2, (H-h2)*3/5), msg2, (255, 255, 0), font = font)
    draw.text(((W-w3)/2, (H-h3)*3/5+15), str(pop), (255, 255, 0), font = font)
    draw.rectangle(((250 - 210 * pop1/300 , 250 - 210 * pop1 /300) , (250 + 210 * pop1/300, (H-h3)*3/5)), fill="black")
    image.show()
    image.save('population.png', transparent = True)

def create_map(job):
    """
    This function creates a choropleth U.S. map, where the shade of colors
    in each state represents the density of people holding the occupation in
    each state.
    """
    if job == 'mechancinal engineer':
        job = 'mech_eng'
    elif job == 'farmers':
        job = 'farm'
    data = dt.get_state_data(job)
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
def compare_suicide(job):
    """
    This function shows a bar graph that compares the average suicide rate
    of U.S. workers with the suicide rate of people holding partiular job.
    """
    if job == 'Software Developers':
        job = 'software'
    value = int(float(dt.get_specfic_value(suiciderate_df, job, 'total')))
    fig, ax = plt.subplots()
    index = np.arange(2)
    bar_width = 0.3
    opacity = 0.8
    rects1 = plt.bar(index, [dt.get_average(suiciderate_df, 'total'), value], bar_width,
                 alpha=opacity,
                 color='r')
    plt.ylabel('Suicide Rate (per 100000 people)')
    plt.title('Suicide Rate')
    if job == 'software':
        job = 'Software Developers'
    plt.xticks(index, ('Average Job', job))
    plt.tight_layout()
    plt.show()
    fig.savefig('mort.png', transparent = True)

def create_graphs(job):
    """
    This function generates all the necessary graphs at once. You simply type
    the occupation name.
    """
    create_population(job)
    create_income(job)
    compare_suicide(job)
    get_gender(job)
    get_race(job)
    create_worktime(job)
    create_map(job)
#create_population('Farm')
#create_graphs('Software Developers')
compare_suicide('Software Developers')
