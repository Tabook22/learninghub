/****------- MySQL ------****/
/*Creating user table*/
CREATE TABLE user (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    username VARCHAR(80) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    user_type VARCHAR(50) NOT NULL DEFAULT 'user',
    PRIMARY KEY (id),
    UNIQUE INDEX user_email_key (email),
    UNIQUE INDEX user_username_key (username)
);