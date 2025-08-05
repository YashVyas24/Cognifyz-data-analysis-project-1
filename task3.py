import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\ASUS\OneDrive\Desktop\CSE Project\internship\Dataset.csv'
df = pd.read_csv(file_path)

price_counts = df['Price range'].value_counts().sort_index()


total = len(df)
price_percentages = (price_counts / total * 100).round(2)


print("Percentage of Restaurants by Price Range:")
for price, percent in price_percentages.items():
    print(f"Price Range {price}: {percent}%")


plt.figure(figsize=(8,5))
plt.bar(price_counts.index.astype(str), price_counts.values, color='red', edgecolor='black')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.title('Distribution of Price Ranges Among Restaurants')
plt.xticks(ticks=[1, 2, 3, 4], labels=['Low (1)', 'Medium (2)', 'High (3)', 'Luxury (4)'])
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
