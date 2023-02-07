import socket
import threading
import pyfiglet
ascii_banner = pyfiglet.figlet_format("KeK  PortScan")

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except socket.error:
        return "Unknown service"
def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        con = s.connect((host, port))
        servName= get_service_name(port)
        if port==8080: servName ='http'
        elif port==8443: servName ='https'
        print(f'Port {port} is open. Service name is --> ',servName)
        con.close()
    except:
        pass

def main(host,threadnum,portnum):
    threads = []
    for port in range(1, portnum):
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
    for i in range(0, len(threads), threadnum):
        for j in range(i, min(i+threadnum, len(threads))):
            threads[j].start()
        for j in range(i, min(i+threadnum, len(threads))):
            threads[j].join()

if __name__ == '__main__':
    print(ascii_banner)
    host = input("Target ip or url : ")
    threadnum = int(input("How much thread do you want : "))
    portnum=int(input("Which port will you scan until? : "))
    main(host,threadnum,portnum)
    
    
