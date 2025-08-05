import pandas as pd

file_path = r'C:\Users\ASUS\OneDrive\Desktop\CSE Project\internship\Dataset.csv'
df = pd.read_csv(file_path)

online_counts = df['Has Online delivery'].value_counts()
total = len(df)
online_yes = online_counts.get('Yes', 0)
online_delivery_percent = (online_yes / total) * 100

print(f"Percentage of restaurants offering online delivery: {online_delivery_percent:.2f}%")

avg_rating_online = df[df['Has Online delivery'] == 'Yes']['Aggregate rating'].mean().round(2)
avg_rating_offline = df[df['Has Online delivery'] == 'No']['Aggregate rating'].mean().round(2)

print(f"\nAverage rating WITH online delivery: {avg_rating_online}⭐")
print(f"Average rating WITHOUT online delivery: {avg_rating_offline}⭐")
