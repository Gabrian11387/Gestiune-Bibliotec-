from domeniu.client import Client
import random
import string
from Sortari import quickSort
from Sortari import GnomeSort
from Sortari import GnomeSortCriterii

class ServiceClienti:

    def __init__(self, validator_clienti, repo_clienti):
        """
        functia initializeaza atributele obiectului curent cu obiectele primite ca parametrii
        :param validator_clienti: obiect de tipul ValidatorClienti
        :param repo_clienti: obiect de tipul RepoClienti
        """
        self.__validator_clienti = validator_clienti
        self.__repo_clienti = repo_clienti

    def adauga_client(self, id_client, nume, cnp):
        """
        functia creaza un client cu datele primite ca parametru, pe care-l valideaza, iar mai apoi il adauga
        in repo-ul de clienti
        :param id_client: integer
        :param nume: string
        :param cnp: integer
        :return: -
        """
        client = Client(id_client, nume, cnp)
        self.__validator_clienti.valideaza(client)
        self.__repo_clienti.adauga_client(client)


    def sterge_client_dupa_id(self, id_client):
        """
        functia sterge clientul cu id-ul primit ca parametru din repo-ul de clienti
        :param id_client: integer
        :return: -
        """
        self.__repo_clienti.sterge_client_dupa_id(id_client)

    def modifica_client_dupa_id(self, id_client, nou_nume, nou_cnp):
        """
        functia modifica in repo-clienti clientul cu id-ul primit ca parametru cu noile date primite de la utilizator
        :param id_client: integer
        :param nou_id_client: integer
        :param nou_nume: string
        :param nou_cnp: integer
        :return: -
        """
        client = Client(id_client, nou_nume, nou_cnp)
        self.__validator_clienti.valideaza(client)
        client_curent = self.__repo_clienti.cauta_client_dupa_id(id_client)
        self.__repo_clienti.sterge_client_dupa_id(id_client)
        self.__repo_clienti.adauga_client(client)


    def cauta_clienti_dupa_nume(self, nume):
        """
        functia cauta in lista de clienti clientii cu numele primit ca si parametru
        :param nume: string
        :return: lista de clienti care au numele precizat
        """
        return self.__repo_clienti.cauta_clienti_dupa_nume(nume)


    def ordoneaza_clienti_dupa_carti_inch(self):
        """
        functia ordoneaza descrescator clientii care au inchiriat carti dupa numarul de carti inchiriate
        :return:lista cu clientii ordonati
        """
        clienti_pt_ord = self.__repo_clienti.cauta_clienti_cu_carti_inch()
        clienti_ord = quickSort(clienti_pt_ord, Client.get_nr_carti_inch, True)
        """
        nr_clienti = len(clienti_pt_ord)
        for i in range(0, nr_clienti - 1):
            for j in range(i + 1, nr_clienti):
                if clienti_pt_ord[i].get_nr_carti_inch() < clienti_pt_ord[j].get_nr_carti_inch():
                    clienti_pt_ord[i], clienti_pt_ord[j] = clienti_pt_ord[j], clienti_pt_ord[i]
        """
        return clienti_ord[:]


    def ordoneaza_clienti_dupa_nume(self):
        """
        functia ordoneaza alfabetic clientii care au inchiriat carti dupa numele lor
        :return: lista cu clientii ordonati
        """
        clienti_pt_ord = self.__repo_clienti.cauta_clienti_cu_carti_inch()
        n = len(clienti_pt_ord)
        #clienti_ord = quickSort(clienti_pt_ord, key=Client.get_nume_client)
        clienti_ord = GnomeSortCriterii(clienti_pt_ord, n)
        """
        nr_clienti = len(clienti_pt_ord)
        for i in range(0, nr_clienti - 1):
            for j in range(i + 1, nr_clienti):
                if clienti_pt_ord[i].get_nume_client() > clienti_pt_ord[j].get_nume_client():
                    clienti_pt_ord[i], clienti_pt_ord[j] = clienti_pt_ord[j], clienti_pt_ord[i]
        """
        return clienti_ord[:]

    def cei_mai_activi_clienti(self):
        """
        functia determina cei mai activi 20% dintre clienti
        :return: lista cu cei mai activi 20% dintre clienti
        """
        clienti_pt_ord = self.__repo_clienti.cauta_clienti_cu_carti_inch()
        nr_clienti = len(clienti_pt_ord)
        clienti_ord = GnomeSort(clienti_pt_ord, nr_clienti, Client.get_nr_carti_inch, True)
        """
        for i in range(0, nr_clienti - 1):
            for j in range(i + 1, nr_clienti):
                if clienti_pt_ord[i].get_nr_carti_inch() < clienti_pt_ord[j].get_nr_carti_inch():
                    clienti_pt_ord[i], clienti_pt_ord[j] = clienti_pt_ord[j], clienti_pt_ord[i]
        """
        capat_lista = nr_clienti // 5
        return clienti_pt_ord[:capat_lista]

    def numar_inch_clienti_cu_litera(self, litera):
        """
        functia gaseste inchirierile totale ale clientilor a caror nume incepe cu litera litera
        :param litera: string
        :return: suma inchirierilor tuturor clientilor care incep cu litera litera
        """
        s = 0
        clienti_cu_litera = self.__repo_clienti.cauta_clienti_care_incep_cu_litera(litera)
        for client in clienti_cu_litera:
            s += client.get_nr_carti_inch()
        return s

    def clienti_cu_numele(self, list, nume):
        if list == []:
            return []
        if list[0].get_nume_client() == nume:
            return [list[0]] + self.clienti_cu_numele(list[1:], nume)
        else:
            return self.clienti_cu_numele(list[1:], nume)

    def get_all_clienti(self):
        """
        functie returneaza lista de clienti (atribut al obiectului curent)
        :return: repo-ul de clienti (lista)
        """
        return self.__repo_clienti.get_all()
