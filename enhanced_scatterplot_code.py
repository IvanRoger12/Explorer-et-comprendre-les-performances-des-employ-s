import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Simulated data for performance scores and hours worked (for demonstration purposes)
np.random.seed(42)
hours_worked = np.random.normal(40, 5, 200).clip(25, 60)
performance_scores = np.random.choice([1, 2, 3, 4, 5], size=200, p=[0.05, 0.1, 0.5, 0.3, 0.05])

# Set up the plot
plt.figure(figsize=(10, 6))
sns.set_theme(style="whitegrid")

# Scatterplot with outliers highlighted
scatter = sns.scatterplot(x=hours_worked, y=performance_scores, hue=performance_scores, 
                          palette='cool', s=80, edgecolor='black', alpha=0.7)

# Adding a trendline using regression
sns.regplot(x=hours_worked, y=performance_scores, scatter=False, color='darkred', 
            line_kws={"linewidth": 2, "label": "Droite de tendance"})

# Title and labels
plt.title("Corrélation entre les heures travaillées et la performance", fontsize=16, fontweight='bold', color="#2E8B57")
plt.xlabel("Heures travaillées par semaine", fontsize=12)
plt.ylabel("Score de performance", fontsize=12)

# Annotations for outliers
outlier_indices = np.where((hours_worked > 55) | (hours_worked < 30))[0]  # Simulating outlier logic
for i in outlier_indices:
    plt.text(hours_worked[i], performance_scores[i] + 0.2, "Outlier", fontsize=8, color='red', ha='center')

# Legend placement
plt.legend(title="Score de performance", loc='upper left', bbox_to_anchor=(1.05, 1))

# Save the final scatterplot with enhancements
plt.savefig("final_scatterplot_with_trendline.png", bbox_inches='tight', dpi=300)
plt.show()
