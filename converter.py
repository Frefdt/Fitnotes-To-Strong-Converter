import pandas as pd
import datetime
import numpy as np

FITNOTESCSV = "fitnotes.csv" #Put fitnotes import here
TARGETCSV = "target.csv"
CONVERSIONS = "conversions.xlsx" # Fitnotes to Strong lookup

df = pd.read_csv(FITNOTESCSV, sep=",", header=0, index_col=False)

enddf = pd.read_csv(TARGETCSV, nrows=0)  # just get columns
enddf = pd.DataFrame(columns=enddf.columns)  # new empty DataFrame with same columns
enddf = enddf.reindex(index=df.index)  # now match number of rows in df


#Convert date to correct format

df["Date"] = pd.to_datetime(df["Date"],"raise",False,True,True,"%Y-%m-%d",True).dt.strftime("%#d %b %Y, %H:%M")

#Index workouts

dates = df["Date"].unique()
#categories = df["Exercise"].unique()
tempdf = pd.DataFrame()
df.insert(3,"set_index",df.groupby(["Date","Exercise"]).cumcount())


        


#Format time
enddf["title"] = "Workout"
enddf["start_time"] = df["Date"]
enddf["end_time"] = (pd.to_datetime(enddf["start_time"]) + datetime.timedelta(hours=1)).dt.strftime("%#d %b %Y, %H:%M")

#format description
enddf["description"] = "EMPTY_QUOTE"



#replace workout names
conversionsdf = pd.read_excel(CONVERSIONS,index_col=0)
print(conversionsdf)
conversions = conversionsdf.to_dict()["New"]
df = df.replace(conversions)


#Format workout names
enddf["exercise_title"] = df["Exercise"]

#Format superset id (not implemented)
enddf["superset_id"] = pd.Series()


#Format comments
enddf["exercise_notes"] = df["Comment"].fillna("EMPTY_QUOTE")
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

#Finished CSV needs quotes but .to_csv doesn't let you only keep some columns NA with others as empty quotes 
csv_string = enddf.to_csv(index=False)
csv_string = csv_string.replace("EMPTY_QUOTE", '""')
with open("converted.csv", "w", newline="") as f:
    f.write(csv_string)

print("Finished converting. File saved to converted.csv")