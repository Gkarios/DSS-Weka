import streamlit as st
from py4j.java_gateway import JavaGateway, GatewayParameters

# Connect to the manually started gateway
try:
    gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25333, auto_convert=True))
except Exception as e:
    st.error(f"Error connecting to the Java Gateway: {e}")

# Check connection
try:
    jvm_version = gateway.jvm.java.lang.System.getProperty("java.version")
    st.write(f"Connected to JVM version: {jvm_version}")
except Exception as e:
    st.error(f"Error accessing JVM: {e}")

# Load your Weka model
model_path = r"C:\Users\nikol\OneDrive\Documents\demo\src\main\java\com\example\demo\student_perfomance.model"

try:
    serialization_helper = gateway.entry_point.getSerializationHelper()
    classifier = serialization_helper.read(model_path)
    st.write("Model loaded successfully.")
except Exception as e:
    st.error(f"Error loading Weka model: {e}")

# Define the Streamlit app
st.title("Predict Student's Performance")

# Get user input
sex = st.selectbox("Sex", ["M", "F"])
address = st.selectbox("Address (urban or rural)", ["U", "R"])
familySize = st.selectbox("Family size (Greater Than 3 members?)", ["GT3", "LT3"])
pStatus = st.selectbox("Parental status", ["A", "T"])
Medu = st.selectbox("Mother's education", [0, 1, 2, 3, 4])
Fedu = st.selectbox("Father's education", [0, 1, 2, 3, 4])
Mjob = st.selectbox("Mother's job", ["at_home", "health", "other", "services", "teacher"])
Fjob = st.selectbox("Father's job", ["teacher", "other", "services", "health", "at_home"])
reason = st.selectbox("Reason", ["course", "other", "home", "reputation"])
guardian = st.selectbox("Kid's guardian", ["mother", "father", "other"])
schoolsup = st.selectbox("School support", ["yes", "no"])
paid = st.selectbox("Paid classes", ["yes", "no"])
activities = st.selectbox("Extra-curricular activities", ["yes", "no"])
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
Walc = st.number_input("Alcohol Consumption during weekends")
absences = st.number_input("Absences")
g1 = st.number_input("Grade during first Semester")
school = st.selectbox("School", ["GP", "MS"])
famsup = st.selectbox("Family educational support", ["yes", "no"])
romantic = st.selectbox("With a romantic relationship?", ["yes", "no"])
Dalc = st.number_input("Workday alcohol consumption")
health = st.number_input("Current health status")
G3_default = 0

# Create an instance from user input
data = [school, sex, age, address, familySize, pStatus, Medu, Fedu, Mjob, Fjob, reason, guardian, traveltime, studytime, failures, schoolsup, famsup, paid, activities, nursery, higher, internet, romantic, famrel, freetime, goout, Dalc, Walc, health, absences, g1,G3_default]


# Map categorical values to numeric values if needed
# This mapping should include all possible values for each attribute
categorical_mapping = {
    "M": 0, "F": 1,
    "GP": 0, "MS": 1,
    "U": 0, "R": 1,
    "LE3": 0, "GT3": 1,
    "T": 0, "A": 1,
    "teacher": 0, "health": 1, "services": 2, "at_home": 3, "other": 4,
    "course": 0, "other": 1, "home": 2, "reputation": 3,
    "mother": 0, "father": 1, "other": 2,
    "yes": 1, "no": 0
    # Add mappings for other categorical values as needed
}

# Map categorical values to numeric values
mapped_data = [categorical_mapping.get(value, value) for value in data]

st.write(f"Mapped data: {mapped_data}")

st.write(f"Number of attributes: {len(mapped_data)}")

# Calculate class index (assuming G1 is the last attribute in the dataset)
class_index = len(mapped_data) - 1

# Define a function to predict using the Weka model
def predict(data):
    try:
        # Create a DenseInstance with the provided data
        attributes = gateway.jvm.java.util.ArrayList()
        for i in range(len(mapped_data) - 1):  # Exclude the target attribute
            attributes.add(gateway.jvm.weka.core.Attribute(f"attr{i}"))
        instances = gateway.jvm.weka.core.Instances("Rel", attributes, 0)
        instances.setClassIndex(class_index)
        
        # Prepare attribute values for the DenseInstance
        attribute_values = gateway.jvm.java.util.ArrayList()
        for value in data[:-1]:  # Exclude the target attribute value
            attribute_values.add(value)
        
        instance = gateway.jvm.weka.core.DenseInstance(1.0, attribute_values)
        instance.setDataset(instances)
        
        # Make prediction
        prediction = classifier.classifyInstance(instance)
        return prediction
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Make prediction
if st.button("Predict"):
    prediction = predict(mapped_data)
    st.write("Prediction:", prediction)
