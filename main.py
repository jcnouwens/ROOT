import pandas as pd

from Validations.validations import *

# Execute unit-tests
execute_unit_tests()

bom = pd.read_csv("BOM.csv")

if zero_level_present(bom["Level"].tolist()):  # TODO: present or missing?
    raise Exception("Zero level missing")

if not validate_levels(bom["Level"].tolist()):
    raise Exception("Level sequence in BOM invalid")

bom = bom.assign(Match=[False for i in range(len(bom))])
for index, row in bom.iterrows():
    # match_bom = pd.DataFrame(columns=bom.columns)
    if valid_quantity(row):
        bom.at[index, 'Match'] = True

# # Create DataFrame of the LCIA tab of .xlsx file
# source_path = "LCIA.xlsx"
# try:
#     lcia = pd.read_excel(
#         source_path,
#         header=3,
#         sheet_name='LCIA',
#         keep_default_na=False
#     )
# except FileNotFoundError as e:
#     raise ValueError(f"File not found.\n {e}")
