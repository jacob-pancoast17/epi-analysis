import pandas as pd

wastewater_cleaned = (
    # Read in the CSV
    pd.read_csv("CDC_Wastewater_Data_for_RSV_20260428.csv")

    # Filter by Vermont to lower # of rows
    .query("state_territory == 'vt'")
    )

wastewater_cleaned.to_csv('CDC_RSV_Wastewater_Data.csv', index = False)