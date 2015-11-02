#!/usr/bin/python3
import abc

__author__ = 'paranoia'


class AbstractEmpleado(metaclass=abc.ABCMeta):

    """AbstractEmpleado is Adaptee Interface"""

    @abc.abstractclassmethod
    def get_nombre(self):
        """get_nombre :return nombre, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def set_nombre(self, nombre):
        """set_nombre :arg nombre, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def get_apellido(self):
        """get_apellido :return apellido, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def set_apellido(self, apellido):
        """set_apellido :arg apellido, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def get_salario(self):
        """get_salario :return salario, String"""
        raise NotImplemented

    @abc.abstractclassmethod
    def set_salario(self, salario):
        """set_salario :arg salario, String"""
        raise NotImplemented


class Empleado(AbstractEmpleado):

    def __init__(self, nombre, apellido, salario):
        super(Empleado, self).__init__()
        self.__nombre = nombre
        self.__apellido = apellido
        self.__salario = salario

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
    	return self.__apellido

    def set_apellido(self, apellido):
    	self.__apellido = apellido

    def get_salario(self):
    	return self.__salario

    def set_salario(self, salario):
    	self.__salario = salario

