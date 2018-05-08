# Project Evolution

We began this project wanting to find unique data that gives the viewer a more in-depth perspective on what different occupations are like, but we didn't know if the data was out there, which libraries we could use and how we wanted to present the data.

During our first Architecture Review, we got feedback from our peers on possible data sources, what to do if we didn't find data and some Python libraries to try for the graphs and interface.

Luckily, we found the U.S. Bureau of Labor Statistics, which contains a plethora of data in the field that we're looking at. From there, we found other, supporting data sources. We also decided to try the libraries recommended in the first architecture review and that's what we're using now.

We each worked on our tasks until the second Architecture Review. During this, we asked for advice on extracting and compiling data more smoothly, and we were told to use Pandas to solve our compiling issues. Pandas has made our data extraction noticeably more effective. We went from finding data in a file like this:
```
#creating a list of professions
lifescience = []
farmer = []
business = []
computer = []
repair = []
engineering = []
professions = [lifescience, farmer, business, computer, repair, engineering]
x_real= []
y = [] #for the y axis of the graph , later

```
to
```
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
```
and now we have:
```
def get_hoursworked(profession):
    """
    This code will take a profession that you give it and find the accompanying
    row. It will return a list of all the hours of the day and the percentage of
    workers in the specified occupation working at that hour.
```
A function in which the argument is just a string. 

We also asked for feedback on the types of graphs and their appearance. Our audience suggested to use a treemap for population instead of a bubble chart. They also suggested that we get help from our classmates on constructing a map of the US. In terms of aesthetics of the graphs, we were told that altair is a data visualization library that we could use. From this information, we have decided to use our intended bubble graph, considering that we only want to represent one occupation individually, instead of all the occupations at once. For the map of the U.S., the classmates we asked about it suggested that we use Bokeh. Consequently, we decided to use Bokeh to create the choropleth map that showed the density of people holding particular occupations in each state. For simple graphs like pie charts and bar graphs, our classmates suggested matplotlib, so we used this library to produce the rest of the graphs.

For questions relating to the UI, we were told that our idea of using a chalkboard style background could be interesting, but it our audience did not think it was an important factor for the overall project. We were also advised to clearly come up with a unified goal for the project and that would make figuring out which graphs to include as well as other design choices easier. Right after the session, we thought of a unified goal and it has solidified our decisions on which graphs to use. Now, we are excited to finalize our code and create an initial, finished product.

With that in mind we went along with a whiteboard aesthetic that went along with the transparent graphs that w made for it. The UI soon went from being a couple photos that we click to a clean user interface that is easy to use. In terms of the code itself we evolved from hardcoding every single figure entry to creating functions in the Screen class that took care of all of the monotonous work for us.



Go Back to the [Index](index.md)
