import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
laptops = pd.read_csv('laptop_prices.csv')

# Split the 'Storage' column into 'Storage Size' and 'Storage Type'
laptops[['Storage Size', 'Storage Type']] = laptops['Storage'].str.split(' ', expand=True)
laptops.drop('Storage', axis=1, inplace=True)

# Reorder columns
new_order = ['Brand', 'Processor', 'RAM (GB)', 'Storage Type', 'Storage Size', 'GPU', 
             'Screen Size (inch)', 'Resolution', 'Battery Life (hours)', 'Weight (kg)', 
             'Operating System', 'Price ($)']
laptops = laptops[new_order]

def convert_storage_size(value):
    value = value.upper().replace(' ', '')
    if 'TB' in value:
        return float(value.replace('TB', '')) * 1024  # Convert TB to GB
    elif 'GB' in value:
        return float(value.replace('GB', ''))
    return None

laptops['Storage Size'] = laptops['Storage Size'].apply(convert_storage_size)

# Set Seaborn style
sns.set_style('whitegrid')

# Quick look at the data
print(laptops.head())

# Create a grid of subplots for various visualizations
fig, axes = plt.subplots(2, 3, figsize=(20,8))

# Price vs RAM
sns.boxplot(x='RAM (GB)', y='Price ($)', data=laptops, ax=axes[1][0], palette='coolwarm')
axes[1][0].set_title('Price depending on the amount of RAM')
axes[1][0].set_xlabel('RAM (GB)')
axes[1][0].set_ylabel('Price ($)')

# Price vs Storage Size (with hue = Storage Type)
sns.boxplot(x='Storage Size', y='Price ($)', data=laptops, ax=axes[1][1], hue='Storage Type', palette='viridis')
axes[1][1].set_title('Price depending on the storage capacity')
axes[1][1].set_xlabel('Storage Size (GB)')
axes[1][1].set_ylabel('Price ($)')

# Price vs GPU
sns.boxplot(x='GPU', y='Price ($)', data=laptops, ax=axes[1][2], palette='magma')
axes[1][2].set_title('Price depending on the GPU')
axes[1][2].set_xlabel('GPU')
axes[1][2].set_ylabel('Price ($)')
axes[1][2].tick_params(axis='x', rotation=45)

# Price distribution histogram
sns.histplot(x='Price ($)', data=laptops, ax=axes[0][0])
axes[0][0].set_title('Price distribution of laptops')

# Price vs Brand
sns.boxplot(x='Brand', y='Price ($)', data=laptops, ax=axes[0][1], palette='Spectral')
axes[0][1].set_title('Price depending on the Brand')
axes[0][1].set_xlabel('Brand')
axes[0][1].set_ylabel('Price ($)')
axes[0][1].tick_params(axis='x', rotation=45)

# Price vs Processor
sns.boxplot(x='Processor', y='Price ($)', data=laptops, ax=axes[0][2], palette='cividis')
axes[0][2].set_title('Price depending on the CPU')
axes[0][2].set_xlabel('CPU')
axes[0][2].set_ylabel('Price ($)')
axes[0][2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('visualizations/combined_plots.png', dpi = 300)
plt.show()
plt.clf()

brand_avg_price = laptops.groupby('Brand')['Price ($)'].mean().sort_values(ascending=False)

plt.figure(figsize=(10,5))
sns.barplot(x=brand_avg_price.index, y=brand_avg_price.values, palette='coolwarm')
plt.title('Average price depending on brand')
plt.xticks(rotation=45)
plt.ylabel('Average Price ($)')
plt.savefig('visualizations/average_price_brand.png', dpi = 300)
plt.show()
plt.clf()

laptops['Price Category'] = pd.cut(laptops['Price ($)'],
                                  bins=[0, 800, 1500, 3000, laptops['Price ($)'].max()],
                                  labels=['Low-End', 'Mid-End', 'High-End', 'Luxury'])

price_segments = laptops['Price Category'].value_counts()

plt.figure(figsize=(8,5))
sns.barplot(x=price_segments.index, y=price_segments.values, palette='viridis')
plt.title('Distribution of laptops by price segments')
plt.ylabel('Number of laptops')
plt.savefig('visualizations/price_segments.png', dpi = 300)
plt.show()
plt.clf()

