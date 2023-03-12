#!/usr/bin/env python3
"""

$$\   $$\                     $$\       $$\                  $$\     
$$ |  $$ |                    $$ |      $$ |                 $$ |    
$$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$$\  $$$$$$$\   $$$$$$\ $$$$$$\   
$$$$$$$$ | \____$$\ $$  _____|$$  __$$\ $$  __$$\  \____$$\\_$$  _|  
$$  __$$ | $$$$$$$ |\$$$$$$\  $$ |  $$ |$$ |  $$ | $$$$$$$ | $$ |    
$$ |  $$ |$$  __$$ | \____$$\ $$ |  $$ |$$ |  $$ |$$  __$$ | $$ |$$\ 
$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$ |  $$ |$$$$$$$  |\$$$$$$$ | \$$$$  |
\__|  \__| \_______|\_______/ \__|  \__|\_______/  \_______|  \____/ 
                                                                     
====================================================================                                                                    
                                                                     
Made by : Muhammed Alkohawaldeh AKA (Twister_froste)
----------------------------------------------------
"""
import hashlib as hl
import sys
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


    
def hash_file(filename, hash_type = 'sha1'):
        
        if hash_type.lower() in ['sha1', 'sha-1', 'sha 1', '1']:
             hash = hl.sha1()

        elif hash_type.lower() in ['sha224', 'sha-224', 'sha 224', '2']:
             hash = hl.sha224()

        elif hash_type.lower() in ['sha256', 'sha-256', 'sha 256', '3']:           
             hash = hl.sha256()

        elif hash_type.lower() in ['sha384', 'sha-384', 'sha 384', '4']:           
             hash = hl.sha384()

        elif hash_type.lower() in ['sha512', 'sha-512', 'sha 512', '5']:          
             hash = hl.sha512()

        elif hash_type.lower() in ['md5', '6']:       
             hash = hl.md5()

        try:
            with open(filename,'rb') as file:

                chunk: int = 0
                while chunk != b'':
                    chunk = file.read(1024)
                    hash.update(chunk)

            return hash.hexdigest()
        
        except FileNotFoundError:
             print(f"""{Fore.LIGHTRED_EX}The file you entered does not exist
Please verify that the path you entered is correct""")
             sys.exit(1)

#   This function was biuld to get the hash for text but ...
def hash_blane():
    root_object: str = input(f"{Fore.LIGHTWHITE_EX}{Back.YELLOW}{Style.BRIGHT}Enter a password to get a hash: ")

    hash_object = hl.sha1(f'{root_object}'.encode())
    pbHash = hash_object.hexdigest()

    return pbHash


print(f"""{Fore.YELLOW}{Style.BRIGHT}
  _    _           _     _           _   
 | |  | |         | |   | |         | |  
 | |__| | __ _ ___| |__ | |__   __ _| |_ 
 |  __  |/ _` / __| '_ \| '_ \ / _` | __|
 | |  | | (_| \__ \ | | | |_) | (_| | |_ 
 |_|  |_|\__,_|___/_| |_|_.__/ \__,_|\__|
                                         
 {Style.NORMAL}Hashing tool, Made By ({Fore.BLACK}{Style.BRIGHT}Twister_Froste{Style.NORMAL}{Fore.YELLOW}).

 {Fore.GREEN}Hash (Types\Modes):
    {Fore.YELLOW}1) {Fore.BLUE}SHA-1{Fore.YELLOW}
    2) {Fore.BLUE}SHA-224{Fore.YELLOW}
    3) {Fore.BLUE}SHA-256{Fore.YELLOW}
    4) {Fore.BLUE}SHA-384{Fore.YELLOW}
    5) {Fore.BLUE}SHA-512{Fore.YELLOW}
    6) {Fore.BLUE}MD5{Fore.YELLOW}

{Fore.GREEN}Default Mode: {Fore.MAGENTA}{Style.BRIGHT}SHA-1                                       
""", end='\n\n')

mode = input(f"{Fore.WHITE}{Back.BLACK}{Style.BRIGHT}Please enter the Hash (Types\Mode): {Fore.BLUE}")

file = input(f"{Fore.WHITE}{Back.BLACK}{Style.BRIGHT}Please enter a file name: {Fore.BLUE}")

if file == '':
     print(f"""{Fore.LIGHTRED_EX}This field cannot be left blank.
The program fails.""")
     sys.exit(1)

hashed_file = hash_file(filename = file, hash_type = mode)

print(f"{Fore.GREEN}File Name: {Fore.YELLOW}{file}")

if mode.lower() in ['sha1', 'sha-1', 'sha 1', '1', '']:
    print(f"{Fore.GREEN}{Style.BRIGHT}Hash type: {Fore.MAGENTA}{Style.BRIGHT}SHA-1")

elif mode.lower() in ['sha224', 'sha-224', 'sha 224', '2']:
    print(f"{Fore.GREEN}{Style.BRIGHT}Hash type: {Fore.MAGENTA}{Style.BRIGHT}SHA-224")

elif mode.lower() in ['sha256', 'sha-256', 'sha 256', '3']:           
    print(f"{Fore.GREEN}{Style.BRIGHT}Hash type: {Fore.MAGENTA}{Style.BRIGHT}SHA-256")

elif mode.lower() in ['sha384', 'sha-384', 'sha 384', '4']:           
    print(f"{Fore.GREEN}{Style.BRIGHT}Hash type: {Fore.MAGENTA}{Style.BRIGHT}SHA-384")

elif mode.lower() in ['sha512', 'sha-512', 'sha 512', '5']:          
    print(f"{Fore.GREEN}{Style.BRIGHT}Hash type: {Fore.MAGENTA}{Style.BRIGHT}SHA-512")

elif mode.lower() in ['md5', '6']:       
    print(f"{Fore.GREEN}{Style.BRIGHT}Hash type: {Fore.MAGENTA}{Style.BRIGHT}MD5")

print(f"{Fore.GREEN}{Style.BRIGHT}Hash code: {Fore.RESET}{hashed_file}")