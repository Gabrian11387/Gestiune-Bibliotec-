from erori.Repo_error import RepoError


class RepoInchirieri:
    def __init__(self):
        self._inchirieri = []

    def adauga_inchiriere(self, inchiriere):
        """
        functia adauga inchirierea in lista de inchirieri daca aceasta nu exista deja,
        iar in caz contrar va ridica o eroare e tipul RepoError: "Inchiriere existenta!"
        :param inchiriere: obiect de tipul Inchiriere
        :return: -
        """
        for inch in self._inchirieri:
            if inch.get_id_inchiriere() == inchiriere.get_id_inchiriere():
                raise RepoError("Inchiriere existenta!")
        self._inchirieri.append(inchiriere)

    def sterge_inchirieri_cu_cartea(self, id_carte):
        """
        functia sterge inchirierile care contin cartea identificabila prin id-ul id_carte in cazul in care aceasta apare in lista
        de inchirieri, altfel va ridica eroarea de tipul RepoError:"Carte nexistenta printre inchirieri!"
        :param id_carte: integer
        :return: -
        """
        for inch in self._inchirieri:
            if inch.get_id_carte_inchiriere() == id_carte:
                self._inchirieri.remove(inch)
                return
        raise RepoError("Carte nexistenta printre inchirieri!")

    def sterge_inchirieri_cu_clientul(self, id_client):
        """
        functia sterge inchirierile care contin clientul identificabil prin id-ul id_client in cazul in care aceasta apare in lista
        de inchirieri, altfel va ridica eroarea de tipul RepoError:"Client inexistent printre inchirieri!"
        :param id_client:
        :return: -
        """
        for inch in self._inchirieri:
            if inch.get_id_client_inchiriere() == id_client:
                self._inchirieri.remove(inch)
                return
        raise RepoError("Client inexistent printre inchirieri!")

    def sterge_inchiriere_dupa_id(self, id_inchiriere):
        """
        functia sterge inchirierea identificabila prin id-ul id_inchiriere, iar in cazul in care aceasta nu exista,
        va ridica eroarea de tipul RepoError: "Inchiriere inexistenta!"
        :param id_inchiriere: integer
        :return: -
        """
        for inch in self._inchirieri:
            if inch.get_id_inchiriere() == id_inchiriere:
                self._inchirieri.remove(inch)
                return
        raise RepoError("Inchiriere inexistenta!")

    def get_all(self):
        """
        functia ofera lista cu toate inchirierile
        :return: lista de inchirieri
        """
        return self._inchirieri[:]

    def __len__(self):
        """
        functia afla numarul de inchirieri
        :return: numarul de inchirieri
        """
        return len(self._inchirieri)