from cv2 import mean
import pandas as pd 
import csv
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import random 
import statistics

df = pd.read_csv("StudentsPerformance.csv")
perfomance = df["reading score"].tolist()


#mean

mean = sum(perfomance) / len(perfomance)
print(mean)

#median
perfomance_median = statistics.median(perfomance)
print(perfomance_median)

#mode
perfomance_mode = statistics.mode(perfomance)
print(perfomance_mode)

#std deviation
std_dev=statistics.stdev(perfomance)
print(std_dev)

first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)

#ploting a graph

fig = ff.create_distplot([perfomance], ["reading scores"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_std_dev_start, third_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_std_dev_end, third_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()