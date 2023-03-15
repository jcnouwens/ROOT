import pandas as pd

from Validations import validations

data = {"Level": [1, 2, 2, 3],
        "Name": ["Seat", "PP (polypropyleen)", "Screws", "Stainless steel"],
        "Quantity": [1, 2.4, 4, 0.1],
        "Unit": ["Items", "kg", "Items", "kg"]}
bom = pd.DataFrame(data=data)
levels = bom["Level"].values
quantity = bom["Quantity"].values
row = bom.loc[3]

# Create DataFrame of the LCIA tab of .xlsx file
source_path = "LCIA1.xlsx"
# source_path = "Jesse_Cut-off Cumulative LCIA v3.9.1 (empty).xlsx" #175 seconds
try:
    lcia = pd.read_excel(
        source_path,
        header=3,
        sheet_name='LCIA',
        # dtype="string",
        keep_default_na=False
    )
except FileNotFoundError as e:
    raise ValueError(f"File not found.\n {e}")
