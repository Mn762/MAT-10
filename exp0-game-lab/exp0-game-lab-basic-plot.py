"""
Experiment 0: Game Lab
Course: MAT 010
Date:
Name:

Description of script
"""

# importing 'libraries' gives you access to all of the 'methods' in the library 
import pandas as pd  # dataframes
import numpy as np  # math for arrays (columns)
from scipy import stats  # regression line
import matplotlib.pyplot as plt  # plotting


# VARIABLES

# CREATE VARIABLES FOR FILEPATHS
#  "data/fname.csv" implies the fname.csv file is in a
#  subdirectory "data" within the current directory
# TODO: enter the filepath
filepath = "data/dilation.csv"


def load_data(filepath, csv_kws={}):
    """Function to load data from a csv file into a Pandas DataFrame"""

    # df stands for dataframe
    df_loaded = pd.read_csv(filepath, **csv_kws)
    return df_loaded

# CALL FUNCTION AND ASSIGN DATAFRAME TO VARIABLE DF
# NOTE: csv is usually comma separated, so sep='\t' tells the read_csv() 
#       function that the separator is a tab character, not a comma
df = load_data(filepath, csv_kws=dict(sep='\t'))

# VIEW DATA
print(df.head())
print(df.describe())
print(df.info())


def plot_data(df, x, y, info_scatter={}):
    """Function to plot x and y data, and return the matplotlib figure

    Parameters:
    - df: pandas dataframe, 
    - x: column name, 
    - y: column name
    - info_scatter: optional dictionary of key word values passed to plt.scatter()
    """

    # GET FIGURE AND AXES OBJECTS
    fig, ax = plt.subplots()  # create new figure and axes

    # PLOT THE DATA
    plt.scatter(df[x], df[y], **info_scatter)

    return fig


# CALL FUNCTION AND ASSIGN FIGURE TO VARIABLE FIG
# TODO: enter the name of the x column and the name of the y column
fig = plot_data(df, "Temp", "Dilation")

# SAVE IMAGE IN PLOTS FOLDER
fig.savefig("plots/figure1.png", dpi=200, bbox_inches="tight")

# SHOW WINDOW WITH PLOT
#  plt.show() must be after savefig()
plt.show()