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

