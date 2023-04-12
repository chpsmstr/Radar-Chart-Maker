import numpy as np
import matplotlib.pyplot as plt
from data_creator import input_data

if __name__ == "__main__":
    
    categories, data = input_data(4, 3, 0, 100)


    
    chart = RadarChart(categories, data)
    chart.draw_chart()