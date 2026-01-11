# Matplotlib Plotting Style Guide

## Overview
This document defines the standard plotting style for scientific data visualization using Python's matplotlib library, optimized for IEEE publication format.

## Figure Dimensions

### Two-column (full width)
```python
fig_width_full = 7.0  # inches
fig_height_full = 4.5  # inches
figsize_full = (7.0, 4.5)
```

### Single-column
```python
fig_width_single = 3.5  # inches
fig_height_single = 2.8  # inches
figsize_single = (3.5, 2.8)
```

## Export Settings
- **Format**: PDF
- **DPI**: 300 (for high quality)
- **Bbox**: 'tight'
- **No title** on figures

## Font Hierarchy

### Font Sizes
```python
FONT_SIZE_AXIS_LABEL = 14   # Largest - for xlabel and ylabel
FONT_SIZE_TICK = 11          # Medium - for tick labels
FONT_SIZE_LEGEND = 11        # Medium - for legend text
```

### Font Configuration
```python
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.labelsize'] = FONT_SIZE_AXIS_LABEL
plt.rcParams['xtick.labelsize'] = FONT_SIZE_TICK
plt.rcParams['ytick.labelsize'] = FONT_SIZE_TICK
plt.rcParams['legend.fontsize'] = FONT_SIZE_LEGEND
```

## Axis Settings

### X-axis Text Labels
When x-axis tick labels are text (not numbers), rotate them for better readability.

**Centering Rotated Labels**: A common problem is that rotated labels appear misaligned with their corresponding tick positions. This happens because matplotlib's default `ha='right'` aligns the text by its endpoint, not its visual center.

**Wrong approach** (labels shift away from tick center):
```python
ax.set_xticklabels(labels, rotation=45, ha='right')  # Labels not centered!
```

**Correct approach** (labels centered at tick positions):
```python
ax.set_xticklabels(labels, rotation=45, ha='center', rotation_mode='anchor')
ax.tick_params(axis='x', pad=10)  # Add padding to avoid overlap with plot area
```

**Explanation**:
- `ha='center'`: Aligns the text horizontally by its center point
- `rotation_mode='anchor'`: Rotates around the alignment anchor point, keeping the center aligned with the tick
- `tick_params(pad=...)`: Moves labels down to prevent rotated text from overlapping with bars/data

**Recommended padding values**:
- `rotation=30`: `pad=10`
- `rotation=45`: `pad=15` to `pad=20`
- Long labels or wide bar groups: increase `pad` as needed

## Scatter Plot Style

### Basic Configuration
```python
# Scatter plot parameters
marker_size = 50
alpha = 0.7
edgecolors = 'black'
linewidths = 0.5
```

### Example
```python
plt.scatter(x, y, s=marker_size, alpha=alpha, edgecolors=edgecolors, linewidths=linewidths)
```

## Bar Plot Style

### General Requirements
- **Always add edge color** (borderline) to bars
- Edge color: black
- Edge width: 1.0-1.5

### Two-Series Bar Plot (Comparison)
Use **Red vs Blue** color scheme:

```python
colors_two_series = ['#D62728', '#1F77B4']  # Red, Blue
```

Example:
```python
width = 0.35
x = np.arange(len(labels))

plt.bar(x - width/2, series1, width, label='Series 1',
        color='#D62728', edgecolor='black', linewidth=1.2)
plt.bar(x + width/2, series2, width, label='Series 2',
        color='#1F77B4', edgecolor='black', linewidth=1.2)
```

### Multi-Series Bar Plot (3+ Series)
Use **White-Gray** color scheme combined with hatch patterns for maximum distinction:

```python
# Only use white and gray colors
colors_multi_series = ['#FFFFFF', '#808080']  # White, Gray

# Only use these hatch patterns: empty, forward slash, x, and dot
hatch_patterns = ['', '///', 'xxx', '...']

# Generate combinations of colors and hatches for up to 8 series
# Examples:
# Series 1: White + No fill
# Series 2: White + Slash fill
# Series 3: White + X fill
# Series 4: White + Dot fill
# Series 5: Gray + No fill
# Series 6: Gray + Slash fill
# Series 7: Gray + X fill
# Series 8: Gray + Dot fill
```

**IMPORTANT**: For multi-series bar plots, ensure that:
- X-axis tick positions are set at the center of each bar group
- X-axis tick labels are centered at the tick positions
- Use combinations of white/gray colors with different hatch patterns for distinction
- Not every series needs a hatch pattern - some can be solid fill

