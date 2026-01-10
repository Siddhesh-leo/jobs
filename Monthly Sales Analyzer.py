import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
dates = pd.date_range('2025-01-01', '2025-12-31')
df = pd.DataFrame({'Sales': np.random.randint(100, 1000, len(dates))}, index=dates)

monthly = df.resample('MS')['Sales'].sum()

print(f"--- Sales Summary ---\n{monthly}")
print(f"\nBest Month: {monthly.idxmax():} ({monthly.max()})")
print(f"Worst Month: {monthly.idxmin():} ({monthly.min()})")

ax = monthly.plot(figsize=(12, 6), marker='o', c='purple', title='Monthly Sales Trend (2025)')

plt.scatter([monthly.idxmax(), monthly.idxmin()], [monthly.max(), monthly.min()], c=['g', 'r'], s=150, zorder=5, label='Best/Worst')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
