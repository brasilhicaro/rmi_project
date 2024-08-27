import Pyro4
from datetime import datetime


@Pyro4.expose
class ChatServer(object):
    def __init__(self):
        self.clients = {}

    def register_client(self, name, ip, port):
        if name in self.clients:
            return f"Error: The name '{name}' is already in use."
        self.clients[name] = (ip, port)
        return f"Client '{name}' successfully registered."

    def list_active_clients(self):
        return self.clients

    def find_client(self, name):
        return self.clients.get(name, "Client not found.")

    def send_broadcast(self, name, message):
        print(f"[Broadcast] {name}: {message}")
        return "Broadcast message sent."

    def write_msg(self, msg):
        print(msg)

    def today_date(self):
        return datetime.now()


def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(ChatServer)

    ns = Pyro4.locateNS()
    ns.register("chat.server", uri)

    print(f"Server available. URI: {uri}")
    daemon.requestLoop()


if __name__ == "__main__":
    main()
