# PyPersLib
Libreria funzioni di comodità in Python3

***

Le funzioni sotto presentate sono frutto di lavoro svolto negli anni e che spesso sono venute comode durante lo sviluppo di applicazione full text.

## Cls()

Viene determinato l’ambiente operativo ed usato il comando adatto per pulire lo schermo

***

## Allarme()

Viene meramente suonato il *bell di sistema* char(7) per attirare l’attenzione dell’utente.

***

## intesta()

Esegue una intestazione video, utile di norma in programmi solo testuali.

***

## menu()

Blueprint di un menu da cui selezionare una voce: l’ultima è sempre *Uscita*

***

## is_numeric(val)

Torna **True** se il valore passato alla funzione è un numero, **False** in ogni altro caso

***

## ChekIfExists(NomeFile: str)

Verifica, usando le funzioni di sistema, se un file esiste o meno: torna **True** oppure **False**

***

## trova_files(dir: str, pattern: str)

Nella ***dir*** cerca file, in base al ***patter***. Entrambi i dati sono passati come argomento.

***

## check_dir_to_scan(dir_to_scan: str)

Verifica l’esistenza della ***dir_to_scan*** tornando **True** o **False** a seconda del caso

***

## UserPassReq()

Chiede *Username* e *password* oscurando i caratteri digitati per comporre la password. L’oscuramento dei caratteri viene ottenuto usando la funzione *gettpass* dell’omonimo modulo. Vengono restituite due stringhe 

- Una per il nome utente
- Una per la password

Non viene effettuato alcun controllo su lunghezza minima, massima o presenza di caratteri particolari: potrei aggiungerli, ma credo che il controllo sia più efficiente se svolto da chi usa la procedura. Questo perché ognuno ha le proprie esigenze in fatto di composizione di password.

***

## Altre saranno aggiunte con il tempo.

