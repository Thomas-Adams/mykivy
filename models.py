from peewee import *
import os

data_dir = os.path.dirname(__file__)
contactdb = SqliteDatabase( os.path.join(data_dir, 'contacts.db'))


class Tag(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=30, index=True, null=False)
    description = CharField(max_length=255,null=True)
    color = CharField(max_length=10, index=True, null=True)
    class Meta:
        database = contactdb


class Country(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50, index=True, unique=True)
    tld = CharField(max_length=10, index=True, null=True)
    abbr = CharField(max_length=10, index=True, null=True)
    phone = CharField(max_length=10, index=True, null=True)

    class Meta:
        database = contactdb


class Contact(Model):
    id = AutoField(primary_key=True)
    givenName = CharField(max_length=50, index=True)
    surName = CharField(max_length=50, index=True)
    phone = CharField(max_length=20, index=True)
    email = CharField(max_length=100, index=True)
    birthDay = DateField(index=True)
    street = CharField(max_length=100, index=True)
    zip = CharField(max_length=10, index=True)
    city = CharField(max_length=50, index=True)
    country = CharField(max_length=50, index=True)

    class Meta:
        database = contactdb


def start_db():
    contactdb.connect(reuse_if_open=True)
    contactdb.drop_tables([Country, Tag, Contact])
    contactdb.create_tables([Country, Tag, Contact])


def connect():
    contactdb.connect(reuse_if_open=True)

def stop_db():
    contactdb.close()
