import psycopg

with psycopg.connect("host=localhost port=5432 user=postgres password=docker") as conn:
    with conn.cursor() as cur:
        try:
            cur.execute("""
                        CREATE SCHEMA IF NOT EXISTS main
                        """)
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS main.users (
                id text PRIMARY KEY,
                username text,
                password bytea,
                role text)
                """
            )
        except Exception as e:
            print("Error creating schema:", e)
        print("Created DB SCHEMA!")
