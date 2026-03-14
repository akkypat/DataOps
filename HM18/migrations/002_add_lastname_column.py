from yoyo import step

steps = [
    step(
        """
        ALTER TABLE users
        ADD COLUMN lastname VARCHAR(100);
        """,
        """
        ALTER TABLE users
        DROP COLUMN IF EXISTS lastname;
        """
    )
]
