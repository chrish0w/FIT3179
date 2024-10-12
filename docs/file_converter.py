import pandas as pd

# Load the data from your file path
file_path = 'C:/Users/chris/OneDrive/Documents/Uni/Year 4/Sem2/FIT3179/homework w10/FIT3179/docs/aggregated_by_year.csv'
df = pd.read_csv(file_path)

# Group by 'Year' and aggregate the loan commitments
df_grouped = df.groupby('Year').agg({'Loan_Commitments': 'sum'}).reset_index()

# Save the grouped data to a new CSV file
output_file_path = 'C:/Users/chris/OneDrive/Documents/Uni/Year 4/Sem2/FIT3179/homework w10/FIT3179/docs/aggregated_by_year_grouped.csv'
df_grouped.to_csv(output_file_path, index=False)

# Print the grouped DataFrame to verify
print(df_grouped)
