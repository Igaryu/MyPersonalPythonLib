#!/usr/bin/env python3
'''
    Libreria personale di fuzioni di utilizzo comune
'''

def cls():
    from os import name, system
    '''
    Definisce cosa usare per pulire lo schermo in base al sistema
    dando per scontato che se non è Linux o Mac sarà Windows.
    '''

    if name == 'posix':
        system('clear')
    else:
        system('cls')

def Allarme(n):
    ''' 
        Suona semplicmente n volte il carattere BELL
    '''
    print (n * chr(7))


def intesta():
	cls()
	print("\nSfida Scrittura							Ver 1.0")
	print("\nUna spinta verso la scrittura creativa\n\n")


def menu():
    ''' 
    Visulizza il menu a tre voci ed invoca la funzione corrispondente
    alle voci selezionate.
    '''
    
    risp=0
    while ((risp < 1) or (risp > 3)):
        intesta()
        print("\n\n\n\n\n")
        print("\t\t\t[ 1 ] Prima Voce\n\n")
        print("\t\t\t[ 2 ] Seconda Voce\n\n")
        print("\t\t\t[ 3 ] Esci\n\n")
        risp=input('\n\n Seleziona voce menu [ 1 - 3 ] ')
        if risp in "123":
            risp=int(risp)
        else:
            risp=0
        return(risp)

def is_numeric(i):
    '''
        Ritorna True se il parametro è numerico
    '''
    try:
        float(i)
        return True
    except ValueError:
        return False

def ChekIfExists(NomeFile: str):
    from os.path import isfile
    '''
        verifica se un file esiste: ritorna True o False
    '''

    if isfile(NomeFile):
        return True
    else:
        return False



def trova_files(dir: str, pattern: str):
    '''
        Trova tutti i files corrispondenti a PATTERN scandendo la
        struttura DIRECTORY
    '''
    for root, _, files in os.walk(dir):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

def check_dir_to_scan(dir_to_scan: str):
    '''
    Se il parametro esistee, come percorso assoluto, lo restituisce;
    altrimenti verifica se esiste come percorso relativo alla $HOME e, se si,
    resistuisce il paramentro anteposto dal contenuto di $HOME.

    Se non sono vere nessuna delle due situazioni, segnala l'inesitenza della
    directory ed esce con un error code -9

    :param home_dir Cartella home dell'utente
    :param dir_to_scan Cartella segnalata dall'utente come oggetto della scansione

    :return percorso assoluto se lo è altrimenti restituisce la somma dei due paramentri
    '''
    from os import environ
    from os.path import exists, join
    from sys import exit

    if exists(dir_to_scan) is True:
        return dir_to_scan

    home_dir = environ['HOME']

    #if exists(home_dir+'/'+dir_to_scan) is True:
    if exists(join(home_dir,dir_to_scan)) is True:
        return join(home_dir,dir_to_scan)
    
    print("Directory inesistente !!!")
    return False

def UserPassReq():
    from getpass import getpass

    '''
    Richiede username e password mascherando i caratteri durante 
    la digitazione della password.
    '''
    user, passwd = '', ''

    user = input("Digita il tuo username: ")
    passwd = getpass()
    return user, passwd    



