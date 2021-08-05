import streamlit as st
import pickle
import pandas as pd 
import datetime



def main():
    st.title("Flight Fare Prediction")
    st.write("  ")
    st.subheader('Made By: MAAZ KHALID') 
    st.image("airline-logos.jpg",use_column_width=True)

    st.sidebar.subheader("Departure Details :airplane: ")
    m = pd.to_datetime("today").month
    d = pd.to_datetime("today").day
    y = pd.to_datetime("today").year
    
    dep = st.sidebar.date_input("Date" , datetime.date(y,m,d))
    if dep is not None:
        mon_d = dep.month
        day_d = dep.day

        hour_1 = st.sidebar.selectbox("Hour", list(range(1,25)))
        minute_1 = st.sidebar.selectbox("Minute", list(range(0,61)))

    st.subheader("Departure Time : :clock1:")
    x = "2021" + "/"  +str(mon_d) + "/" + str(day_d) + " " + str(hour_1) + ":" + str(minute_1)
    if x is not None:
        
        op = pd.to_datetime([x])
        if op is not None:
            st.write(op.item())
    

    st.sidebar.subheader("Arrival Details :airplane: ")
    arr = st.sidebar.date_input("Date." , datetime.date(y,m,d+1))
    if arr is not None:
    
        mon_a = arr.month
        day_a = arr.day
        
        hour_2 = st.sidebar.selectbox("Hour.", list(range(1,25)) ,2)
        minute_2 = st.sidebar.selectbox("Minute.", list(range(0,61)))

    st.subheader("Arrival Time : :clock5: ")
    x1 = "2020" + "/"  +str(mon_a) + "/" + str(day_a) + " " + str(hour_2) + ":" + str(minute_2)
    if x1 is not None:
        
        op1 = pd.to_datetime([x1] )
        if op1 is not None:
            st.write(op1.item())
            

     #source
    st.subheader("Select Source: :statue_of_liberty: ")
    source = st.selectbox(" " , ['Bangalore', 'Mumbai','Delhi','Kolkata',"Chennai"])
    if source == "Bangalore":
        source_inp = 0
    elif source == "Chennai":
        source_inp = 1
    elif source == "Delhi":
        source_inp = 2
    elif source == "Kolkata":
        source_inp = 3
    elif source == "Mumbai":
        source_inp = 4
    
    st.write("Departure from :airplane: --> " , source)

    #destination
    st.subheader("Select Destination: :tokyo_tower: ")
    dest = st.selectbox("" , ['Delhi', 'Cochin', 'Hyderabad',"New Delhi",'Bangalore','Kolkata'])

    if dest == "Bangalore":
        dest_inp = 0
    elif dest == "Cochin":
        dest_inp = 1
    elif dest == "Delhi":
        dest_inp = 2
    elif dest == "Hyderabad":
        dest_inp = 3
    elif dest == "Kolkata":
        dest_inp = 4
    elif dest == "New Delhi":
        dest_inp = 5

    st.write("Destination :airplane: -->  ",dest)

    #airline
    st.subheader("Select Airline")
    airline = st.selectbox("  " , ["Air India","GoAir","IndiGo","Jet Airways","Multiple carriers","SpiceJet",
                                    "Vistara","Air Asia"])

    if airline == "Jet Airways":
        air_inp = 0
    elif airline == "IndiGo":
        air_inp = 1
    elif airline == "Air India":
        air_inp = 2
    elif airline == "Multiple carriers":
        air_inp = 3
    elif airline == "SpiceJet":
        air_inp = 4
    elif airline == "Vistara":
        air_inp = 5
    elif airline == "Air Asia":
        air_inp = 6
    elif airline == "GoAir":
        air_inp = 7
    
    st.write("Airline selected :airplane: -->  " , airline)

    #stops
    st.subheader("Select Stops")
    stop = st.selectbox("   " , [0,1,2,3,4])
    st.write("Number of layovers --> ", stop)

    #if st.button("Duration"):
    #    if op1 is not None:
    #        
    #        st.write((op1.item() - op.item()))

    
    op2 = str(op1-op)
    if op2 is not None:
        hr = int(op2.split(']')[0][-9:-7])
        mini = int(op2.split(']')[0][-6:-4])


    rfr_model = pickle.load(open("flight_fare_rf.pkl", "rb"))

    #prediction

    par = [air_inp , source_inp , dest_inp ,stop , mon_d , day_d , hour_1 , minute_1 , hour_2 ,minute_2 ,hr , mini]

    
    
    if st.button("PREDICT"):
        pred = rfr_model.predict([par])
        for i in pred:
            st.balloons()
            st.write("Your Fare Price is : " , round(i ,3)  , "INR")
            st.success(":airplane: Head onto [MAKEMYTRIP](https://www.makemytrip.com/flights/) to book now! :airplane: ")
            
       
    st.write("""    """)
    st.write("""    """)
   



if __name__ == "__main__":
    main()