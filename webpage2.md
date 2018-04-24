#How We Are Creating Our Visualization

## Overview
We are extracting online data, placing it into graphs using Matplotlib and creating a graphic user interface with Pygame.

The nuances of this operation are captured in our system architecture diagram:
~add diagram~ ![alt text](https://github.com/coreyacl/DataViz/blob/master/Assignments/improved_system_architecture.pdf)

### Collecting Data
We're collecting data from a variety of sources, including:
-U.S. Bureau of Labor Statistics
-U.S. Bureau of Labor

From these websites, we're pulling either csv files, excel files or pdf files. In the case of pdf files, we are converting them to csv files via Tabula. 
From there, we are using Pandas to search the datasheets for specific values. We are creating functions that will easily find the correct data for the implementation of the graphs.

### Creating Graphs
### Creating an Interface
