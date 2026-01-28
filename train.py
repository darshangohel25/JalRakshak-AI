import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# -----------------------------
# 1. Load dataset (Excel)
# -----------------------------
data = pd.read_excel("drought_data.csv.xlsx")

print("Columns:", data.columns)
print(data["risk"].value_counts())

# -----------------------------
# 2. Features and Target
# -----------------------------
X = data.drop("risk", axis=1)
y = data["risk"]

# -----------------------------
# 3. Train-Test Split
# (NO stratify because dataset is small)
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# -----------------------------
# 4. Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# 5. Save Model
# -----------------------------
os.makedirs("model", exist_ok=True)

with open("model/jalrakshak_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully")
