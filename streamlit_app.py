
import streamlit  as st
import joblib
import pandas as pd
import category_encoders
import sklearn
import xgboost

Model = joblib.load("Model.pkl")
Inputs = joblib.load("Inputs.pkl")

def prediction(Airline, Source, Destination, Month_of_Journey, Stops,Day_of_Journey_numbers,Duration_Categorized,Trip_distance,Dep_Day_Period,Arrival_Day_Period, Dep_Hour, Arrival_Hour,Meal):
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"Airline"] = Airline
    test_df.at[0,"Source"] = Source
    test_df.at[0,"Destination"] = Destination
    test_df.at[0,"Month_of_Journey"] = Month_of_Journey
    test_df.at[0,"Stops"] = Stops
    test_df.at[0,"Day_of_Journey_numbers"] = Day_of_Journey_numbers
    test_df.at[0,"Duration_Categorized"] = Duration_Categorized
    test_df.at[0,"Trip_distance"] = Trip_distance
    test_df.at[0,"Dep_Day_Period"] = Dep_Day_Period
    test_df.at[0,"Arrival_Day_Period"] = Arrival_Day_Period
    test_df.at[0,"Dep_Hour"] = Dep_Hour
    test_df.at[0,"Arrival_Hour"] = Arrival_Hour
    test_df.at[0,"Meal"] = Meal
    result = Model.predict(test_df)
    return result[0]
def main():
    Airline = st.selectbox("Airline" ,['Airline', 'Source', 'Destination', 'Month_of_Journey', 'Stops','Day_of_Journey_numbers', 'Duration_Categorized', 'Trip_distance','Dep_Day_Period', 'Arrival_Day_Period', 'Dep_Hour', 'Arrival_Hour','Meal'] )
    Source  = st.selectbox("Source" , ['Kolkata', 'Delhi', 'Banglore', 'Chennai', 'Mumbai'])
    Destination = st.selectbox("Destination" ,['Banglore', 'Cochin', 'New Delhi', 'Kolkata', 'Delhi', 'Hyderabad'] )
    Month_of_Journey = st.selectbox("Month_of_Journey" ,[5, 6, 3, 4] )
    Stops = st.selectbox("Stops" , [2, 1, 0, 3, 4])
    Day_of_Journey_numbers = st.selectbox("Day_of_Journey_numbers" , [ 1,  9, 12, 24, 27, 18,  3, 15,  6, 21])
    Duration_Categorized = st.selectbox("Duration_Categorized" , ['Short_duration', 'Medium_duration', 'Long_duration'])
    Trip_distance = st.selectbox("Trip_distance" , ['Medium_Dist', 'Long_Dist', 'Short_Dist'])
    Dep_Day_Period = st.selectbox("Dep_Day_Period" , ['Ealry_Morning', 'Afternoon', 'Evening', 'Night'])
    Arrival_Day_Period = st.selectbox("Arrival_Day_Period" ,['Afternoon', 'Night', 'Evening', 'Ealry_Morning'] )
    Dep_Hour = st.selectbox("Dep_Hour",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    Arrival_Hour = st.selectbox("Arrival_Hour",[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    Meal = st.selectbox("Meal" , [0, 1])
    if st.button("predict"):
        results = prediction(Airline, Source, Destination, Month_of_Journey, Stops,Day_of_Journey_numbers,Duration_Categorized,Trip_distance,Dep_Day_Period,Arrival_Day_Period, Dep_Hour, Arrival_Hour,Meal)
        st.text(f"The flight cost will be {results}")
if __name__ == '__main__':
    main() 
