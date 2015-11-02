#!/usr/bin/python3
import abc

__author__ = 'paranoia'


class AbstractEmployer(metaclass=abc.ABCMeta):

    """AbstractEmployer is Adaptee Interface"""

    @abc.abstractclassmethod
    def get_name(self):
        """get_name :return name, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def set_name(self, name):
        """set_nome :arg nome, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def get_last_name(self):
        """get_last_name :return last_name, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def set_last_name(self, last_name):
        """set_last_name :arg last_name, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def get_salary(self):
        """get_salary :return salary, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def set_salary(self, salary):
        """set_salary :arg salary, String"""
        raise NotImplemented


class Employer(AbstractEmployer):

    def __init__(self, name, last_name, salary):
        super(Employer, self).__init__()
        self.__name = name
        self.__last_name = last_name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary
