import matplotlib.pyplot as plt
import numpy as np
import random
import itertools

# Categories
slopes = ["Flat", "Inclined", "Cliff"]
textures = ["Smooth", "Rough", "Uneven", "Irregular"]
compositions = ["Firm", "Soft", "Loose", "Slippery"]

# Function to generate a 3D terrain surface visualization
def generate_terrain(ax, slope, texture, composition, seed=None):
    np.random.seed(seed)
    x = np.linspace(0, 10, 100)
    y = np.linspace(0, 10, 100)
    X, Y = np.meshgrid(x, y)

    # Base slope/elevation
    if slope == "Flat":
        Z = np.zeros_like(X, dtype=float)
    elif slope == "Inclined":
        Z = 0.3 * X  # gentle slope
    elif slope == "Cliff":
        Z = np.where(X < 5, 0.0, 8.0)  # sharp elevation change

    # Add texture
    if texture == "Smooth":
        pass  # no change
    elif texture == "Rough":
        Z += 0.3 * np.sin(3*X) * np.cos(3*Y)
    elif texture == "Uneven":
        Z += np.sin(0.5*X) * np.cos(0.5*Y) * 2
    elif texture == "Irregular":
        Z += np.random.normal(0, 1.0, X.shape)

    # Choose color based on composition
    color_dict = {
        "Firm": "dimgray",
        "Soft": "lightcoral",
        "Loose": "sandybrown",
        "Slippery": "lightblue"
    }
    color = color_dict[composition]

    # Plot as 3D surface
    ax.plot_surface(X, Y, Z, cmap=None, color=color, rstride=2, cstride=2, linewidth=0, antialiased=False, shade=True)
    ax.set_title(f"{slope}, {texture}, {composition}", fontsize=8)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.view_init(elev=30, azim=135)  # perspective view

# Pick 6 random combinations for clarity (3D surfaces take space)
combinations = [(s, t, c) for s in slopes for t in textures for c in compositions]
random.seed(123)
sampled_combos = random.sample(combinations, 6)

# Plot
fig = plt.figure(figsize=(15, 10))
for i, combo in enumerate(sampled_combos, 1):
    ax = fig.add_subplot(2, 3, i, projection='3d')
    generate_terrain(ax, *combo, seed=random.randint(0,20))

plt.tight_layout()
plt.show()


# # Plot
#     ax.plot_surface(X, Y, Z, color=color, rstride=2, cstride=2,
#                     linewidth=0, antialiased=False, shade=True)
#     ax.set_title(f"{slope}, {texture}, {composition}", fontsize=7)
#     ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
#     ax.view_init(elev=30, azim=135)

# # Generate all 48 combinations
# combinations = list(itertools.product(slopes, textures, compositions))

# # Plot in groups of 12
# for i in range(0, 48, 12):
#     fig = plt.figure(figsize=(15, 12))
#     for j, combo in enumerate(combinations[i:i+12], 1):
#         ax = fig.add_subplot(3, 4, j, projection='3d')
#         generate_terrain(ax, *combo, seed=j)
#     plt.tight_layout()
#     plt.show()