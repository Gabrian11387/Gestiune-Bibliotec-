import unittest

from business.service_carti import ServiceCarti
from business.service_clienti import ServiceClienti
from business.service_inchirieri import ServiceInchirieri
from domeniu.carti import Carte
from domeniu.client import Client
from domeniu.inchiriere import Inchiriere
from erori.Repo_error import RepoError
from erori.validation_error import ValidationError
from infrastructura.file_repo_carti import FileRepoCarti
from infrastructura.file_repo_clienti import FileRepoClienti
from infrastructura.file_repo_inchirieri import FileRepoInchirieri
from infrastructura.repo_carti import RepoCarti
from infrastructura.repo_clienti import RepoClienti
from infrastructura.repo_inchirieri import RepoInchirieri
from validare.validator_carte import ValidatorCarte
from validare.validator_client import ValidatorClient
from validare.validator_inchiriere import ValidatorInchiriere


class Teste(unittest.TestCase):

    def ruleaza_toate_testele(self):
        self.teste_domeniu_client()
        print("Teste domeniu client rulate cu succes!")
        self.teste_domeniu_carte()
        print("Teste domeniu carte rulate cu succes!")
        self.teste_domeniu_inchirieri()
        print("Teste domeniu inchirieri rulate cu succes!")
        self.teste_repo_clienti()
        print("Teste repo clienti rulate cu succes!")
        self.teste_repo_carti()
        print("Teste repo cati rulate cu succes!")
        self.teste_repo_inchirieri()
        print("Teste repo inchirieri rulate cu succes!")
        self.teste_service_clienti()
        print("Teste service clienti rulate cu succes!")
        self.teste_service_carti()
        print("Teste service carti rulate cu succes!")
        self.teste_service_inchirieri()
        print("Teste service inchirieri rulate cu succes!")
        self.teste_validare_client()
        print("Teste validare client rulate cu succes!")
        self.teste_validare_carte()
        print("Teste validare carte rulate cu succes!")
        self.teste_validare_inchiriere()
        print("Teste validare inchiriere rulate cu succes!")
        self.teste_black_box_test_adauga_client_repo_clienti()
        print("Teste black-box client repo adauga client rulate cu succes!")
        self.teste_file_repo_clienti()
        print("Teste file repo clienti rulate cu succes!")
        self.teste_file_repo_carti()
        print("Teste file repo carti rulate cu succes!")
        self.teste_file_repo_inchirieri()
        print("Teste file repo inchirieri rulate cu succes!")

    def goleste_fisier(self, cale_fisier):
        with open(cale_fisier, "w") as f:
            pass

    def teste_domeniu_client(self):
        client = Client(1, "Mihai", 6031009060011)
        self.assertTrue(client.get_id_client() == 1)
        self.assertTrue(client.get_nume_client() == "Mihai")
        self.assertTrue(client.get_cnp_client() == 6031009060011)
        self.assertTrue(client.get_nr_carti_inch() == 0)
        client.set_cnp_client(5031009060011)
        self.assertTrue(client.get_cnp_client() == 5031009060011)
        client.set_nume_client("Alex")
        self.assertTrue(client.get_nume_client() == "Alex")
        client.creste_numar_inch()
        self.assertTrue(client.get_nr_carti_inch() == 1)
        client.scade_numar_inch()
        self.assertTrue(client.get_nr_carti_inch() == 0)
        client_egal = Client(1, "Gabi", 5031001060011)
        self.assertTrue(client == client_egal)

    def teste_domeniu_carte(self):
        carte = Carte(2, "Enigma", "interesanta", "Sadoveanu")
        self.assertTrue(carte.get_id_carte() == 2)
        self.assertTrue(carte.get_titlu_carte() == "Enigma")
        self.assertTrue(carte.get_descriere_carte() == "interesanta")
        self.assertTrue(carte.get_autor_carte() == "Sadoveanu")
        self.assertTrue(carte.get_nr_inch_carte() == 0)
        carte.creste_numar_inchirieri_carte()
        self.assertTrue(carte.get_nr_inch_carte() == 1)
        carte.scade_numar_inchirieri_carte()
        self.assertTrue(carte.get_nr_inch_carte() == 0)
        carte_egala = Carte(2, "Enigma_noua", "neinteresanta", "Mihail")
        self.assertTrue(carte == carte_egala)

    def teste_domeniu_inchirieri(self):
        inchiriere = Inchiriere(1, 1, "Alex", 1, "Enigma")
        self.assertTrue(inchiriere.get_id_inchiriere() == 1)
        self.assertTrue(inchiriere.get_id_carte_inchiriere() == 1)
        self.assertTrue(inchiriere.get_titlu_carte_inchiriere() == "Enigma")
        self.assertTrue(inchiriere.get_nume_client_inchiriere() == "Alex")
        inch_egala = Inchiriere(1, 2, "Mihai", 2, "Ion")
        self.assertTrue(inch_egala == inchiriere)
        self.assertTrue(inchiriere.get_nume_client_inchiriere() == "Alex")
        self.assertTrue(inchiriere.get_titlu_carte_inchiriere() == "Enigma")

    def teste_repo_clienti(self):
        repo_clienti = RepoClienti()
        self.assertTrue(repo_clienti.get_all() == [])
        self.assertTrue(len(repo_clienti) == 0)
        client = Client(1, "Alex", 10)
        repo_clienti.adauga_client(client)
        self.assertTrue(len(repo_clienti) == 1)
        id_client_pt_sterge = 1
        repo_clienti.sterge_client_dupa_id(id_client_pt_sterge)
        self.assertTrue(len(repo_clienti) == 0)
        repo_clienti.adauga_client(client)
        self.assertTrue(len(repo_clienti) == 1)
        acelasi_client = Client(1, "Gabi", 15)
        self.assertRaises(RepoError, repo_clienti.adauga_client, acelasi_client)
        id_gresit = 3
        self.assertRaises(RepoError, repo_clienti.sterge_client_dupa_id, id_gresit)
        nume = "Alex"
        self.assertTrue(repo_clienti.cauta_clienti_dupa_nume(nume) == [client])
        client.creste_numar_inch()
        self.assertTrue(repo_clienti.cauta_clienti_cu_carti_inch() == [client])
        id_de_cautat = 1
        self.assertTrue(repo_clienti.cauta_client_dupa_id(id_de_cautat) == client)
        id_gresit = 4
        self.assertRaises(RepoError, repo_clienti.cauta_client_dupa_id, id_gresit)

    def teste_repo_carti(self):
        repo_carti = RepoCarti()
        self.assertTrue(len(repo_carti) == 0)
        carte = Carte(2, "Enigma", "interesanta", "Sadoveanu")
        repo_carti.adauga_carte(carte)
        self.assertTrue(len(repo_carti) == 1)
        self.assertTrue(repo_carti.get_all() == [carte])
        aceeasi_carte = Carte(2, "Ion", "neinteresanta", "Rebreanu")
        self.assertRaises(RepoError, repo_carti.adauga_carte, aceeasi_carte)
        id_carte = 2
        repo_carti.sterge_carte_dupa_id(id_carte)
        self.assertTrue(len(repo_carti) == 0)
        repo_carti.adauga_carte(carte)
        id_gresit = 3
        self.assertRaises(RepoError, repo_carti.sterge_carte_dupa_id, id_gresit)
        autor = "Sadoveanu"
        carti_cu_autorul_autor = repo_carti.cauta_carti_dupa_autor(autor)
        self.assertTrue(carti_cu_autorul_autor == [carte])
        id_de_cautat = 2
        carte_cu_id_de_cautat = repo_carti.cauta_carte_dupa_id(id_de_cautat)
        self.assertTrue(carte_cu_id_de_cautat == carte)
        id_gresit = 3
        self.assertRaises(RepoError, repo_carti.cauta_carte_dupa_id, id_gresit)

    def teste_repo_inchirieri(self):
        repo_inch = RepoInchirieri()
        self.assertTrue(len(repo_inch) == 0)
        self.assertTrue(repo_inch.get_all() == [])
        inchiriere = Inchiriere(1, 1, "Alex", 1, "Enigma")
        repo_inch.adauga_inchiriere(inchiriere)
        self.assertTrue(repo_inch.get_all() == [inchiriere])
        acelasi_id = 1
        self.assertRaises(RepoError, repo_inch.adauga_inchiriere, Inchiriere(acelasi_id, 2, "Ion", 1, "Enigma"))
        id_carte = 1
        repo_inch.sterge_inchirieri_cu_cartea(id_carte)
        self.assertTrue(repo_inch.get_all() == [])
        repo_inch.adauga_inchiriere(inchiriere)
        id_carte_gresit = 2
        self.assertRaises(RepoError, repo_inch.sterge_inchirieri_cu_cartea, id_carte_gresit)
        id_client = 1
        repo_inch.sterge_inchirieri_cu_clientul(id_client)
        self.assertTrue(len(repo_inch) == 0)
        repo_inch.adauga_inchiriere(inchiriere)
        id_client_gresit = 5
        self.assertRaises(RepoError, repo_inch.sterge_inchirieri_cu_clientul, id_client_gresit)
        id_inchiriere = 1
        repo_inch.sterge_inchiriere_dupa_id(id_inchiriere)
        self.assertTrue(len(repo_inch) == 0)
        repo_inch.adauga_inchiriere(inchiriere)
        id_inchiriere_gresit = 8
        self.assertRaises(RepoError, repo_inch.sterge_inchiriere_dupa_id, id_inchiriere_gresit)

    def teste_service_clienti(self):
        repo_clienti = RepoClienti()
        validator_clienti = ValidatorClient()
        service_clienti = ServiceClienti(validator_clienti, repo_clienti)
        id_client = 1
        nume_client = "Alex"
        cnp_client = 10
        self.assertTrue(len(repo_clienti) == 0)
        service_clienti.adauga_client(id_client, nume_client, cnp_client)
        self.assertTrue(len(repo_clienti) == 1)
        lista_clienti = service_clienti.get_all_clienti()
        client = Client(id_client, nume_client, cnp_client)
        self.assertTrue(lista_clienti == [client])
        id_pt_sters = id_client
        service_clienti.sterge_client_dupa_id(id_pt_sters)
        self.assertTrue(len(repo_clienti) == 0)
        service_clienti.adauga_client(id_client, nume_client, cnp_client)
        self.assertTrue(len(repo_clienti) == 1)
        id_curent = 1
        nume_nou = "Gabi"
        cnp_nou = 15
        service_clienti.modifica_client_dupa_id(id_curent, nume_nou, cnp_nou)
        self.assertTrue(len(repo_clienti) == 1)
        client_nou = Client(id_curent, nume_nou, cnp_nou)
        self.assertTrue(service_clienti.get_all_clienti() == [client_nou])
        nume = "Gabi"
        clienti_cu_numele_nume = service_clienti.cauta_clienti_dupa_nume(nume)
        self.assertTrue(len(clienti_cu_numele_nume) == 1)
        service_clienti.adauga_client(2, "Mihai", 450)
        self.assertTrue(len(repo_clienti) == 2)
        client1 = client_nou
        client2 = Client(2, "Mihai", 450)
        self.assertTrue(service_clienti.get_all_clienti() == [client1, client2])
        for cli in service_clienti.get_all_clienti():
            cli.creste_numar_inch()
        clienti_cu_carti_inch_ordonati_dupa_nume = service_clienti.ordoneaza_clienti_dupa_nume()
        self.assertTrue(clienti_cu_carti_inch_ordonati_dupa_nume == [client1, client2])
        service_clienti.get_all_clienti()[0].creste_numar_inch()
        clienti_ord_dupa_cart_inch = service_clienti.ordoneaza_clienti_dupa_carti_inch()
        self.assertTrue(clienti_ord_dupa_cart_inch == [client1, client2])
        service_clienti.adauga_client(3, "Alex", 200)
        service_clienti.adauga_client(4, "Mircea", 500)
        service_clienti.adauga_client(5, "Traian", 600)
        self.assertTrue(len(repo_clienti) == 5)
        for cli in service_clienti.get_all_clienti():
            cli.creste_numar_inch()
        cei_mai_activi_clienti = service_clienti.cei_mai_activi_clienti()
        self.assertTrue(cei_mai_activi_clienti == [client1])

    def teste_service_carti(self):
        repo_carti = RepoCarti()
        validator_carti = ValidatorCarte()
        service_carti = ServiceCarti(validator_carti, repo_carti)
        id_carte = 1
        nume_carte = "Enigma"
        descriere_carte = "interesanta"
        autor_carte = "Sadoveanu"
        self.assertTrue(len(repo_carti) == 0)
        service_carti.adauga_carte(id_carte, nume_carte, descriere_carte, autor_carte)
        self.assertTrue(len(repo_carti) == 1)
        lista_carti = service_carti.get_all_carti()
        carte = Carte(id_carte, nume_carte, descriere_carte, autor_carte)
        self.assertTrue(lista_carti == [carte])
        service_carti.sterge_carte_dupa_id(id_carte)
        self.assertTrue(len(repo_carti) == 0)
        self.assertTrue(service_carti.get_all_carti() == [])
        service_carti.adauga_carte(id_carte, nume_carte, descriere_carte, autor_carte)
        autor = "Sadoveanu"
        carti_cu_autorul_autor = service_carti.cauta_carti_dupa_autor(autor)
        self.assertTrue(carti_cu_autorul_autor == [carte])
        service_carti.adauga_carte(2, "Bubico", "neinteresanta", "Eminescu")
        carte1 = Carte(id_carte, nume_carte, descriere_carte, autor_carte)
        carte2 = Carte(2, "Bubico", "neinteresanta", "Eminescu")
        for carte in service_carti.get_all_carti():
            carte.creste_numar_inchirieri_carte()
        service_carti.get_all_carti()[1].creste_numar_inchirieri_carte()
        carti_ord_dupa_nr_inch = service_carti.ordoneaza_carti_dupa_nr_inchirieri()
        self.assertTrue(carti_ord_dupa_nr_inch == [carte2, carte1])

    def teste_service_inchirieri(self):
        validator_inchirieri = ValidatorInchiriere()
        repo_inchirieri = RepoInchirieri()
        repo_clienti = RepoClienti()
        repo_carti = RepoCarti()
        service_inchirieri = ServiceInchirieri(validator_inchirieri, repo_inchirieri, repo_clienti, repo_carti)
        id_inch = 1
        id_client = 1
        nume_client = "Alex"
        id_carte = 1
        titlu_carte = "Enigma"
        repo_carti.adauga_carte(Carte(id_carte, titlu_carte, "interesanta", "Sadoveanu"))
        repo_clienti.adauga_client(Client(id_client, nume_client, 450))
        service_inchirieri.adauga_inchiriere(id_inch, id_client, nume_client, id_carte, titlu_carte)
        self.assertTrue(len(service_inchirieri.get_all_inchirieri()) == 1)
        service_inchirieri.sterge_inchiriere(id_inch, id_client, nume_client, id_carte, titlu_carte)
        self.assertTrue(len(service_inchirieri.get_all_inchirieri()) == 0)
        service_inchirieri.adauga_inchiriere(id_inch, id_client, nume_client, id_carte, titlu_carte)
        service_inchirieri.sterge_inchirieri_cu_cartea(id_carte)
        self.assertTrue(len(service_inchirieri.get_all_inchirieri()) == 0)
        service_inchirieri.adauga_inchiriere(id_inch, id_client, nume_client, id_carte, titlu_carte)
        service_inchirieri.sterge_inchiriere_cu_clientul(id_client)
        self.assertTrue(len(service_inchirieri.get_all_inchirieri()) == 0)

    def teste_validare_client(self):
        validator_client = ValidatorClient()
        id_gresit = -1
        nume_gresit = ""
        cnp_gresit = -2
        client_gresit = Client(id_gresit, nume_gresit, cnp_gresit)
        self.assertRaises(ValidationError, validator_client.valideaza, client_gresit)

    def teste_validare_carte(self):
        validator_carte = ValidatorCarte()
        id_carte_gresit = -1
        titlu_carte_gresit = ""
        descriere_carte_gresita = ""
        autor_carte_gresit = ""
        carte_gresita = Carte(id_carte_gresit, titlu_carte_gresit, descriere_carte_gresita, autor_carte_gresit)
        self.assertRaises(ValidationError, validator_carte.valideaza, carte_gresita)

    def teste_validare_inchiriere(self):
        validator_inchirieri = ValidatorInchiriere()
        id_inch_gresit = -1
        id_client_gresit = -1
        nume_client_gresit = ""
        id_carte_gresit = -1
        titlui_carte_gresit = ""
        inch_gresita = Inchiriere(id_inch_gresit, id_client_gresit, nume_client_gresit, id_carte_gresit,
                                  titlui_carte_gresit)
        self.assertRaises(ValidationError, validator_inchirieri.valideaza, inch_gresita)

    def teste_black_box_test_adauga_client_repo_clienti(self):
        repo_clienti = RepoClienti()
        client = Client(1, "Mihai", 100)
        self.assertTrue(len(repo_clienti) == 0)
        repo_clienti.adauga_client(client)
        self.assertTrue(len(repo_clienti) == 1)
        client_existent = Client(1, "George", 2424)
        self.assertRaises(RepoError, repo_clienti.adauga_client, client_existent)

    def teste_file_repo_clienti(self):
        calea_catre_fisier_test = "testare/clienti_test.txt"
        self.goleste_fisier(calea_catre_fisier_test)
        file_repo_clienti = FileRepoClienti(calea_catre_fisier_test)
        client = Client(1, "Mihai", 100)
        self.assertTrue(len(file_repo_clienti) == 0)
        file_repo_clienti.adauga_client(client)
        self.assertTrue(len(file_repo_clienti) == 1)
        self.assertRaises(RepoError, file_repo_clienti.adauga_client, client)
        id_client = 1
        file_repo_clienti.sterge_client_dupa_id(id_client)
        self.assertTrue(len(file_repo_clienti) == 0)
        file_repo_clienti.adauga_client(client)
        id_gresit = 5
        self.assertRaises(RepoError, file_repo_clienti.sterge_client_dupa_id, id_gresit)
        self.assertTrue(file_repo_clienti.cauta_clienti_dupa_nume("Mihai") == [client])
        self.assertTrue(file_repo_clienti.cauta_clienti_cu_carti_inch() == [])
        self.assertTrue(file_repo_clienti.cauta_client_dupa_id(id_client) == client)
        self.assertRaises(RepoError, file_repo_clienti.cauta_client_dupa_id, id_gresit)
        client_nou = Client(1, "Alex", 500)
        file_repo_clienti.modifica_client(id_client, client_nou)
        self.assertTrue(file_repo_clienti.get_all() == [client_nou])
        self.assertRaises(RepoError, file_repo_clienti.modifica_client, id_gresit, client_nou)


    def teste_file_repo_carti(self):
        calea_catre_fiser_test = "testare/carti_test.txt"
        self.goleste_fisier(calea_catre_fiser_test)
        carte = Carte(1, "Enigma", "interesanta", "Calinescu")
        file_repo_carti = FileRepoCarti(calea_catre_fiser_test)
        self.assertTrue(len(file_repo_carti) == 0)
        file_repo_carti.adauga_carte(carte)
        self.assertTrue(len(file_repo_carti) == 1)
        self.assertRaises(RepoError, file_repo_carti.adauga_carte, carte)
        id_carte = 1
        file_repo_carti.sterge_carte_dupa_id(id_carte)
        self.assertTrue(file_repo_carti.get_all() == [])
        file_repo_carti.adauga_carte(carte)
        id_gresit = 5
        self.assertRaises(RepoError, file_repo_carti.sterge_carte_dupa_id, id_gresit)
        self.assertTrue(file_repo_carti.cauta_carti_dupa_autor("Calinescu") == [carte])
        self.assertTrue(file_repo_carti.cauta_carte_dupa_id(id_carte) == carte)
        self.assertRaises(RepoError, file_repo_carti.cauta_carte_dupa_id, id_gresit)
        self.assertTrue(file_repo_carti.cauta_carti_cu_inch() == [])

    def teste_file_repo_inchirieri(self):
        calea_catre_fisier_test = "testare/inchirieri_test.txt"
        self.goleste_fisier(calea_catre_fisier_test)
        file_repo_inch = FileRepoInchirieri(calea_catre_fisier_test)
        self.assertTrue(len(file_repo_inch) == 0)
        inchiriere = Inchiriere(1, 1, "Enigma", 1, "Alex")
        file_repo_inch.adauga_inchiriere(inchiriere)
        self.assertEqual(len(file_repo_inch), 1)
        self.assertRaises(RepoError, file_repo_inch.adauga_inchiriere, inchiriere)
        id_carte = 1
        file_repo_inch.sterge_inchirieri_cu_cartea(id_carte)
        self.assertTrue(len(file_repo_inch) == 0)
        file_repo_inch.adauga_inchiriere(inchiriere)
        id_carte_gresit = 5
        self.assertRaises(RepoError, file_repo_inch.sterge_inchirieri_cu_cartea, id_carte_gresit)
        id_client = 1
        file_repo_inch.sterge_inchirieri_cu_clientul(id_client)
        self.assertTrue(len(file_repo_inch) == 0)
        file_repo_inch.adauga_inchiriere(inchiriere)
        id_client_gresit = 5
        self.assertRaises(RepoError, file_repo_inch.sterge_inchirieri_cu_clientul, id_client_gresit)
        id_inch = 1
        file_repo_inch.sterge_inchiriere_dupa_id(id_inch)
        self.assertTrue(file_repo_inch.get_all() == [])
        file_repo_inch.adauga_inchiriere(inchiriere)
        id_inch_gresit = 5
        self.assertRaises(RepoError, file_repo_inch.sterge_inchiriere_dupa_id, id_inch_gresit)


