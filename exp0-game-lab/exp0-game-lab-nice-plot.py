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
filepath = "data/dilation.csv"


def load_data(filepath, csv_kws={}):
    """Function to load data from a csv file into a Pandas DataFrame"""

    # df stands for dataframe
    df_loaded = pd.read_csv(filepath, **csv_kws)
    return df_loaded

# CALL FUNCTION AND ASSIGN DATAFRAME TO VARIABLE DF
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

    # PLOT VARIABLES
    PLOT_TEXTSIZE_SM = 10
    PLOT_TEXTSIZE_MD = 12
    TEXT_BOLD = "bold"

    # FONT SETTINGS
    plt.rc('font', size=PLOT_TEXTSIZE_SM)  # controls default text sizes
    plt.rc('axes', labelsize=PLOT_TEXTSIZE_MD, labelweight=TEXT_BOLD)
    plt.rc('axes', titlesize=PLOT_TEXTSIZE_SM)
    plt.rc(('xtick', 'ytick'), labelsize=PLOT_TEXTSIZE_MD)


    # GET FIGURE AND AXES OBJECTS
    fig, ax = plt.subplots()


    # FIGURE SETTINGS
    ax.set_axisbelow(True) # send gridlines behind datapoints
    plt.grid() # TODO: customize the grid with axis='y', color='lightgray', linewidth=0.5
    plt.minorticks_on()


    # PLOT THE DATA
    plt.scatter(df[x], df[y], **info_scatter)


    # SET AXIS LABELS
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Dilation (mm)")
    # alternatively, rename the columns to include the units,
    #  and use plt.xlabel(x)

    # SET AXIS LIMITS
    #  axis limits must be set after plot is made
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=-0.02)
    
    # LEGEND (optional)
    # If you want a legend, uncomment the line below,
    # and add the 'label' parameter to plt.scatter()
    # plt.legend()

    return fig


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

    # Text for the annotation on the plot
    # TODO: format equation on plot.
    # .5f means 5 decimal places will be displayed
    # Change it so that 3 decimal places are displayed
    txt_equ = f"$y = {b:.5f} + {a:.5f}x$"
    txt_r2 = f"$R^2 = {r2:.5f}$"
    txt_annotation = f"{txt_equ}\n{txt_r2}"

    return [a, b, r2, txt_annotation]


def plot_add_linear_fit(df, x, y):

    a, b, r2, txt_annotation = get_linear_fit(df[x], df[y])
    
    # plt.plot(df[x], a*df[x] + b, c='orangered', label="_none_")

    ax = plt.gca()
    ax.axline((df.reset_index()[x][0], a*df.reset_index()[x][0] + b), slope=a,
        color='orangered', label='_none_')


    # TODO: change the coordinates 0, 0 so that the equation is visible
    # HINT: df.reset_index()[x][0] gives you the first x value in df, and
    # df.reset_index()[x][-1] gives you the last x value in df
    plt.text(0, 0, txt_annotation, va='bottom', ha='left')



def get_slice(df, r):
    # CREATE A SLICE OF THE DATA BASED ON THE INDEX
    if (r[1] == -1):  # create slice from r[0] to the end of the data
        df_slice = df.loc[(df.index >= r[0])]

    else:  # create slice between r[0] and r[1]
        df_slice = df.loc[(df.index >= r[0]) & (df.index <= r[1])]

    # df_slice.reset_index(inplace=True, drop=True)
    return df_slice


# CALL FUNCTION AND ASSIGN FIGURE TO VARIABLE FIG
# fig = plot_data(df, "Temp", "Dilation")
fig = plot_data(df, "Temp", "Dilation", info_scatter=dict(s=5))


# # ADD A LINEAR FIT OVER THE FULL RANGE OF THE DATA
# plot_add_linear_fit(df, "Temp", "Dilation")


# CREATE A SLICE OF DATA
# TODO: change the range of the slice
df_slice = get_slice(df, r=[0, -1])

# ADD A LINEAR FIT OF A SLICE OF DATA TO THE PLOT
plot_add_linear_fit(df_slice, "Temp", "Dilation")


# SAVE IMAGE IN PLOTS FOLDER
# fig.savefig("plots/figure1.png", dpi=200, bbox_inches="tight")
fig.savefig("plots/figure2.png", dpi=200, bbox_inches="tight")

# SHOW WINDOW WITH PLOT
#  plt.show() must be after savefig()
plt.show()