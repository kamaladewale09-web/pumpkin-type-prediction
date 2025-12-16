import streamlit as st
import numpy as np
import pandas as pd

import pickle
from sklearn.neighbors import KNeighborsClassifier 

st.header(":blue Pumpkin variety prediction app.")
st.subheader("This app will predict the class of a pumpkin seed giving some features.")

#Loading the dataset
#pump = pd.read_excel('Pumpkin_Seeds_Dataset - Copy.xlsx')
#st.dataframe(pump)

#setting input parameters
left_column, middle_column, right_columns = st.columns(3)
Area = left_column.number_input('Area', min_value = 47939.000, max_value = 136574.00)
Perimeter = middle_column.number_input('Perimeter', min_value = 868.485000, max_value = 1559.450000)
Major_Axis_Length = right_columns.number_input('Major_Axis_Length', min_value = 320.844600, max_value = 661.911300)
Minor_Axis_Length = left_column.number_input('Minor_Axis_Length', min_value = 152.171800, max_value = 305.818000)
Convex_Area = middle_column.number_input('Convex_Area', min_value = 48366.000000, max_value = 138384.000000)
Equiv_Diameter = right_columns.number_input('Equiv_Diameter', min_value = 247.058400, max_value = 417.002900)
Eccentricity = left_column.number_input('Eccentricity', min_value = 0.492100, max_value = 0.948100)
Solidity = middle_column.number_input('Solidity', min_value = 0.918600, max_value = 0.994400)
Extent = right_columns.number_input('Extent', min_value = 0.468000, max_value = 0.8296000)
Roundness = left_column.number_input('Roundness', min_value = 0.554900, max_value = 0.939600)
Aspect_Ration = middle_column.number_input('Aspect_Ration', min_value = 1.148700, max_value = 3.144400)
Compactness = right_columns.number_input('Compactness', min_value = 0.560800, max_value = 0.904900)
#loading model
with open('svm_class.sav', 'rb') as m:
          model = pickle.load(m)

#input as dataframe
input_features =({'Area': Area, 'Perimeter':Perimeter, 'Major_Axis_Length': Major_Axis_Length, 'Minor_Axis_Length': Minor_Axis_Length, 'Convex_Area':Convex_Area,'Equiv_Diameter': Equiv_Diameter, 'Eccentricity':Eccentricity, 'Solidity':Solidity, 'Extent':Extent,'Roundness':Roundness, 'Aspect_Ration':Aspect_Ration, 'Compactness':Compactness})
        
input_df = pd.DataFrame(input_features, index = [0])
                         
#predicting
predicted_type = model.predict(input_df)

#printing prediction
if st.button('Show predicted_type'):
    st.subheader(f":blue The  predicted type of the pumpkin is {predicted_type[0]}.")
