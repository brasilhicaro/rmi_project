import Pyro4


def main():
    server = Pyro4.Proxy("PYRONAME:chat.servidor")

    name = input("Enter your @ for the chat: ")
    ip = "127.0.0.1"
    port = "9090"

    response = server.register_client(name, ip, port)
    print(response)

    print("Active clients:")
    active_clients = server.list_active_clients()
    for client, (ip, port) in active_clients.items():
        print(f"{client} - IP: {ip}, Port: {port}")

    message = input("Enter a message to send to everyone: ")
    server.send_broadcast(name, message)

    client_to_connect = input("Enter the @ of the client you want to chat with: ")
    client_info = server.find_client(client_to_connect)
    if client_info != "Client not found.":
        print(f"Connecting to client {client_to_connect} at {client_info[0]}:{client_info[1]}")

    today_date = server.today_date()
    print(f"The server's date/time is: {today_date}")


if __name__ == "__main__":
    main()
