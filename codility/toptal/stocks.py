import numpy as np
import pandas as pd


def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    df = pd.DataFrame()
    for file in files:
        dff = pd.read_csv(file, parse_dates=['date'])
        print(dff.head())
    #     df = pd.concat([df, dff])
    # df.head()