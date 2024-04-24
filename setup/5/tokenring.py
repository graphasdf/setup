
class TokenRing:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.token = 0

    def send_data(self, sender, receiver, data):
        print("Token passing:", end="")
        for i in range(self.token, sender):
            print(f" {i % self.num_nodes}->", end="")
        print(f" {sender}")
        print(f"Sender {sender} sending data: {data}")

        for i in range(sender + 1, receiver):
            print(f"Data {data} forwarded by {i}")

        print(f"Receiver {receiver} received data: {data}\n")
        self.token = sender

if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes: "))
    token_ring = TokenRing(num_nodes)

    while True:
        sender = int(input("Enter sender: "))
        receiver = int(input("Enter receiver: "))
        data = input("Enter data: ")

        token_ring.send_data(sender, receiver, data)

        send_again = input("Do you want to send again? (yes/no): ")
        if send_again.lower() != "yes":
            break

