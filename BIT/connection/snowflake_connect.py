import snowflake.connector
from config.settings import *

class SnowflakeConnection:
    def __init__(self):
        # Connection initialization
        self.connection = self._connect_to_snowflake()

    def _connect_to_snowflake(self):
        # DB connect in Snowflake
        return snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )

    def fetch_data_from_default(self, limit=100):
        # Fetch data from the default table
        query = f"SELECT * FROM {SNOWFLAKE_DEFAULT_TABLE} LIMIT {limit}"
        return self.fetch_data(query)

    def fetch_data(self, query):
        try:
            cur = self.connection.cursor()
            cur.execute(query)
            return cur.fetchall()
        except Exception as e:
            print(f"Warning!! Something went wrong: {e}")
            raise
        finally:
            cur.close()

    def save_data(self, transformed_data):
        # Convert 'NULL' string in timestamp columns to actual None
        for idx, row in enumerate(transformed_data):
            transformed_data[idx] = tuple([None if item == 'NULL' else item for item in row])

        try:
            cur = self.connection.cursor()
            
            insert_query = """
                INSERT INTO LeadEvents (Id, EventType, EventEmployee, EventDate, LeadId, UpdatedDateUtc)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            cur.executemany(insert_query, transformed_data)
            
            # Final commiting for initialization
            self.connection.commit()

        except Exception as e:
            print(f"Something went wrong while saving data: {e}")

            # Adding Rollback if there is any error
            self.connection.rollback()
            raise
        finally:
            cur.close()
