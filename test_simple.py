#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("✅ All packages imported successfully!")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")
print(f"Matplotlib version: {plt.matplotlib.__version__}")
print(f"Seaborn version: {sns.__version__}")

# Create a simple test plot
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
sns.lineplot(data=df, x='x', y='y')
plt.title('Test Plot')
plt.savefig('test_plot.png')
print("✅ Test plot saved as 'test_plot.png'")
print("✅ Environment is working correctly!")
