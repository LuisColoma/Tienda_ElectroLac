from django.db import models

# Create your models here.
import psycopg2
# Create your models here.

class Tables(models.Model):
    conn = psycopg2.connect("dbname='ElectroLac3' user='postgres' host='localhost' password='1234'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"username\", \"ip_address\", \"id\", \"attempt_time\",\"logout_time\" FROM \"axes_accesslog\";")
    rows = cur.fetchall()
    conn.close();
class Tables2(models.Model):
    conn = psycopg2.connect("dbname='ElectroLac3' user='postgres' host='localhost' password='1234'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"username\", \"ip_address\", \"id\", \"attempt_time\", \"failures_since_start\" FROM \"axes_accessattempt\";")
    rows = cur.fetchall()
    conn.close();

class Tables3(models.Model):
    conn = psycopg2.connect("dbname='ElectroLac3' user='postgres' host='localhost' password='1234'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"id\", \"summary\", \"Amount\", \"stock\",\"category_id\" FROM \"venta_product\";")
    rows = cur.fetchall()
    conn.close();
class Tables4(models.Model):
  conn = psycopg2.connect("dbname='ElectroLac3' user='postgres' host='localhost' password='1234'")
  cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'""" 
  cur.execute("SELECT \"cliente\", \"nit\", \"direccion\", \"total\", \"forma_pago\",  \"entrega\" FROM \"venta_venta\";")
  rows = cur.fetchall()
  conn.close();

class Tables5(models.Model):
   conn = psycopg2.connect("dbname='ElectroLac3' user='postgres' host='localhost' password='1234'")
   cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
   cur.execute("SELECT \"cliente\", \"producto\" FROM \"venta_carrito\";")
   rows = cur.fetchall()
   conn.close();