#!/usr/bin/python3
import abc

__author__ = 'paranoia'


class AbstractImpiegato(metaclass=abc.ABCMeta):

    """AbstractImpiegato is Adaptee Interface"""

    @abc.abstractclassmethod
    def get_nome(self):
        """get_nome :return nome, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def set_nome(self, nome):
        """set_nome :arg nome, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def get_cognome(self):
        """get_cognome :return cognome, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def set_cognome(self, cognome):
        """set_cognome :arg cognome, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def get_stipendio(self):
        """get_stipendio :return stipendio, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def set_stipendio(self, stipendio):
        """set_stipendio :arg stipendio, String"""
        raise NotImplemented


class Impiegato(AbstractImpiegato):

    def __init__(self, nome, cognome, stipendio):
        super(Impiegato, self).__init__()
        self.__nome = nome
        self.__cognome = cognome
        self.__stipendio = stipendio

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_cognome(self):
    	return self.__cognome

    def set_cognome(self, cognome):
    	self.__cognome = cognome

    def get_stipendio(self):
    	return self.__stipendio

    def set_stipendio(self, stipendio):
    	self.__stipendio = stipendio

