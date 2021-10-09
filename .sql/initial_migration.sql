drop table if exists category cascade;
drop table if exists offer cascade;

CREATE TABLE category (
	"id" serial NOT NULL PRIMARY KEY,
	"name" varchar(200) NOT NULL,
	"ordering" integer NOT NULL CHECK ("ordering" >= 0)
);

CREATE TABLE offer (
	"id" serial NOT NULL PRIMARY KEY,
	"title" varchar(200) NOT NULL,
	"description" varchar(1000) NOT NULL,
	"price" decimal NOT NULL,
	"created_at" timestamp with time zone NOT NULL,
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

INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Apples', 'Apples for sale', 1.50, NOW(), 1);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Oranges', 'Oranges for sale', 3.50, NOW(), 1);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Fast cars for rent', 'Brand new and exclusive cars for rent, price to be negotiated', 999999, NOW(), 3);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Hanabi', 'Great cooperative card game with a twist!', 40, NOW(), 2);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Brandon Sanderson Stormlight Archives', 'Amazing fantasy world and a must read!', 250, NOW(), 4);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('Python Fullstack Developer needed!', 'Tech stack: Django Rest Framework + Angular', 0, NOW(), 6);
INSERT INTO offer ("title", "description", "price", "created_at", "category_id") VALUES ('CODA - great Oscar-worthy film', 'You should definitely watch it', 25, NOW(), 5);
