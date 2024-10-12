import pandas as pd

# Load the data from your file path
file_path = 'C:/Users/chris/OneDrive/Documents/Uni/Year 4/Sem2/FIT3179/homework w10/FIT3179/docs/new_fhome_buyer_loan.csv'
df = pd.read_csv(file_path)

# Mapping months to their corresponding numbers
month_map = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}

# Apply mapping and create a new column 'Month_Number'
df['Month_Number'] = df['Month'].map(month_map)

# Create the new 'Date' column in YYYY-MM format
df['Date'] = df['Year'].astype(str) + '-' + df['Month_Number']

# Drop the now redundant 'Month_Number' column
df = df[['Date', 'State', 'Loan_Commitments', 'Year', 'Month']]

# Save the modified DataFrame to a new CSV file
df.to_csv('updated_loan_commitments_yyyy_mm.csv', index=False)

print("New dataset with 'Date' column in YYYY-MM format created and saved as 'updated_loan_commitments_yyyy_mm.csv'.")
