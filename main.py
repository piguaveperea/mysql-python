from distutils.log import error
from msilib.schema import Error
from turtle import color
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    database='db_test'
)

cursor=conn.cursor()

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
        sql = "select id, color, forma from casa"
        cursor.execute(sql)
        for casa in cursor.fetchall():
            print(casa)
    
    def leerId(self, id):
        sql = "select id, color, forma from casa where casa.id = '{0}'".format(id)
        cursor.execute(sql)
        for casa in cursor.fetchall():
            print(casa)
        pass

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
        casa.color = input("Ingresar color: ")
        casa.forma = input("Ingresar forma: ")
        casa.crear()
    if comando == "E":
        id_casa = input("Ingrese el Id ")
        casa.eliminar(id_casa)

    if comando == "R":
        casa.leer()

    if comando == "L":
        id_casa = input("Ingrese el Id ")
        casa.leerId(id_casa)
    
    if comando == "A":
        id_casa = input("Ingrese el Id ")
        casa.color = input("Ingresar color: ")
        casa.forma = input("Ingresar forma: ")
        casa.actualiza(id_casa)

