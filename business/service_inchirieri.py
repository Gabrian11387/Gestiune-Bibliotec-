from domeniu.inchiriere import Inchiriere

class ServiceInchirieri:
    def __init__(self, validator_inchirieri, repo_inchirieri, repo_clienti, repo_carti):
        """
        functia initializeaza atributele obiectului curent cu parametrii primti
        :param validator_inchirieri: ValidatorInchirieri
        :param repo_inchirieri: RepoInchirieri
        :param repo_clienti: RepoClienti
        :param repo_carti: RepoCarti
        """
        self.__validator_inchirieri = validator_inchirieri
        self.__repo_inchirieri = repo_inchirieri
        self.__repo_clienti = repo_clienti
        self.__repo_carti = repo_carti

    def adauga_inchiriere(self, id_inchiriere, id_client, nume_client, id_carte, titlu_carte):
        """
        functia adauga o inchiriere in lista de inchirieri dupa ce aceasta a fost validata. Totodata, functia actualizeaza
        numarul de inchirieri pentru clientul si cartea regasiti in inchiriere
        :param id_inchiriere: integer
        :param id_client: integer
        :param nume_client: string
        :param id_carte: integer
        :param titlu_carte: string
        :return: -
        """
        inchiriere = Inchiriere(id_inchiriere, id_client, nume_client, id_carte, titlu_carte)
        self.__validator_inchirieri.valideaza(inchiriere)
        carte_cu_inch = self.__repo_carti.cauta_carte_dupa_id(id_carte)
        carte_cu_inch.creste_numar_inchirieri_carte()
        self.__repo_carti.sterge_carte_dupa_id(id_carte)
        self.__repo_carti.adauga_carte(carte_cu_inch)
        client_cu_inch = self.__repo_clienti.cauta_client_dupa_id(id_client)
        client_cu_inch.creste_numar_inch()
        self.__repo_clienti.sterge_client_dupa_id(id_client)
        self.__repo_clienti.adauga_client(client_cu_inch)
        self.__repo_inchirieri.adauga_inchiriere(inchiriere)

    def sterge_inchiriere(self, id_inchiriere, id_client, nume_client, id_carte, titlu_carte):
        """
        functia sterge inchirierea cu datele specificate dupa ce o valideaza pe aceasta. Daca inchirierea nu este valida
        va ridica o eroare de tipul ValidationError, iar daca inchirierea nu exista in lista de inchirieri va ridica o eroare
        de tipul RepoError. Totdata, functia scade numarul de inchirieri ale clientului si cartii regasite in inchiriere
        :param id_inchiriere: integer
        :param id_client: integer
        :param nume_client: string
        :param id_carte: integer
        :param titlu_carte: string
        :return: -
        """
        inchiriere = Inchiriere(id_inchiriere, id_client, nume_client, id_carte, titlu_carte)
        self.__validator_inchirieri.valideaza(inchiriere)
        self.__repo_clienti.cauta_client_dupa_id(id_client).scade_numar_inch()
        self.__repo_carti.cauta_carte_dupa_id(id_carte).scade_numar_inchirieri_carte()
        self.__repo_inchirieri.sterge_inchiriere_dupa_id(id_inchiriere)

    def sterge_inchirieri_cu_cartea(self, id_carte):
        """
        functia sterge inchirierile care contin cartea identificabila prin id_carte
        :param id_carte: integer
        :return: -
        """
        self.__repo_inchirieri.sterge_inchirieri_cu_cartea(id_carte)

    def sterge_inchiriere_cu_clientul(self, id_client):
        """
        functia sterge inchirierile care contin clientul idenificabil prin id_client
        :param id_client: integer
        :return: -
        """
        self.__repo_inchirieri.sterge_inchirieri_cu_clientul(id_client)

    def get_all_inchirieri(self):
        """
        functia returneaza lista de inchirieri
        :return: lista de inchirieri
        """
        return self.__repo_inchirieri.get_all()
