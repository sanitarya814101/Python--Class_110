import pandas as pd
import statistics
import plotly.figure_factory as ff
import random

df = pd.read_csv("data.csv")

data = df["temp"].tolist()

# mean = statistics.mean(data)

# print(mean)
# fig = ff.create_distplot([data], ["temp"], show_hist=False)
# fig.show()


# standard_deviation = statistics.stdev(data)
# print(standard_deviation)

# data_set = []

# for i in range(0, 100):
#     index = random.randint(0, len(data))
#     value = data[index]
#     data_set.append(value)

# mean = statistics.mean(data_set)
# standard_deviation = statistics.stdev(data_set)

# print(mean)
# print(standard_deviation)

def RandomSetOFMean(counter):
    data_set = []
    for i in range(0, counter):
        index = random.randint(0, len(data)-1)
        value = data[index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    return(mean)


def ShowFig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()


def setup():
    mean_list = []
    for i in range(0, 1000):
        mean = RandomSetOFMean(100)
        mean_list.append(mean)

    ShowFig(mean_list)

    mean = statistics.mean(mean_list)
    standard_deviation = statistics.stdev(mean_list)

    print(mean)
    print(standard_deviation)


setup()
