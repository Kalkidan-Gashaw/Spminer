import networkx as nx
import pickle

txt_path = "./datasets/web-Stanford.txt"
pkl_path = "./datasets/webStanford.pkl"

G = nx.DiGraph()

# Read txt file
with open(txt_path, "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("FromNodeId"):
            continue
        parts = line.split("\t")  # 
        if len(parts) >= 2:
            src, tgt = int(parts[0]), int(parts[1])
            G.add_edge(src, tgt)

print(f" Loaded {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

# Save as pickle
with open(pkl_path, "wb") as f:
    pickle.dump(G, f)

print(f"Dataset saved as '{pkl_path}'")