from domeniu.carti import Carte
import random
import string

class ServiceCarti:

    def __init__(self, validator_carti, repo_carti):
        """
        functia initializeaza atributele obiectului curent cu parametrii primti
        :param validator_carti: obiect de tipul ValidatorCarte
        :param repo_carti: obiect de tipul RepoCarti
        """
        self.__validator_carti = validator_carti
        self.__repo_carti = repo_carti

    def adauga_carte(self, id_carte, titlu_carte, descriere_carte, autor_carte):
        """
        functia creeaza o carte cu datele primite, pe care o valideaza si mai apoi o adauga in repo-ul de carti
        :param id_carte: integer
        :param titlu_carte: string
        :param descriere_carte: string
        :param autor_carte: string
        :return: -
        """
        carte = Carte(id_carte, titlu_carte, descriere_carte, autor_carte)
        self.__validator_carti.valideaza(carte)
        self.__repo_carti.adauga_carte(carte)

    def cauta_carti_dupa_autor(self, autor):
        """
        functia cauta cartile care au autorul autor
        :param autor: string
        :return: lista de carti cu autorul autor
        """
        return self.__repo_carti.cauta_carti_dupa_autor(autor)

    def cauta_carti_cu_autorul(self, list, autor):
        if list == []:
            return []
        if list[0].get_autor_carte() == autor:
            return [list[0]] + self.cauta_carti_cu_autorul(list[1:], autor)
        else:
            return self.cauta_carti_cu_autorul(list[1:], autor)

    def get_all_carti(self):
        """
        functia returneaza toate cartile din repo-ul de carti
        :return: repo-ul de carti (lista)
        """
        return self.__repo_carti.get_all()

    def sterge_carte_dupa_id(self, id_carte):
        """
        functia sterge din repo-carti cartea cu id-ul primit ca parametru
        :param id_carte:integer
        :return:-
        """
        self.__repo_carti.sterge_carte_dupa_id(id_carte)


    def ordoneaza_carti_dupa_nr_inchirieri(self):
        """
        functia ordoneaza descrescator cartile care au cel putin o inchiriere dupa numarul lor de inchirieri
        :return: lista de carti ordonata
        """
        carti_pt_ord = self.__repo_carti.cauta_carti_cu_inch()
        nr_carti = len(carti_pt_ord)
        for i in range(0, nr_carti - 1):
            for j in range(i + 1, nr_carti):
                if carti_pt_ord[i].get_nr_inch_carte() < carti_pt_ord[j].get_nr_inch_carte():
                    carti_pt_ord[i], carti_pt_ord[j] = carti_pt_ord[j], carti_pt_ord[i]
        return carti_pt_ord[:]




