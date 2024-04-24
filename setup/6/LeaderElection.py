
class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.is_coordinator = False

    def initiate_election(self, nodes):
        for node in nodes:
            if node.id > self.id:
                print(f"Node {self.id} sends election message to Node {node.id}")
                node.start_election(nodes)
        self.is_coordinator = True
        print(f"Node {self.id} becomes the coordinator.")

    def start_election(self, nodes):
        for node in nodes:
            if node.id > self.id:
                print(f"Node {self.id} sends election message to Node {node.id}")
                node.start_election(nodes)
        self.is_coordinator = True
        print(f"Node {self.id} becomes the coordinator.")

if __name__ == "__main__":
    # Create nodes
    nodes = [Node(i) for i in range(1, 6)]

    # Simulate Bully Algorithm
    print("Bully Algorithm:")
    # Node with highest ID starts the election
    nodes[-1].initiate_election(nodes)

    # Simulate Ring Algorithm
    print("\nRing Algorithm:")
    # Node with lowest ID starts the election
    nodes[0].start_election(nodes)

