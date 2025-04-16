import pandas as pd
import datetime
import numpy as np

FITNOTESCSV = "fitnotes.csv"
TARGETCSV = "target.csv"
CONVERSIONS = "conversions.xlsx"


enddf=  pd.read_csv(TARGETCSV,header=0,index_col=False)

df = pd.read_csv(FITNOTESCSV, sep=",", header=0, index_col=False)
print(df)

#Convert date to correct format

df["Date"] = pd.to_datetime(df["Date"],"raise",False,True,True,"%Y-%m-%d",True).dt.strftime("%#d %b %Y, %H:%M")
print(df)







#Index workouts

dates = df["Date"].unique()
#categories = df["Exercise"].unique()
tempdf = pd.DataFrame()
df.insert(3,"set_index",df.groupby(["Date","Exercise"]).cumcount())


        


#Format time
enddf["title"] = "Workout"
enddf["start_time"] = df["Date"]
enddf["end_time"] = pd.to_datetime(df["Date"]) + datetime.timedelta(hours=1)

#format description
enddf["description"] = ""



#replace workout names
conversionsdf = pd.read_excel(CONVERSIONS,index_col=0)
print(conversionsdf)
conversions = conversionsdf.to_dict()["New"]

#Average out workouts with aliases

aliases = conversionsdf.to_dict()["Variations"]

#for alias in aliases:
    #for item in aliases[alias].split(","):
        


print("Before")
print(df["Exercise"].head(50))
df = df.replace(conversions)
print("After")
print(df["Exercise"].head(50))




#Format workout names
enddf["exercise_title"] = df["Exercise"]

#Format superset id (not implemented)
enddf["superset_id"] = pd.Series()


#Format comments
enddf["exercise_notes"] = df["Comment"]
print(enddf)

#Format set index
enddf["set_index"] = df["set_index"]

#Format set type (no superset functionality yet)
enddf["set_type"] = "normal"

#Add weight and reps
enddf["weight_kg"] = df["Weight"]
enddf["reps"] = df["Reps"]

#Finish off with filler stuff
enddf["distance_miles"] = pd.Series()
enddf["duration_seconds"] = pd.Series()
enddf["rpe"] = pd.Series()
