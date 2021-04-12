CREATE VIEW 	interview_view 	AS
	SELECT 		Fid, timestamp, hyperlink, image, text
	FROM			ASSETS
	WHERE 		Fid =	(
                  SELECT id
                  FROM interview
                  WHERE title LIKE 'Garfing%'
	);

CREATE VIEW 	admin_info_view AS
	SELECT 	users.userID, username
	FROM		USERS
	RIGHT JOIN 	ADMINISTRATOR
ON USERS.userID = ADMINISTRATOR.userID;
