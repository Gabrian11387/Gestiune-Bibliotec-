from erori.validation_error import ValidationError

class ValidatorCarte:
    def __init__(self):
        pass

    def valideaza(self, carte):
        """
        functia valideaza datele introduse de utilizator si ridica o eroare pentru fiecare caz:
        > id-ul este negativ - ridicam eroarea id invalid!
        > titlul cartii este vid - titlu carte invalid!
        > descrierea cartii este vida - descriere carte invalida!
        > autorul cartii este vid - autor carte invalid!
        Daca datele sunt valide, nu se ridica nicio eroare in urma exxecutiei functiei
        :param carte: obiect de tipul Carte
        :return: -
        """
        erori = ""
        if carte.get_id_carte() < 0:
            erori += "id invalid!\n"
        if carte.get_titlu_carte() == "":
            erori += "titlu carte invalid!\n"
        if carte.get_descriere_carte() == "":
            erori += "descriere carte invalida!\n"
        if carte.get_autor_carte() == "":
            erori += "autor carte invalid!\n"
        if len(erori) > 0:
            raise ValidationError(erori)