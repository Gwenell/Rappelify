import socket
import json
from utils.settings import settings

class SyncManager:
    def __init__(self):
        """
        Initialize the SyncManager with a default sync code and port number.
        """
        self.sync_code = None
        self.port = 12345

    def generate_sync_code(self):
        """
        Generate a random sync code consisting of uppercase letters and digits.
        Returns:
            str: The generated sync code.
        """
        import random
        import string
        self.sync_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return self.sync_code

    def start_server(self):
        """
        Start a server to listen for incoming synchronization requests.
        When a client connects and sends the correct sync code, the server
        sends back the sync data.
        """
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', self.port))
        server.listen(1)
        conn, addr = server.accept()
        data = conn.recv(1024)
        received_code = data.decode()
        if received_code == self.sync_code:
            sync_data = json.dumps(self.get_sync_data())
            conn.sendall(sync_data.encode())
        conn.close()

    def connect_to_network(self, sync_code, ip_address):
        """
        Connect to a server to synchronize data.
        Parameters:
            sync_code (str): The sync code to send to the server.
            ip_address (str): The IP address of the server to connect to.
        """
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip_address, self.port))
        client.sendall(sync_code.encode())
        data = client.recv(1024)
        sync_data = json.loads(data.decode())
        self.apply_sync_data(sync_data)
        client.close()

    def get_sync_data(self):
        """
        Retrieve the data to be synchronized.
        Returns:
            dict: The data to synchronize.
        """
        return settings.get_all()

    def apply_sync_data(self, sync_data):
        """
        Apply the synchronized data to the current settings.
        Parameters:
            sync_data (dict): The synchronized data to apply.
        """
        settings.set_all(sync_data)
