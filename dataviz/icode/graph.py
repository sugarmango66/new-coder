from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from parse import parse

MY_FILE = '../data/sample_sfpd_incident_all.csv'

def visualize_days():
    '''Visualize data by day of week'''
    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ',')
    # print(len(data_file)) #99
    
    # make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week
    #===========basic for loop================
    # all_DayOfWeek = []
    # for ele in data_file:
    #     all_DayOfWeek.append(ele['DayOfWeek'])
    # counter = Counter(all_DayOfWeek)
    # print(counter)
    # print(sum(counter.values())) #99
    #==================================
    #=============list comprehension============
    counter = Counter([ele['DayOfWeek'] for ele in data_file])
     
    # separate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])
    data_list = [
        counter['Monday'],
        counter['Tuesday'],
        counter['Wednesday'],
        counter['Thursday'],
        counter['Friday'],
        counter['Saturday'],
        counter['Sunday']
    ]
    # with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)
    # create the amount of ticks needed for our x-axis, and assign
    # the labels
    plt.xticks(range(len(day_tuple)), day_tuple)
    # save the plot!
    plt.savefig('Days.png')
    # close plot file
    plt.clf()
    
def visualize_type():
    '''Visualize data by category in a bar graph'''
    # grab our parsed data
    data = parse(MY_FILE, ',')
    # make a new variable, 'counter', from iterating through each line
    # of data in the parsed data, and count how many incidents happen
    # by category
    counter = Counter([ele['Category'] for ele in data])
    # Set the labels which are based on the keys of our counter.
    # Since order doesn't matter, we can just used counter.keys()
    labels = tuple(counter.keys())
    # Set exactly where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5
    # Width of each bar that will be plotted
    width = 0.5
    # Assign data to a bar plot (similar to plt.plot()!)
    plt.bar(xlocations, counter.values(), width=width)
    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)
    # Give some more room so the x-axis labels aren't cut off in the
    # graph
    plt.subplots_adjust(bottom=0.4)
    # Make the overall graph/figure is larger
    plt.rcParams['figure.figsize'] = 12, 8
    # Save the graph!
    plt.savefig('Type.png')
    # Close plot figure
    plt.clf()

def main():
    visualize_days()
    visualize_type()
    
if __name__ == '__main__':
    main()