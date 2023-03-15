from domeniu.client import Client
from domeniu.carti import Carte
from domeniu.inchiriere import Inchiriere
from business.service_clienti import ServiceClienti
from business.service_carti import ServiceCarti
from business.service_inchirieri import ServiceInchirieri
from infrastructura.repo_carti import RepoCarti
from infrastructura.repo_clienti import RepoClienti
from infrastructura.repo_inchirieri import RepoInchirieri
from validare.validator_carte import ValidatorCarte
from validare.validator_client import ValidatorClient
from validare.validator_inchiriere import ValidatorInchiriere
from erori.validation_error import ValidationError
from erori.Repo_error import RepoError

def teste_domeniu_client():
    client = Client(1, "Mihai", 6031009060011)
    assert client.get_id_client() == 1
    assert client.get_nume_client() == "Mihai"
    assert client.get_cnp_client() == 6031009060011
    assert client.get_nr_carti_inch() == 0
    client.set_cnp_client(5031009060011)
    assert client.get_cnp_client() == 5031009060011
    client.set_nume_client("Alex")
    assert client.get_nume_client() == "Alex"
    client.creste_numar_inch()
    assert client.get_nr_carti_inch() == 1
    client.scade_numar_inch()
    assert client.get_nr_carti_inch() == 0
    client_egal = Client(1, "Gabi", 5031001060011)
    assert client == client_egal


def teste_domeniu_carti():
    carte = Carte(2, "Enigma", "interesanta", "Sadoveanu")
    assert carte.get_id_carte() == 2
    assert carte.get_titlu_carte() == "Enigma"
    assert carte.get_descriere_carte() == "interesanta"
    assert carte.get_autor_carte() == "Sadoveanu"
    assert carte.get_nr_inch_carte() == 0
    carte.creste_numar_inchirieri_carte()
    assert carte.get_nr_inch_carte() == 1
    carte.scade_numar_inchirieri_carte()
    assert carte.get_nr_inch_carte() == 0
    carte_egala = Carte(2, "Enigma_noua", "neinteresanta", "Mihail")
    assert carte == carte_egala


def teste_domeniu_inchirieri():
    inchiriere = Inchiriere(1, 1, "Alex", 1, "Enigma")
    assert inchiriere.get_id_inchiriere() == 1
    assert inchiriere.get_id_carte_inchiriere() == 1
    assert inchiriere.get_titlu_carte_inchiriere() == "Enigma"
    assert inchiriere.get_nume_client_inchiriere() == "Alex"
    inch_egala = Inchiriere(1, 2, "Mihai", 2, "Ion")
    assert inch_egala == inchiriere
    assert inchiriere.get_nume_client_inchiriere() == "Alex"
    assert inchiriere.get_titlu_carte_inchiriere() == "Enigma"


def teste_repo_clienti():
    repo_clienti = RepoClienti()
    assert repo_clienti.get_all() == []
    assert len(repo_clienti) == 0
    client = Client(1, "Alex", 10)
    repo_clienti.adauga_client(client)
    assert len(repo_clienti) == 1
    id_client_pt_sterge = 1
    repo_clienti.sterge_client_dupa_id(id_client_pt_sterge)
    assert len(repo_clienti) == 0
    repo_clienti.adauga_client(client)
    assert len(repo_clienti) == 1
    acelasi_client = Client(1, "Gabi", 15)
    try:
        repo_clienti.adauga_client(acelasi_client)
        assert False
    except RepoError as rp:
        assert str(rp) == "Client existent!"
    id_gresit = 3
    try:
        repo_clienti.sterge_client_dupa_id(id_gresit)
        assert False
    except RepoError as rp:
        assert str(rp) == "Client inexistent!"
    nume = "Alex"
    clienti_cu_numele_nume = repo_clienti.cauta_clienti_dupa_nume(nume)
    assert clienti_cu_numele_nume == [client]
    client.creste_numar_inch()
    clienti_cu_carti_inch = repo_clienti.cauta_clienti_cu_carti_inch()
    assert clienti_cu_carti_inch == [client]
    id_de_cautat = 1
    client_gasit = repo_clienti.cauta_client_dupa_id(id_de_cautat)
    assert client_gasit == client
    id_gresit = 4
    try:
        repo_clienti.cauta_client_dupa_id(id_gresit)
        assert False
    except RepoError as rp:
        assert str(rp) == "Client inexistent!"


