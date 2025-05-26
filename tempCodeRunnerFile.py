        user = os.getenv("DB_USER", "postgres")
        pwd = quote_plus(os.getenv("DB_PASSWORD", "2005_Gokul"))  # match your Docker password
        name = os.getenv("DB_NAME", "vectordb")                   # match your Docker DB name
        host = os.getenv("DB_HOST", "localhost:5435")             # your new port

