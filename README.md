# DataViz - Occupation Visualization

A visualization of occupations in the US to get a better idea of what their walk of life is like presented in an interactive way.

If you want to see our project website, go [here](https://coreyacl.github.io/DataViz/)

### Install
The data viz uses the pygame package as the main engine behind the visualization. Follow the directions [here](https://www.pygame.org/wiki/GettingStarted) in order to install pygame on your system. A mouse is also required for the user interface.

Generating the graphs and the visualization requires matplotlib and pillow packages. To install matplotlib and pillow, follow the directions [here](https://matplotlib.org/users/installing.html) and [here](https://pillow.readthedocs.io/en/5.0.0/installation.html), respectively.

Manipulating the data requires the pandas package. To install, follow the directions [here](https://pandas.pydata.org/pandas-docs/stable/install.html).

### Experiencing the User Interface

In order to run the user interface, in your terminal type:
```
python UI.py
```

### Using and manipulating all the scripts

#### Data Extraction and Manipulation
The code that is responisble for extracting the data from files and preparing it for creating graphs can be found at datacollection.py. Databases are added at the top of the file and running the different functions in the script return the specified values. For example:
```
output = get_specfic_value(gender_df, 'mechanical engineer', 'Man')
```
will return the percentage of male mechanical engineers. 
#### Creating Graphs

### Creating the User Interface

### Authors
Corey, Alli, Junwon

[![Corey Cochran-Lepiz](https://avatars2.githubusercontent.com/u/31522468?s=400&v=4)](https://github.com/coreyacl) | [![Alli Busa](https://avatars3.githubusercontent.com/u/31522841?s=400&v=4)](https://github.com/allisonbusa) | [![Junwon Lee](https://avatars1.githubusercontent.com/u/31522211?s=400&v=4)](https://github.com/junwonlee5)
---|---|---
[Corey Cochran-Lepiz](https://github.com/coreyacl) | [Alli Busa](https://github.com/allisonbusa) | [Junwon Lee](https://github.com/junwonlee5)
