import pandas as pd
import os
from datetime import datetime

# Path to the Excel file
file_path = "./translations/parent_text_crisis_palestine/excel files/Palestine strings for translation.xlsx"

# Directory where the .po files should be saved
output_dir = "./translations/parent_text_crisis_palestine/ar"
os.makedirs(output_dir, exist_ok=True)

# Mapping of sheet names to output file names
sheet_to_filename = {
    "Latest Modules and Activities": "ar_modules_and_activities.po",
    "Latest Navigation": "ar_navigation.po",
    "Latest Onboarding": "ar_onboarding.po",
    "Latest Survey": "ar_survey.po"
}

# Template for PO header
def generate_po_header():
    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M+0000')
    return f"""msgid ""
msgstr ""
"Project-Id-Version: Palestine Translation\\n"
"Report-Msgid-Bugs-To: \\n"
"POT-Creation-Date: {now}\\n"
"PO-Revision-Date: {now}\\n"
"Last-Translator: \\n"
"Language-Team: Arabic\\n"
"Language: ar\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=2; plural=(n != 1);\\n"

"""

# Escape quotes
def escape_quotes(text):
    return text.replace('"', '\\"')

# Main processing loop
for sheet_name, file_name in sheet_to_filename.items():
    df = pd.read_excel(file_path, sheet_name=sheet_name, keep_default_na=False)

    # Filter rows that have non-empty English, Arabic, and Type values
    valid_rows = df[
        (df["English"].astype(str).str.strip() != "") &
        (df["Arabic"].astype(str).str.strip() != "") &
        (df["Type"].astype(str).str.strip() != "")
    ]


    # If there are no rows with Arabic translations, skip creating the file
    if valid_rows.empty:
        print(f"Skipped {sheet_name} - no Arabic translations found.")
        continue

    output_path = os.path.join(output_dir, file_name)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(generate_po_header())

        for i, row in valid_rows.iterrows():
            english = str(row["English"]).strip()
            arabic = str(row["Arabic"]).strip()
            type = str(row["Type"]).strip()

            f.write(f"#. type={escape_quotes(type)}\n")
            f.write(f"msgctxt \"{escape_quotes(type)}\"\n")
            f.write(f"msgid \"{escape_quotes(english)}\"\n")
            f.write(f"msgstr \"{escape_quotes(arabic)}\"\n\n")

print(f"PO files created successfully in: {os.path.abspath(output_dir)}")

