-- Script that creates an index idx_name_first_score on the tabe names and
-- firstletter of the name and the score
CREATE INDEX idx_name_first_score on names(name(1), score)
