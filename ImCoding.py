import csv
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objs as go

counter = 30

df = pd.read_csv("Data.csv")

data = df["date"].tolist()
mean = statistics.mean(data)
sd = statistics.stdev(data)

def random_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,1000):
        set_mean = random_mean(100)
        mean_list.append(set_mean)
    show_fig(mean_list)

mean = statistics.mean(mean_list)
sd = statistics.stdev(mean_list)
print("Mean is ====>", mean)
print("StandDv is ====>", sd)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["date"], show_hist = False)
    fig.show()

first_sd_start, first_sd_end = mean - sd, mean + sd
second_sd_start, second_sd_end = mean -(2 * sd), mean +(2* sd)
third_sd_start, third_sd_end = mean -(3 * sd), mean +(3 * sd)

print("StandD1", first_sd_start, first_sd_end)
print("StandD2", second_sd_start, second_sd_end)
print("StandD3", third_sd_start, third_sd_end)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist= False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.20], mode ="lines", name="MEAN"))
fig.add_trace(go.Scatter(x = [first_sd_start,first_sd_start], y = [0,0.20], mode ="lines", name="Sd one Start"))
fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.20], mode ="lines", name="Sd one end"))
fig.add_trace(go.Scatter(x = [second_sd_start,second_sd_start], y = [0,0.20], mode ="lines", name="Sd two Start"))
fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.20], mode ="lines", name="Sd two end"))
fig.add_trace(go.Scatter(x = [third_sd_start,third_sd_start], y = [0,0.20], mode ="lines", name="Sd 3 Start"))
fig.add_trace(go.Scatter(x = [third_sd_end,third_sd_end], y = [0,0.20], mode ="lines", name="Sd 3 end"))
fig.show()