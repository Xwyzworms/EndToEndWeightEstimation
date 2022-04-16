#%%

import socket, cv2, pickle, struct,imutils
#%%
## Creating Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP IPV4
host_name = socket.gethostname()
#host_ip = socket.gethostbyname(host_name)
host_ip = "192.168.0.113" # Lan 
print("Host IP: {}".format(host_ip))
port : int = 9999

# used for binding the socket
socket_address = (host_ip, port)

server_socket.bind(socket_address)

server_socket.listen(5)
print("Listening AT : {}".format(socket_address))

# listen
run : bool = True
vid = cv2.VideoCapture(0)
print("YOMAN")
while True:
	client_socket, addr = server_socket.accept() ## Accept request
	print("Got a connection from: {}".format(addr))
	if run :
			## lAter do The Inference
		img, frame = vid.read()
		frame = imutils.resize(frame, width=400) #Resizing Frame
		
		#Save the frames into the bytes
		data = pickle.dumps(frame) #Convert the frame into bytes
		message = struct.pack("Q", len(data)) + data # Data Unsigned Long long, Dengan pnajng data dari pickle.dumps
		#message =b"hellow"
		client_socket.sendall(message)

		cv2.imshow("Transmitting Video", frame)
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			client_socket.close()
			break

# %%
