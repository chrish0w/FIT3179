import pandas as pd

# Load the data
file_path = 'C:/Users/chris/OneDrive/Documents/Uni/Year 4/Sem2/FIT3179/homework w10/FIT3179/docs/fhome_buyer_loan.csv'
df = pd.read_csv(file_path)

# Split the 'Month' column into 'Month' and 'Year'
df['Year'] = df['Month'].apply(lambda x: '20' + x[-2:] if int(x[-2:]) < 25 else '19' + x[-2:])
df['Month'] = df['Month'].apply(lambda x: x[:-3])

# Save the modified DataFrame to a new CSV file
df.to_csv("new_fhome_buyer_loan.csv", index=False)

print("Conversion complete. New CSV saved as 'new_fhome_buyer_loan.csv'.")
