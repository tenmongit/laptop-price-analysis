import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

laptops = pd.read_csv('laptop_prices.csv')

print(laptops.head())

# Устанавливаем стиль
sns.set_style("whitegrid")

# Фигуры для графиков
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# RAM vs Price
sns.boxplot(x="RAM (GB)", y="Price ($)", data=laptops, ax=axes[0], palette="coolwarm")
axes[0].set_title("Цена в зависимости от объема RAM")
axes[0].set_xlabel("RAM (GB)")
axes[0].set_ylabel("Цена ($)")

# Storage Size vs Price
#sns.scatterplot(x="Storage Size", y="Price ($)", data=laptops, ax=axes[1], hue="Storage Type", palette="viridis")
#axes[1].set_title("Цена в зависимости от объема накопителя")
#axes[1].set_xlabel("Объем накопителя (GB)")
#axes[1].set_ylabel("Цена ($)")

# GPU vs Price
sns.boxplot(x="GPU", y="Price ($)", data=laptops, ax=axes[2], palette="magma")
axes[2].set_title("Цена в зависимости от GPU")
axes[2].set_xlabel("GPU")
axes[2].set_ylabel("Цена ($)")
axes[2].tick_params(axis='x', rotation=45)

# Отобразить графики
plt.tight_layout()
plt.show()

