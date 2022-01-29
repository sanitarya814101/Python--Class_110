import plotly.figure_factory as ff
import pandas as pd
import random
import statistics

df = pd.read_csv("average.csv")

list = df["average"].tolist()

fig = ff.create_distplot([list], ["aver"], show_hist=False)
# fig.show()


def RandomSetOFMean(counter):
    data_set = []
    for i in range(0, counter):
        index = random.randint(0, len(list)-1)
        value = list[index]
        data_set.append(value)

    mean = statistics.mean(data_set)
    return(mean)


def ShowFig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["average"], show_hist=False)
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
