#!/usr/bin/python3
from impiegato import AbstractImpiegato
from employer import Employer
from empleado import Empleado

__author__ = 'paranoia'


class AdapterEmployer(AbstractImpiegato, Employer):

    _rapporto = 1.10

    def __init__(self, nome, cognome, stipendio):
        Employer.__init__(self, nome, cognome, stipendio)

    def get_nome(self):
        return self.get_name()

    def set_nome(self, nome):
        self.set_name(nome)

    def get_cognome(self):
        return self.get_last_name()

    def set_cognome(self, cognome):
        self.set_last_name(cognome)

    def get_stipendio(self):
        return (self.get_salary() / self._rapporto)

    def set_stipendio(self, stipendio):
        self.set_salary(stipendio * self._rapporto)


class AdapterEmpleado(AbstractImpiegato, Empleado):

    _rapporto = 1

    def __init__(self, nome, cognome, stipendio):
        Empleado.__init__(self, nome, cognome, stipendio)

    def get_nome(self):
        return self.get_nombre()

    def set_nome(self, nome):
        self.set_nombre(nome)

    def get_cognome(self):
        return self.get_apellido()

    def set_cognome(self, cognome):
        self.set_apellido(cognome)

    def get_stipendio(self):
        return (self.get_salario() / self._rapporto)

    def set_stipendio(self, stipendio):
        self.set_salario(stipendio * self._rapporto)