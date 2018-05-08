# About Our Code

## Overview
We are extracting online data, placing it into graphs using Matplotlib and creating a graphic user interface with Pygame.

The nuances of this operation are captured in our system architecture diagram:
![](./final_system_architecture-1.png)

### Collecting Data
We're collecting data from a variety of sources, including:
- U.S. Bureau of Labor Statistics
- U.S. Bureau of Labor
- Center for Disease Control and Prevention

For a complete list of sources, see [sources](Sources.md)

From these websites, we're pulling either csv files, excel files or pdf files. In the case of pdf files, we are converting them to csv files via Tabula.
From there, we are using Pandas to import the datasheets to dataframes. Ex:
```
gender = pd.read_csv('files/tabula-gender.csv')
gender_df = pd.DataFrame(gender)
```
We are creating functions that will easily find the correct data for the implementation of the graphs. One cell can be extracted using:
```
def get_specfic_value(database, profession, datatype):
    """This works for OES data, divorce rate, suicide rate, gender ratio, spending
    *note : for divorce rate, the profession for mech e is "mechanical engineer"
            also for divorce rate, the profession for software is "software developer"
    *note 2: the same applies for race. Also, the physicist data doesn't exist and
    the columns for the race data are : White, Black or African American,
    Asian, Hispanic or Latino

    """
    #formatting
    datatype = datatype.lower()
    database.columns = database.columns.str.lower()
    database = database.apply(lambda x: x.astype(str).str.lower())

    #finding the column and its index
    colNames = database.columns[database.columns.str.contains(pat = str(datatype))]
    column = colNames[0]
    colindex = database.columns.get_loc(column)
    #finding row index
    row, row_index = get_right_row(database, profession)
    #getting ouput
    output = database.iloc[int(row_index),int(colindex)]

    return output

```

### Creating Graphs
Using the data collected in csv format, we produced different graphs to visualize different types of data

The graphs are produced using the collected data. Some graphs simply takes the name of the occupation as an arguments, while some require pre-evaluated data to be the argument.

For instance, the income diagram, which represents annual income with a stack of "dollar bills", requires the argument to be a numerical value.

```
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

```
As a result, this function generates graphs like this.
![]({{"income.png"|absolute_url}})

On the other hand, the schedule diagram, which shows the percentage of people with particular occupation at work in specific hour frame, requires the input to be Pandas Series. The function separates the index, or the hour frame, from the data, which contains the percentages of people at work. The snippet below demonstrates this process.

```
def create_worktime(work_time):
    """
    This function creates a histogram that shows the percentage of workers
    working throughout the 24 hour period.
    Note: work_time is Pandas Series
    """
    fig, ax = plt.subplots()
    time_list = work_time[0].index.tolist() + work_time[1].index.tolist()
    percent_list = work_time[0].tolist() + work_time[1].tolist()
    percent_list = [x for x in percent_list if "plumber" not in x]
    time_list = [x for x in time_list if "occupation" not in x]
    percent_list = list(map(float, percent_list))

```

As a result of this function, the graph below is created.
![]({{"Pie_Chart.png"|absolute_url}})

To represent the population of people holding the particular job in the U.S., we used a create_population function, which produces a circle diagram, where the sizes of the two circles portray the ratio of the population holding particular job to the entire U.S. adult population. The create_population takes the integer as an argument.

```
def create_population(population):
    """
    This is simply the snippet of the code.
    This function creates a circle diagram that represents population holding
    particular occupation in the U.S.
    """
    pop = int(dt.get_specfic_value(OES_df, population, 'employment'))
    pop1 = pop/1000000
    W, H = (500, 500)
```

![]({{"Population_circle_diagram.png"|absolute_url}})

To display the suicide rate of people holding the job, we used a bar graph which compares the average suicide rate with the suicide rate of people with specific occupation.

```
def compare_happiness(a, b):
```


![]({{"Suicide_Rate.png"|absolute_url}})


### Creating an Interface
Using Pygame as a platform for the interface of the visualization seemed like the best route to go considering our previous exprience with it as well as the not-so-bright reviews about other means of creating an interactive interface. The process has been pretty straightforward in terms of coding the infrastructure for it. It currrently remains as a click-based interface. 
![](./UI_pic.png)
We aimed for a simplistic aethetic for the project.

Some example code for our Screen class that made the UI possible:

```
class Screen():
    """ This is the basis for the entire UI
    Each 'screen' is saved as this object that contains all of the
    photos that appear as well as some helpful functions to render text
    as weel as a zoom in function that the main while loop helps manage.
    """
    black = (0,0,0)
    white = (255,255,255)
    bx = 700
    by = 100
    font = py.font.SysFont("couriernew",25) #for regular text
    title = py.font.SysFont("couriernew",50) #for title text
    bg = py.image.load('FinalFigures/Wb-5.jpg') #for background
    w,h = bg.get_size()
    bg = py.transform.scale(bg,(int(w*.7),int(h*.7))) #scaling for grey button that sometimes appears
    listOfNames  = ['Farmer','Software Developer','Surgeon','Mechanical Engineer',
                    'Physicist','Plumber','Accountant'] #unhealthy hardcode but neccesary 
    z = False #zoom boolean

    def __init__(self,gD,name):
        """
        gD: gameDisplay for pygame
        name: name of screen (string)
        figures: list of figures (pygame img)
        locs: list of location (tuple)
        clickbox: list of clickbox blits (pygame rectangle)
        """
        self.gD = gD
        self.name = name
        self.figures = []
        self.locs = []
        self.clickbox = []


        button = py.image.load('FinalFigures/arrow.png')
        scale = .1
        lx,ly = 20,20
        # lx,ly = 1400,1000
        w,h = button.get_size()
        button = py.transform.scale(button,(int(w*scale),int(h*scale)))

        self.figures.append(button)
        self.locs.append((lx,ly))
        self.clickbox.append(gameDisplay.blit(button,(lx,ly)))
```


Go Back to the [Index](index.md)
