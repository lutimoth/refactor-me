import pandas as pd

# Read in a data file
df = pd.read_csv('data/raw/shopping_behavior_updated.csv')

# calculate summary statistics on the Purchase Amount column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?

print("Summary statistics on Purchase Amount (USD)")
print(df['Purchase Amount (USD)'].describe())

# calculate summary statistics on the Age column
# TODO: Is there a way to encapsulate all this functionality
# TODO: in one function call?

print("Summary statistics on Age")
print(df['Age'].describe())

# summary statistics
# TODO: is there another function we can use to calculate metrics on groups?

print("Seasonal Summary Statistics on Purchase Amount (USD)")
print(df.groupby('Season')['Purchase Amount (USD)'].describe())

# keep all columns except for "Customer ID", & "Discount Applied"
# TODO: is there a more efficient way to exclude columns in your dataset?
df = df.drop(["Customer ID","Discount Applied"], axis=1)

# figure out most popular payment method in NY
# TODO: is there anyway we could modularize this behavior to apply to all
# TODO: possible states? (OR possibly use a pandas function that does this
# TODO: for us already?)
most_frequent_method = {}

for state in df['Location'].unique():
    most_frequent_method[state] = df[df['Location'] == state]['Payment Method'].value_counts().index[0]

def find_pop_payment(state):
    payment_methods = df['Payment Method'].unique()
    us_state = df[df.Location == state]

    most_frequent_method = {}

    for method in payment_methods:
        most_frequent_method[method] = len(us_state[us_state['Payment Method'] == method])

    print(most_frequent_method)

find_pop_payment("New York")


# print(most_frequent_method['New York'])

# Write this updated data out to csv file
# df.to_csv('data/processed/cleaned_data.csv', index=False)
