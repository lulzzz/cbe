# Common Business Entities (CBE)

[![Licence](https://img.shields.io/github/license/semprini/cbe.svg)](https://github.com/Semprini/cbe/blob/master/LICENSE)
[![GitHub version](https://badge.fury.io/gh/semprini%2Fcbe.svg)](https://badge.fury.io/gh/semprini%2Fcbe)
[![Build Status](https://img.shields.io/circleci/project/github/Semprini/cbe.svg)](https://circleci.com/gh/Semprini/cbe)
[![Coverage Status](https://coveralls.io/repos/github/Semprini/cbe/badge.svg?branch=master)](https://coveralls.io/github/Semprini/cbe?branch=master)


CBE is a realization of a cross industry standard data model. The app provides RESTful CRUD and administration for common business entities persisted on a relational DB. The rationale is discussed in the [Wiki](https://github.com/Semprini/cbe/wiki)

The CBE projects goal is to provide a generic schema/API/persistence layer which can be used for all the common functions in an enterprise and extended for each industry/business. CBE can be used to underpin microservice, SOA, EDA or MDM architecture.

Sources: TM Fourum SID (Telco), IBM IFW (Finance/Banking), IAA (Insurance)

To run:
```shell
git clone https://github.com/Semprini/cbe.git
cd cbe
pip install -r requirements.txt
python manage.py migrate (will use a default sqllite db)
python manage.py createsuperuser
python manage.py runserver
browse to http://localhost:8000/admin for the admin interface
browse to http://localhost:8000/api for the api interface
```

How is this different to an API from a product?
The API/Persistence/Admin uses generic foreign keys to express relationships that would never be part of a product. The persistence layer has pointers to abstract classes which provides a faithful realization of the data model. This enables the data to be used in all business contexts.

Entity Domains:
- Party - Entities relating to individuals, organizations, how to contact them and the roles they play
- Location - Entities for addresses and places
- Business interaction - Entities for how parties interact in the business
- Customer - The parties that a business sells products or services to


Coming soon to a data model near you:
- More roles for PartyRole and BusinessInteraction
- Product
- Trouble Ticket


The data model is designed to be extended for each industry. In Party, the PartyRole class is the main abstract entity from which concrete classes like Customer or Supplier should be derived.

Check the [Wiki](https://github.com/Semprini/cbe/wiki) for more info. The data model is held in the Docs folder as a Sparx EA model
