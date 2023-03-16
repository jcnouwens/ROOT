import pandas as pd

from Validations.validations import *

# Execute unit-tests
execute_unit_tests()

bom = pd.read_csv("BOM.csv")

if zero_level_present(bom["Level"].tolist()):
    raise Exception("Zero level not excepted when uploading single-product BOM")

if not validate_levels(bom["Level"].tolist()):
    raise Exception("Level sequence in BOM invalid")

# Add Match and Error column to BOM DataFrame
bom = bom.assign(
    Match=[False for x in range(len(bom))],
    Error=[[] for y in range(len(bom))]
)

match_levels = match_level_indices(bom['Level'])

for index, row in bom.iterrows():
    if index in match_levels:       # Set Match to True according to match_level_indices() logic.
        bom.at[index, 'Match'] = True
    if not valid_quantity(row):
        bom.at[index, 'Match'] = False
        bom.at[index, 'Error'].append('Quantity invalid')
    if not valid_unit(row):
        bom.at[index, 'Match'] = False
        bom.at[index, 'Error'].append('Unit invalid')
    else:
        pass

match_bom = bom[bom['Match']]

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
