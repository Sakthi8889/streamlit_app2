import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error

st.title(" ML App (Sample Data)")

df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5],
    "Pass": [0, 0, 1, 1, 1]
})

st.write("Dataset:", df)

X = df[["Hours"]]
y = df["Pass"]


model = LogisticRegression()
model.fit(X, y)

st.success("Model trained successfully!")


value = st.number_input("Enter study hours", value=3)

if st.button("Predict"):

    pred = model.predict([[value]])
    st.write("Prediction:", pred[0])

    sqrt_val = np.sqrt(value)
    st.write("Square Root:", sqrt_val)

  
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)

    st.write("Mean Squared Error (MSE):", mse)