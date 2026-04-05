import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from fairlearn.metrics import MetricFrame, selection_rate, demographic_parity_difference

# === Load Dataset ===
df = pd.read_csv(r"C:\Users\tejas\Downloads\HR.csv")

st.title("Bias-Free Recruitment AI Dashboard")

st.subheader("Dataset Preview")
st.write(df.head())

# === Define Target & Sensitive Features ===
target_col = "left"
sensitive_salary = df["salary"]
sensitive_sales = df["sales"]

X = df.drop(columns=[target_col])
y = df[target_col]

# Encode categorical variables
for col in X.select_dtypes(include=['object']).columns:
    X[col] = LabelEncoder().fit_transform(X[col].astype(str))

# Train-test split
X_train, X_test, y_train, y_test, sens_salary_train, sens_salary_test, sens_sales_train, sens_sales_test = train_test_split(
    X, y, sensitive_salary, sensitive_sales, test_size=0.3, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

st.subheader("Model Performance")
st.write("Accuracy:", accuracy_score(y_test, y_pred))
st.write("F1 Score:", f1_score(y_test, y_pred))

# Bias Analysis Salary
mf_salary = MetricFrame(
    metrics={"accuracy": accuracy_score, "selection_rate": selection_rate},
    y_true=y_test, y_pred=y_pred, sensitive_features=sens_salary_test
)
st.subheader("Bias Analysis by Salary")
st.write(mf_salary.by_group)

# Bias Analysis Department
mf_sales = MetricFrame(
    metrics={"accuracy": accuracy_score, "selection_rate": selection_rate},
    y_true=y_test, y_pred=y_pred, sensitive_features=sens_sales_test
)
st.subheader("Bias Analysis by Department (Sales)")
st.write(mf_sales.by_group)

# === Dashboard Visuals ===
st.subheader("Confusion Matrix")
fig, ax = plt.subplots()
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues", ax=ax)
st.pyplot(fig)

st.subheader("Bias Metrics by Salary")
fig, ax = plt.subplots()
mf_salary.by_group.plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("Bias Metrics by Department")
fig, ax = plt.subplots()
mf_sales.by_group.plot(kind="bar", ax=ax)
st.pyplot(fig)
