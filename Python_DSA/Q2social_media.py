# Question 2 : 
'''
A social media platform stores friendships between users.

Requirements
    Create a graph where each user is connected to their friends.
    Display all users and their friends in a formated way.
    Store all usernames in a list.
    Sort the usernames using Insertion Sort.
    Ask the user to enter a name to see if they exists (binary search) and if they are connected.
    If found, display all of the user's friends.
'''
import networkx as nx
import matplotlib.pyplot as plt

# Graph representation using dictionary
social_graph = {
    'Aditya': ['Aman', 'Prem'],
    'Alice': ['Samul', 'Sam'],
    'Bob': ['Adam', 'David'],
    'David': ['Bob'],
    'Evam': ['Citra'],
    'Fready': []
}

# Create graph
G = nx.Graph()

# Add nodes and edges
for user, friends in social_graph.items():
    G.add_node(user)

    for friend in friends:
        G.add_node(friend)
        G.add_edge(user, friend)

# Draw graph
plt.figure(figsize=(8, 6))

pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="skyblue")
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

plt.title("Social Media Friendship Graph")
plt.axis("off")
plt.show()