from infrastructura.repo_inchirieri import RepoInchirieri
from domeniu.inchiriere import Inchiriere


class FileRepoInchirieri(RepoInchirieri):
    def __init__(self, calea_catre_fisier):
        RepoInchirieri.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._inchirieri.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_inch = int(parts[0])
                    id_client = int(parts[1])
                    nume_client = parts[2]
                    id_carte = int(parts[3])
                    titlu_carte = parts[4]
                    inchiriere = Inchiriere(id_inch, id_client, nume_client, id_carte, titlu_carte)
                    self._inchirieri.append(inchiriere)

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for inch in self._inchirieri:
                f.write(str(inch) + "\n")

    def adauga_inchiriere(self, inchiriere):
        self.__read_all_from_file()
        RepoInchirieri.adauga_inchiriere(self, inchiriere)
        self.__write_all_to_file()

    def sterge_inchirieri_cu_cartea(self, id_carte):
        self.__read_all_from_file()
        RepoInchirieri.sterge_inchirieri_cu_cartea(self, id_carte)
        self.__write_all_to_file()

    def sterge_inchirieri_cu_clientul(self, id_client):
        self.__read_all_from_file()
        RepoInchirieri.sterge_inchirieri_cu_clientul(self, id_client)
        self.__write_all_to_file()

    def sterge_inchiriere_dupa_id(self, id_inchiriere):
        self.__read_all_from_file()
        RepoInchirieri.sterge_inchiriere_dupa_id(self, id_inchiriere)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepoInchirieri.get_all(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoInchirieri.__len__(self)