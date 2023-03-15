class Carte:
    def __init__(self, id_carte, titlu, descriere, autor):
        """
        functia initializeaza atributele obiecutlui de tip Carte cu datele primite ca parametri
        :param id_carte: integer
        :param titlu: string
        :param descriere: string
        :param autor: string
        """
        self.__id_carte = id_carte
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor
        self.__nr_inchirieri = 0

    def creste_numar_inchirieri_carte(self):
        """
        functia creste numarul de inchirieri ale cartii curente cu o unitate
        :return: -
        """
        self.__nr_inchirieri = self.__nr_inchirieri + 1

    def scade_numar_inchirieri_carte(self):
        """
        functia creste numarul de inchirieri ale cartii curente cu o unitate
        :return: -
        """
        self.__nr_inchirieri = self.__nr_inchirieri - 1

    def get_nr_inch_carte(self):
        """
        functia returneaza numarul de inchirieri ale cartii curente
        :return: -
        """
        return self.__nr_inchirieri

    def get_id_carte(self):
        """
        functia obtine id-ul cartii pe care il returneaza
        :return: id-ul obiectului curent
        """
        return self.__id_carte

    def get_titlu_carte(self):
        """
        functia obtine titlul obiectului curent pe care-l returneaza
        :return: titlul obiectului curent
        """
        return self.__titlu

    def get_descriere_carte(self):
        """
        functia obtine descrierea obiectului curent pe care o returneaza
        :return: descrierea obiectului curent
        """
        return self.__descriere

    def get_autor_carte(self):
        """
        functia obtine autorul obiectului curent pe care-l returneaza
        :return: autorul obiectului curent
        """
        return self.__autor

    def set_nr_inch(self, nr_inch):
        """
        functia seteaza numarul de inchirieri ale cartii
        :param nr_inch:
        :return:
        """
        self.__nr_inchirieri = nr_inch

    def __eq__(self, other):
        """
        functia verifica daca obiectul curent si obiectul other de tip carte sunt egale ca si id
        :param other: obiect de tipul Carte
        :return: True - daca obiectele comparate au acelasi id
                 False - altfel
        """
        return self.__id_carte == other.__id_carte

    def __str__(self):
        """
        functia converteste atributele obietului curent la string si le returneaza
        :return: string - atributele obiectului curent enuntate unul dupa celalalt
        """
        return f"{self.__id_carte},{self.__titlu},{self.__descriere},{self.__autor},{self.__nr_inchirieri}"