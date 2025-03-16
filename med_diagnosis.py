import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Ensure that heart_disease_prediction.py is in the same directory or provide the correct path

st.set_page_config(page_title="Medical diagnosis using AI", page_icon="🩺") 

hide_st_style = """
	         <style>
		 #MainMenu {visibility: hidden;}
		 header {visibility: hidden;}
		 footer {visibility: hidden;}
		 </style>
		 """
st.markdown(hide_st_style, unsafe_allow_html=True)

background_image_url = "https://d2jx2rerrg6sh3.cloudfront.net/image-handler/ts/20240405072922/ri/950/src/images/news/ImageForNews_776422_17123165547518811.jpg"

page_by_image = f"""
<style>
[data-testid = "stAppViewContainer"] {{
 background-image: url({background_image_url});
 background-size: cover;
 background-position: center;
 background-attachment: fixed;
}}

[data-testid = "stAppViewContainer"]:: before {{
 content: "";
 position: absolute;
 top: 0;
 left: 0;
 width: 100%;
 height: 100%;
 background: linear-gradient(rgba(0, 0, 0, 0.2),rgba(0, 0, 0, 0.5));
}}
</style>
"""

st.markdown(page_by_image, unsafe_allow_html=True)

models = { 'Heart Disease': pickle.load(open(r"C:\Users\bhava\OneDrive\Desktop\AICTE PROJECT\heart_disease_model.sav",'rb')),
          'Liver Cancer': pickle.load(open(r"C:\Users\bhava\OneDrive\Desktop\AICTE PROJECT\liver_cancer_model.sav",'rb')),
          'Dementia': pickle.load(open(r"C:\Users\bhava\OneDrive\Desktop\AICTE PROJECT\dementia_model.sav",'rb')),
          'Chronic Kidney Disease': pickle.load(open(r"C:\Users\bhava\OneDrive\Desktop\AICTE PROJECT\chronic_kidney_disease_model.sav",'rb')),
     }

selected = st.selectbox(
     'Select a disease to predict',
     ['Heart Disease Prediction',
      'Liver Cancer Prediction',
      'Dementia Prediction',
      'Chronic Kidney Disease Prediction',]
)

def display_input(key, tooltip, label, input_type, options=None):
     if input_type == "text":
          return st.text_input(label, key=key)
     elif input_type == "number":
          return st.number_input(label, key=key, step=0.0001, format="%.6f")
     elif input_type == "radio":
          return st.radio(label, options, key=key)


