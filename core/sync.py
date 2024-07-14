import socket
import json
from utils.settings import settings

class SyncManager:
    def __init__(self):
        self.sync_code = None
        self.port = 12345

    def generate_sync_code(self):
        import random
        import string
        self.sync_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        return self.sync_code

    def start_server(self):
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
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip_address, self.port))
        client.sendall(sync_code.encode())
        data = client.recv(1024)
        sync_data = json.loads(data.decode())
        self.apply_sync_data(sync_data)
        client.close()

    def get_sync_data(self):
        # Get data to synchronize
        return settings.get_all()

    def apply_sync_data(self, sync_data):
        # Apply synchronized data
        settings.set_all(sync_data)