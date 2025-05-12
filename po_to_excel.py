import polib
import pandas as pd
import re

def po_to_excel(po_file_path, excel_file_path):
    # Load the PO file
    po = polib.pofile(po_file_path)
    
    # Extract English (msgid), Arabic (msgstr), and type
    data = []
    for entry in po:
        if entry.msgid:
            # Extract type from comment like "#. type=text"
            type_match = re.search(r'type=([^\s]+)', entry.comment or '')
            entry_type = type_match.group(1) if type_match else ''
            data.append((entry.msgid, entry.msgstr, entry_type))
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=['English', 'Arabic', 'Type'])
    
    # Save to Excel (overwrite if exists)
    with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, index=False)
    
    print(f"Excel file saved: {excel_file_path}")

# Processing files:
base_path = "./translations/parent_text_crisis_palestine/"
file_list = ["modules and activities", "navigation", "onboarding", "survey"]
for file in file_list:
    po_to_excel(base_path + "en/" + file + ".po", base_path + "excel files/" + file + ".xlsx")
