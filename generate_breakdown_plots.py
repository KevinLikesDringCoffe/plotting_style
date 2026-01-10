import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 11

# Breakdown colors
breakdown_colors = [
    '#4472C4',  # Blue
    '#ED7D31',  # Orange
    '#A5A5A5',  # Gray
    '#FFC000',  # Yellow
    '#5B9BD5',  # Light Blue
    '#70AD47',  # Green
]

# Example 1: Single-column single breakdown bar
fig, ax = plt.subplots(figsize=(3.5, 2.8))

components = [35, 25, 20, 12, 8]
component_labels = ['Processing', 'Communication', 'Storage', 'Overhead', 'Other']
colors = breakdown_colors[:len(components)]

# Create stacked bar
bottom = 0
for i, (value, label, color) in enumerate(zip(components, component_labels, colors)):
    ax.bar(0, value, width=0.4, bottom=bottom, label=label,
           color=color, edgecolor='black', linewidth=1.2)
    bottom += value

ax.set_ylabel('Time Breakdown (%)')
ax.set_xticks([0])
ax.set_xticklabels(['System'])
ax.set_ylim([0, 100])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=True)

plt.tight_layout()
plt.savefig('example_breakdown_single.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated: example_breakdown_single.pdf")

# Example 2: Two-column breakdown comparison (Before vs After)
fig, ax = plt.subplots(figsize=(7.0, 4.5))

labels = ['Before', 'After']
component_a = [35, 28]  # Processing
component_b = [25, 30]  # Communication
component_c = [20, 22]  # Storage
component_d = [12, 13]  # Overhead
component_e = [8, 7]    # Other

components_data = [component_a, component_b, component_c, component_d, component_e]
component_labels = ['Processing', 'Communication', 'Storage', 'Overhead', 'Other']

width = 0.5
x = np.arange(len(labels))

# Stack bars for each component
for i, (data, label, color) in enumerate(zip(components_data, component_labels, breakdown_colors)):
    if i == 0:
        ax.bar(x, data, width, label=label, color=color, edgecolor='black', linewidth=1.2)
        bottom = np.array(data)
    else:
        ax.bar(x, data, width, bottom=bottom, label=label, color=color, edgecolor='black', linewidth=1.2)
        bottom += np.array(data)

ax.set_xlabel('Configuration')
ax.set_ylabel('Time Breakdown (%)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim([0, 100])
ax.legend(loc='best', frameon=True)

plt.tight_layout()
plt.savefig('example_breakdown_comparison.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated: example_breakdown_comparison.pdf")

# Example 3: Two-column breakdown with multiple scenarios
fig, ax = plt.subplots(figsize=(7.0, 4.5))

labels = ['Baseline', 'Optimized-v1', 'Optimized-v2', 'Final']
component_a = [40, 35, 30, 25]  # Computation
component_b = [30, 28, 30, 32]  # Memory Access
component_c = [15, 20, 22, 25]  # I/O
component_d = [10, 12, 13, 13]  # Network
component_e = [5, 5, 5, 5]      # Other

components_data = [component_a, component_b, component_c, component_d, component_e]
component_labels = ['Computation', 'Memory Access', 'I/O', 'Network', 'Other']

width = 0.6
x = np.arange(len(labels))

# Stack bars for each component
for i, (data, label, color) in enumerate(zip(components_data, component_labels, breakdown_colors)):
    if i == 0:
        ax.bar(x, data, width, label=label, color=color, edgecolor='black', linewidth=1.2)
        bottom = np.array(data)
    else:
        ax.bar(x, data, width, bottom=bottom, label=label, color=color, edgecolor='black', linewidth=1.2)
        bottom += np.array(data)

ax.set_xlabel('Optimization Stage')
ax.set_ylabel('Runtime Breakdown (%)')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=20, ha='right')
ax.set_ylim([0, 100])
ax.legend(loc='best', frameon=True)

plt.tight_layout()
plt.savefig('example_breakdown_multiple.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()

print("Generated: example_breakdown_multiple.pdf")

print("\nAll breakdown example plots generated successfully!")
