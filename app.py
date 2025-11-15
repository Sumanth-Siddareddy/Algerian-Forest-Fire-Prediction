import streamlit as st
import pickle
import numpy as np

# --- 1. LOAD MODELS ---

@st.cache_resource
def load_model():
    """Loads the pickled Ridge model."""
    try:
        with open('ridge.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Error: 'ridge.pkl' not found. Please ensure the file is in the same directory.")
        return None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

@st.cache_resource
def load_scaler():
    """Loads the pickled StandardScaler."""
    try:
        with open('scaler.pkl', 'rb') as file:
            scaler = pickle.load(file)
        return scaler
    except FileNotFoundError:
        st.error("Error: 'scaler.pkl' not found. Please ensure the file is in the same directory.")
        return None
    except Exception as e:
        st.error(f"Error loading scaler: {e}")
        return None

# Load the models
model = load_model()
scaler = load_scaler()

# --- 2. APP INTERFACE (UI) ---

st.title('🔥 Algerian Forest Fire (FWI) Prediction')
st.write("""
Provide the feature values to predict the Fire Weather Index (FWI).
The inputs will be scaled before prediction.
""")

st.divider()

# --- 3. INPUT FORM ---
# We use st.form to group inputs and have a single submit button
with st.form(key='prediction_form'):
    st.header("Enter Feature Values")

    # Create columns for a cleaner layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Climatic Data")
        # Integer inputs
        Temperature = st.number_input('Temperature (°C)', min_value=22, max_value=42, value=32, step=1, help="Temperature in Celsius")
        RH = st.number_input('Relative Humidity (%)', min_value=21, max_value=90, value=55, step=1, help="Relative Humidity in percentage")
        Ws = st.number_input('Wind Speed (km/h)', min_value=6, max_value=29, value=15, step=1, help="Wind speed in km/h")
        
        # Float input
        Rain = st.number_input('Rain (mm)', min_value=0.0, value=0.0, step=0.1, format="%.1f", help="Rainfall in mm")

    with col2:
        st.subheader("FWI System Components")
        # Float inputs
        FFMC = st.number_input('FFMC (Fine Fuel Moisture Code)', min_value=28.6, value=80.5, step=0.1, format="%.1f")
        DMC = st.number_input('DMC (Duff Moisture Code)', min_value=1.1, value=15.0, step=0.1, format="%.1f")
        ISI = st.number_input('ISI (Initial Spread Index)', min_value=0.0, value=7.0, step=0.1, format="%.1f")

    st.divider()

    col3, col4 = st.columns(2)

    with col3:
        # Categorical input (mapped to float)
        region_str = st.selectbox('Region', ('Bejaia', 'Sidi-Bel Abbes'), help="Select the region")
        # Map string to float
        Region = 0.0 if region_str == 'Bejaia' else 1.0

    with col4:
        # Categorical input (mapped to float)
        classes_str = st.selectbox('Classes', ('Not Fire', 'Fire'), help="Select the fire class")
        # Map string to float
        Classes = 0.0 if classes_str == 'Not Fire' else 1.0
        

    # The form submit button
    st.write("") # Add some space
    submitted = st.form_submit_button("Predict FWI")

# --- 4. PREDICTION LOGIC ---

# This block runs *after* the form is submitted
if submitted:
    if model is not None and scaler is not None:
        try:
            # 1. Collect all features into a 2D numpy array
            # The order MUST be the same as your model's training data
            input_data = np.array([[
                Temperature, 
                RH, 
                Ws, 
                Rain, 
                FFMC, 
                DMC, 
                ISI, 
                Classes, 
                Region
            ]])

            # 2. Scale the input data
            scaled_data = scaler.transform(input_data)

            # 3. Make prediction
            prediction = model.predict(scaled_data)

            # 4. Display the result
            st.subheader('Prediction Result')
            st.success(f'**Predicted FWI:** `{prediction[0]:.2f}`')
            
            # Optional: Show the inputs
            st.subheader("Inputs Provided:")
            st.write(f"- **Climatic:** Temp: {Temperature}, RH: {RH}, Ws: {Ws}, Rain: {Rain}")
            st.write(f"- **Components:** FFMC: {FFMC}, DMC: {DMC}, ISI: {ISI}")
            st.write(f"- **Area:** Classes: {classes_str} ({Classes}), Region: {region_str} ({Region})")


        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
            st.error("Please check that your input data matches the model's requirements.")
    else:
        st.error("Models are not loaded. Please check file paths and errors above.")