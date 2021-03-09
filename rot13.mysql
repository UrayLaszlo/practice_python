DROP TABLE student;

CREATE TABLE student (
    student_id INT AUTO_INCREMENT,
    name VARCHAR(50),
    major VARCHAR(20) DEFAULT 'undecided',
    PRIMARY KEY(student_id)
);
SELECT * 
FROM student;

INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Kate', 'Sociology');
INSERT INTO student(name, major) VALUES('Claire', 'Chemistry');
INSERT INTO student(name, major) VALUES('Jack', 'Biology');
INSERT INTO student(name, major) VALUES('Mike', 'Computer Science');

SELECT *
FROM student
WHERE major = 'Chemistry'
ORDER BY major, student_id DESC
LIMIT 2;

SELECT *
FROM student
WHERE student_id > 2 AND name <> 'Jack';

SELECT *
FROM student
WHERE name IN ('Jack', 'Kate', 'Claire') AND student_id >= 2;

-- Comment hee
-- Logical operators: <, >, <=, >=, =, <>(isnot), AND, OR

UPDATE student
SET major = 'Bio'
WHERE major = 'Biology';

UPDATE student
SET major = 'BioChemistry'
WHERE major = 'Bio' OR major = 'Chemistry';

UPDATE student
SET name = 'Tom', major = 'undecided'
WHERE student_id = 1;

UPDATE student
SET major = 'undecided'

DELETE FROM student
WHERE student_id = 5;