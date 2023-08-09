from connection.snowflake_connect import SnowflakeConnection
from transform.transform_data import transform, format_datetime_for_snowflake

def main():
    # Setting things up
    snowflake_conn = SnowflakeConnection()
    
    # Getting our data. Wondering if there's a more efficient way?
    data = snowflake_conn.fetch_data("SELECT * FROM CompanyLeads")
    
    transformed_data = transform(data)
    
    for row in data:
        if 'CreatedDateUtc' in row and row['CreatedDateUtc']: 
            row['CreatedDateUtc'] = format_datetime_for_snowflake(row['CreatedDateUtc'])
    snowflake_conn.save_data(transformed_data)

if __name__ == "__main__":
    main()
