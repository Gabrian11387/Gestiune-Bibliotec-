from erori.Repo_error import RepoError
from erori.validation_error import ValidationError

class UI:

    def __init__(self, service_clienti, service_carti, service_inchirieri):
        self.__service_clienti = service_clienti
        self.__service_carti = service_carti
        self.__service_inchirieri = service_inchirieri
        self.__comenzi = {
            "adauga_client": self.__ui_adauga_client,
            "print_clienti": self.__ui_print_clienti,
            "sterge_client_dupa_id": self.__ui_sterge_client_dupa_id,
            "modifica_client_dupa_id": self.__ui_modifica_client_dupa_id,
            "adauga_carte": self.__ui_adauga_carte,
            "sterge_carte_dupa_id": self.__ui_sterge_carte_dupa_id,
            "print_carti": self.__ui_print_carti,
            "cauta_carti_dupa_autor": self.__ui_cauta_carti_dupa_autor,
            "cauta_clienti_dupa_nume": self.__ui_cauta_clienti_dupa_nume,
            "inchiriaza_carte": self.__ui_adauga_inchiriere_carte,
            "print_inchirieri": self.__ui_print_inchirieri,
            "returneaza_carte": self.__ui_returneaza_carte,
            "cele_mai_inchiriate_carti": self.__ui_cele_mai_inchiriate_carti,
            "ordoneaza_clienti_cu_carti_inch_dupa_nume": self.__ui_ordoneaza_clienti_cu_carti_inch_dupa_nume,
            "ordoneaza_clienti_dupa_carti_inch": self.__ui_ordoneaza_clienti_dupa_carti_inch,
            "cei_mai_activi_20%_dintre_clienti": self.__ui_cei_mai_activi_clienti,
            "nr_carti_inch_clienti_care_incep_cu_litera": self.__ui_nr_carti_inch_clienti_care_incep_cu_litera
        }

    def __ui_adauga_client(self):
        if len(self.__params) != 3:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        nume = self.__params[1]
        cnp = int(self.__params[2])
        self.__service_clienti.adauga_client(id_client, nume, cnp)
        print("client adaugat cu succes!")


    def __ui_print_clienti(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        clienti = self.__service_clienti.get_all_clienti()
        if len(clienti) == 0:
            print("Nu exista clienti in aplicatie!")
            return
        for x in clienti:
            print(x)


    def __ui_sterge_client_dupa_id(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        self.__service_clienti.sterge_client_dupa_id(id_client)
        self.__service_inchirieri.sterge_inchiriere_cu_clientul(id_client)
        print("Client sters cu succes!")


    def __ui_modifica_client_dupa_id(self):
        if len(self.__params) != 3:
            print("numar parametri invalid!")
            return
        id_client = int(self.__params[0])
        nou_nume = self.__params[1]
        nou_cnp = int(self.__params[2])
        self.__service_clienti.modifica_client_dupa_id(id_client, nou_nume, nou_cnp)
        print("Client modificat cu succes!")


    def __ui_cauta_clienti_dupa_nume(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        nume = self.__params[0]
        toti_clientii = self.__service_clienti.get_all_clienti()
        clienti_buni = self.__service_clienti.clienti_cu_numele(toti_clientii, nume)
        #clienti_buni = self.__service_clienti.cauta_clienti_dupa_nume(nume)
        if len(clienti_buni) == 0:
            print("Nu exista niciun client cu acest nume!")
            return
        for client in clienti_buni:
            print(client)

    def __ui_adauga_carte(self):
        if len(self.__params) != 4:
            raise ValueError("numar parametri invalid!")
        id_carte = int(self.__params[0])
        titlu_carte = self.__params[1]
        descriere_carte = self.__params[2]
        autor_carte = self.__params[3]
        self.__service_carti.adauga_carte(id_carte, titlu_carte, descriere_carte, autor_carte)
        print("carte adaugata cu succes!")


    def __ui_print_carti(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        carti = self.__service_carti.get_all_carti()
        if len(carti) == 0:
            print("Nu exista nicio carte in aplicatie!")
            return
        for carte in carti:
            print(carte)


    def __ui_sterge_carte_dupa_id(self):
        if len(self.__params) != 1:
            raise ValueError("numar parametri invalid!")
        id_carte = int(self.__params[0])
        self.__service_carti.sterge_carte_dupa_id(id_carte)
        self.__service_inchirieri.sterge_inchirieri_cu_cartea(id_carte)
        print("Carte stearsa cu succes!")


    def __ui_cauta_carti_dupa_autor(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        autor = self.__params[0]
        total_carti = self.__service_carti.get_all_carti()
        carti_bune = self.__service_carti.cauta_carti_cu_autorul(total_carti,autor)
        if len(carti_bune) == 0:
            print("Nu exista carti cu acest autor!")
            return
        for carte in carti_bune:
            print(carte)


    def __ui_adauga_inchiriere_carte(self):
        if len(self.__params) != 5:
            print("numar parametri invalid!")
            return
        id_inchiriere = int(self.__params[0])
        id_client = int(self.__params[1])
        nume_client = self.__params[2]
        id_carte = int(self.__params[3])
        titlu_carte = self.__params[4]
        self.__service_inchirieri.adauga_inchiriere(id_inchiriere, id_client, nume_client, id_carte, titlu_carte)
        print("Inchiriere adaugata cu succes!")


    def __ui_print_inchirieri(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        inchirieri = self.__service_inchirieri.get_all_inchirieri()
        if len(inchirieri) == 0:
            print("Nu exista nicio inchiriere in aplicatie!")
        for inch in inchirieri:
            print(inch)

    def __ui_returneaza_carte(self):
        if len(self.__params) != 5:
            print("numar parametri invalid!")
            return
        id_inchiriere = int(self.__params[0])
        id_client = int(self.__params[1])
        nume_client = self.__params[2]
        id_carte = int(self.__params[3])
        titlu_carte = self.__params[4]
        self.__service_inchirieri.sterge_inchiriere(id_inchiriere, id_client, nume_client, id_carte, titlu_carte)
        print("Returnare facuta cu succes!")


    def __ui_cele_mai_inchiriate_carti(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        carti_ordonate = self.__service_carti.ordoneaza_carti_dupa_nr_inchirieri()
        if len(carti_ordonate) == 0:
            print("Nu exista nicio carte inchiriata!")
            return
        for carte in carti_ordonate:
            print(carte)


    def __ui_ordoneaza_clienti_cu_carti_inch_dupa_nume(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        clienti_ordonati = self.__service_clienti.ordoneaza_clienti_dupa_nume()
        if len(clienti_ordonati) == 0:
            print("Nu exista clienti care au inchiriat carti!")
            return
        for client in clienti_ordonati:
            print(client)


    def __ui_ordoneaza_clienti_dupa_carti_inch(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        clienti_ordonati = self.__service_clienti.ordoneaza_clienti_dupa_carti_inch()
        if len(clienti_ordonati) == 0:
            print("Nu exista clienti care au inchiriat carti!")
            return
        for client in clienti_ordonati:
            print(client)


    def __ui_cei_mai_activi_clienti(self):
        if len(self.__params) != 0:
            print("numar parametri invalid!")
            return
        clienti_activi = self.__service_clienti.cei_mai_activi_clienti()
        if len(clienti_activi) == 0:
            print("Trebuie sa existe cel putin 5 clienti care au inchiriat fiecare cel putin o carte pentru a putea fi alesi cei mai activi 20% dintre acestia")
            return
        for client in clienti_activi:
            print(client)


    def __ui_nr_carti_inch_clienti_care_incep_cu_litera(self):
        if len(self.__params) != 1:
            print("numar parametri invalid!")
            return
        litera = self.__params[0].upper()
        if len(litera) != 1:
            print("lungime caracter invalida!")
            return
        nr_inch_clienti_cu_litera = self.__service_clienti.numar_inch_clienti_cu_litera(litera)
        if nr_inch_clienti_cu_litera == 0:
            print(f"Nu exista niciun client care incepe cu litera {litera}")
            return
        print(nr_inch_clienti_cu_litera)


    def run(self):
        while True:
            comanda = input(">>> ")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("Eroare UI: tip numeric invalid!")
                except ValidationError as ve:
                    print(f"Validation Error:{ve}")
                except RepoError as re:
                    print(f"Repo Error: {re}")
            else:
                print("comanda invalida!")