Example:
```python
width = 0.2
x = np.arange(len(labels))

# Define color and hatch combinations for each series
series_styles = [
    {'color': '#FFFFFF', 'hatch': ''},      # White, no fill
    {'color': '#FFFFFF', 'hatch': '///'},   # White, slash fill
    {'color': '#808080', 'hatch': ''},      # Gray, no fill
    {'color': '#808080', 'hatch': 'xxx'},   # Gray, x fill
]

for i, (data, style) in enumerate(zip(series_list, series_styles)):
    offset = width * (i - len(series_list)/2 + 0.5)
    ax.bar(x + offset, data, width, label=f'Series {i+1}',
           color=style['color'], edgecolor='black', linewidth=1.2, hatch=style['hatch'])

# Set tick positions at the center of each group
ax.set_xticks(x)
ax.set_xticklabels(labels)
```

### Breakdown Stacked Bar Plot
Use **stacked bar chart** to show composition breakdown of a whole. This is useful for analyzing the proportion of each component in the total.

**Color Scheme**: Use distinct colors for each component:

```python
# Breakdown colors - use visually distinct colors for components
breakdown_colors = [
    '#4472C4',  # Blue
    '#ED7D31',  # Orange
    '#A5A5A5',  # Gray
    '#FFC000',  # Yellow
    '#5B9BD5',  # Light Blue
    '#70AD47',  # Green
]
```

**Single Breakdown Bar**:
```python
# Data: components should sum to 100% or total value
components = [30, 25, 20, 15, 10]
component_labels = ['Component A', 'Component B', 'Component C', 'Component D', 'Component E']
colors = breakdown_colors[:len(components)]

# Create stacked bar
bottom = 0
for i, (value, label, color) in enumerate(zip(components, component_labels, colors)):
    ax.bar(0, value, width=0.5, bottom=bottom, label=label,
           color=color, edgecolor='black', linewidth=1.2)
    bottom += value

ax.set_ylabel('Percentage (%)')
ax.set_xticks([0])
ax.set_xticklabels(['System'])
```

**Two-Series Breakdown Comparison** (e.g., Before vs After):
```python
# Data for two scenarios
labels = ['Before', 'After']
component_a = [30, 25]  # Component A values for before and after
component_b = [25, 30]
component_c = [20, 15]
component_d = [15, 18]
component_e = [10, 12]

components_data = [component_a, component_b, component_c, component_d, component_e]
component_labels = ['Component A', 'Component B', 'Component C', 'Component D', 'Component E']
colors = breakdown_colors[:len(components_data)]

width = 0.5
x = np.arange(len(labels))

# Stack bars for each category
for i, (data, label, color) in enumerate(zip(components_data, component_labels, colors)):
    if i == 0:
        ax.bar(x, data, width, label=label, color=color, edgecolor='black', linewidth=1.2)
        bottom = np.array(data)
    else:
        ax.bar(x, data, width, bottom=bottom, label=label, color=color, edgecolor='black', linewidth=1.2)
        bottom += np.array(data)

ax.set_ylabel('Percentage (%)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend(loc='best', frameon=True)
```

**IMPORTANT**: For breakdown stacked bar plots:
- Each component should have a distinct color (no hatch patterns needed)
- Always add black edge color to distinguish boundaries between components
- Components are stacked vertically, summing to 100% or total value
- Use legend to identify each component
- Suitable for showing composition changes between scenarios

## Complete Example Templates

### Template 1: Two-Column Scatter Plot
```python
import matplotlib.pyplot as plt
import numpy as np

# Settings
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 11

# Create figure
fig, ax = plt.subplots(figsize=(7.0, 4.5))

# Plot
ax.scatter(x, y, s=50, alpha=0.7, edgecolors='black', linewidths=0.5)

# Labels
ax.set_xlabel('X Axis Label')
ax.set_ylabel('Y Axis Label')

# Grid (optional)
ax.grid(True, alpha=0.3, linestyle='--')

# Save
plt.tight_layout()
plt.savefig('output.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
```

### Template 2: Single-Column Two-Series Bar Plot
```python
import matplotlib.pyplot as plt
import numpy as np

# Settings
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 11

# Create figure
fig, ax = plt.subplots(figsize=(3.5, 2.8))

# Data
labels = ['A', 'B', 'C', 'D']
series1 = [10, 20, 15, 25]
series2 = [12, 18, 20, 22]

# Plot
width = 0.35
x = np.arange(len(labels))

ax.bar(x - width/2, series1, width, label='Method 1',
       color='#D62728', edgecolor='black', linewidth=1.2)
ax.bar(x + width/2, series2, width, label='Method 2',
       color='#1F77B4', edgecolor='black', linewidth=1.2)

# Labels
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_xticks(x)
ax.set_xticklabels(labels)

# Legend
ax.legend(loc='best', frameon=True)

# Save
plt.tight_layout()
plt.savefig('output.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
```

