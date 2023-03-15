from erori.validation_error import ValidationError


class ValidatorClient:

    def __init__(self):
        pass

    def valideaza(self, client):
        """
        functia valideaza datele introduse de utilizator si ridica o eroare pentru fiecare caz:
        > id-ul este negativ - ridicam eroarea id invalid!
        > nume client vid - nume invalid!
        > cnp negativ - cnp invalid!
        Daca datele sunt valide, nu se ridica nicio eroare in urma exxecutiei functiei
        :param client - obiect de tipul Client
        :return: -
        """
        erori = ""
        if client.get_id_client() < 0:
            erori += "id invalid!\n"
        if client.get_nume_client() == "":
            erori += "nume invalid!\n"
        if client.get_cnp_client() < 0:
            erori += "cnp invalid!\n"
        if len(erori) > 0:
            raise ValidationError(erori)
