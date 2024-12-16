import socket

def portscanner(ip,startport,endport):
    openports=[]
    for port in range(startport,endport+1):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.2)
        result=sock.connect_ex((ip,port))
        if result==0:
            openports.append(port)

        sock.close()
    return openports

def validazione_ip(ip):
    ottetti = ip.split(".")
    if len(ottetti) != 4:
        return False
    for ottetto in ottetti:
 
        if not ottetto.isdigit() or not 0 <= int(ottetto) <= 255:
            return False
    return True


while True:
    ip=input("INSERISCI L'INDIRIZZO IP DA SCANSIONARE: ").strip()
    if (validazione_ip(ip)):
        print("Hai inserito un Ip Valido.")
        break
    print("L'IP inviato non è valido seguire la formattazione\nxxx.xxx.xxx.xxx dove ogni trio di x va da 0 a 255")
    
while True:    
    start_port= input("INSERISCI LA PORTA DI INIZIO: ").strip()
    if start_port.isdigit():
        start_port = int(start_port)
        if start_port <= 65535:
            break
        else:
            print("Il Valore Massimo Di Una Porta è 65535")
    else:
        print("Inserisci Una Porta Valida!")
    
while True:
    end_port= input("INSERISCI LA PORTA DI FINE: ").strip()
    if end_port.isdigit():
        end_port = int(end_port)
        if end_port <= 65535:
            if end_port >= start_port:
                break
            else:
                print("La Porta Di Inizio Non Puo Essere Maggiore Della Porta Di Fine!")
        else:
            print("Il Valore Massimo Di Una Porta è 65535")
    else:
        print("La Porta Non è Valida!")   

open_ports=portscanner(ip,start_port,end_port)
print(f"Porte Aperte Nel Range {start_port} - {end_port}:")
for port in open_ports:
    print(f'Porta {port} è aperta.')



