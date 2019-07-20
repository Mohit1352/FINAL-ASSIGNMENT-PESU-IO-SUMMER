#accuracy of model by linear regression : 100%
import numpy as np
import pandas as pd
from sklearn import linear_model
import os
import csv
files=os.listdir(".\dataset\Split")
tf=open("results.txt","w")
tacc=0
for file in files:
    if "train" in file:
        model=linear_model.LinearRegression()
        X=pd.read_csv(".\dataset\Split\{f}".format(f=file),sep=',',header=None)
        y=X.iloc[:,4]
        x2=X.iloc[:,[2,3,4,5,6,8,11,12,13,14,15,16,17,18,19,20,22]]
        model.fit(x2,y)
        tf.write(file[:-10])
        tfile=file.replace("train","test")
        X1=pd.read_csv(".\dataset\Split\{f}".format(f=tfile),sep=',',header=None)
        ypred=model.predict(X1.iloc[:,[2,3,4,5,6,8,11,12,13,14,15,16,17,18,19,20,22]])
        ypredl=ypred.tolist()
        ytruel=X1.iloc[:,4].tolist()
        count=0
        for i in range(len(ytruel)):
            if(ytruel[i]-ypredl[i]<=0.000000000005 and ytruel[i]-ypredl[i]>=-0.000000000005):
                count+=1
        acc=(count/len(ytruel))*100
        tacc=tacc+acc
        tf.write(" : "+str(acc)+"%\n")
    print("DONE")
tacc=tacc/(len(files)/2)
tf.write("\naverage_accuracy : "+str(tacc)+"% \n")
tf.write("(Precision: up to +-0.000000000005)\n\n")
tf.close()
print("ALL DONE")
