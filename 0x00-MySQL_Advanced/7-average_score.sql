-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes
-- and store the average score for a student. Note: An average score can be a decimal
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Declare variables to hold the sum of scores and the count of scores
    DECLARE total_score INT DEFAULT 0;
    DECLARE num_scores INT DEFAULT 0;

    -- Calculate the total score and the number of scores for the given user
    SELECT SUM(score), COUNT(*) INTO total_score, num_scores
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average score
    IF num_scores > 0 THEN
        SET @average_score = total_score / num_scores;
    ELSE
        SET @average_score = 0; -- Default to 0 if there are no scores
    END IF;

    -- Update the user's average score
    UPDATE users
    SET average_score = @average_score
    WHERE id = user_id;
END$$

DELIMITER ;
