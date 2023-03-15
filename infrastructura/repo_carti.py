from erori.Repo_error import RepoError

class RepoCarti:

    def __init__(self):
        self._carti = []

    def adauga_carte(self, carte):
        """
        functia adauga cartea primita ca parametru in lista de carti, iar daca aceasta care exista deja in lista,
        va ridica o eroare de tipul RepoError: "Carte existenta!"
        :param carte: obiect de tipul Carte
        :return: -
        """
        for el in self._carti:
            if el.get_id_carte() == carte.get_id_carte():
                raise RepoError("Carte existenta!")
        self._carti.append(carte)

    def sterge_carte_dupa_id(self, id_carte):
        """
        functia sterge cartea cu id-ul primit ca parametru din lista de carti, iar in cazul in care aceasta carte nu
        exista, va ridica eroare de tip RepoError: "Carte inesitenta!"
        :param id_carte: integer
        :return: -
        """
        for el in self._carti:
            if el.get_id_carte() == id_carte:
                self._carti.remove(el)
                return
        raise RepoError("Carte inexistenta!")

    def cauta_carti_dupa_autor(self, autor):
        """
        functia cauta in lista de carti, cartile care au autorul precizat
        :param autor: string
        :return: lista de carti cu autorul precizat
        """
        carti_bune = []
        for carte in self._carti:
            if carte.get_autor_carte().strip() == autor:
                carti_bune.append(carte)
        return carti_bune[:]

    def cauta_carte_dupa_id(self, id_carte):
        """
        functia cauta cartea cu ide-ul precizat, iar in cazul in care aceasta nu exista,
        va ridica eroarea de tipul RepoError: "Carte inexistenta!"
        :param id_carte: integer
        :return: referinta la cartea cu id-ul precizat
        """
        for carte in self._carti:
            if carte.get_id_carte() == id_carte:
                return carte
        raise RepoError("Carte inexistenta!")

    def cauta_carti_cu_inch(self):
        """
        functia cauta carile care au cel putin o inchiriere
        :return: lista de carti cu cel putin o inchiriere
        """
        carti_bune = []
        for carte in self._carti:
            if carte.get_nr_inch_carte() > 0:
                carti_bune.append(carte)
        return carti_bune[:]

    def get_all(self):
        """
        functia returneaza lista de carti
        :return: lista de carti (lista)
        """
        return self._carti[:]

    def __len__(self):
        """
        functia returneaza numarul de carti din lista de carti
        :return: numarul de carti (interger)
        """
        return len(self._carti)