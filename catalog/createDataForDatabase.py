#!/usr/bin/env python

# Create database test data 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Item, Base, User

#engine = create_engine('sqlite:///carItems_catalog.db')

engine = create_engine('postgresql://catalog:catalog@localhost/catalog')

Base.metadata.bind = engine

# bind the session with the engine
DBSession = sessionmaker(bind=engine)

# create a new session
session = DBSession()

print("Session created!")


# create a test user
userDemo = User(id=5,
             name="Corvette Ray",
             email="CorvetteRay@gmail.com",
             picture='https://cars.usnews.com/static/images/Auto/izmo/i67064107/2019_chevrolet_corvette_angularfront.jpg')

session.add(userDemo)
session.commit()


# create Categories and Items

'''
#### Data for Demo Car Catalog####
'''
'''
#### SubCompact####
'''

subcompact = Category(name="SubCompact", user_id=userDemo.id)

session.add(subcompact)
session.commit()

mini_cooper = Item(name="Mini Cooper",
              description="The Mini Cooper is a great vehicle for people seeking athletic handling and brisk acceleration from a subcompact car. "
                          "Its excellent road grip, firm suspension, sturdy brakes, and responsive steering help this vehicle move with an air of zippiness usually reserved for larger hatchbacks.",
              cost="$21,900",
              category=subcompact,
              user_id=userDemo.id)

session.add(mini_cooper)
session.commit()

honda_fit = Item(name="Honda Fit",
             description="It ranks among the best models in the subcompact car class, thanks to its predictable handling, practical cabin, and abundance of available features.  "
                         "The Fit also has the best combination of quality and value in its class, which led us to name it our 2019 Best Subcompact Car for the Money award winner.",
             cost="$16,190", 
             category=subcompact,
             user_id=userDemo.id)

session.add(honda_fit)
session.commit()

accent = Item(name="Hyundai Accent",
              description="It has a spacious and attractive interior, a nice assortment of available features, and a near-perfect predicted reliability rating. "
                          "On the road, the Accent gets decent fuel economy and handles well.",
              cost="$19,000", 
              category=subcompact,
              user_id=userDemo.id)

session.add(accent)
session.commit()

'''
#### Midsize ####
'''

midsize = Category(name="Midsize", user_id=userDemo.id)

session.add(midsize)
session.commit()

camry = Item(name="Toyota Camry",
                 description="The Toyota Camry is an excellent car. "
                             "It offers fuel-efficient and energetic engines, it rides comfortably, and it handles well, making it more fun to drive than many rivals.",
                 cost="$24,000", 
                 category=midsize,
                 user_id=userDemo.id)

session.add(camry)
session.commit()

accord = Item(name="Honda Accord",
              description="The 2019 Accord is an outstanding midsize car that is both practical and fun. "
                          "It has a generous list of standard safety technology and a spacious cabin.",
              cost="$23,720", 
              category=midsize, 
              user_id=userDemo.id)

session.add(accord)
session.commit()

mazda6 = Item(name="Mazda Mazda6",
           description="The 2019 Mazda6 is one of the most athletic sedans in the midsize car class. "
                       "Sharp, responsive steering and confidence-inspiring road grip help make it a blast to drive and a delight on twisty roads.",
           cost="$23,800", 
           category=midsize,
           user_id=userDemo.id)

session.add(mazda6)
session.commit()

'''
#### Sports Cars ####
'''

sports_cars = Category(name="Sports Cars", user_id=userDemo.id)

session.add(sports_cars)
session.commit()

miata = Item(name="Mazda MX-5 Miata",
             description="This two-seat roadster is quick and eager to play, handling winding roads with ease and generally making your drive a memorable experience.",
             cost="$25,500", 
             category=sports_cars,
             user_id=userDemo.id)

session.add(miata)
session.commit()

mustang = Item(name="Ford Mustang",
             description="The Mustang is an excellent sports car, partly because it strikes an appealing balance in so many areas.",
             cost="$25,000",
             category=sports_cars,
             user_id=userDemo.id)

session.add(mustang)
session.commit()

challenger = Item(name="Dodge Challenger",
             description="At the core of every Challenger is a meaty engine.",
             cost="$27,295",
             category=sports_cars,
             user_id=userDemo.id)

session.add(challenger)
session.commit()

print('Test data has been created!')
