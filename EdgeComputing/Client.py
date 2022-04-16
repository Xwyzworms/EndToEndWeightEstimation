#%%
import socket,cv2, pickle, struct

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip : str = "192.168.56.1" # Server IP
port : int = 9999

target_server = (host_ip, port)
client_socket.connect(target_server)

data : bytes = b""

payload_size = struct.calcsize("Q")
while True:
	while len(data) < payload_size:
		packet = client_socket.recv(4096) # 4k
		if not packet: break
		data += packet

	packet_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack("Q", packet_msg_size)[0]

	while len(data) < msg_size:
		data += client_socket.recv(4096)
	frame_data = data[:msg_size]
	frame = pickle.loads(frame_data)
	cv2.imshow("Receiving Video", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
client_socket.close()
# %%
