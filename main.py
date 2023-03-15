import pandas as pd

from Validations.validations import *

# Execute unit-tests
execute_unit_tests()

# Create DataFrame of the LCIA tab of .xlsx file
source_path = "LCIA.xlsx"
# source_path = "Jesse_Cut-off Cumulative LCIA v3.9.1 (empty).xlsx" #175 seconds

bom = pd.read_csv("BOM.csv")
levels = bom["Level"].values
quantity = bom["Quantity"].values
row = bom.loc[3]

try:
    lcia = pd.read_excel(
        source_path,
        header=3,
        sheet_name='LCIA',
        keep_default_na=False
    )
except FileNotFoundError as e:
    raise ValueError(f"File not found.\n {e}")
