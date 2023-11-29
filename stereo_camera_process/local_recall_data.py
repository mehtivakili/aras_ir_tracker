import socket
import struct

def receive_data():
    # Define the IP address and port to listen on
    server_ip = "127.0.0.1"
    server_port = 4000

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # Bind the socket to the specified IP and port
        server_socket.bind((server_ip, server_port))
        print(f"Listening for UDP data on {server_ip}:{server_port}")

        while True:
            # Receive data and the address it was sent from
            data, address = server_socket.recvfrom(4096)

            # Unpack the received binary data using the format provided
            try:
                # Assuming your data contains doubles
                msg_format = f'{len(data)//8}d'
                unpacked_data = struct.unpack(msg_format, data)
                
                # Process the unpacked data as needed
                print("Unpacked data:", unpacked_data)
            except struct.error as e:
                print(f"Error unpacking data: {e}")

# Run the function to start listening for data
if __name__ == "__main__":
    receive_data()
