class Inchiriere:

    def __init__(self, id_inchiriere, id_client, nume_client, id_carte, titlu_carte):
        """
        functia initializeaza atributele obiecutlui de tip Inchiriere cu datele primite ca parametri
        :param id_inchiriere: integer
        :param id_client: integer
        :param nume_client: string
        :param id_carte: integer
        :param titlu_carte: string
        """
        self.__id_inchiriere = id_inchiriere
        self.__id_client = id_client
        self.__nume_client = nume_client
        self.__id_carte = id_carte
        self.__titlu_carte = titlu_carte

    def get_id_inchiriere(self):
        """
        functia returneaza id-ul inchirierii
        :return: id-ul inchirierii
        """
        return self.__id_inchiriere

    def get_id_client_inchiriere(self):
        """
        functia returneaza id-ul clientului din inchirierea curenta
        :return: id-ul clientului din inchirierea curenta
        """
        return self.__id_client

    def get_id_carte_inchiriere(self):
        """
        functia returneaza id-ul cartii din inchirierea curenta
        :return: id-ul cartii din inchirierea curenta
        """
        return self.__id_carte

    def get_nume_client_inchiriere(self):
        """
        functia returneaza numele clientului din inchirierea curenta
        :return: numele clientului din inchirierea curenta
        """
        return self.__nume_client

    def get_titlu_carte_inchiriere(self):
        """
        functia returneaza titlul cartii din inchirierea curenta
        :return: titlul cartii din inchirierea curenta
        """
        return self.__titlu_carte

    def __eq__(self, other):
        """
        functia verifica daca inchirierea curenta este egala cu inchirierea transmisa ca parametru
        :param other: obiect de tipul Inchiriere
        :return: True - daca id-urile inchirierilor sunt egale
                 False - daca id-urile inchirierilor nu sunt egale
        """
        return self.__id_inchiriere == other.__id_inchiriere

    def __str__(self):
        """
        functia returneaza atributele inchirierii sub forma de string
        :return: string care contine atributele
        """
        return f"{self.__id_inchiriere},{self.__id_client},{self.__nume_client},{self.__id_carte},{self.__titlu_carte}"