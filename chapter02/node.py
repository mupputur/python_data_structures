class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        #return f"data : {self.data} next: {self.next}"
        return f"{self.data}"

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next
    def set_next(self, next_node_ref):
        self.next = next_node_ref



if __name__ == "__main__":
    n1 = Node(10)  # object1 or node1
    n2 = Node(20)  # object2 or nodd2
    n1.set_next(n2)

    print(n1)
    #print(n2)