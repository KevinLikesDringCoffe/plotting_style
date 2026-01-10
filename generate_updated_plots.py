import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 11

np.random.seed(42)

# Example 1: Two-column scatter plot
fig, ax = plt.subplots(figsize=(7.0, 4.5))

x1 = np.random.randn(50) * 2 + 5
y1 = np.random.randn(50) * 2 + 5
x2 = np.random.randn(50) * 2 + 10
y2 = np.random.randn(50) * 2 + 8

ax.scatter(x1, y1, s=50, alpha=0.7, edgecolors='black', linewidths=0.5, label='Dataset A', c='#D62728')
ax.scatter(x2, y2, s=50, alpha=0.7, edgecolors='black', linewidths=0.5, label='Dataset B', c='#1F77B4')

ax.set_xlabel('Feature X')
ax.set_ylabel('Feature Y')
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(loc='best', frameon=True)

plt.tight_layout()
plt.savefig('example_scatter_two_column.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated: example_scatter_two_column.pdf")

# Example 2: Single-column two-series bar plot
fig, ax = plt.subplots(figsize=(3.5, 2.8))

labels = ['A', 'B', 'C', 'D']
series1 = [23, 35, 28, 42]
series2 = [28, 30, 35, 38]

width = 0.35
x = np.arange(len(labels))

ax.bar(x - width/2, series1, width, label='Method 1',
       color='#D62728', edgecolor='black', linewidth=1.2)
ax.bar(x + width/2, series2, width, label='Method 2',
       color='#1F77B4', edgecolor='black', linewidth=1.2)

ax.set_xlabel('Test Cases')
ax.set_ylabel('Accuracy (%)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='best', frameon=True)

plt.tight_layout()
plt.savefig('example_bar_two_series_single.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated: example_bar_two_series_single.pdf")

# Example 3: Two-column multi-series bar plot (white-gray with hatch patterns)
fig, ax = plt.subplots(figsize=(7.0, 4.5))

labels = ['Algorithm A', 'Algorithm B', 'Algorithm C', 'Algorithm D']
series1 = [85, 92, 88, 95]
series2 = [80, 88, 90, 92]
series3 = [78, 85, 86, 90]
series4 = [82, 87, 84, 88]

series_list = [series1, series2, series3, series4]

# Define color and hatch combinations
series_styles = [
    {'color': '#FFFFFF', 'hatch': '', 'label': 'Metric 1'},      # White, no fill
    {'color': '#FFFFFF', 'hatch': '///', 'label': 'Metric 2'},   # White, slash fill
    {'color': '#808080', 'hatch': '', 'label': 'Metric 3'},      # Gray, no fill
    {'color': '#808080', 'hatch': 'xxx', 'label': 'Metric 4'},   # Gray, x fill
]

width = 0.2
x = np.arange(len(labels))

for i, (data, style) in enumerate(zip(series_list, series_styles)):
    offset = width * (i - len(series_list)/2 + 0.5)
    ax.bar(x + offset, data, width, label=style['label'],
           color=style['color'], edgecolor='black', linewidth=1.2, hatch=style['hatch'])

ax.set_xlabel('Methods')
ax.set_ylabel('Performance Score')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, ha='right')
ax.legend(loc='best', frameon=True, ncol=2)

plt.tight_layout()
plt.savefig('example_bar_multi_series_two_column.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated: example_bar_multi_series_two_column.pdf")

# Example 4: Single-column scatter plot
fig, ax = plt.subplots(figsize=(3.5, 2.8))

categories = ['Baseline', 'Improved', 'Optimized']
x_pos = np.arange(len(categories))
y_values = np.random.randn(15, 3) * 5 + np.array([50, 65, 75])

for i in range(len(categories)):
    ax.scatter([x_pos[i]] * 15, y_values[:, i], s=50, alpha=0.7,
               edgecolors='black', linewidths=0.5)

ax.set_xlabel('Configuration')
ax.set_ylabel('Latency (ms)')
ax.set_xticks(x_pos)
ax.set_xticklabels(categories)
ax.grid(True, alpha=0.3, linestyle='--', axis='y')

plt.tight_layout()
plt.savefig('example_scatter_single_column.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated: example_scatter_single_column.pdf")

# Example 5: Multi-series bar plot with 6 series (demonstrating more combinations)
fig, ax = plt.subplots(figsize=(7.0, 4.5))

labels = ['Dataset 1', 'Dataset 2', 'Dataset 3']
series1 = [72, 85, 78]
series2 = [68, 82, 75]
series3 = [75, 88, 80]
series4 = [70, 80, 77]
series5 = [65, 78, 72]
series6 = [62, 75, 70]

series_list = [series1, series2, series3, series4, series5, series6]

# Define color and hatch combinations for 6 series
series_styles = [
    {'color': '#FFFFFF', 'hatch': '', 'label': 'Method A'},      # White, no fill
    {'color': '#FFFFFF', 'hatch': '///', 'label': 'Method B'},   # White, slash
    {'color': '#FFFFFF', 'hatch': 'xxx', 'label': 'Method C'},   # White, x
    {'color': '#808080', 'hatch': '', 'label': 'Method D'},      # Gray, no fill
    {'color': '#808080', 'hatch': '///', 'label': 'Method E'},   # Gray, slash
    {'color': '#808080', 'hatch': '...', 'label': 'Method F'},   # Gray, dots
]

width = 0.12
x = np.arange(len(labels))

for i, (data, style) in enumerate(zip(series_list, series_styles)):
    offset = width * (i - len(series_list)/2 + 0.5)
    ax.bar(x + offset, data, width, label=style['label'],
           color=style['color'], edgecolor='black', linewidth=1.2, hatch=style['hatch'])

ax.set_xlabel('Datasets')
ax.set_ylabel('Accuracy (%)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='best', frameon=True, ncol=3)

plt.tight_layout()
plt.savefig('example_bar_6_series_two_column.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated: example_bar_6_series_two_column.pdf")

print("\nAll example plots generated successfully!")
