import pandas as pd

# ── EXTRACT ────────────────────────────
df = pd.read_csv('Sample - Superstore.csv', encoding='latin-1')

# ── TRANSFORM ──────────────────────────

# 1. Fix date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], format='mixed', dayfirst=False)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='mixed', dayfirst=False)

# 2. Create new columns
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.strftime('%b')
df['Ship Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# 3. Flag negative profits
df['Is Loss'] = df['Profit'] < 0

# 4. Verify everything
print("Date types after fix:")
print(df[['Order Date', 'Ship Date']].dtypes)

print("\nShipping days sample:")
print(df['Ship Days'].describe())

print("\nLoss transactions:")
print(df['Is Loss'].value_counts())

print("\nYears in dataset:")
print(df['Order Year'].value_counts().sort_index())