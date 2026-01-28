def calculate_risk(rainfall, groundwater):
    if rainfall < 400 and groundwater < 50:
        return "High Risk"
    elif rainfall < 700:
        return "Medium Risk"
    else:
        return "Low Risk"

rainfall = int(input("Enter rainfall (mm): "))
groundwater = int(input("Enter groundwater (%): "))

risk = calculate_risk(rainfall, groundwater)
print("Drought Risk Level:", risk)





