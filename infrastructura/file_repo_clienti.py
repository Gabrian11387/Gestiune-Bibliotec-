from domeniu.client import Client
from infrastructura.repo_clienti import RepoClienti

class FileRepoClienti(RepoClienti):
    def __init__(self, calea_catre_fisier):
        RepoClienti.__init__(self)
        self.__calea_catre_fisier = calea_catre_fisier

    def __read_all_from_file(self):
        with open(self.__calea_catre_fisier, "r") as f:
            lines = f.readlines()
            self._clienti.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_client = int(parts[0])
                    nume_client = parts[1]
                    cnp_client = int(parts[2])
                    nr_inch = int(parts[3])
                    client = Client(id_client, nume_client, cnp_client)
                    client.set_nr_inch(nr_inch)
                    self._clienti.append(client)

    def __write__all_to_file(self):
        with open(self.__calea_catre_fisier, "w") as f:
            for client in self._clienti:
                f.write(str(client) + "\n")

    def adauga_client(self, client):
        self.__read_all_from_file()
        RepoClienti.adauga_client(self, client)
        self.__write__all_to_file()

    def sterge_client_dupa_id(self, id_client):
        self.__read_all_from_file()
        RepoClienti.sterge_client_dupa_id(self, id_client)
        self.__write__all_to_file()

    def cauta_clienti_dupa_nume(self, nume):
        self.__read_all_from_file()
        return RepoClienti.cauta_clienti_dupa_nume(self, nume)

    def cauta_clienti_cu_carti_inch(self):
        self.__read_all_from_file()
        return RepoClienti.cauta_clienti_cu_carti_inch(self)

    def cauta_client_dupa_id(self, id_client):
        self.__read_all_from_file()
        return RepoClienti.cauta_client_dupa_id(self, id_client)

    def cauta_clienti_care_incep_cu_litera(self, litera):
        self.__read_all_from_file()
        return RepoClienti.cauta_clienti_care_incep_cu_litera(self, litera)

    def modifica_client(self, id_client, client):
        self.__read_all_from_file()
        RepoClienti.modifica_client(self, id_client, client)
        self.__write__all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepoClienti.get_all(self)

    def __len__(self):
        self.__read_all_from_file()
        return len(self._clienti)
        #RepoClienti.__len__(self)
