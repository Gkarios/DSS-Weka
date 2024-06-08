import streamlit as st

def predict_score(age, Mjob, Fjob, reason, failures, higher, freetime, Walc, G1):
    # Encoding categorical variables
    Mjob_services_health_teacher = 1 if Mjob in ['civil services', 'healthcare', 'teacher'] else 0
    Fjob_services_other_health_teacher = 1 if Fjob in ['civil services', 'other', 'healthcare', 'teacher'] else 0
    reason_course_home_reputation = 1 if reason in ['school curriculum', 'close from home', 'reputation of school'] else 0
    higher_yes = 1 if higher == 'yes' else 0

    # Linear regression function
    score = (
        0.2006 * age +
        0.2186 * Mjob_services_health_teacher +
        -0.4898 * Fjob_services_other_health_teacher +
        0.5879 * reason_course_home_reputation +
        -0.5505 * failures +
        0.4265 * higher_yes +
        -0.103 * freetime +
        -0.1115 * Walc +
        0.9047 * G1 +
        -1.5927
    )
    if score > 20:
        score = 19.7
    return score

# Streamlit app
st.title('Predict Score using Linear Regression')

age = st.number_input('Age', min_value=0, max_value=20, value=15)
Mjob = st.selectbox('Mother\'s Job (Mjob)', ['at home', 'healthcare', 'civil services', 'teacher', 'other'])
Fjob = st.selectbox('Father\'s Job (Fjob)', ['at home', 'healthcare', 'civil services', 'teacher', 'other'])
reason = st.selectbox('Reason for choosing school (reason)', ['close from home', 'reputation of school', 'school curriculum', 'other'])
failures = st.number_input('Number of past class failures (failures)', min_value=0, max_value=10, value=0)
higher = st.selectbox('Wants to take higher education (higher)', ['yes', 'no'])
freetime = st.slider('Free time after school (freetime)', min_value=1, max_value=5, value=3)
Walc = st.slider('Weekend alcohol consumption (Walc)', min_value=1, max_value=5, value=2)
G1 = st.slider('First period grade (G1)', min_value=0, max_value=20, value=10)

if st.button('Predict'):
    score = predict_score(age, Mjob, Fjob, reason, failures, higher, freetime, Walc, G1)
    st.write(f'The predicted score is: {score:.2f}')

