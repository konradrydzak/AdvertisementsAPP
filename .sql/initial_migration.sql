drop table if exists category;
drop table if exists offer;

CREATE TABLE category (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"name" varchar(200) NOT NULL, 
	"ordering" integer unsigned NOT NULL CHECK ("ordering" >= 0)
);

CREATE TABLE offer (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"title" varchar(200) NOT NULL, 
	"description" varchar(1000) NOT NULL, 
	"price" decimal NOT NULL, 
	"created_at" datetime NOT NULL, 
	"category_id" int NOT NULL,
	foreign key ("category_id")
		references category ("id") on delete cascade
);

INSERT INTO category ("name", "ordering") VALUES ('Food', 1);
INSERT INTO category ("name", "ordering") VALUES ('Cars', 3);
INSERT INTO category ("name", "ordering") VALUES ('Board games', 2);
INSERT INTO category ("name", "ordering") VALUES ('Books', 4);
INSERT INTO category ("name", "ordering") VALUES ('Job offers', 6);
INSERT INTO category ("name", "ordering") VALUES ('Films', 5);

INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Apples', 'Apples for sale', 1.50, datetime('now'), 1);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Oranges', 'Oranges for sale', 3.50, datetime('now'), 1);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Fast cars for rent', 'Brand new and exclusive cars for rent, price to be negotiated', 999999, datetime('now'), 3);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Hanabi', 'Great cooperative card game with a twist!', 40, datetime('now'), 2);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Brandon Sanderson Stormlight Archives', 'Amazing fantasy world and a must read!', 250, datetime('now'), 4);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Python Fullstack Developer needed!', 'Tech stack: Django Rest Framework + Angular', 0, datetime('now'), 6);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('CODA - great Oscar-worthy film', 'You should definitely watch it', 25, datetime('now'), 5);
