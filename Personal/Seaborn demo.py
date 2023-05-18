import seaborn as sn
import matplotlib.pyplot as mp

#Datasets in seaborn
#l = sn.get_dataset_names()
#for i in l:
#    print(i)

#Styles = white, dark, whitegrid, darkgrid, ticks

f = sn.load_dataset("fmri")
#print(f.columns)
#sn.set(style = "white")
#sn.barplot(x="subject", y="timepoint", data=f)
#mp.show()


df = sn.load_dataset("iris")
#print(df.columns)
#sn.set(style = "ticks")
#sn.barplot(x="sepal_length", y="sepal_width", data=df)
#mp.show()


df1 = sn.load_dataset("titanic")
#print(df1.columns)
#sn.set(style = "dark")
#sn.lineplot(x="age", y="alive", data=df1)
#mp.show()


df2 = sn.load_dataset("planets")
#print(df2.columns)
#sn.set(style = "dark")
#sn.lineplot(x="method", y="distance", data=df2)
#mp.show()


df3 = sn.load_dataset("dowjones")
#print(df3.columns)
#sn.set(style = "dark")
#sn.barplot(x="Date", y="Price", data=df3)
#mp.show()







