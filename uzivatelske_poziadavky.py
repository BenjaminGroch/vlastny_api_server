import requests

def new():   # Funkcia na pridanie novej ulohy
    id = str(input("Zadajte prosim ID cislo: "))
    name = str(input("Zadajte meno ulohy: "))
    description = str(input("Zadajte popis ulohy: "))

    # Posielanie POST požiadavky na server s parametrami
    response = requests.post(f'http://localhost:8000/new-task?id={id}&name={name}&description={description}')
    output = response.text
    print(output)  #pise odpoved servera na konzolu

def get():  # Funkcia na získanie úlohy podľa ID
    id = str(input("Zadajte ID cislo ulohy: "))

    # Posielanie GET požiadavky na server s ID
    response = requests.get(f"http://localhost:8000/get-task?id={id}")
    output = response.text
    print(output)  #pise odpoved servera na konzolu

def get_all(): # Funkcia na získanie všetkých úloh

    # Posielanie GET požiadavky na server pre získanie všetkých úloh
    response = requests.get(f"http://localhost:8000/get-tasks")
    output = response.json()
    print(output)  #pise odpoved servera na konzolu

def delete():  # Funkcia na zmazanie úlohy podľa ID
    id = str(input("Zadajte ID cislo ulohy: "))

    # Posielanie DELETE požiadavky na server s ID
    response = requests.delete(f"http://localhost:8000/delete-task?id={id}")
    output = response.text
    print(output)  #pise odpoved servera na konzolu

#new()                 testovanie kodu
#new()
#get()
#get_all()
#new()S
#get_all()