def teste_repo_carti():
    repo_carti = RepoCarti()
    assert len(repo_carti) == 0
    carte = Carte(2, "Enigma", "interesanta", "Sadoveanu")
    repo_carti.adauga_carte(carte)
    assert len(repo_carti) == 1
    assert repo_carti.get_all() == [carte]
    aceeasi_carte = Carte(2, "Ion", "neinteresanta", "Rebreanu")
    try:
        repo_carti.adauga_carte(aceeasi_carte)
        assert False
    except RepoError as rp:
        assert str(rp) == "Carte existenta!"
    id_carte = 2
    repo_carti.sterge_carte_dupa_id(id_carte)
    assert len(repo_carti) == 0
    repo_carti.adauga_carte(carte)
    id_gresit = 3
    try:
        repo_carti.sterge_carte_dupa_id(id_gresit)
        assert False
    except RepoError as rp:
        assert str(rp) == "Carte inexistenta!"
    autor = "Sadoveanu"
    carti_cu_autorul_autor = repo_carti.cauta_carti_dupa_autor(autor)
    assert carti_cu_autorul_autor == [carte]
    id_de_cautat = 2
    carte_cu_id_de_cautat = repo_carti.cauta_carte_dupa_id(id_de_cautat)
    assert carte_cu_id_de_cautat == carte
    id_gresit = 3
    try:
        repo_carti.cauta_carte_dupa_id(id_gresit)
        assert False
    except RepoError as rp:
        assert str(rp) == "Carte inexistenta!"


def teste_repo_inchirieri():
    repo_inch = RepoInchirieri()
    assert len(repo_inch) == 0
    assert repo_inch.get_all() == []
    inchiriere = Inchiriere(1, 1, "Alex", 1, "Enigma")
    repo_inch.adauga_inchiriere(inchiriere)
    assert repo_inch.get_all() == [inchiriere]
    acelasi_id = 1
    try:
        repo_inch.adauga_inchiriere(Inchiriere(acelasi_id, 2, "Ion", 1, "Enigma"))
        assert False
    except RepoError as rp:
        assert str(rp) == "Inchiriere existenta!"
    id_carte = 1
    repo_inch.sterge_inchirieri_cu_cartea(id_carte)
    assert repo_inch.get_all() == []
    repo_inch.adauga_inchiriere(inchiriere)
    """
    id_carte_gresit = 2
    try:
        repo_inch.sterge_inchirieri_cu_cartea(id_carte_gresit)
        assert False
    except RepoError as rp:
        assert str(rp) == "Carte nexistenta printre inchirieri!"
    id_client = 1
    repo_inch.sterge_inchirieri_cu_clientul(id_client)
    assert repo_inch.get_all() == []
    repo_inch.adauga_inchiriere(inchiriere)
    id_client_gresit = 5
    try:
        repo_inch.sterge_inchirieri_cu_clientul(id_client_gresit)
        assert False
    except RepoError as rp:
        assert str(rp) == "Client inexistent printre inchirieri!"
    id_inchiriere = 1
    repo_inch.sterge_inchiriere_dupa_id(id_inchiriere)
    assert len(repo_inch) == 0
    repo_inch.adauga_inchiriere(inchiriere)
    id_inchiriere_gresit = 10
    try:
        repo_inch.sterge_inchiriere_dupa_id(id_inchiriere_gresit)
        assert False
    except RepoError as rp:
        assert str(rp) == "Inchiriere inexistenta!"
    """