if selected == "Heart Disease Prediction":
     st.title("Heart Disease Prediction 🫀")
     st.write("Enter the following details to predict heart disease")

     AGE = display_input("age", "Enter the age of the person", "AGE", "number")
	
     GENDER = 1 if display_input("sex", "Enter the gender of the person", "GENDER", "radio", ["Male (1)", "Female (0)"]) == "Male (1)" else 0

     CHEST_PAIN_OPTIONS = ["Typical Angina (0)", "Atypical Angina (1)", "Non-Anginal Pain (2)", "Asymptomatic (3)"]
     CHEST_PAIN = CHEST_PAIN_OPTIONS.index(display_input("cp", "Select the type of chest pain", "CHEST PAIN", "radio", CHEST_PAIN_OPTIONS))

     RESTING_BLOOD_PRESSURE = display_input("trestbps", "Enter the resting blood pressure", "RESTING BLOOD PRESSURE", "number")
	
     SERUM_CHOLESTEROL = display_input("chol", "Enter the serum cholesterol level", "SERUM CHOLESTEROL", "number")
	
     FASTING_BLOOD_SUGAR_VALUE = display_input("fbs", "Enter the fasting blood sugar level", "FASTING BLOOD SUGAR VALUE", "number")
	
     FASTING_BLOOD_SUGAR = 1 if FASTING_BLOOD_SUGAR_VALUE > 120 else 0 
     st.write(f"FASTING_BLOOD_SUGAR (Binary): {FASTING_BLOOD_SUGAR}")
	
     RESTING_ELECTROCARDIOGRAPHIC_RESULT_OPTIONS = ["Normal (0)", "Abnormality (1)", "Hypertrophy (2)"]
     RESTING_ELECTROCARDIOGRAPHIC_RESULT = RESTING_ELECTROCARDIOGRAPHIC_RESULT_OPTIONS.index(display_input("restecg", "Select the resting ECG result:", "RESTING ELECTROCARDIOGRAPHIC RESULT", "radio", RESTING_ELECTROCARDIOGRAPHIC_RESULT_OPTIONS))
     
     MAXIMUM_HEART_RATE_ACHIEVED = display_input("thalach", "Enter the maximum heart rate achieved:", "MAXIMUM HEART RATE ACHIEVED", "number")

     EXERCISED_INDUCED_ANGINA_OPTIONS = ["No (0)", "Yes (1)"]
     EXERCISED_INDUCED_ANGINA = EXERCISED_INDUCED_ANGINA_OPTIONS.index(display_input("exang", "Select if exercise-induced angina is present:", "EXERCISE INDUCED ANGINA", "radio", EXERCISED_INDUCED_ANGINA_OPTIONS))

     SLOPE_OF_PEAK_EXERCISE_ST_SEGMENT_OPTIONS = ["Unsloping (0)", "Flat (1)", "Downsloping (2)"]
     SLOPE_OF_PEAK_EXERCISE_ST_SEGMENT = SLOPE_OF_PEAK_EXERCISE_ST_SEGMENT_OPTIONS.index(display_input("slope", "Select the slope of peak exercise ST segment:", "SLOPE OF PEAK EXERCISE ST SEGMENT", "radio", SLOPE_OF_PEAK_EXERCISE_ST_SEGMENT_OPTIONS))

     FLUOROSCOPY = display_input("ca", "Enter the number of major vessels colored by fluoroscopy (0-3):", "FLUOROSCOPY", "number")

     THALASSEMIA_OPTIONS = ["Normal (0)", "Fixed defect (1)", "Reversible defect (2)"]
     THALASSEMIA = THALASSEMIA_OPTIONS.index(display_input("thal", "Select the type of thalassemia:", "THALASSEMIA", "radio", THALASSEMIA_OPTIONS))

     if st.button("HEART DISEASE TEST RESULT"):
          input_data = [[AGE, GENDER, CHEST_PAIN, RESTING_BLOOD_PRESSURE, SERUM_CHOLESTEROL,
                         FASTING_BLOOD_SUGAR, RESTING_ELECTROCARDIOGRAPHIC_RESULT, MAXIMUM_HEART_RATE_ACHIEVED,
                         EXERCISED_INDUCED_ANGINA, SLOPE_OF_PEAK_EXERCISE_ST_SEGMENT,
                         FLUOROSCOPY, THALASSEMIA]]
          heart_disease_prediction = models["Heart Disease"].predict(input_data)[0]
          # st.write(f"The person has a {'high' if heart_disease_prediction == 1 else 'low'} chance of having a heart disease")
          if heart_disease_prediction == 1:
               st.markdown(
                    """
                    <p style="color: red;
                      font-size: 24px;
                      font-weight: bold;
                      text-align: center;">
                      ⚠️ The person has Heart Disease! ⚠️
                    </p>
                    """,
            unsafe_allow_html=True
          )
          else:
               st.markdown(
                    """
                    <p style="color: green;
                      font-size: 24px;
                      font-weight: bold;
                      text-align: center;">
                      ✅ The person does not have Heart Disease.
                    </p>
                    """,
               unsafe_allow_html=True
          )



