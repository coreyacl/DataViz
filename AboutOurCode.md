# About Our Code

## Overview
We are extracting online data, placing it into graphs using Matplotlib and creating a graphic user interface with Pygame.

The nuances of this operation are captured in our system architecture diagram:
![]({{"improved_system_architecture-1.png"|absolute_url}})

### Collecting Data
We're collecting data from a variety of sources, including:
- U.S. Bureau of Labor Statistics
- U.S. Bureau of Labor
- Center for Disease Control and Prevention
- [Flowing Data](http://flowingdata.com/2017/07/25/divorce-and-occupation)

From these websites, we're pulling either csv files, excel files or pdf files. In the case of pdf files, we are converting them to csv files via Tabula.
From there, we are using Pandas to search the datasheets for specific values. Ex:
```
data = pd.read_excel("files/OES_Report(1).xlsx")
df = pd.DataFrame(data)
```
We are creating functions that will easily find the correct data for the implementation of the graphs. If there aren't any complications with the datasheet, one cell can be extracted using: 
```

def get_profession_data(dataframe, profession, info_needed):
    """
    This code will take a string that exactly matches one in the file and
    one of the variables from above. It returns the specific value asked for."""
    output = dataframe.iloc[profession, info_needed]
    return output
```

### Creating Graphs
Using the data collected in csv format, we produced different graphs to visualize different types of data.
First, we represented annual income with a stack of "dollar bills" , where each sheet represents $10000.
![]({{"income.png"|absolute_url}})

To represent the ideal daily schedule of people, we used a pie chart where each piece measures either the free time, work time, or sleep time.
![]({{"Pie_Chart.png"|absolute_url}})

To display the population of people holding the particular job in the U.S., we used a circle diagram, where the sizes of the two circles portray the ratio of the population holding particular job to the entire U.S. adult population.
![]({{"Population_circle_diagram.png"|absolute_url}})

To display the suicide rate of people holding the job, we will use a bar graph which compares the average suicide rate with the suicide rate of people with specific occupation.
![]({{"Suicide_Rate.png"|absolute_url}})


### Creating an Interface
Using Pygame as a platform for the interface of the visualization seemed like the best route to go considering our previous exprience with it as well as the not-so-bright reviews about other means of creating an interactive interface. The process has been pretty straightforward in terms of coding the infrastructure for it. It currrently remains as a click-based interface. The one hurdle that we still face is transitions, which *can* be done but not without struggle. A figure of the current working interface is shown below.
![]({{"UI_Example.png"|absolute_url}})
We aim for a simplistic aethetic for the project that is still in development.



Go Back to the [Index](index.md)

