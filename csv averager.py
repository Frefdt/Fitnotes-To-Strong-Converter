from logging import exception

import pandas as pd
import os
import csv

folders = ["FcfsScheduler","FeedbackRRScheduler","IdealSJFScheduler","RRScheduler","SJFScheduler"]
output_file = "Experiment-1-Averages"
results = {alg:{} for alg in folders}
HEADERS = ["id","priority","createdTime","startedTime","terminatedTime","cpuTime","blockedTime","turnaroundTime","waitingTime","responseTime"]
variables = ["high","low"]
for algorithm in folders:
    variableOuts ={var:pd.DataFrame() for var in variables}
    for variable in variables:
        currentDF=pd
        for filename in os.listdir(f"./{algorithm}"):
            if filename.endswith(".csv") and variable in filename:
                df = pd.read_csv(f"{algorithm}/{filename}", sep=",",header=0,index_col=False)
                currentDF = variableOuts[variable]
                df.apply(pd.to_numeric,errors="coerce")
                #input("")
                variableOuts[variable] = pd.concat([currentDF,df])
                currentDF = variableOuts[variable]
                #input("")

        tempdf=pd.DataFrame(columns=HEADERS)
        print("Tempdf")
        print(tempdf)
        print("tempDF HEADERS")
        print(tempdf.columns)
        print("curentDF")
        print(currentDF)
        results[algorithm][variable]={}
        for head in HEADERS:
            results[algorithm][variable][head]=variableOuts[variable][head].mean()
                #tempdf = tempdf.concat([pd.DataFrame({head:[pd.to_numeric(currentDF[head],errors="coerce").mean(numeric_only=True)]})])
        print()
        #input("")
        #this is so bad
        #for head in variableOuts[variable].columns:
         #   results[algorithm].append(results[algorithm][variable].append({head:variableOuts[variable].mean(numeric_only=True)}))

    print("Results for " + algorithm)
    print("--------------------------------")
    print(results[algorithm])

print("---------------------")
print("RESULTS")
print("------------------")
print(results)


for alg in folders:
    cols=HEADERS.copy()
    cols.append("variable")
    tempdf=pd.DataFrame(columns=cols)
    print("tempdf")
    print(tempdf)
    for v in results[alg]:
        temperdf=pd.DataFrame([results[alg][v]])
        temperdf["variable"]=v
        print("temperdf")
        print(temperdf)
        tempdf=pd.concat([tempdf,temperdf])
        print("conbined df")
        print("tempdf")
    print("finished df")
    print(tempdf)
    tempdf.to_csv(f'{alg}averages.csv', index=False)
    print("created csv "+f'{alg}averages.csv')







