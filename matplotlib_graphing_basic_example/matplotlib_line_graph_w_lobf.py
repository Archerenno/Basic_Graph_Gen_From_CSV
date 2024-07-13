import matplotlib.pyplot as plt
import numpy as np
#Importing the required modules and abbreviating them for easier future use

def read_data(filename):
    """Reads the data from the given CSV file using numpy's loadtxt method"""
    data = np.loadtxt(filename, delimiter = ",", skiprows = 1)
    years = data[:, 0]
    change_distance = data[:, 1]
    #Lines 8 & 9 are using splices to take the 2D matrix in data and convert it into two lists
    return years, change_distance
    

def find_lobf(xs, ys):
    """Finds an equation for the line of best fit (lobf)"""
    a, b = np.polyfit(xs, ys, 1)
    # Polyfit returns a tuple of (a, b) where y = ax + b because polyfit is limited to 1 degree by the third paramter
    y2s = a * xs + b
    # y2s is the y coordinates for the lobf
    return a, y2s 


def plot_change_distances(xs, ys, lobf):
    """Plots the graph using matplotlib techniques"""
    axes = plt.axes()
    axes.plot(xs, ys, marker = "o")
    # Plotting the main graph and setting the markers the be hollow circles
    axes.plot(xs, lobf, color = "orange")
    # Plotting the line of best fit and making it orange
    axes.set_title("Change in distance between Westford, USA and Wettzell, Germany")
    axes.set_xlabel("Time (Year)")
    axes.set_ylabel("Distance (m)")
    axes.grid(True)
    plt.show()


def main():
    """Main function"""
    years, change_distance = read_data("contdrift.csv")
    gradient, lobf = find_lobf(years, change_distance)
    plot_change_distances(years, change_distance, lobf)
    print(f"The average speed the continents are moving is: {(gradient * 100):.2f} cm/year")
    
main()