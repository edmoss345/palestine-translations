import pandas as pd
import os

# Path to the Excel file
file_path = "./translations/parent_text_crisis_palestine/excel files/Palestine strings for translation.xlsx"  

# Directory where the .po files should be saved
output_dir = "./translations/parent_text_crisis_palestine/ar"  

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Mapping of sheet names to output file names
sheet_to_filename = {
    "Latest Modules and Activities": "ar_modules_and_activities.po",
    "Latest Navigation": "ar_navigation.po",
    "Latest Onboarding": "ar_onboarding.po",
    "Latest Survey": "ar_survey.po"
}

# Process each sheet and write to .po file
for sheet_name, file_name in sheet_to_filename.items():
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Full output path
    output_path = os.path.join(output_dir, file_name)
    
    with open(output_path, "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            english = str(row.get("English", "")).strip()
            arabic = str(row.get("Arabic", "")).strip()

            if english and arabic:
                f.write("#. type=text\n")
                f.write("msgctxt \"text\"\n")
                f.write(f"msgid \"{english}\"\n")
                f.write(f"msgstr \"{arabic}\"\n\n")

print(f"PO files created successfully in: {os.path.abspath(output_dir)}")