elif selected == "Liver Cancer Prediction":
     st.title("Liver Cancer Prediction 🍺")
     st.write("Enter the following details to predict liver cancer")

     AGE = display_input("Age", "Enter the age of the person", "AGE", "number")

     GENDER = 1 if display_input("Gender", "Enter the gender of the person", "GENDER", "radio", ["Male (1)", "Female (0)"]) == "Male (1)" else 0

     TOTAL_BILIRUBIN = display_input("Total_Bilirubin", "Enter the total bilirubin level", "TOTAL BILIRUBIN (TB)", "number")

     DIRECT_BILIRUBIN = display_input("Direct_Bilirubin", "Enter the direct bilirubin level", "DIRECT BILIRUBIN (DB)", "number")  

     ALKALINE_PHOSPHOTASE = display_input("Alkaline_Phosphotase", "Enter the alkaline phosphotase level", "ALKALINE PHOSPHOTASE (ALKPHOS)", "number")

     ALAMINE_AMINOTRANSFERASE = display_input("Alamine_Aminotransferase", "Enter the alamine aminotransferase level", "ALAMINE AMINOTRANSFERASE (SGPT)", "number")

     ASPARTATE_AMINOTRANSFERASE = display_input("Aspartate_Aminotransferase", "Enter the aspartate aminotransferase level", "ASPARTATE AMINOTRANSFERASE (SGOT)", "number")

     TOTAL_PROTEINS = display_input("Total_Proteins", "Enter the total proteins level", "TOTAL PROTEINS (TP)", "number")

     ALBUMIN = display_input("Albumin", "Enter the albumin level", "ALBUMIN (ALB)", "number")

     ALBUMIN_AND_GLOBULIN_RATIO = display_input("Albumin_and_Globulin_Ratio", "Enter the albumin and globulin ratio", "(A/G)ALBUMIN AND GLOBULIN RATIO ", "number")

     if st.button("LIVER CANCER TEST RESULT"):
          input_data = [[AGE, GENDER, TOTAL_BILIRUBIN, DIRECT_BILIRUBIN, ALKALINE_PHOSPHOTASE, ALAMINE_AMINOTRANSFERASE, ASPARTATE_AMINOTRANSFERASE, TOTAL_PROTEINS, ALBUMIN, ALBUMIN_AND_GLOBULIN_RATIO]]
          liver_cancer_prediction = models["Liver Cancer"].predict(input_data)[0]
          #st.write(f"The person has a {'high' if liver_cancer_prediction == 1 else 'low'} chance of having liver cancer")
          if liver_cancer_prediction == 1:
               st.markdown(
                    """
                    <p style="color: red;
                      font-size: 24px;
                      font-weight: bold;
                      text-align: center;">
                      ⚠️ The person has Liver Cancer! ⚠️
                    </p>
                    """,
            unsafe_allow_html=True
          )
          else:
               st.markdown(
                    """
                    <p style="color: green;
                      font-size: 24px;
                      font-weight: bold;
                      text-align: center;">
                      ✅ The person does not have Liver Cancer.
                    </p>
                    """,
            unsafe_allow_html=True
          )

