import polib
import pandas as pd

def po_to_excel(po_file_path, excel_file_path):
    # Load the PO file
    po = polib.pofile(po_file_path)
    
    # Extract English (msgid) and Arabic (msgstr) translations
    data = [(entry.msgid, entry.msgstr) for entry in po if entry.msgid]
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=['English', 'Arabic'])
    
    # Save to Excel (overwrite if exists)
    with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, index=False)
    
    print(f"Excel file saved: {excel_file_path}")

# Processing files:
base_path = "./translations/parent_text_crisis_palestine/"
file_list = ["modules and activities","navigation","onboarding", "survey"]
for file in file_list:
    po_to_excel(base_path+"en/"+file+".po",base_path+"excel files/"+file+".xlsx")
