import matplotlib

matplotlib.use('TkAgg')
from DictBuilder import *
from GUIBuilder import *
from BarChartBuilder import *

# 1. See DictBuilder.py

# 2. Import the dictionary using import_dict()
orig_dict = import_dict()
clean_dictionary = dictionary_cleaner(orig_dict)
# Then pass that object as a parameter to dictionary_cleaner(dict)
# You will be using the cleaned dict for this project

# 3. Create a list of strings containing the different attributes
# that your user can select. These are the keys of your inner dictionary
attributes_list = ['Hospital Beds Total', 'Covid Total Cases', 'Housing Cost Changes']

# 4. Create a list of strings of all the counties in your dict.
counties_list = []
for county_key in clean_dictionary:
    counties_list.append(county_key)

# print(counties_list)
# These are stored as keys in your outer dictionary.
# Use a for loop to do this

# 5. Look at the parameters that build_window() can take in GUIBuilder.py
# Pass the lists from steps 1 and 2 into the function.
# You use the third optional parameter to assign a new theme (see canvas writeup
# for more on how to do this)
window = build_window(counties_list, attributes_list, 'DarkRed1')

# This code is necessary for setting up the GUI
figure_agg = None

# The GUI remains open until the user presses the exit button or quits the window
# During the while loop the following occur:
# - Check for events
# - Do something based on events
# - Draw to the window
while True:
    # -------------------
    # CHECK FOR EVENTS
    # -------------------
    # Read in the events and values from the window object
    event, values = window.read()
    # This code removes the chart before drawing a new one
    if figure_agg:
        delete_figure_agg(figure_agg)

    # ------------------------------
    # DO SOMETHING BASED ON EVENTS
    # ------------------------------
    # We store the values that the user selects
    # for both counties and both attributes

    choice1 = values['-ATTRIBUTES1-']
    choice2 = values['-ATTRIBUTES2-']

    county1 = values['-COUNTY1-']
    county2 = values['-COUNTY2-']

    # Check for screen existing
    if event == 'Exit':
        break

    # 6. Check if we should draw the bar chart
    # Using IF statements check that both: 1) the Plot button has been
    # pressed, and 2) that the user has selected values in all four
    # drop-down menus (that all four variables choice1, choice2, county1,
    # and county2 have values)
    # If the plot button is selected and all four values are selected, then
    # set draw_the_bar_chart to True

    # while choice1, choice2, county1, county2 != '':?
    if event == 'Plot' and choice1 != '' and choice2 != '' and county1 != '' and county2 != '':
        draw_the_bar_chart = True
    else:
        draw_the_bar_chart = False

    # ---------------------
    # DRAW TO THE WINDOW
    # ---------------------
    # This code draws the barchart

    # 7. Pass your dictionary to barchart()
    # The barchart() function takes 5 parameters -- look at the definition
    # of the function in BarChartBuilder.py to figure out how to pass in
    # your dictionary in the call to barchart() below
    if draw_the_bar_chart:
        fig = barchart(county1[0], county2[0], choice1[0], choice2[0], clean_dictionary)
        figure_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
