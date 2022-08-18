"""
Experiment 2: Heat Treat Lab
Course: MAT 010
Date:
Name:

Effect of cooling media in heat treatment of 
AISI 1020, 1040, and 1080 steels on cooling rate 
using air, oil, and water quenching.

Import data into a pandas dataframe,
and create plot using matplotlib.
"""

# importing 'libraries' gives you access to all of the 'methods' in the library 
import pandas as pd  # dataframes
import numpy as np  # math for arrays (columns)
from scipy import stats  # regression line
import matplotlib.pyplot as plt  # plotting


# VARIABLES

#  CREATE VARIABLES FOR FILEPATHS
#  TODO: change filenames
filepath_air = "data/############"
filepath_oil = "data/############"
filepath_h2o = "data/############"


# COLUMNS
# TODO: add axis title
x_axis = "x axis title"
y_axis = "y axis title"


# DICTIONARIES
#  Create a python dictionary for common 
#  arguments when calling load_data()
info_data = {
    'x': x_axis,
    'y': y_axis,
    'col_names': [y_axis],
    'header_line': 0 # TODO: update value
}

#  Create dictionary with sample specific values
# 'freq' is the frequency of the data measurements in Hz
# 'r' is the range over which to do a linear regression line of best fit
info_air = {
    'freq': 1,  # Hz, TODO: update value
    'r': [0, -1]  # TODO: update range
}

info_oil = {
    'freq': 1,  # Hz, TODO: update value
    'r': [0, -1]  # TODO: update range
}

info_h2o = {
    'freq': 1,  # Hz, TODO: update value
    'r': [0, -1]  # TODO: update range
}

def load_data(filepath, info_data={}, freq=1, view_data=False):
    """
    Function that takes a filepath and returns a pandas dataframe.
    Generates the df.index based on freq value in Hz.
    """
    x = info_data.get('x', 'x')
    cols = info_data.get('col_names', ['y'])
    header_line = info_data.get('header_line', 0)

    # LOAD DATA from file into pandas dataframe, and set the column name
    # TODO: if needed customize data import
    df_loaded = pd.read_csv(filepath, header=header_line, names=cols, encoding='unicode_escape')

    # generate the column of time values given the frequency of the sensor
    # data, add the column to the dataframe, and set it to be the index
    df_loaded[x] = np.arange(start=0, stop=len(df_loaded)/freq, step=(1/freq))  # add column for x axis
    df_loaded.set_index(x, inplace=True, drop=True)

    if view_data:
        # VIEW DATA
        print(df_loaded.head(5), "\n")
        print(df_loaded.info(), "\n")

    return df_loaded


# CALL FUNCTION AND SAVE DATAFRAMES TO VARIABLES
df_air = load_data(filepath_air, info_data=info_data, freq=info_air['freq'], view_data=True)
df_oil = load_data(filepath_oil, info_data=info_data, freq=info_oil['freq'])
df_h2o = load_data(filepath_h2o, info_data=info_data, freq=info_h2o['freq'])

# -----------------------------------------------

def get_slice(df, r, y):
    # CREATE A SLICE OF THE DATA
    if (r[1] == -1):  # create slice from r[0] to the end of the data
        df_slice = df.loc[(df.index >= r[0])]

    else:  # create slice between r[0] and r[1]
        df_slice = df.loc[(df.index >= r[0]) & (df.index <= r[1])]

    x_slice = df_slice.index  # assumes plotting against the index
    y_slice = df_slice[y]
    # print(df_slice.head(5))  # view slice

    return x_slice, y_slice

def get_linear_fit(x, y):
    # GET LINEAR FIT REGRESSION LINE PARAMETERS ax+b
    #  Use scipy.stats to do the linear regression on the dataframe slices.
    equ = stats.linregress(x, y)
    a = equ.slope
    b = equ.intercept
    r2 = equ.rvalue**2  # r_squared = r_value^2

    # view regression information on terminal
    print(f"y = {b:.3f} + {a:.3f}x")  # linear regression equation
    print(f"R-Squared is {r2:0.5f}")
    print(f"Cooling rate is {a:.1f}ºC/s\n")

    # Text for the annotation on the plot
    txt_equ = f"$y = {b:.3f} + {a:.3f}x$"
    txt_r2 = f"$R^2 = {r2:.3f}$"
    txt_annotation = f"{txt_equ}\n{txt_r2}"

    return [a, b, r2, txt_annotation]

def plot_data(df, x, y, info={}, info_scatter={}):
    """
    Creates a scatter plot with a regression line on the range specified by r

    Parameters
    ----------
    df : pandas dataframe, data to plot on scatterplot
    x : str, name of x axis
    y : str, name of y axis
    r : list, range of data overwhich to fit the regression line
    title: str, plot title
    """

    # PLOT VARIABLES
    # TODO: customize plot settings
    PLOT_TEXTSIZE_SM = 8
    PLOT_TEXTSIZE_MD = 9

    # FONT SETTINGS
    plt.rc('font', size=PLOT_TEXTSIZE_MD)  # controls default text sizes
    # plt.rc('axes', labelsize=PLOT_TEXTSIZE_MD, titlesize=PLOT_TEXTSIZE_SM)  # controls axes text sizes
    # plt.rc(('xtick', 'ytick'), labelsize=PLOT_TEXTSIZE_MD)

    # GET FIGURE AND AXES OBJECTS
    # TODO: choose figure size in inches
    fig, ax = plt.subplots(figsize=(3,2))  # create new figure and axes
    

    #  GET SLICE
    r = info.get('r', [0,-1])
    x_slice, y_slice = get_slice(df, r, y)

    # GET LINEAR FIT OF SLICE
    a, b, r2, txt_annotation = get_linear_fit(x_slice, y_slice)


    # PLOT THE DATA
    plt.scatter(df.index, df[y], **info_scatter)
    
    # PLOT LINEAR FIT
    ax.axline((x_slice[0], a*x_slice[0] + b), slope=a, label='_none_', color='black')  # TODO: customize fit line

    # ADD ANNOTATIONS TO PLOT: add linear fit equation to plot
    #  TODO: place the annotation close to the regression line
    plt.text(0, 0, txt_annotation, va='bottom', ha='left')


    # SET AXIS LABELS
    plt.xlabel(x)
    plt.ylabel(y)

    # SET AXIS LIMITS
    #  axis limits must be set after plot is made
    #  TODO: customize axis limits
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0)

    return fig



# CALL FUNCTION AND SHOW PLOTS
# TODO: customize plot aesthetics.
info_scatter=dict()
fig1 = plot_data(df_air, x=x_axis, y=y_axis, info=info_air, info_scatter=info_scatter)
fig2 = plot_data(df_oil, x=x_axis, y=y_axis, info=info_oil, info_scatter=info_scatter)
fig3 = plot_data(df_h2o, x=x_axis, y=y_axis, info=info_h2o, info_scatter=info_scatter)


# TODO: customize saved image
# SAVE PLOTS TO filename.png in the plots/ folder
fig1.savefig("plots/figure1.png", dpi=150, bbox_inches="tight")
fig2.savefig("plots/figure2.png", dpi=150, bbox_inches="tight")
fig3.savefig("plots/figure3.png", dpi=150, bbox_inches="tight")

# SHOW PLOTS in their own windows
#  plt.show() must be called after fig.savefig() 
#  otherwise the figure saved will be blank
plt.show()
