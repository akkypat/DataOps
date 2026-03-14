from yoyo import step

steps = [
    step(
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """,
        """
        DROP TABLE IF EXISTS users;
        """
    )
]
