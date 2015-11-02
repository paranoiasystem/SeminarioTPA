#!/usr/bin/python3
from impiegato import AbstractImpiegato

__author__ = 'paranoia'


class AdapterEmployer(AbstractImpiegato):

    _rapporto = 1.10

    def __init__(self, employer):
        self.employer = employer

    def __getattr__(self, attr):
        return getattr(self.employer, attr)

    def get_nome(self):
        return self.employer.get_name()

    def set_nome(self, nome):
        self.employer.set_name(nome)

    def get_cognome(self):
        return self.employer.get_last_name()

    def set_cognome(self, cognome):
        self.employer.set_last_name(cognome)

    def get_stipendio(self):
        return (self.employer.get_salary() / self._rapporto)

    def set_stipendio(self, stipendio):
        self.employer.set_salary(stipendio * self._rapporto)


class AdapterEmpleado(AbstractImpiegato):

    _rapporto = 1

    def __init__(self, empleado):
        self.empleado = empleado

    def get_nome(self):
        return self.empleado.get_nombre()

    def set_nome(self, nome):
        self.empleado.set_nombre(nome)

    def get_cognome(self):
        return self.empleado.get_apellido()

    def set_cognome(self, cognome):
        self.empleado.set_apellido(cognome)

    def get_stipendio(self):
        return (self.empleado.get_salario() / self._rapporto)

    def set_stipendio(self, stipendio):
        self.empleado.set_salario(stipendio * self._rapporto)