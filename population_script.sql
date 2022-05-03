INSERT INTO product_category (name) VALUES('Art');
INSERT INTO product_category (name) VALUES('Electronics');
INSERT INTO product_category (name) VALUES('Entertainment');
INSERT INTO product_category (name) VALUES('Fashion');
INSERT INTO product_category (name) VALUES('Furniture');
INSERT INTO product_category (name) VALUES('Home & Garden');
INSERT INTO product_category (name) VALUES('Sports');
INSERT INTO product_category (name) VALUES('Vehicles');

INSERT INTO product_condition (condition) VALUES('New');
INSERT INTO product_condition (condition) VALUES('Used - Like New');
INSERT INTO product_condition (condition) VALUES('Used - Very Good');
INSERT INTO product_condition (condition) VALUES('Used - Good');
INSERT INTO product_condition (condition) VALUES('Used - Acceptable');
INSERT INTO product_condition (condition) VALUES('Used - Sold as is');

INSERT INTO product_product (name, price, description, "CreatedAt", "SoldOrNot","categoryID_id", "ConditionID_id")
VALUES ('Smart TV', 20.00, 'An LG smart tv, with remote and power cable', '2021-08-09 13:57:40', 0, 2, 2);
INSERT INTO product_product (name, price, description, "CreatedAt", "SoldOrNot","categoryID_id", "ConditionID_id")
VALUES ('Dr. Martin boots', 10.00, 'Nearly new, no wear and tear. Don´t smell', '2021-09-10 13:45:00', 0, 4, 2);

