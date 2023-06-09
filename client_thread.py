import threading
import time
import socket
import logging


def send_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('172.16.16.101', 45000)
    logging.warning(f"opening socket {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        msg = 'TIME\r\n'
        logging.warning(f"sending {msg}")
        sock.sendall(msg.encode('utf-8'))
        # Look for the response
        data = sock.recv(32)
        result = data.decode('utf-8')
        logging.warning(f"{result}")
    finally:
        logging.warning("closing")
        sock.close()


if __name__ == '__main__':
    counter = 0
    max_thread = 0
    start_time = time.time()
    while time.time() - start_time < 30:
        thread = threading.Thread(target=send_data)
        thread.start()
        thread.join()

        counter += 1
        if counter > max_thread:
            max_thread = counter

    f = open('maximum_threading.txt', 'w')
    f.write(f"Maximum threads acquired: {max_thread}")
    f.close()

    logging.warning(f"Maximum threads: {max_thread}")
