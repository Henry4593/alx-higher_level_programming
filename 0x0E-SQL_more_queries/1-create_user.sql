-- Create user 'user_0d_1' on localhost with password 'user_0d_1_pwd' if it
-- doesn't exist.and grant all the privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';