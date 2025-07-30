CREATE TABLE POTS (
    category TEXT,
    description TEXT
);

CREATE TABLE PostCovidDysautonomia (
    category TEXT,
    description TEXT
);
INSERT INTO POTS (category, description) VALUES
('Trigger', 'Often follows viral infection, surgery, or trauma'),
('System Affected', 'Autonomic nervous system'),
('Heart Rate Change', 'HR increase ≥30 bpm (≥40 bpm in teens) within 10 minutes of standing'),
('Symptoms', 'Tachycardia, dizziness, fatigue, brain fog, nausea, exercise intolerance'),
('Demographics', 'More common in females, ages 15–50'),
('Diagnosis', 'Tilt table test, 10-minute stand test'),
('Treatment', 'Fluids, salt, compression, exercise, medications');




INSERT INTO PostCovidDysautonomia (category, description) VALUES
('Trigger', 'Triggered specifically by COVID-19 infection'),
('System Affected', 'Autonomic nervous system'),
('Heart Rate Change', 'Same pattern—HR increase on standing'),
('Symptoms', 'Tachycardia, dizziness, fatigue, brain fog, chest pain, shortness of breath'),
('Demographics', 'Similar profile—especially young women'),
('Diagnosis', 'Tilt table test, 10-minute stand test'),
('Treatment', 'Similar strategies: fluids, salt, compression, exercise, medications');

SELECT 
    p.category,
    p.description AS POTS_Description,
    pc.description AS PostCOVID_Description
FROM 
    POTS p
JOIN 
    PostCovidDysautonomia pc ON p.category = pc.category;
