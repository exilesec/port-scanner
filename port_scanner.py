import socket, os, pyfiglet

os.system("clear")
banner = pyfiglet.figlet_format("exilesec")
print(banner)

ip = input("\nip: ")

for port in range(1,1000):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip,port))
        print(str(port), "Open.")
    except Exception as e:
        # print(str(port), "Closed.")
        pass
    finally:
        s.close()
