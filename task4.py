import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("traffic_accidents_synthetic.csv")

# Display dataset information
print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# ---------------- 1. ACCIDENTS BY WEATHER ----------------

weather_counts = df["Weather_Condition"].value_counts()

plt.figure(figsize=(10, 6))
weather_counts.plot(kind="bar")
plt.title("Accidents by Weather Condition")
plt.xlabel("Weather Condition")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_accidents.png")
plt.close()

# ---------------- 2. ACCIDENTS BY ROAD CONDITION ----------------

road_counts = df["Road_Condition"].value_counts()

plt.figure(figsize=(10, 6))
road_counts.plot(kind="bar")
plt.title("Accidents by Road Condition")
plt.xlabel("Road Condition")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("road_accidents.png")
plt.close()

# ---------------- 3. ACCIDENTS BY TIME OF DAY ----------------

time_counts = df["Time_of_Day"].value_counts()

plt.figure(figsize=(10, 6))
time_counts.plot(kind="bar")
plt.title("Accidents by Time of Day")
plt.xlabel("Time of Day")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("time_accidents.png")
plt.close()

# ---------------- 4. ACCIDENT HOTSPOTS BY CITY ----------------

city_counts = df["City"].value_counts()

plt.figure(figsize=(10, 6))
city_counts.plot(kind="bar")
plt.title("Accident Hotspots by City")
plt.xlabel("City")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("city_accidents.png")
plt.close()

# ---------------- 5. ACCIDENTS BY SEVERITY ----------------

severity_counts = df["Severity"].value_counts().sort_index()

plt.figure(figsize=(10, 6))
severity_counts.plot(kind="bar")
plt.title("Accidents by Severity")
plt.xlabel("Severity Level")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("severity_accidents.png")
plt.close()

# ---------------- SUMMARY ----------------

print("\nTop Weather Condition:")
print(weather_counts.idxmax())

print("\nMost Common Road Condition:")
print(road_counts.idxmax())

print("\nMost Common Time of Day:")
print(time_counts.idxmax())

print("\nCity with Most Accidents:")
print(city_counts.idxmax())

print("\nTask 4 completed successfully!")
print("Five visualizations created.")