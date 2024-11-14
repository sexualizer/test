CREATE TABLE names(person_id SERIAL, name VARCHAR(20));
CREATE TABLE surnames(person_id SERIAL, surname VARCHAR(20));
CREATE TABLE patronymics(person_id SERIAL, patronymic VARCHAR(20));

INSERT INTO surnames(surname) VALUES
    ('Ivanov'),
    ('Petrov'),
    ('Sidorov');

INSERT INTO names(name) VALUES
    ('Ivan'),
    ('Petr'),
    ('Sidor');

INSERT INTO patronymics(patronymic) VALUES
    ('Ivanovich'),
    ('Petrovich'),
    ('Sidorovich');

SELECT s.surname, n.name, p.patronymic 
FROM surnames s, names n, patronymics p
WHERE s.person_id = n.person_id and s.person_id = p.person_id
ORDER BY s.surname DESC;