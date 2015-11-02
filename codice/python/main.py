#!/usr/bin/python3
from impiegato import Impiegato
from employer import Employer
from empleado import Empleado
import class_adapter
import object_adapter
import special_adapter

__author__ = 'paranoia'


def my_print_method(objects):
    for obj in objects:
        print(
        obj.get_nome(),
        obj.get_cognome() + ": ",
        obj.get_stipendio(), "€"
        )

def main_class_adapter():
    print("Class Adapter")
    objects = []
    objects.append(Impiegato("Marco", "Ferraioli", 4000))
    objects.append(class_adapter.AdapterEmployer("John", "Simpson", 2500))
    objects.append(class_adapter.AdapterEmpleado("Casandra", "González", 3000))
    my_print_method(objects)

def main_object_adapter():
    print("Object Adapter")
    objects = []
    objects.append(Impiegato("Marco", "Ferraioli", 4000))
    objects.append(object_adapter.AdapterEmployer(Employer("John", "Simpson", 2500)))
    objects.append(object_adapter.AdapterEmpleado(Empleado("Casandra", "González", 3000)))
    my_print_method(objects)

def main_special_adapter():
    print("Special Adapter")
    objects = []
    objects.append(Impiegato("Marco", "Ferraioli", 4000))
    impiegato_us = Employer("John", "Simpson", 2500)
    rapporto_us = 1.10
    objects.append(special_adapter.Adapter(impiegato_us, dict(
        get_nome = impiegato_us.get_name,
        set_nome = impiegato_us.set_name,
        get_cognome = impiegato_us.get_last_name,
        set_cognome = impiegato_us.set_last_name,
        get_stipendio = lambda: (impiegato_us.get_salary() / rapporto_us),
        set_stipendio = lambda stipendio: impiegato_us.set_salary(stipendio * rapporto_us)
        )))
    impiegato_es = Empleado("Casandra", "González", 3000)
    rapporto_es = 1
    objects.append(special_adapter.Adapter(impiegato_es, dict(
        get_nome = impiegato_es.get_nombre,
        set_nome = impiegato_es.set_nombre,
        get_cognome = impiegato_es.get_apellido,
        set_cognome = impiegato_es.set_apellido,
        get_stipendio = lambda: (impiegato_es.get_salario() / rapporto_es),
        set_stipendio = lambda stipendio: impiegato_es.set_salario(stipendio * rapporto_es)
        )))
    my_print_method(objects)

if __name__ == '__main__':
    main_class_adapter()
    main_object_adapter()
    main_special_adapter()
