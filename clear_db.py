import dotenv
import os
import psycopg

dotenv.load_dotenv()
conn_str = f"postgresql://{os.environ.get('PGSQL_USERNAME')}:{os.environ.get('PGSQL_PASSWORD')}@{os.environ.get('PGSQL_HOST')}:{os.environ.get('PGSQL_PORT')}/{os.environ.get('PGSQL_NAME')}?sslmode=require&channel_binding=require"
try:
    with psycopg.connect(conn_str) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM ingested_documents")
            docs = cur.fetchall()
            print("Documents before deletion:", docs)
            
            cur.execute("DELETE FROM ingested_documents")
            conn.commit()
            print("Deleted all documents from Postgres.")
except Exception as e:
    print(f"Error: {e}")
