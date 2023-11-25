use wardrobe_db;

-- Below are the queries based on application functionality, where we have used
-- two nested queries for retrieving category and item name from the categoryitems table
-- and user and item name from the useritems table. One join query is used to retrieve 
-- all the items involved along with their colours in the outfits table.
-- Three aggregate queries with union operation are used, in order to retrieve the 
-- the appearances of various types of items, along with their count.

SELECT
                        (SELECT Category.category_name FROM Category WHERE Category.category_id = CategoryItems.category_id) AS category_name,
                        (SELECT Items.item_name FROM Items WHERE Items.item_id = CategoryItems.item_id) AS item_name
                        FROM CategoryItems;

SELECT
                        (SELECT Users.user_name FROM Users WHERE Users.user_id = UserItems.user_id) AS user_name,
                        (SELECT Items.item_name FROM Items WHERE Items.item_id = UserItems.item_id) AS item_name
                        FROM UserItems;

SELECT
                        Outfits.outfit_name,
                        Outfits.outfit_occasions,
                        TopItem.item_colour AS top_item_colour,
                        TopItem.item_name AS top_item_name,
                        BottomItem.item_colour AS bottom_item_colour,
                        BottomItem.item_name AS bottom_item_name,
                        ShoeItem.item_colour AS shoe_item_colour,
                        ShoeItem.item_name AS shoe_item_name
                        FROM
                            Outfits
                        JOIN
                            Items AS TopItem ON Outfits.top_item_id = TopItem.item_id
                        JOIN
                            Items AS BottomItem ON Outfits.bottom_item_id = BottomItem.item_id
                        JOIN
                            Items AS ShoeItem ON Outfits.shoe_item_id = ShoeItem.item_id;

WITH ShoeCount AS (
                        SELECT
                            'Total Shoes' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            COUNT(*) AS total_item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'shoe'
                        )

                        SELECT
                            item_id,
                            item_colour,
                            item_name,
                            1 AS item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'shoe'

                        UNION ALL

                        SELECT
                            'Total Shoes' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            total_item_count
                        FROM
                            ShoeCount;

WITH TopCount AS (
                        SELECT
                            'Total Tops' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            COUNT(*) AS total_item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'top'
                        )

                        SELECT
                            item_id,
                            item_colour,
                            item_name,
                            1 AS item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'top'

                        UNION ALL

                        SELECT
                            'Total Tops' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            total_item_count
                        FROM
                            TopCount;

WITH BottomCount AS (
                        SELECT
                            'Total Bottoms' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            COUNT(*) AS total_item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'bottom'
                        )

                        SELECT
                            item_id,
                            item_colour,
                            item_name,
                            1 AS item_count
                        FROM
                            Items
                        WHERE
                            item_type = 'bottom'

                        UNION ALL

                        SELECT
                            'Total Bottoms' AS item_name,
                            '' AS item_colour,
                            '' AS item_id,
                            total_item_count
                        FROM
                            BottomCount;

