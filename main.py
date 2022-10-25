# Los comentarios comienzan con almohadilla
"""
Comentario multilínea
"""
'''
También con comilla simple
'''

a = True or 3  # ||
b = True and 3  # &&
print(b)

age = 3
print(type(age))

print(f"Hola, tu edad es {age}")

if age > 5:
    print("Mayor a 5")
elif age < 3:
    print("ddd")
else:
    print("www")

for i in range(0, 10):
    print(i)

nombre = "Antonio"
for i in nombre:
    print(i)


# class

class HelloWorld:
    def __init__(self, msg):
        self.msg = msg

    def hablar(self):
        print(self.msg)


miInstancia = HelloWorld("Hola")
miInstancia.hablar()


def hablar(nombre, msg="Hola"):
    print(f"{msg} {nombre}")


hablar("Juan")

a = []
a = [3, True, "Marcos"]
print(a[0])
a[0] = 456
print(a)
a.append(245)
print(a)
a.insert(1, "Mundo")
print(a)
b = ["H", 7]
a.insert(0, b)
print(a)

print()
# diccionarios

my_dict = {}
#  my_dict = dict()

my_dict = {
    "nombre": "Juan",
    "apellido": "Rodriguez",
    "edad": 23,
    "casado": False
}

print(my_dict["nombre"])
"""if "edad" in my_dict:
    edad = my_dict["edad"]
else:
    edad = None"""

edad = my_dict.get("edad")

if edad is None:
    print("No estaba la edad en el diccionario")

for k in my_dict.keys():
    print(k)
for v in my_dict.values():
    print(v)
for kv in my_dict.items():
    print(kv)
for key, value in my_dict.items():
    print(key, value)

b = {}
for key, value in my_dict.items():
    b[key] = value


def get_strings(dict1):
    my_list = []
    for v in my_dict.values():
        if type(v) == int:
            my_list.append(v)
    return my_list


resultado = get_strings(my_dict)
print(resultado)
