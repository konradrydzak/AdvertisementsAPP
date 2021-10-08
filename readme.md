# AdvertisementsAPP
Project for recruitment and Django Rest Framework learning purposes. 

Simulates a simple portal with advertisements.



## Setup

1. Fill in required details in *.env* and *database.ini* files (use *\<file>.example* for reference)
2. Docker compose

## Entity-Relationship Diagram
![AdvertisementsAPP-ERD.png](docs/AdvertisementsAPP-ERD.png "Simple ERD diagram for a advertisements portal")

## Skills used
- created a functioning API with CRUD functionality in Django Rest Framework
- learned and applied DRF utilities
- implement option to docker compose PostgreSQL and Django app instances
- provided end2end RestAPI endpoints tests in a Postman collection

### Possible improvements
- improve project structure (organize the code into controllers, services, etc.)
- provide a more user-friendly display for offer category in text, rather than related id
- implement authorization to restrict database access for manipulating functions
- develop front-end for the app