def teste_service_clienti():
    repo_clienti = RepoClienti()
    validator_clienti = ValidatorClient()
    service_clienti = ServiceClienti(validator_clienti, repo_clienti)
    id_client = 1
    nume_client = "Alex"
    cnp_client = 10
    assert len(repo_clienti) == 0
    service_clienti.adauga_client(id_client, nume_client, cnp_client)
    assert len(repo_clienti) == 1
    lista_clienti = service_clienti.get_all_clienti()
    client = Client(id_client, nume_client, cnp_client)
    assert lista_clienti == [client]
    id_pt_sters = id_client
    service_clienti.sterge_client_dupa_id(id_pt_sters)
    assert len(repo_clienti) == 0
    service_clienti.adauga_client(id_client, nume_client, cnp_client)
    assert len(repo_clienti) == 1
    id_curent = 1
    nume_nou = "Gabi"
    cnp_nou = 15
    service_clienti.modifica_client_dupa_id(id_curent, nume_nou, cnp_nou)
    assert len(repo_clienti) == 1
    client_nou = Client(id_curent, nume_nou, cnp_nou)
    assert service_clienti.get_all_clienti() == [client_nou]
    nume = "Gabi"
    clienti_cu_numele_nume = service_clienti.cauta_clienti_dupa_nume(nume)
    assert len(clienti_cu_numele_nume) == 1
    service_clienti.adauga_client(2, "Mihai", 450)
    assert len(repo_clienti) == 2
    client1 = client_nou
    client2 = Client(2, "Mihai", 450)
    assert service_clienti.get_all_clienti() == [client1, client2]
    for cli in service_clienti.get_all_clienti():
        cli.creste_numar_inch()
    clienti_cu_carti_inch_ordonati_dupa_nume = service_clienti.ordoneaza_clienti_dupa_nume()
    assert clienti_cu_carti_inch_ordonati_dupa_nume == [client1, client2]
    service_clienti.get_all_clienti()[0].creste_numar_inch()
    clienti_ord_dupa_cart_inch = service_clienti.ordoneaza_clienti_dupa_carti_inch()
    assert clienti_ord_dupa_cart_inch == [client1, client2]
    service_clienti.adauga_client(3, "Alex", 200)
    service_clienti.adauga_client(4, "Mircea", 500)
    service_clienti.adauga_client(5, "Traian", 600)
    assert len(repo_clienti) == 5
    for cli in service_clienti.get_all_clienti():
        cli.creste_numar_inch()
    cei_mai_activi_clienti = service_clienti.cei_mai_activi_clienti()
    assert cei_mai_activi_clienti == [client1]

def teste_service_carti():
    repo_carti = RepoCarti()
    validator_carti = ValidatorCarte()
    service_carti = ServiceCarti(validator_carti, repo_carti)
    id_carte = 1
    nume_carte = "Enigma"
    descriere_carte = "interesanta"
    autor_carte = "Sadoveanu"
    assert len(repo_carti) == 0
    service_carti.adauga_carte(id_carte, nume_carte, descriere_carte, autor_carte)
    assert len(repo_carti) == 1
    lista_carti = service_carti.get_all_carti()
    carte = Carte(id_carte, nume_carte, descriere_carte, autor_carte)
    assert lista_carti == [carte]
    service_carti.sterge_carte_dupa_id(id_carte)
    assert len(repo_carti) == 0
    assert service_carti.get_all_carti() == []
    service_carti.adauga_carte(id_carte, nume_carte, descriere_carte, autor_carte)
    autor = "Sadoveanu"
    carti_cu_autorul_autor = service_carti.cauta_carti_dupa_autor(autor)
    assert carti_cu_autorul_autor == [carte]
    service_carti.adauga_carte(2, "Bubico", "neinteresanta", "Eminescu")
    carte1 = Carte(id_carte, nume_carte, descriere_carte, autor_carte)
    carte2 = Carte(2, "Bubico", "neinteresanta", "Eminescu")
    for carte in service_carti.get_all_carti():
        carte.creste_numar_inchirieri_carte()
    service_carti.get_all_carti()[1].creste_numar_inchirieri_carte()
    carti_ord_dupa_nr_inch = service_carti.ordoneaza_carti_dupa_nr_inchirieri()
    assert carti_ord_dupa_nr_inch == [carte2, carte1]


