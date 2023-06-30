class Settings:
    db_user = "postgres"
    db_password = "postgres"
    db_address = "localhost"
    db_name = "postgres"
    db_port = "5432"

    db_host = f"postgresql+psycopg2://{db_user}:{db_password}@{db_address}:{db_port}/{db_name}"
