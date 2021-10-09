# AdvertisementsAPP

Project for recruitment and Django Rest Framework learning purposes.

Simulates a simple portal with advertisements.

You can preview the app at: http://srv08.mikr.us:40304 (with */admin*, */offers*, */category* endpoints) or
at: http://srv08.mikr.us:40306 - to see my Single Page Application implementation

## Setup

1. Fill in required details in *database.ini* and *.env* files (in root of repo):

***database.ini***

```
[postgresql]
engine=django.db.backends.postgresql_psycopg2
name=advertisements
user=postgres
password=Password
host=postgres
port=5432
```

***.env***

```
POSTGRES_EXTERNAL_PORT=5433
POSTGRES_PASSWORD=Password
DJANGO_EXTERNAL_PORT=8001
ANGULAR_EXTERNAL_PORT=4200
```

> > **Recommended to use *DJANGO_EXTERNAL_PORT=8001* in *.env*** to avoid an additional step:
> >
> > Provided Angular website uses static *api_url*, so if you want to use custom *api_url* you need to manually change value of *this.http.get("http://host.docker.internal:8001/offers?format=json")* in *.angular/AdvertisementsAngular/dist/AdvertisementsAngular/main.\*.js* file

2. Docker compose (*docker-compose up -d*)

> > Aditionally if you want to create a superuser (to use Django admin site), you need to run *docker exec -it AdvertisementsAPP bash* and then enter two commands: *python manage.py migrate* and *python manage.py createsuperuser* with provided input for name, email and password accordingly

## Entity-Relationship Diagram

![AdvertisementsAPP-ERD.png](docs/AdvertisementsAPP-ERD.png "Simple ERD diagram for a advertisements portal")

## Skills used

- created a functioning API with CRUD functionality in Django Rest Framework
- learned and applied DRF utilities
- implement option to docker compose PostgreSQL and Django app instances
- provided end2end RestAPI endpoints tests in a Postman collection
- developed a Single Page Application in Angular

### Possible improvements

- properly learn how to develop on frontend side (I have planned to complete
  the [Microsoft Web-Dev Course](https://github.com/microsoft/Web-Dev-For-Beginners))
- improve project structure (organize the code into controllers, services, etc.)
- provide a more user-friendly display for offer category in text, rather than related id
- implement authorization to restrict database access for manipulating functions