def teste_service_inchirieri():
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
    assert len(service_inchirieri.get_all_inchirieri()) == 1
    service_inchirieri.sterge_inchiriere(id_inch, id_client, nume_client, id_carte, titlu_carte)
    assert len(service_inchirieri.get_all_inchirieri()) == 0
    service_inchirieri.adauga_inchiriere(id_inch, id_client, nume_client, id_carte, titlu_carte)
    service_inchirieri.sterge_inchirieri_cu_cartea(id_carte)
    assert len(service_inchirieri.get_all_inchirieri()) == 0
    service_inchirieri.adauga_inchiriere(id_inch, id_client, nume_client, id_carte, titlu_carte)
    service_inchirieri.sterge_inchiriere_cu_clientul(id_client)
    assert len(service_inchirieri.get_all_inchirieri()) == 0


def teste_validare_client():
    validator_client = ValidatorClient()
    id_gresit = -1
    nume_gresit = ""
    cnp_gresit = -2
    client_gresit = Client(id_gresit, nume_gresit, cnp_gresit)
    try:
        validator_client.valideaza(client_gresit)
        assert False
    except ValidationError as ve:
        assert (str(ve) == "id invalid!\nnume invalid!\ncnp invalid!\n")


def teste_validare_carti():
    validator_carte = ValidatorCarte()
    id_carte_gresit = -1
    titlu_carte_gresit = ""
    descriere_carte_gresita = ""
    autor_carte_gresit = ""
    carte_gresita = Carte(id_carte_gresit, titlu_carte_gresit, descriere_carte_gresita, autor_carte_gresit)
    try:
        validator_carte.valideaza(carte_gresita)
        assert False
    except ValidationError as ve:
        assert str(ve) == "id invalid!\ntitlu carte invalid!\ndescriere carte invalida!\nautor carte invalid!\n"


def teste_validare_inchirieri():
    validator_inchirieri = ValidatorInchiriere()
    id_inch_gresit = -1
    id_client_gresit = -1
    nume_client_gresit = ""
    id_carte_gresit = -1
    titlui_carte_gresit = ""
    inch_gresita = Inchiriere(id_inch_gresit, id_client_gresit, nume_client_gresit, id_carte_gresit, titlui_carte_gresit)
    try:
        validator_inchirieri.valideaza(inch_gresita)
        assert False
    except ValidationError as ve:
        assert str(ve) == "id invalid!\nnume client invalid!\ntitlu carte invalid!\nid carte invalid!\nid client invalid!\n"


def ruleaza_toate_testele():
    teste_domeniu_client()
    print("teste domeniu client rulate cu succes!")
    teste_domeniu_carti()
    print("teste domeniu carte rulate cu succes!")
    teste_domeniu_inchirieri()
    print("teste domeniu inchirieri rulate cu succes!")
    teste_repo_clienti()
    print("teste repo clienti rulate cu succes!")
    teste_repo_carti()
    print("teste repo carti rulate cu succes!")
    teste_repo_inchirieri()
    print("teste repo inchirieri rulate cu succes!")
    teste_service_clienti()
    print("teste service clienti rulate cu succes!")
    teste_service_carti()
    print("teste service carti rulate cu succes!")
    teste_service_inchirieri()
    print("teste service inchirieri rulate cu succes!")
    teste_validare_client()
    print("teste validare client rulate cu succes!")
    teste_validare_carti()
    print("teste validare carti rulate cu succes!")
    teste_validare_inchirieri()
    print("teste validare inchirieri rulate cu succes!")