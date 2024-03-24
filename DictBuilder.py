# Import dictionary from text file
# We have handled this for you
def import_dict():
    import numpy as np

    dictionary = np.load('dictionary.npy',allow_pickle='TRUE').item()
    return dictionary

# 1. Use this function to create a new version of the imported dictionary
# - Your new dictionary should have three keys and values for each county
# - The keys should be descriptive (instead of 'beds' you could use '# of Hospital Beds' for example)
# - The value for housing data should be divided by 100. That way when we create the bar chart
#   the housing prices won't distort the other values.
def dictionary_cleaner(dict):
    new_dict = {}
    #for county, values1 in dict.items():
    for item,values in dict.items():
        if 'beds' in values:
            beds = values['beds']
        else:
            beds = 0
        if 'cases' in values:
            cases = values['cases']
        else:
            cases = 0
        if 'housing' in values:
            housing = values['housing']/100
        else:
            housing = 0
        new_dict[item] = {'Hospital Beds Total': beds, 'Covid Total Cases': cases, 'Housing Cost Changes': housing}
    return new_dict

# This runs if the file is executed and doesn't if the file is imported
# This is where you can test the output of your functions.
if __name__ == '__main__':
    imported_dict = import_dict()
    print("Imported Dictionary: ", imported_dict)
    print('TEST:', dictionary_cleaner(imported_dict))