### Template 3: Two-Column Multi-Series Bar Plot (White-Gray)
```python
import matplotlib.pyplot as plt
import numpy as np

# Settings
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 11

# Create figure
fig, ax = plt.subplots(figsize=(7.0, 4.5))

# Data
labels = ['Category A', 'Category B', 'Category C']
series1 = [20, 35, 30]
series2 = [25, 32, 34]
series3 = [22, 30, 28]
series4 = [18, 28, 32]

series_list = [series1, series2, series3, series4]

# Define color and hatch combinations
series_styles = [
    {'color': '#FFFFFF', 'hatch': '', 'label': 'Method 1'},      # White, no fill
    {'color': '#FFFFFF', 'hatch': '///', 'label': 'Method 2'},   # White, slash fill
    {'color': '#808080', 'hatch': '', 'label': 'Method 3'},      # Gray, no fill
    {'color': '#808080', 'hatch': 'xxx', 'label': 'Method 4'},   # Gray, x fill
]

# Plot
width = 0.2
x = np.arange(len(labels))

for i, (data, style) in enumerate(zip(series_list, series_styles)):
    offset = width * (i - len(series_list)/2 + 0.5)
    ax.bar(x + offset, data, width, label=style['label'],
           color=style['color'], edgecolor='black', linewidth=1.2, hatch=style['hatch'])

# Labels
ax.set_xlabel('Categories')
ax.set_ylabel('Performance Metric')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30, ha='center', rotation_mode='anchor')
ax.tick_params(axis='x', pad=10)  # Avoid overlap with bars

# Legend
ax.legend(loc='best', frameon=True, ncol=2)

# Save
plt.tight_layout()
plt.savefig('output.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
```

### Template 4: Two-Column Breakdown Stacked Bar Plot (Before vs After)
```python
import matplotlib.pyplot as plt
import numpy as np

# Settings
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11
plt.rcParams['legend.fontsize'] = 11

# Create figure
fig, ax = plt.subplots(figsize=(7.0, 4.5))

# Data - percentage breakdown for Before and After scenarios
labels = ['Before', 'After']
component_a = [35, 28]  # Component A
component_b = [25, 30]  # Component B
component_c = [20, 22]  # Component C
component_d = [12, 13]  # Component D
component_e = [8, 7]    # Component E

components_data = [component_a, component_b, component_c, component_d, component_e]
component_labels = ['Processing', 'Communication', 'Storage', 'Overhead', 'Other']

# Breakdown colors
breakdown_colors = [
    '#4472C4',  # Blue
    '#ED7D31',  # Orange
    '#A5A5A5',  # Gray
    '#FFC000',  # Yellow
    '#5B9BD5',  # Light Blue
]

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

# Labels
ax.set_xlabel('Configuration')
ax.set_ylabel('Time Breakdown (%)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylim([0, 100])

# Legend
ax.legend(loc='best', frameon=True)

# Save
plt.tight_layout()
plt.savefig('output.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.close()
```

## Quick Reference

### Color Codes
**Two-series bar plots:**
- **Red**: `#D62728`
- **Blue**: `#1F77B4`

**Multi-series bar plots:**
- **White**: `#FFFFFF`
- **Gray**: `#808080`

**Breakdown stacked bar plots:**
- **Blue**: `#4472C4`
- **Orange**: `#ED7D31`
- **Gray**: `#A5A5A5`
- **Yellow**: `#FFC000`
- **Light Blue**: `#5B9BD5`
- **Green**: `#70AD47`

### Hatch Patterns (Multi-series bar plots only)
- Empty (solid): `''`
- Forward slash: `'///'`
- X pattern: `'xxx'`
- Dots: `'...'`

### Multi-Series Style Combinations
Combine white/gray with hatch patterns for up to 8 distinct series:
1. White + No fill
2. White + Slash fill (`///`)
3. White + X fill (`xxx`)
4. White + Dot fill (`...`)
5. Gray + No fill
6. Gray + Slash fill (`///`)
7. Gray + X fill (`xxx`)
8. Gray + Dot fill (`...`)

## Checklist Before Saving
- [ ] No title added to figure
- [ ] Correct figure size (single-column or two-column)
- [ ] Font sizes: axis labels (14), ticks/legend (11)
- [ ] Rotated text labels use `ha='center', rotation_mode='anchor'` with `tick_params(pad=...)`
- [ ] Bar plots have black edge color
- [ ] Correct color scheme:
  - Red-blue for 2 series comparison
  - White-gray combinations for multi-series
  - Distinct colors for breakdown stacked bars
- [ ] Multi-series bar plots: only use white/gray with hatch patterns (///, xxx, ...)
- [ ] Multi-series bar plots: tick positions centered at each group
- [ ] Breakdown stacked bars: components sum to 100% or total value
- [ ] Export format is PDF
- [ ] `bbox_inches='tight'` in savefig()
