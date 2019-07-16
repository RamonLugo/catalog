#!/usr/bin/env python

#Base imports
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#create declarative_base instance
Base = declarative_base()

#Create user object
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(1024))

    @property
    def serialize(self):

        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'picture': self.picture
        }


class Category(Base):
    __tablename__ = 'category'

    # creating id as primary key
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):

        return {
            'id': self.id,
            'name': self.name,
        }


class Item(Base):
    # creating an item object
    __tablename__ = 'items'

    #id is a primary key
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(1000))
    cost = Column(String(15))
    #category.id a foreign key 
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    # user.id a the foreign key
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):

        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'cost': self.cost,
            'category_id': self.category_id,
            'user_id': self.user_id
        }

# creating engine on carItems_catalog.db
#engine = create_engine('sqlite:///carItems_catalog.db')
engine = create_engine('postgresql://catalog:catalog@localhost/catalog')

# add the classes we created as tables onto the database
Base.metadata.create_all(engine)

print('The empty database structure has been created!')