elif selected == "Dementia Prediction":
     st.title("Dementia Prediction 🧠")
     st.write("Enter the following details to predict dementia")

     NO_OF_VISITS = display_input("Visit", "Enter the no of visits by the person", "NUMBER OF VISITS", "number")

     MRI_DELAY = display_input("MR Delay", "Enter the no of days between previous MRI scan and the current one", "MRI DELAY(no of days between consecutive MRI scans)", "number")

     GENDER = 1 if display_input("M/F", "Enter the gender of the person", "GENDER", "radio", ["Male (1)", "Female (0)"]) == "Male (1)" else 0

     HAND = 1 if display_input("Hand", "Enter the handedness of the person", "HANDEDNESS", "radio", ["Right (0)", "Left (1)"]) == "Left (1)" else 0

     AGE = display_input("Age", "Enter the age of the person", "AGE", "number")

     EDUCATION = display_input("EDUC", "Enter the no of years of education of the person", "EDUCATION", "number")

     SOCIOECONOMIC_STATUS_OPTIONS = ["Lower Class (1)", "Middle Class (2)", "Upper Middle Class (3)", "High Class (4)"]
     SOCIOECONOMIC_STATUS = SOCIOECONOMIC_STATUS_OPTIONS.index(display_input("SES", "Select the Socio-economic status of the person", "SOCIO-ECONOMIC STATUS", "radio", SOCIOECONOMIC_STATUS_OPTIONS))

     MMSE = display_input("MMSE", "Enter the score of the Mini-Mental State Examination", "MMSE (MINI-MENTAL STATE EXAMINATION)", "number")

     CDR = display_input("CDR", "Enter the Clinical Dementia Rating", "CDR (CLININAL DEMENTIA RATING: 0, 0.5, 1)", "number")

     ETIV = display_input("eTIV", "Enter the Estimated Total Intracranial Volume", "ETIV: Estimated Total Intracranial Volume", "number")

     NWBV = display_input("nWBV", "Enter the Normalized Whole Brain Volume", "NWBV: Normalized Whole Brain Volume", "number")

     ASF = display_input("ASF", "Enter the Atlas Scaling Factor", "ASF: Atlas Scaling Factor", "number")

     if st.button("DEMENTIA TEST RESULT"):
          input_data = [[NO_OF_VISITS, MRI_DELAY, GENDER, HAND, AGE, EDUCATION, SOCIOECONOMIC_STATUS, MMSE, CDR, ETIV, NWBV, ASF]]
          dementia_prediction = models["Dementia"].predict(input_data)[0]
          if dementia_prediction == 0:
               #dementia_diagnosis = "The person might develop dementia in a short while"
               st.markdown("""<p style="color: orange; font-size: 24px; font-weight: bold; text-align: center;">⚠️ WARNING: The person has high chances of developing dementia </p>""", unsafe_allow_html=True)
          elif dementia_prediction == 1:
               #dementia_diagnosis = "The person has dementia (or is demented)"
               st.markdown("""<p style="color: red; font-size: 24px; font-weight: bold; text-align: center;">⚠️ The person has dementia (or is demented).</p>""", unsafe_allow_html=True)
          else:
               #dementia_diagnosis = "The person does not have dementia (or is non-demented)"
               st.markdown("""<p style="color: green; font-size: 24px; font-weight: bold; text-align: center;">✅ The person does not have dementia (or is non-demented).</p>""", unsafe_allow_html=True)

