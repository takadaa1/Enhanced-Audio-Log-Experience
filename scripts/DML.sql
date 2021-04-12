INSERT INTO users (username,password) VALUES ('george123','monke123');
INSERT INTO users (username,password) VALUES ('dwarfhamsters','112233');
INSERT INTO users (username,password) VALUES ('johnnyboy','imcool');
INSERT INTO users (username,password) VALUES ('muffinman','dogsncats');

INSERT INTO administrator (userID) VALUES (1);
INSERT INTO administrator (userID) VALUES (2);
INSERT INTO administrator (userID) VALUES (3);

INSERT INTO interview (title, date, audio, thumbnail, uID) VALUES ('Finkle, Herman Humpsy','2003-10-06','https://archive.org/download/JHS10SideA/JHS%2010-%20side%20A.ogg','https://static.timesofisrael.com/njjewishnews/uploads/2018/03/TrentonFinkleStoreP-640x400.jpg',1);

INSERT INTO interview (title, date, audio, thumbnail, uID) VALUES ('Millner, Joel','1995-05-31','https://ia601203.us.archive.org/7/items/JHS13SideA/JHS%2013-%20side%20A.ogg','https://i.vimeocdn.com/portfolio_header/24701_402',1);

INSERT INTO interview (title, date, audio, thumbnail, uID) VALUES ('Dr. Paul Loser', '1976-08-12','https://ia802908.us.archive.org/0/items/OralHistroyWithDr.PaulLoserSideA/Oral%20Histroy%20with%20Dr.%20Paul%20Loser%20-%20side%20A.ogg','https://bloximages.chicago2.vip.townnews.com/trentonian.com/content/tncms/assets/v3/editorial/f/5c/f5ce912f-0051-580c-bcca-4abf595605c2/5bbb97a886fa0.image.jpg',2);

INSERT INTO interview (title, date, audio, thumbnail, uID) VALUES ('Garfing, Arthur (JHS16)','1995-02-07','https://ia801207.us.archive.org/18/items/JHS16SideA/JHS%2016-%20side%20A.ogg','https://unitedmeatco.com/wp-content/uploads/2020/12/united.png',3);

INSERT INTO assets (FiD, timestamp, hyperlink, image, text)
SELECT
Id,
'00:02:31',
'https://en.wikipedia.org/wiki/Nazi_Party',
'https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Parteiadler_Nationalsozialistische_Deutsche_Arbeiterpartei_%281933%E2%80%931945%29.svg/1280px-Parteiadler_Nationalsozialistische_Deutsche_Arbeiterpartei_%281933%E2%80%931945%29.svg.png',
'Garfing’s father left Vilna and was killed by the Germans in 1940'
FROM interview
WHERE title like 'Garfing%';

INSERT INTO assets (FiD, timestamp, hyperlink, image, text)
SELECT
Id,
'00:02:14',
'https://en.wikipedia.org/wiki/Vilnius',
'https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Flag_of_Lithuania.svg/188px-Flag_of_Lithuania.svg.png',
'He left his family in Europe - discusses his Mother’s death in 1937 in Vilna, capital of Lithuania'
FROM interview
WHERE title like 'Garfing%';

INSERT INTO assets (FiD, timestamp, hyperlink, image, text)
SELECT
Id,
'00:02:34',
'https://en.wikipedia.org/wiki/The_Holocaust',
'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Selection_on_the_ramp_at_Auschwitz-Birkenau%2C_1944_%28Auschwitz_Album%29_1a.jpg/435px-Selection_on_the_ramp_at_Auschwitz-Birkenau%2C_1944_%28Auschwitz_Album%29_1a.jpg',
'6,500 Jews were killed in 7 days and Arthur did not know for 2-3 years that his father had been killed.'
FROM interview
WHERE title like 'Garfing%';
