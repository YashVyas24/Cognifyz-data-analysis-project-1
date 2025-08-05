import pandas as pd

file_path = r'C:\Users\ASUS\OneDrive\Desktop\CSE Project\internship\Dataset.csv'
df = pd.read_csv(file_path)

city_counts = df['City'].value_counts()
top_city = city_counts.idxmax()
top_city_counts = city_counts.max()

print(f"City with the highest number of restaurants: {top_city} ({top_city_counts} restaurants)")

city_avg_ratings = df.groupby('City')['Aggregate rating'].mean().round(2)
print("\nAverage rating per city:")
print(city_avg_ratings.sort_values(ascending=False))

highest_avg_city = city_avg_ratings.idxmax()
highest_avg_rating = city_avg_ratings.max()

print(f"\nCity with the highest average rating: {highest_avg_city} ({highest_avg_rating}⭐)")


