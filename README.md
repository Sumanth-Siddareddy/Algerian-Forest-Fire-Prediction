# 🔥 Algerian Forest Fire (FWI) Prediction

This project is a machine learning web application built with Streamlit to predict the **Fire Weather Index (FWI)**. The model is trained on a dataset of forest fire observations from two regions in Algeria: Bejaia and Sidi-Bel Abbes.

The app allows a user to input various meteorological features and receive a real-time FWI prediction, which is a key indicator of wildfire risk.

---

## 🚀 Live Demo

[App : ](https://algerian-forest-fire-prediction-gsbk5hyj4c9jmamygakeqi.streamlit.app/)

---

## 📸 Application Screenshot

![App Demo](https://github.com/Sumanth-Siddareddy/Algerian-Forest-Fire-Prediction/blob/main/app_screenshot.png)

---

## 🛠️ Tech Stack

* **Python**
* **Data Analysis:** Pandas, NumPy
* **ML Model:** Scikit-learn (Ridge Regression, Lasso, Linear Regression)
* **Web App:** Streamlit
* **EDA:** Matplotlib, Seaborn 

---

## ⚙️ How to Run Locally

Follow these steps to set up and run the project on your own machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Sumanth-Siddareddy/Algerian-Forest-Fire-Prediction](https://github.com/Sumanth-Siddareddy/Algerian-Forest-Fire-Prediction)
    cd Algerian-Forest-Fire-Prediction
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Unix/Mac
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

5.  Open your browser and navigate to `http://localhost:8501`.

---

## 📊 Project Workflow

This project followed a standard data science workflow:

### 1. Data Cleaning
The raw dataset, which combined data from two regions, required several cleaning steps:
* Removed extra headers that were repeated in the middle of the file.
* Dropped rows with all `NaN` values.
* Created a new `Region` feature (Bejaia=0, Sidi-Bel Abbes=1).
* Corrected column data types (e.g., to `int` and `float`).
* Stripped extra spaces from column names.
* Saved the preprocessed data to a new CSV file.

### 2. Exploratory Data Analysis (EDA)
After cleaning, I analyzed the data to find insights:
* Dropped the original `day`, `month`, and `year` columns as they were not needed for the model.
* Converted the `Classes` column (not fire, fire) into numerical format (0, 1).
* Performed correlation analysis to understand relationships between features.
* Drop DC, BUI features to handle multi-colinearity.
* Analyzed monthly fire trends for each region.

### 3. Model Training & Selection
The goal was to build a regression model to predict the `FWI`.
* **Models Tested:** Ridge Regression, Lasso Regression, and standard Linear Regression.
* **Validation:** Cross-validation was used to ensure the models generalized well.
* **Result:** Both Ridge and Linear Regression performed well. **Ridge Regression** was selected as the final model for deployment due to its robustness (handles multicollinearity).

---

## 📈 Features

The model uses the following features to predict the FWI:

1.  **Temperature:** Noon temperature in Celsius (22-42 °C)
2.  **RH:** Relative Humidity in % (21-90%)
3.  **Ws:** Wind speed in km/h (6-29 km/h)
4.  **Rain:** Total daily rain in mm (0-16.8 mm)
5.  **FFMC:** Fine Fuel Moisture Code (28.6-92.5)
6.  **DMC:** Duff Moisture Code (1.1-65.9)
7.  **DC:** Drought Code (7-220.4)
8.  **ISI:** Initial Spread Index (0-18.5)
9.  **BUI:** Buildup Index (1.1-68)
10. **Classes:** Fire (1) or Not Fire (0)
11. **Region:** Bejaia (0) or Sidi-Bel Abbes (1)

**Target Variable:**
* **FWI:** Fire Weather Index (0-31.1)

---

## 📓 Dataset Details

### Algerian Forest Fires Dataset

* **Source:** [UCI Machine Learning Repository (or link to data source)]
* **Information:** The dataset includes 244 instances, with 122 instances from the Bejaia region and 122 from the Sidi Bel-abbes region.
* **Period:** June 2012 to September 2012.
* **Attributes:** 11 input attributes and 1 output class (later used as a feature).

---

## 🧑‍💻 Author

* **Venkata Sumanth Siddareddy**
* [GitHub](https://github.com/Sumanth-Siddareddy)
* [LinkedIn](https://www.linkedin.com/in/sumanth-siddareddy/)

---
## Thank you Note 
* Thank to Krish Naik (Tutor, Udemy) I learn this EDA, feature engineering from Udemy course.
---

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.
