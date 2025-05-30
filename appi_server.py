from fastapi import FastAPI
import json, os

app = FastAPI()             #Vytvaranie api
TASKS_FILE = "tasks.json"   #Vytvaranie json suboru na ukladanie udajov

def load_tasks():                                             #funkcia na ukladanie udajov
    if os.path.exists(TASKS_FILE):                            #ak subor existuje, tak ho otvor
        with open(TASKS_FILE, "r", encoding="utf-8") as f:    #otvara subor
            return json.load(f)                               #vracia ulozene udaje ako slovnik 
    return {}

def save_tasks(tasks):                                        #funkcia na ulozenie udajov        
    with open(TASKS_FILE, "w", encoding="utf-8") as f:        #otvara subor
        json.dump(tasks, f, ensure_ascii=False, indent=2)     #uklada udaje do suboru vo formate json

@app.post("/new-task")                                         #tvorba endpointu pre vytvorenie novej ulohy
async def post_task(id: str, name: str, description: str):     #berie parametre pre vytvorenie
    tasks = load_tasks()                                       #nacita ulozene udaje 
    if id in tasks:                                            #ak uz sa ID v zozname nachadza, nevytvara novu ulohu
        return("uloha s tymto ID uz existuje, prosime zvolte ine ID")
    else:
        tasks[id] = {"id": id, "name": name, "description": description}        #ak ID neexistuje, vytvara ulohu a uklada ju do slovnika
        save_tasks(tasks)           #uklada zmeny do suboru   
        return(f'Vytvorili ste ulohu s menom: {name}, jej ID je: {id}. Popis tejto ulohy je: {description}')

@app.get("/get-task")               #tvorba endpointu pre ziskanie ulohy podla ID    
async def get_task(id: str):        #berie parameter ID
    tasks = load_tasks()            #nacita ulozene udaje
    task = tasks.get(id)            #ziskava ulohu podla ID
    if task:                        #ak sa uloha podla ID nachadza, vracia udaje o ulohe   
        return(f'Uloha s tymto ID je: {task["name"]}, popisok tejto ulohy je: {task["description"]}')
    return("Uloha s tymto ID neexistuje")

@app.get("/get-tasks")              #tvorba endpointu pre ziskanie vsetkych uloh
async def all_tasks():
    tasks = load_tasks()            #nacita ulozene udaje
    if not tasks:                   #ak zoznam uloh je prazdny, vracia spravu, ze ziadne ulohy neexistuju 
        return("Ziadne ulohy neexistuju")
    else:                             #ak zoznam uloh nie je prazdny
        vypis = []                    #vytvara prazdny zoznam pre vypis uloh
        for task in tasks.values():   #prechadza vsetky ulohy v slovniku
            vypis.append(f'ID ulohy je: {task["id"]}, Meno je: {task["name"]}, a popisok je: {task["description"]}')
        return (vypis)                #vracia vypis vsetkych uloh ako zoznam

@app.delete("/delete-task")         #tvorba endpointu pre zmazanie ulohy podla ID
async def delete_task(id: str):     #berie parameter ID
    tasks = load_tasks()            #nacita ulozene udaje
    task = tasks.pop(id)            #odstranuje ulohu podla ID, ak sa nachadza v zozname
    if task:
        save_tasks(tasks)           #uklada zmeny do suboru
        return(f'Vymazali ste ulohu s ID: {task["id"]}, meno tejto ulohy bolo: {task["name"]}')
    return("Uloha s tymto ID neexistuje")
