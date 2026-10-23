import matplotlib.pyplot as plt
import networkx as nx
from data.trains_loader import TRAINS

G = nx.MultiDiGraph()

for train in TRAINS:
    G.add_edge(
        train.origin,
        train.destination,
        label=train.id
    )
    
positions = {
    "A": (0,0),
    "B": (2,0),
    "C": (1,1)
}

fig, ax = plt.subplots(figsize=(9,6))

nx.draw_networkx_nodes(
    G, positions,
    node_size=2000,
    node_color="lightblue",
    ax=ax
)

nx.draw_networkx_labels(G, positions, ax=ax)

connectionstyle = [
    "arc3,rad=0.20",
    "arc3,rad=0.40",
    "arc3,rad=0.60",
    "arc3,rad=-0.20",
    "arc3,rad=-0.40",
    "arc3,rad=-0.60",
]

# Rysowanie krawędzi
nx.draw_networkx_edges(
    G,
    positions,
    connectionstyle=connectionstyle,
    arrows=True,
    arrowsize=20,
    node_size=2000,
    edge_color="dimgray",
    ax=ax
)

# Etykiety poszczególnych krawędzi
edge_labels = {
    (u, v, key): data["label"]
    for u, v, key, data in G.edges(keys=True, data=True)
}

nx.draw_networkx_edge_labels(
    G,
    positions,
    edge_labels=edge_labels,
    connectionstyle=connectionstyle,
    label_pos=0.25,
    font_size=10,
    rotate=False,
    bbox=dict(
        facecolor="white",
        edgecolor="none",
        alpha=0.9,
        pad=2
    ),
    ax=ax
)

ax.set_title("Graf połączeń kolejowych")
ax.axis("off")
plt.tight_layout()
plt.show()