import matplotlib.pyplot as pt
import pandas as pd
data=pd.read_csv("Book1.csv")
fig=pt.figure()
fig.patch.set_facecolor("gray")
graph1=fig.add_subplot(2,2,1,facecolor="yellow")
graph1.bar(data["Marks"],data["Points"],color=["orange","green","red"])
graph1.set_title("Marks vs Points")

graph2=fig.add_subplot(2,2,2,facecolor="lightgreen")
graph2.plot(data["Rupees"],data["Points"],color="orange")
graph2.set_title("Rupees vs Point")

graph3=fig.add_subplot(2,1,2,facecolor="orange")

x=len(data[data.Rupees>=100])
x1=len(data[data.Points<50])
x2=len(data[data.Marks>50])
graph3.pie([x,x1,x2],colors=["Yellow","orange","Red"],labels=['9 pointer','8 pointer','others'])


pt.show()



#pt.plot(data["Marks"],data["Points"],color="orange",label="bakchodi")
#pt.scatter(data["Marks"],data["Points"],color=["blue"],label="chutiyapna")
#pt.xlabel("Marks",color="red")
#pt.ylabel("Pota chatai",color="red")
#pt.legend()
#pt.title("Chutiya Banaya Bda Mja Aya",color="green")
#pt.show()
