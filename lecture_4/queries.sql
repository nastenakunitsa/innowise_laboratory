-- ================================
-- Включаем поддержку внешних ключей
-- ================================
PRAGMA foreign_keys = ON;

-- ================================
-- 1. Создание таблиц
-- ================================
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY,
  full_name TEXT NOT NULL,
  birth_year INTEGER NOT NULL CHECK (birth_year > 1900)
);

CREATE TABLE IF NOT EXISTS grades (
  id INTEGER PRIMARY KEY,
  student_id INTEGER NOT NULL,
  subject TEXT NOT NULL,
  grade INTEGER NOT NULL CHECK (grade BETWEEN 1 AND 100),
  FOREIGN KEY (student_id) REFERENCES students(id)
);

-- ================================
-- 2. Вставка данных
-- ================================
INSERT INTO students (full_name, birth_year) VALUES
  ('Alice Johnson', 2005),
  ('Brian Smith', 2004),
  ('Carla Reyes', 2006),
  ('Daniel Kim', 2005),
  ('Eva Thompson', 2003),
  ('Felix Nguyen', 2007),
  ('Grace Patel', 2005),
  ('Henry Lopez', 2004),
  ('Isabella Martinez', 2006);

INSERT INTO grades (student_id, subject, grade) VALUES
  (1, 'Math', 88),
  (1, 'English', 92),
  (1, 'Science', 85),
  (2, 'Math', 75),
  (2, 'History', 83),
  (2, 'English', 79),
  (3, 'Science', 95),
  (3, 'Math', 91),
  (3, 'Art', 89),
  (4, 'Math', 84),
  (4, 'Science', 88),
  (4, 'Physical Education', 93),
  (5, 'English', 90),
  (5, 'History', 85),
  (5, 'Math', 88),
  (6, 'Science', 72),
  (6, 'Math', 78),
  (6, 'English', 81),
  (7, 'Art', 94);

-- ================================
-- 3. Запросы по заданию
-- ================================

-- 3.1 Все оценки Alice Johnson
SELECT g.subject, g.grade
FROM grades g
JOIN students s ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson';

-- 3.2 Средняя оценка каждого студента
SELECT s.full_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.full_name;

-- 3.3 Студенты, рождённые после 2004
SELECT full_name, birth_year
FROM students
WHERE birth_year > 2004;

-- 3.4 Средняя оценка по предметам
SELECT subject, AVG(grade) AS avg_grade
FROM grades
GROUP BY subject;

-- 3.5 Топ-3 студентов по среднему баллу
SELECT s.full_name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON g.student_id = s.id
GROUP BY s.id, s.full_name
ORDER BY avg_grade DESC
LIMIT 3;

-- 3.6 Студенты с оценкой ниже 80
SELECT DISTINCT s.full_name
FROM students s
JOIN grades g ON g.student_id = s.id
WHERE g.grade < 80;

-- ================================
-- 4. Индексы (опционально)
-- ================================
CREATE INDEX IF NOT EXISTS idx_grades_student_id ON grades(student_id);
CREATE INDEX IF NOT EXISTS idx_grades_subject ON grades(subject);
CREATE INDEX IF NOT EXISTS idx_students_full_name ON students(full_name);
