from erori.Repo_error import RepoError


class RepoClienti:

    def __init__(self):
        self._clienti = []

    def adauga_client(self, client):
        """
        functia adauga un client nou in lista de clienti, iar daca clientul pe care doreste sa il adauge
        exista deja, va ridica eroare de tip RepoError: "Client existent!"
        :param client: obiect de clasa client
        :return: -
        """
        for el in self._clienti:
            if el.get_id_client() == client.get_id_client():
                raise RepoError("Client existent!")
        self._clienti.append(client)


    def sterge_client_dupa_id(self, id_client):
        """
        functia sterge clientul cu id-ul primit ca parametru din lista de clienti, iar daca acest client nu exista
        va ridica o eroare de tipul RepoError: "Client inexsitent!"
        :param id_client: integer
        :return: -
        """
        for el in self._clienti:
            if el.get_id_client() == id_client:
                self._clienti.remove(el)
                return
        raise RepoError("Client inexistent!")


    def cauta_clienti_dupa_nume(self, nume):
        """
        functia cauta in lista de clienti clientii cu numele primit ca si parametru
        :param nume: string
        :return: lista de clienti care au numele precizat
        """
        clienti_buni = []
        for client in self._clienti:
            if client.get_nume_client() == nume:
                clienti_buni.append(client)
        return clienti_buni[:]

    def cauta_clienti_cu_carti_inch(self):
        """
        functia cauta clientii care au cel putin o carte inchiriata
        :return: lista de clienti cu cel putin o carte inchiriata
        """
        clienti_buni = []
        for client in self._clienti:
            if client.get_nr_carti_inch() > 0:
                clienti_buni.append(client)
        return clienti_buni[:]

    def cauta_client_dupa_id(self, id_client):
        """
        fucntia cauta in lista de clienti, clientul cu id-ul primti ca si parametru, iar daca acest client nu este gasit,
        va ridica eroare de tipul RepoError: "Client inexsitent!"
        :param id_client: integer
        :return: referinta la cleintul cu id-ul cautat
        Complexitate: best-case: O(1) - clientul pe care il cautam se afla chiar la inceputul listei
                      worst-case: O(n) - clientul nu se regaseste in lista de clienti
                      average-case: O(n) - clientul se afla in lista la o oarecare pozitie => n/k pasi, k - natural => O(n)
        """
        for client in self._clienti:
            if client.get_id_client() == id_client:
                return client
        raise RepoError("Client inexistent!")


    def cauta_clienti_care_incep_cu_litera(self, litera):
        """
        functia gaseste clientii a caror nume incepe cu litera litera
        :param litera: string
        :return: lista de clienti a caror nume incep cu litera litera
        """
        clienti_buni = []
        for client in self._clienti:
            if client.get_nume_client().startswith(litera):
                clienti_buni.append(client)
        return clienti_buni[:]

    def modifica_client(self, id_client, client):
        """
        functia modifica clientul cu id-ul id_client cu datele continute de obiectul client
        :param id_client: integer
        :param client: Client
        :return: -
        """
        for cl in self._clienti:
            if cl.get_id_client() == id_client:
                cl.creste_numar_inch()
                return
        raise RepoError("Client inexistent!")

    def get_all(self):
        """
        functia returneaza lista clientilor
        :return: lista de clienti (lista)
        """
        return self._clienti[:]

    def __len__(self):
        """
        funcitia returneaza numarul de clienti din lista
        :return: numarul de clienti din lista (integer)
        """
        return len(self._clienti)