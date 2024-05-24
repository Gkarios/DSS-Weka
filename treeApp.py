import streamlit as st

# Define the decision tree prediction function
def predict_student_performance(features):
    G1 = features['G1']
    absences = features['absences']
    Fjob = features['Fjob']
    reason = features['reason']
    failures = features['failures']
    age = features['age']
    goout = features['goout']
    Pstatus = features['Pstatus']
    activities = features['activities']
    Mjob = features['Mjob']
    Fedu = features['Fedu']
    famrel = features['famrel']

    if G1 < 11.5:
        if G1 < 8.5:
            if absences < 1:
                return 5
            else:
                if Fjob == 'teacher':
                    return 11
                elif Fjob == 'other':
                    if reason == "school's course program":
                        return 8.86
                    elif reason == 'other':
                        return 8
                    elif reason == 'close from home':
                        return 9.2
                    elif reason == 'reputation of school':
                        return 9.83
                elif Fjob == 'services':
                    if reason == "school's course program":
                        return 8.5
                    elif reason == 'other':
                        return 5.5
                    elif reason == 'close from home':
                        return 8.5
                    elif reason == 'reputation of school':
                        return 8
                elif Fjob == 'health':
                    return 7
                elif Fjob == 'at_home':
                    return 8.29
        else:
            if failures < 0.5:
                if G1 < 10.5:
                    if absences < 20:
                        if age < 16.5:
                            if absences < 1.5:
                                if Mjob == 'at_home':
                                    return 9.25
                                elif Mjob == 'health':
                                    return 11
                                elif Mjob == 'other':
                                    return 11
                                elif Mjob == 'services':
                                    return 11.71
                                elif Mjob == 'teacher':
                                    return 12
                            else:
                                return 10.21
                        else:
                            if reason == "school's course program":
                                if Fjob == 'teacher':
                                    return 9
                                elif Fjob == 'other':
                                    if goout < 4.5:
                                        if Mjob == 'at_home':
                                            return 10.8
                                        elif Mjob == 'health':
                                            return 11.27
                                        elif Mjob == 'other':
                                            return 12.33
                                        elif Mjob == 'services':
                                            return 11
                                        elif Mjob == 'teacher':
                                            return 11
                                    else:
                                        return 10.67
                                elif Fjob == 'services':
                                    return 10.11
                                elif Fjob == 'health':
                                    return 10.58
                                elif Fjob == 'at_home':
                                    return 10
                            elif reason == 'other':
                                return 10.2
                            elif reason == 'close from home':
                                if Pstatus == 'living apart':
                                    return 13.5
                                elif Pstatus == 'living together':
                                    if activities == 'no':
                                        return 10.88
                                    elif activities == 'yes':
                                        return 12.25
                            elif reason == 'reputation of school':
                                return 11.57
                    else:
                        return 7.5
                else:
                    if absences < 8.5:
                        if reason == "school's course program":
                            if Fedu == "Has finished high school":
                                return 11.35
                            else:
                                return 13
                        elif reason == 'other':
                            return 11.58
                        elif reason == 'close from home':
                            return 12
                        elif reason == 'reputation of school':
                            return 11.65
                    else:
                        return 10.38
            else:
                return 9.37
    else:
        if G1 < 13.5:
            return 12.89
        else:
            if G1 < 15.5:
                if age < 16.5:
                    return 14.34
                else:
                    if famrel < 3.5:
                        return 14.18
                    else:
                        return 15.64
            else:
                if G1 < 16.5:
                    return 16.45
                else:
                    if studytime == "More than 3 hours":
                        return 18.33
                    else:
                        return 17.54

# Define the Streamlit app
st.title("Predict Student's Performance")

# Get user input
age = st.number_input("Age", min_value=15, max_value=20, step=1)
Pstatus = st.selectbox("Parental status", [ "living together", "living apart"])
Mjob = st.selectbox("Mother's job", ["civil services", "healthcare related", "at_home", "teacher", "other"])
Fjob = st.selectbox("Father's job", ["civil services", "healthcare related", "at_home", "teacher", "other"])
reason = st.selectbox("Reason for choosing the school", ["reputation of school", "school's course program", "close from home", "other", ])
activities = st.selectbox("Extra-curricular activities", ["yes", "no"])
failures = st.number_input("Past failed classes", min_value=0, max_value=5, step=1)
studytime = st.selectbox("Daily study Time", ["More than 3 hours", "Less than 3 hours"])
famrel = st.number_input("Time spent with family (hours)", min_value=0, max_value=15, step=1)
goout = st.number_input("Time spent outside (hours)", min_value=0, max_value=10, step=1)
absences = st.number_input("Absences", min_value=0, max_value=150, step=1)
Fedu = st.selectbox("Father's Education Level", ["Has finished high school", "Has not finished high school"])
G1 = st.number_input("Grade during first Semester", min_value=0.0, max_value=20.0, step=0.1)

# Collect user input into a dictionary
user_input = {
    'Pstatus': Pstatus,
    'Mjob': Mjob,
    'Fjob': Fjob,
    'reason': reason,
    'activities': activities,
    'age': age,
    'studytime' : studytime,
    'failures': failures,
    'famrel': famrel,
    'goout': goout,
    'absences': absences,
    'G1': G1,
    'Fedu': Fedu
}

# Make prediction
if st.button("Predict"):
    prediction = predict_student_performance(user_input)
    st.write(f"Prediction: {prediction}")

