import pymysql
from prettytable import PrettyTable

conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='db_test'
)

cursor=conn.cursor()

table = PrettyTable()

table.field_names = ["Id", "Color", "Figura"]

class Casa:
    color = ""
    forma = ""
    
    def crear(self):
        sql ="""
        insert into casa (forma, color) values('{0}','{1}')
        """.format(self.forma, self.color)
        try:
            cursor.execute(sql)
            conn.commit()
            print("Se guardo correctamente")
        except conn.Error as error:
            print(error)
        pass
    
    def eliminar(self, id):
        sql = """
            delete from casa where id = '{0}'
        """.format(id)
        cursor.execute(sql)
        conn.commit()
        pass
    
    def actualiza(self,id):
        sql = """
            update  casa  set  color = '{0}', forma='{1}' where casa.id = '{2}'
        """.format(self.color, self.forma, id)
        cursor.execute(sql)
        conn.commit()
        pass
    
    def leer(self):
        sql = "select  id, color, forma  from casa"
        try:
            cursor.execute(sql)
            table.add_rows(cursor.fetchall())
            print(table)
        except conn.Error as err:
            print(err)


    def leerId(self, id):
        sql = "select id, color, forma from casa where casa.id = '{0}'".format(id)
        cursor.execute(sql)
        for casa in cursor.fetchall():
            print(casa)
        pass

    def buscar(self, id):
        sql = """
            select * from  casa where casa.id = '{0}'
        """.format(id)

        cursor.execute(sql)
        return cursor.fetchall()
class Menu:
    def ui_menu(self):
        print(
            """
            ******************************************
            |        Menu Sencillo CRUD Casa         |
            ******************************************
            Crear (C)
            Leer (R)
            Actualizar(A)
            Eliminar (E)
            Leer Id (L)
            Salir (Q)
            """ 
        )

casa = Casa()
menu = Menu()


while True:
    menu.ui_menu()
    comando = input("Ingrese comando:  ").upper()
    if comando == 'Q':
        print("Gracias vuelve pronto")
        exit()

    if comando == "C":
        print("\n Registrar nueva casas \n")
        casa.color = input("Ingresar color: ")
        casa.forma = input("Ingresar forma: ")
        casa.crear()    
    if comando == "E":
        id_casa = input("Ingrese el Id ")
        if casa.buscar == ():
            print("No existe")
        else:
            casa.eliminar(id_casa)

    if comando == "R":
        casa.leer()

    if comando == "L":
        id_casa = input("Ingrese el Id ")
        casa.leerId(id_casa)
    
    if comando == "A":
        id_casa = input("Ingrese el Id ")
        if casa.buscar(id_casa) == ():
            print("No existe la casa")
        else:
            print(casa.buscar(id_casa))
            casa.color = input("Ingresar color: ")
            casa.forma = input("Ingresar forma: ")
            casa.actualiza(id_casa)

