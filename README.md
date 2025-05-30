# vlastny_api_server

moduly na stiahnutie : 
requests, fastapi

Kod obsahuje 3 subory:
1. samotny server
2. json subor kde sa ukladaju ulohy
3. uzivatelske poziadavky

pouzivatel vyuziva hlavne 3. subor s uzivatelskymi poziadavkamy
ten obsahuje metody:
1. new - vytvara novu ulohu, berie parametre id, meno a popisok
2. get - vracia udaje o ulohe ktoej id je id zadane uzivatelom
3. get_all - vracia udaje vsetkych uloh
4. delete - maze ulohu ktorej id je id zadane uzivatelom

