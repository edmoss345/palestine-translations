# palestine-translations
This repo is used to store translations as required by the ParentText Palestine chatbot. It also contains two functions to convert back and forth between PO and excel files. The excel files are subsequently uploaded/ downloaded to google sheets where they are worked on by translators

### Setup

1. Clone or fork the repo to a local folder
1. Install Python >= 3.8
1. Create a Python virtual environment `python -m venv .venv`
1. Activate the environment:
    - Linux: `source .venv/bin/activate`
    - Windows: `.venv/Scripts/activate`
1. Upgrade pip `pip install --upgrade pip`
1. Install project Python dependencies `pip install -r requirements.txt`

## Run

```
python po_to_excel

python excel_to_po
```

