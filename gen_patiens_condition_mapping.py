import pandas as pd
import random

# Sample data for patient-condition mapping
mapping_data = []

# Map each patient to a random number of conditions (1 to 3)
for patient_id in range(1, 51):
    condition_count = random.randint(1, 3)  # Randomly assign 1 to 3 conditions
    assigned_conditions = random.sample(range(1, 6), condition_count)  # Choose random conditions
    for condition_id in assigned_conditions:
        mapping_data.append({'PatientID': patient_id, 'ConditionID': condition_id})

# Create a DataFrame
mapping_df = pd.DataFrame(mapping_data)

# Save to CSV
mapping_df.to_csv('patient_condition_mapping.csv', index=False)

print("Patient-Condition Mapping CSV file created with mapping data.")
