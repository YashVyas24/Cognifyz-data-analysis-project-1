import pandas as pd

file_path = 'C:\\Users\\ASUS\\OneDrive\\Desktop\\CSE Project\\internship\\Dataset.csv'
df = pd.read_csv(file_path)

df_cuisines = df['Cuisines'].dropna().str.split(',')

all_cuisines = df_cuisines.explode().str.strip()

cuisine_counts = all_cuisines.value_counts()

top_3_cuisines = cuisine_counts.head(3)

total_restaurants = len(df)
top_3_percentages = (top_3_cuisines / total_restaurants)*100

print("Top 3 Most Common Cuisines:")
print(top_3_cuisines)

print("\nPercentage of Restaurants Serving Top Cuisines:")
print(top_3_percentages.round(2))