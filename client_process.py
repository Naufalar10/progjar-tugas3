import multiprocessing
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
    max_process = 0
    start_time = time.time()
    while time.time() - start_time < 45:
        process = multiprocessing.Process(target=send_data)
        process.start()
        process.join()

        counter += 1
        if counter > max_process:
            max_process = counter

    f = open('maximum_processing.txt', 'w')
    f.write(f"Maximum processes acquired: {max_process}")
    f.close()

    logging.warning(f"Maximum processes: {max_process}")
