import streamlit as st
import joblib


# Initialize the JVM

# Load the Weka model

# Define the Streamlit app
st.title("Predict Student's Performance")

# Get user input
sex = st.selectbox("Sex", ["M","F"])
address = st.selectbox("Address (urban or rural)", ["U","R"])
familySize = st.selectbox("Family size (Greater Than 3 members?)", ["GT3", "LT3"])
pStatus = st.selectbox("Parental status", ["A", "T"])
Mjob = st.selectbox("Mother's job", ["at_home", "health", "other", "services", "teacher"])
Fjob = st.selectbox("Father's job", ["teacher", "other", "services", "health", "at_home"])
reason = st.selectbox("Reason", ["course", "other", "home", "reputation"])
guardian = st.selectbox("Kid's guardian", ["mother", "father", "other"])
schoolsup = st.selectbox("School support", ["yes", "no"])
paid = st.selectbox("Paid classes", ["yes", "no"])
activities = st.selectbox("Extra-cirriculum activities", ["yes", "no"])
nursery = st.selectbox("Nursery", ["yes", "no"])
higher = st.selectbox("Higher Education", ["yes", "no"])
internet = st.selectbox("Internet at home?", ["yes", "no"])
age = st.number_input("Age")
traveltime = st.number_input("Travel time from home to school (minutes)")
studytime = st.number_input("Study time (hours)")
failures = st.number_input("Past failed classes")
famrel = st.number_input("Time spent with family (hours)")
freetime = st.number_input("Free time (hours)")
goout = st.number_input("Time spent outside (hours)")
Walc = st.number_input("Alchohol Consumption during weekends")
absences = st.number_input("Absences")
G1 = st.number_input("Grade during first Semester")




# Create an instance from user input
data = [sex, address, familySize, pStatus, Mjob, Fjob, reason, guardian, schoolsup, paid, activities, nursery, higher, internet, age, traveltime, studytime, failures, famrel, freetime, goout, absences, G1]

# Make prediction
if st.button("Predict"):
    st.write("Prediction ")
# Display the prediction
