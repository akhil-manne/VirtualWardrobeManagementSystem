create database wardrobe_db;
use wardrobe_db;

CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(255),
    user_mail_id VARCHAR(255),
    user_password VARCHAR(255)
);

CREATE TABLE Items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(255),
    item_colour VARCHAR(255),
    item_image_url VARCHAR(255),
    item_type ENUM('top', 'bottom', 'shoe')
);

CREATE TABLE Category (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(255),
    description TEXT
);

CREATE TABLE Outfits (
    outfit_id INT PRIMARY KEY,
    outfit_name VARCHAR(255),
    outfit_occasions VARCHAR(255),
    top_item_id INT,
    bottom_item_id INT,
    shoe_item_id INT,
    FOREIGN KEY (top_item_id) REFERENCES Items(item_id),
    FOREIGN KEY (bottom_item_id) REFERENCES Items(item_id),
    FOREIGN KEY (shoe_item_id) REFERENCES Items(item_id)
);

CREATE TABLE UserItems (
    user_id INT,
    item_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (item_id) REFERENCES Items(item_id)
);

CREATE TABLE CategoryItems (
    category_id INT,
    item_id INT,
    FOREIGN KEY (category_id) REFERENCES Category(category_id),
    FOREIGN KEY (item_id) REFERENCES Items(item_id)
);

INSERT INTO Users (user_id, user_name, user_mail_id, user_password)
VALUES
    (1, 'JohnDoe', 'john.doe@example.com', 'password123'),
    (2, 'JaneSmith', 'jane.smith@example.com', 'securePassword'),
    (3, 'BobJohnson', 'bob.johnson@example.com', 'strongPassword');

INSERT INTO Items (item_id, item_name, item_colour, item_image_url, item_type)
VALUES
    (1, 'T-shirt', 'Blue', 'https://example.com/tshirt.jpg', 'top'),
    (2, 'Jeans', 'Black', 'https://example.com/jeans.jpg', 'bottom'),
    (3, 'Sneakers', 'White', 'https://example.com/sneakers.jpg', 'shoe'),
	(4, 'Dress Shirt', 'White', 'https://example.com/dress-shirt.jpg', 'top'),
    (5, 'Chinos', 'Khaki', 'https://example.com/chinos.jpg', 'bottom'),
    (6, 'Formal Shoes', 'Black', 'https://example.com/formal-shoes.jpg', 'shoe'),
    (7, 'Hoodie', 'Gray', 'https://example.com/hoodie.jpg', 'top'),
    (8, 'Shorts', 'Blue', 'https://example.com/shorts.jpg', 'bottom'),
    (9, 'Running Shoes', 'Red', 'https://example.com/running-shoes.jpg', 'shoe');

-- Example: User 1 has items 1 and 2
INSERT INTO UserItems (user_id, item_id)
VALUES
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (3, 6),
	(1, 9),
    (2, 8),
    (3, 7);
    
-- Insert values into Category table
INSERT INTO Category (category_id, category_name, description)
VALUES
    (1, 'Clothing', 'Various types of clothing items'),
    (2, 'Footwear', 'Different styles of shoes'),
    (3, 'Accessories', 'Various accessories like hats, belts, etc.');

-- Insert values into Outfits table
INSERT INTO Outfits (outfit_id, outfit_name, outfit_occasions, top_item_id, bottom_item_id, shoe_item_id)
VALUES
    (1, 'Casual Day Outfit', 'Casual occasions', 1, 8, 5),
    (2, 'Formal Business Attire', 'Business meetings', 4, 5, 6),
    (3, 'Sporty Look', 'Sporting events', 7, 8, 9),
    (4, 'Weekend Comfort', 'Relaxing weekends', 1, 8, 3),
    (5, 'Evening Party', 'Night out with friends', 1, 2, 3);

INSERT INTO CategoryItems (category_id, item_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 4),
    (1, 5),
    (1, 7),
    (1, 8),
	(2, 3),
    (2, 6),
    (2, 9);

ALTER TABLE Items
ADD COLUMN last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

ALTER TABLE Users
ADD COLUMN user_last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

-- Trigger for BEFORE INSERT
CREATE TRIGGER before_insert_trigger
BEFORE INSERT
ON Items
FOR EACH ROW
SET NEW.last_modified = CURRENT_TIMESTAMP;

-- Trigger for BEFORE UPDATE
CREATE TRIGGER before_update_trigger
BEFORE UPDATE
ON Items
FOR EACH ROW
SET NEW.last_modified = CURRENT_TIMESTAMP;

-- Trigger for BEFORE INSERT on Users
CREATE TRIGGER before_insert_users_trigger
BEFORE INSERT
ON Users
FOR EACH ROW
SET NEW.user_last_modified = CURRENT_TIMESTAMP;

-- Trigger for BEFORE UPDATE on Users
CREATE TRIGGER before_update_users_trigger
BEFORE UPDATE
ON Users
FOR EACH ROW
SET NEW.user_last_modified = CURRENT_TIMESTAMP;

DELIMITER //

CREATE PROCEDURE GetRecentUsers()
BEGIN
    -- Set the time threshold to one minute ago
    DECLARE time_threshold TIMESTAMP;
    SET time_threshold = NOW() - INTERVAL 1 MINUTE;

    -- Fetch user entries created less than a minute ago
    SELECT *
    FROM users
    WHERE user_last_modified >= time_threshold;
END //

DELIMITER ;