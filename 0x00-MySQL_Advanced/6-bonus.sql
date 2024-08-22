-- script that creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Check if the project exists
    DECLARE project_exists BOOLEAN;
    SELECT EXISTS(SELECT 1 FROM projects WHERE name = project_name) INTO project_exists;

    IF NOT project_exists THEN
        -- Project does not exist, insert a new project
        INSERT INTO projects (name) VALUES (project_name);
        SET @new_project_id = LAST_INSERT_ID();
    ELSE
        -- Project exists, get its ID
        SELECT id INTO @existing_project_id FROM projects WHERE name = project_name;
    END IF;

    -- Insert a new correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, IF(project_exists, @existing_project_id, @new_project_id), score);
END$$

DELIMITER ;
