import pandas as pd
import time

source_path = "LCIA.xlsx"
# source_path = "Jesse_Cut-off Cumulative LCIA v3.9.1 (empty).xlsx" #175 seconds


start = time.perf_counter()

# Create DataFrame of the LCIA tab of .xlsx file
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

end = time.perf_counter()
print(end - start)

