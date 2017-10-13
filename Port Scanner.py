import socket, subprocess,sys
from datetime import datetime
subprocess.call('clear',shell=True)
ip = input("Digite o ip do host:")
var1 = int(input("Digite a port inicial"))
var2 = int (input("Digite a porta final"))
print ("#"*40)
print ("\n Scanner em andamento ",ip)
print ("#"*40)

t1= datetime.now()
try:
     for port in range(var1,var2):
         sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         socket.setdefaulttimeout(1)
         result = sock.connect_ex((ip,port))
     if result==0:
         print ("Porta Aberta:-->\t", port)
       #####----#####
     sock.close()
except KeyboardInterrupt:
     print ("Finalizado ")
     sys.exit()
except socket.gaierror:
     print ("O nome do host não pode ser resolvido")
     sys.exit()
except socket.error:
     print ("Não pode se conectar ao server")
     sys.exit()
t2= datetime.now()
total =t2-t1
print ("Completado em " , total)
