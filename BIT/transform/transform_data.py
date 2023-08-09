import uuid
from datetime import datetime

def transform(data):
    """
    Transforms the input data by applying specific transformations on each row.

    For each row in the input data:
    - Applies the `transform_lead_data` function to transform the row.
    - Filters out any rows that are transformed to None.

    Returns:
    - list: A list of transformed rows.
    """
    transformed_data = [transform_lead_data(row) for row in data if transform_lead_data(row) is not None]
    return transformed_data

def transform_lead_data(row):
    try:
        # Extracting columns
        lead_id, state, created_employee, cancellation_requested_employee, cancellation_employee, cancellation_rejection_employee, created_date, cancellation_request_date, cancellation_date, cancellation_rejection_date = row
        
        # Using a dictionary to determine the event type and the relevant columns based on the required state as per task
        states = {
            '0': ('LeadSold', created_employee, created_date),
            '1': ('LeadRequestedCancellation', 'Unknown', cancellation_request_date),
            '2': ('LeadCancelled', cancellation_employee, cancellation_date),
            '3': ('LeadCancellationRejected', 'Unknown', cancellation_rejection_date)
        }
        
        event_type, event_employee, event_date = states.get(state, ('Unknown', 'Unknown', 'Unknown'))
        
        # Convert date format if the date is not 'Unknown' or None
        event_date = format_datetime_for_snowflake(event_date) if event_date not in ['Unknown', None] else event_date
        updated_date_utc = format_datetime_for_snowflake(cancellation_rejection_date) if cancellation_rejection_date not in ['Unknown', None] else cancellation_rejection_date
        
        # Generate unique UUID
        id = str(uuid.uuid4())
        
        return (id, event_type, event_employee, event_date, lead_id, updated_date_utc)
    
    except ValueError as e:
        print(f"Skipping problematic row: {row}")
        return None

def format_datetime_for_snowflake(date_str):

    # This will be inserted as NULL in Snowflake
    if date_str in ['NULL', 'Unknown']:
        return None  
    
    try:
        # Convert from 'M/D/YYYY H:M' format
        date_obj = datetime.strptime(date_str, '%m/%d/%Y %H:%M')
    except:
        try:
            # Converting again to another 'YYYY-MM-DD H:M:S' format
            date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        except Exception as e:
            print(f"Excluding invalid timestamp value: {date_str}")

    return date_obj.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
