import os, sys
import pandas as pd
df = pd.read_csv("/Users/karansagoo/PycharmProjects/Resume/mkaedir/MMgroup.csv")
df1 = df.astype(basestring).copy()
# print df1["name"][2]
#
#
# print df.info()


for i in range(0,153):
    path = "/Users/karansagoo/PycharmProjects/Resume/mkaedir/"
    os.mkdir(path + df1["name"][i], 0755);


