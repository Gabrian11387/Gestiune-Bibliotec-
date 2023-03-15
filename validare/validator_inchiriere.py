from erori.validation_error import ValidationError

class ValidatorInchiriere:
    def __init__(self):
        pass

    def valideaza(self, inchiriere):
        erori = ""
        if inchiriere.get_id_inchiriere() < 0:
            erori += "id invalid!\n"
        if inchiriere.get_nume_client_inchiriere() == "":
            erori += "nume client invalid!\n"
        if inchiriere.get_titlu_carte_inchiriere() == "":
            erori += "titlu carte invalid!\n"
        if inchiriere.get_id_carte_inchiriere() < 0:
            erori += "id carte invalid!\n"
        if inchiriere.get_id_client_inchiriere() < 0:
            erori += "id client invalid!\n"
        if len(erori) > 0:
            raise ValidationError(erori)

