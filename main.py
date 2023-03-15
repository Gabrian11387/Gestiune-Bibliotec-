import unittest
from business.service_inchirieri import ServiceInchirieri
from infrastructura.file_repo_carti import FileRepoCarti
from infrastructura.file_repo_clienti import FileRepoClienti
from infrastructura.file_repo_inchirieri import FileRepoInchirieri
from infrastructura.repo_carti import RepoCarti
from infrastructura.repo_clienti import RepoClienti
from infrastructura.repo_inchirieri import RepoInchirieri
from validare.validator_client import ValidatorClient
from validare.validator_carte import ValidatorCarte
from business.service_clienti import ServiceClienti
from business.service_carti import ServiceCarti
from prezentare.consola import UI
from validare.validator_inchiriere import ValidatorInchiriere
from testare.Teste_Unitest import Teste

if __name__ == '__main__':
    cale_fisier_clienti = "clienti.txt"
    cale_fisier_carti = "carti.txt"
    cale_fisier_inchirieri = "inchirieri.txt"
    validator_client = ValidatorClient()
    validator_carte = ValidatorCarte()
    validator_inchiriere = ValidatorInchiriere()
    repo_clienti = FileRepoClienti(cale_fisier_clienti)
    repo_carti = FileRepoCarti(cale_fisier_carti)
    repo_inchirieri = FileRepoInchirieri(cale_fisier_inchirieri)
    #repo_clienti = RepoClienti()
    #repo_carti = RepoCarti()
    #repo_inchirieri = RepoInchirieri()
    service_clienti = ServiceClienti(validator_client, repo_clienti)
    service_carti = ServiceCarti(validator_carte, repo_carti)
    service_inchirieri = ServiceInchirieri(validator_inchiriere, repo_inchirieri, repo_clienti, repo_carti)
    consola = UI(service_clienti, service_carti, service_inchirieri)
    Teste = Teste()
    Teste.ruleaza_toate_testele()
    consola.run()