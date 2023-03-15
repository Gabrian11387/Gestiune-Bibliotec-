from domeniu.carti import Carte
from infrastructura.repo_carti import RepoCarti


class FileRepoCarti(RepoCarti):
    def __init__(self, calea_catre_fisier):
        RepoCarti.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._carti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_carte = int(parts[0])
                    titlu_carte = parts[1]
                    descriere_carte = parts[2]
                    autor_carte = parts[3]
                    nr_inch = int(parts[4])
                    carte = Carte(id_carte, titlu_carte, descriere_carte, autor_carte)
                    carte.set_nr_inch(nr_inch)
                    self._carti.append(carte)

    def __write_all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for carte in self._carti:
                f.write(str(carte) + "\n")

    def adauga_carte(self, carte):
        self.__read_all_from_file()
        RepoCarti.adauga_carte(self, carte)
        self.__write_all_to_file()

    def sterge_carte_dupa_id(self, id_carte):
        self.__read_all_from_file()
        RepoCarti.sterge_carte_dupa_id(self, id_carte)
        self.__write_all_to_file()

    def cauta_carti_dupa_autor(self, autor):
        self.__read_all_from_file()
        return RepoCarti.cauta_carti_dupa_autor(self, autor)

    def cauta_carte_dupa_id(self, id_carte):
        self.__read_all_from_file()
        return RepoCarti.cauta_carte_dupa_id(self, id_carte)

    def cauta_carti_cu_inch(self):
        self.__read_all_from_file()
        return RepoCarti.cauta_carti_cu_inch(self)

    def get_all(self):
        self.__read_all_from_file()
        return RepoCarti.get_all(self)

    def __len__(self):
        self.__read_all_from_file()
        return RepoCarti.__len__(self)