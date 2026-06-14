import socket
import threading
import time

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8888
BUFFER_SIZE = 1024


class TCPServer:
    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.host = host
        self.port = port
        self.clients = []
        self.chat_log = []

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.server_socket.bind((self.host, self.port))
        except socket.error:
            print("端口已被占用，请更换端口后重试")
            return
        self.server_socket.listen(5)
        print(f"TCP服务器启动 {self.host}:{self.port}")

        try:
            while True:
                client_socket, addr = self.server_socket.accept()
                print(f"新连接: {addr}")
                client_socket.send("连接成功".encode("utf-8"))
                self.clients.append(client_socket)
                thread = threading.Thread(target=self.handle_client,
                                          args=(client_socket, addr))
                thread.daemon = True
                thread.start()
        except KeyboardInterrupt:
            print("\n服务器关闭")
        finally:
            self.server_socket.close()

    def handle_client(self, client_socket, addr):
        while True:
            try:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                message = data.decode("utf-8")
                print(f"收到 [{addr[0]}:{addr[1]}]: {message}")
                timestamp = time.strftime("%H:%M:%S")
                self.chat_log.append(f"[{timestamp}] {addr}: {message}")
                self.broadcast(f"广播: {message}", client_socket)
                client_socket.send(f"已收到消息：{message}".encode("utf-8"))
            except (ConnectionResetError, BrokenPipeError):
                break
        print(f"客户端{addr}已断开连接")
        if client_socket in self.clients:
            self.clients.remove(client_socket)
        client_socket.close()

    def broadcast(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message.encode("utf-8"))
                except Exception:
                    pass


class TCPClient:
    def __init__(self, host=DEFAULT_HOST, port=DEFAULT_PORT):
        self.host = host
        self.port = port

    def start(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((self.host, self.port))
        except (socket.error, ConnectionRefusedError):
            print("连接已中断")
            return

        data = self.client_socket.recv(BUFFER_SIZE)
        print(data.decode("utf-8"))

        recv_thread = threading.Thread(target=self.receive_messages)
        recv_thread.daemon = True
        recv_thread.start()

        while True:
            try:
                msg = input()
                if msg.strip().lower() == "exit":
                    break
                self.client_socket.send(msg.encode("utf-8"))
            except (EOFError, KeyboardInterrupt):
                break
            except Exception:
                print("连接已中断")
                break
        self.client_socket.close()
        print("已断开连接")

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                print(data.decode("utf-8"))
            except Exception:
                break


def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        server.bind((DEFAULT_HOST, 9999))
    except socket.error:
        print("UDP端口已被占用")
        return
    print("UDP服务器启动 127.0.0.1:9999")
    try:
        while True:
            data, addr = server.recvfrom(BUFFER_SIZE)
            message = data.decode("utf-8")
            print(f"UDP收到 [{addr}]: {message}")
            server.sendto(f"已收到: {message}".encode("utf-8"), addr)
    except KeyboardInterrupt:
        print("\nUDP服务器关闭")
    finally:
        server.close()


def udp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg = input("UDP消息(exit退出): ")
        if msg.strip().lower() == "exit":
            break
        client.sendto(msg.encode("utf-8"), (DEFAULT_HOST, 9999))
        try:
            client.settimeout(2)
            data, _ = client.recvfrom(BUFFER_SIZE)
            print(data.decode("utf-8"))
        except socket.timeout:
            print("无响应")
    client.close()


if __name__ == "__main__":
    import sys

    print("=== Python 网络通信实验 ===")
    print("TCP与UDP对比:")
    print("  TCP: 面向连接,可靠传输,适合文件传输/网页浏览")
    print("  UDP: 无连接,速度快,适合视频直播/在线游戏")
    print()

    if len(sys.argv) < 2:
        print("用法: python 8-1.py [server|client|udpserver|udpclient]")
        print("  启动TCP服务器: python 8-1.py server")
        print("  启动TCP客户端: python 8-1.py client")
        print("  启动UDP服务器: python 8-1.py udpserver")
        print("  启动UDP客户端: python 8-1.py udpclient")
        sys.exit(0)

    mode = sys.argv[1]
    if mode == "server":
        TCPServer().start()
    elif mode == "client":
        TCPClient().start()
    elif mode == "udpserver":
        udp_server()
    elif mode == "udpclient":
        udp_client()
