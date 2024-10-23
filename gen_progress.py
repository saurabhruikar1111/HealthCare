import pandas as pd
import random
from datetime import datetime, timedelta

# Parameters
num_patients = 50
num_days = 60  # Total records per patient
start_date = datetime(2024, 1, 1)

# Generate sample data
progress_data = []

# Generate daily progress for each patient over a range of num_days
for patient_id in range(1, num_patients + 1):
    for day in range(num_days):
        date = (start_date + timedelta(days=day)).strftime('%Y-%m-%d')
        
        # Randomly decide to include or exclude each parameter
        heart_rate = random.randint(60, 100) if random.random() > 0.1 else None  # 10% chance of missing
        blood_sugar = random.randint(70, 180) if random.random() > 0.1 else None  # 10% chance of missing
        blood_pressure = random.randint(70, 120) if random.random() > 0.1 else None  # 10% chance of missing
        
        # Medical compliance with 80% rate
        medical_compliance = 'Yes' if random.random() < 0.8 else 'No'

        progress_data.append({
            'ProgressID': len(progress_data) + 1,
            'PatientID': patient_id,
            'Date': date,
            'HeartRate': heart_rate,
            'BloodSugar': blood_sugar,
            'BloodPressure': blood_pressure,
            'MedicalCompliance': medical_compliance
        })

# Create a DataFrame
progress_df = pd.DataFrame(progress_data)

# Save to CSV
progress_df.to_csv('daily_progress.csv', index=False)

print("Daily Progress CSV file created with records for each patient, including medical compliance.")
