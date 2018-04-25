# Project Evolution

We began this project wanting to find unique data that gives the viewer a more in-depth perspective on what different occupations are like, but we didn't know if the data was out there, which libraries we could use and how we wanted to present the data.

During our first Architecture Review, we got feedback from our peers on possible data sources, what to do if we didn't find data and some Python libraries to try for the graphs and interface. 

Luckily, we found the U.S. Bureau of Labor Statistics, which contains a plethora of data in the field that we're looking at. From there, we found other, supporting data sources. We also decided to try the libraries recommended in the first architecture review and that's what we're using now. 

We each worked on our tasks until the second Architecture Review. During this, we asked for advice on extracting and compiling data more smoothly, and we were told to use Pandas to solve our compiling issues. Pandas has made our data extraction noticeably more effective. We went from finding data in a file like this:
````
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

def store_data_list(file_name, csv_text, profession_list):
    """
    Takes the file and finds the row with the text you're looking for. In this
    case, it will take the name of a profession and returns a list that contains
    the name of the profession and the data associated with it. In the example I'm using,
    it's time.
    """
    with open(file_name, 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=",")
        for row in plots:
            if csv_text in row:
                profession_list.append(row)
````
to
````
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
````
Even though it's still not ideal, we no longer have to create many lists to sort through the data. 

We also asked for feedback on the types of graphs and their appearance. Our audience suggested to use a treemap for population instead of a bubble chart. They also suggested that we get help from our classmates on constructing a map of the US. In terms of aesthetics of the graphs, we were told that altair is a data visualization library that we could use. From this information, we have decided to use our intended bubble graph, considering that we only want to represent one occupation individually, instead of all the occupations at once. For the map of the U.S., the classmates we asked about it suggested that we use Bokeh. Therefore, we are still deciding which library to use.

For questions relating to the UI, we were told that our idea of using a chalkboard style background could be interesting, but it our audience did not think it was an important factor for the overall project. We were also advised to clearly come up with a unified goal for the project and that would make figuring out which graphs to include as well as other design choices easier. Right after the session, we thought of a unified goal and it has solidified our decisions on which graphs to use. Now, we are excited to finalize our codes and create an initial, finished product.



Go Back to the [Index](index.md)
