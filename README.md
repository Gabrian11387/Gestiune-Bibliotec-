# Gestiune Bibliotecă

Aplicația gestionează operațiile efctuate într-o bibliotecă obișnuită. Aplicația stochează cărți și clienți, fiecare având diferite atribute, după cum urmează:

    - Carte (id, titlu, descriere, autor)
    - Client (id, nume, CNP)

## Funcționalități
- Adăugare de noi clienți, cărți
- Ștergerea unui client sau a unei cărți
- Modificarea unui client/a unei cărți
- Căutare carte/ client 
- Închiriere/returnare carte
- Găsirea celor mai închiriate cărți
- Găsirea clienților cu cărți închiriate ordonați după nume/după numărul de cărți închiriate
- Găsirea celor mai activi 20% dintre clienți 

# Aspecte generale
Aplicația are o arhiterctură stratificată, fiind realizată pe 3 nivele: ui(consola) -> service(business) -> repository(storage).
Ca și paradigmă de programare apare programarea orientată pe obiect. Aplicația poate lucra cu date din fișiere, dar și de la utilizator. Fiecare funcție este testată(100% coverage), iar datele primite de la utilizator trec printr-un validator înainte de a intra în structura aplicației.  
