class Client:

    def __init__(self, id_client, nume, cnp):
        """
        functia initializeaza atributele obiecutlui de tip Carte cu datele primite ca parametri
        :param id_client: integer
        :param nume: string
        :param cnp: integer
        """
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp
        self.__nr_carti_inch = 0

    def get_id_client(self):
        """
        functia obtine id-ul  pe care-l returneaza
        :return: id-ul cartii
        """
        return self.__id_client

    def get_nume_client(self):
        """
        functia obtine numele clientului pe care-l returneaza
        :return: numele clientului
        """
        return self.__nume

    def get_cnp_client(self):
        """
        functia obtine cnp-ul clientului pe care-l returneaza
        :return: cnp-ul clientului
        """
        return self.__cnp

    def get_nr_carti_inch(self):
        """
        functia returneaza numarul de carti inchiriate ale clientului
        :return: numarul de carti inchiriate ale clientului
        """
        return self.__nr_carti_inch

    def set_nume_client(self, nume):
        """
        functia seteaza numele clientului cu numele nume
        :param nume: string
        :return: -
        """
        self.__nume = nume

    def set_cnp_client(self, cnp):
        """
        functia seteza cnp-ul clientului cu cnp-ul cnp
        :param cnp: integer
        :return: -
        """
        self.__cnp = cnp

    def creste_numar_inch(self):
        """
        functia creste numarul de inchirieri ale clientului cu 1
        :return: -
        """
        self.__nr_carti_inch += 1

    def scade_numar_inch(self):
        """
        funcita scade numarul de inchirieri ale clientului cu 1
        :return:
        """
        self.__nr_carti_inch -= 1

    def set_nr_inch(self, nr_inch):
        self.__nr_carti_inch = nr_inch

    def __eq__(self, other):
        """
        functia verifica daca 2 clienti sunt egali folosindu-se de id-ul lor
        :param other: obiect de tipul Client
        :return: -
        """
        return self.__id_client == other.__id_client

    def __str__(self):
        """
        functia converteste atributele clientului la string
        :return: atributele clientului sub forma de string
        """
        return f"{self.__id_client},{self.__nume},{self.__cnp},{self.__nr_carti_inch}"

    def __lt__(self, other):
        return self.__nume < other.get_nume_client()

    def __ge__(self, other):
        return self.__nume >= other.get_nume_client()