elif selected == "Chronic Kidney Disease Prediction":
     st.title("Chronic Kidney Disease Prediction 🩸")
     st.write("Enter the following details to predict chronic kidney disease")

     AGE = display_input("age", "Enter the age of the person", "AGE", "number")

     BLOOD_PRESSURE = display_input("blood_pressure", "Enter the blood pressure of the person", "BLOOD PRESSURE", "number")

     SPECIFIC_GRAVITY = display_input("specific_gravity", "Enter the specific gravity of the urine of the person", "SPECIFIC GRAVITY", "number")

     ALBUMIN = display_input("albumin", "Enter the albumin level in the urine of the person", "ALBUMIN", "number")

     SUGAR = display_input("sugar", "Enter the sugar level in the urine of the person", "SUGAR", "number")

     RED_BLOOD_CELLS = 1 if display_input("red_blood_cells", "Enter the red blood cell count condition in the urine of the person", "RED BLOOD CELLS", "radio", ["Normal (1)", "Abnormal (0)"]) == "Normal (1)" else 0
          
     PUS_CELL = 1 if display_input("pus_cell", "Enter the pus cell count condition in the urine of the person", "PUS CELL", "radio", ["Normal (1)", "Abnormal (0)"]) == "Normal (1)" else 0
          
     PUS_CELL_CLUMPS = 1 if display_input("pus_cell_clumps", "Enter the pus cell clumps condition in the urine of the person", "PUS CELL CLUMPS", "radio", ["Present (1)", "Absent (0)"]) == "Present (1)" else 0

     BACTERIA = 1 if display_input("bacteria", "Enter the bacteria condition in the urine of the person", "BACTERIA", "radio", ["Present (1)", "Absent (0)"]) == "Present (1)" else 0    

     BLOOD_GLUCOSE_RANDOM = display_input("blood_glucose_random", "Enter the random blood glucose level of the person", "BLOOD GLUCOSE RANDOM", "number")

     BLOOD_UREA_LEVEL = display_input("blood_urea_level", "Enter the blood urea level of the person", "BLOOD UREA LEVEL", "number")

     SERUM_CREATININE = display_input("serum_creatinine", "Enter the serum creatinine level of the person", "SERUM CREATININE", "number")   

     SODIUM = display_input("sodium", "Enter the sodium level of the person", "SODIUM", "number")

     POTASSIUM = display_input("potassium", "Enter the potassium level of the person", "POTASSIUM", "number")

     HEMOGLOBIN = display_input("hemoglobin", "Enter the hemoglobin level of the person", "HEMOGLOBIN", "number")

     PACKED_CELL_VOLUME = display_input("packed_cell_volume", "Enter the packed cell volume of the person", "PACKED CELL VOLUME", "number")

     WHITE_BLOOD_CELL_COUNT = display_input("white_blood_cell_count", "Enter the white blood cell count of the person", "WHITE BLOOD CELL COUNT", "number")

     RED_BLOOD_CELL_COUNT = display_input("red_blood_cell_count", "Enter the red blood cell count of the person", "RED BLOOD CELL COUNT", "number")

     HYPERTENSION = 1 if display_input("hypertension", "Enter if the person has hypertension", "HYPERTENSION", "radio", ["Yes (1)", "No (0)"]) == "Yes (1)" else 0

     DIABETES_MELLITUS = 1 if display_input("diabetes_mellitus", "Enter if the person has diabetes mellitus", "DIABETES MELLITUS", "radio", ["Yes (1)", "No (0)"]) == "Yes (1)" else 0

     CORONARY_ARTERY_DISEASE = 1 if display_input("coronary_artery_disease", "Enter if the person has coronary artery disease", "CORONARY ARTERY DISEASE", "radio", ["Yes (1)", "No (0)"]) == "Yes (1)" else 0

     APPETITE = 1 if display_input("appetite", "Enter the appetite condition of the person", "APPETITE", "radio", ["Good (0)", "Poor (1)"]) == "Poor (1)" else 0   

     PEDAL_EDEMA = 1 if display_input("pedal_edema", "Enter if the person has pedal edema", "PEDAL EDEMA", "radio", ["Yes (1)", "No (0)"]) == "Yes (1)" else 0  

     ANEMIA = 1 if display_input("anemia", "Enter if the person has anemia", "ANEMIA", "radio", ["Yes (1)", "No (0)"]) == "Yes (1)" else 0

     if st.button("CHRONIC KIDNEY DISEASE TEST RESULT"):
          input_data = [[AGE, BLOOD_PRESSURE, SPECIFIC_GRAVITY, ALBUMIN, SUGAR, RED_BLOOD_CELLS, PUS_CELL, PUS_CELL_CLUMPS, BACTERIA, BLOOD_GLUCOSE_RANDOM, BLOOD_UREA_LEVEL, SERUM_CREATININE, SODIUM, POTASSIUM, HEMOGLOBIN, PACKED_CELL_VOLUME, WHITE_BLOOD_CELL_COUNT, RED_BLOOD_CELL_COUNT, HYPERTENSION, DIABETES_MELLITUS, CORONARY_ARTERY_DISEASE, APPETITE, PEDAL_EDEMA, ANEMIA]]
          chronic_kidney_disease_prediction = models["Chronic Kidney Disease"].predict(input_data)[0]
          #st.write(f"The person has a {'high' if chronic_kidney_disease_prediction == 1 else 'low'} chance of having chronic kidney disease")    
          if chronic_kidney_disease_prediction == 1:
               st.markdown(
                    """
                    <p style="color: red;
                      font-size: 24px;
                      font-weight: bold;
                      text-align: center;">
                      ⚠️ The person has Chronic Kidney Disease! ⚠️
                    </p>
                    """,
            unsafe_allow_html=True
          ) 
          else:
               st.markdown(
                    """
                    <p style="color: green;
                      font-size: 24px;
                      font-weight: bold;
                      text-align: center;">
                      ✅ The person does not have Chronic Kidney Disease.
                    </p>
                    """,
            unsafe_allow_html=True
          )