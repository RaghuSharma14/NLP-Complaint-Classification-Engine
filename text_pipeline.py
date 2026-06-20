import os
import re
import pandas as pd
import glob

# folder paths
input_folder = "raw_logs"
output_filename = "structured_risk_report.csv"

print(f"Scanning folder: '{input_folder}' for raw CSV files...")

if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    print(f"Created '{input_folder}' directory. Please add the CSV files inside it and run again.")
    exit()

# BATCH PROCESSING: Find all CSVs in the folder and merge them
all_files = glob.glob(os.path.join(input_folder, "*.csv"))

if not all_files:
    print(f"No CSV files found in the '{input_folder}' folder! Please add data and try again.")
    exit()

df_list = []
for file in all_files:
    df = pd.read_csv(file)
    df_list.append(df)

# Combine all found datasets into one massive DataFrame
final_df = pd.concat(df_list, ignore_index=True)
print(f"Successfully merged {len(all_files)} files. Total rows to analyze: {len(final_df)}")

# Define Risk Keywords (Regex Dictionary)
# Using generic, industry-standard risk buckets
RISK_KEYWORDS = {
    "Deceptive Fees": r"hidden charge|scam|overcharged|hidden fee",
    "Security Breach": r"stole my identity|unauthorized|stolen card|identity theft",
    "Customer Service": r"rude|wait time|on hold|ignored"
}

# Text Analysis Logic
def analyze_text(text):
    # Standardize the text: lowercase and remove trailing whitespaces
    text_clean = str(text).lower().strip()
    detected_risks = []
    
    # Scan the text against our Regex dictionary
    for category, pattern in RISK_KEYWORDS.items():
        if re.search(pattern, text_clean):
            detected_risks.append(category)
            
    # Return the joined risks, or a default safe flag
    if detected_risks:
        return ", ".join(detected_risks)
    else:
        return "Normal Inquiry"

# Apply logic and create flags
print("Running NLP text analytics and applying risk flags...")
final_df["Risk_Category"] = final_df["Complaint_Text"].apply(analyze_text)

final_df["Urgency_Flag"] = final_df["Risk_Category"].apply(
    lambda x: "LOW" if x == "Normal Inquiry" else "HIGH"
)

# Exporting the final structured dataset
final_df.to_csv(output_filename, index=False)
print(f"Pipeline Complete! Master dataset saved as '{output_filename}'")