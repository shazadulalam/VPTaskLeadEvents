# VPTaskLeadEvents

The `VPTaskLeadEvents` task focuses on refining how a lead's life cycle in the VP Verbund Pflegehilfe GmbH system. By transitioning to the 'LeadEvents' table in Snowflake, every significant event in a lead's journey will be individually recorded, providing granular insights into the lead's progression.

## Task Summary

Currently, the task focuses on improving how to display the life cycle of a lead. At the moment, each lead's status changes are recorded in a single row. The intention of this task is to migrate to Snowflake's 'LeadEvents' table, where each event in a lead's journey is uniquely recorded. To do this, Azure Data Factory will be used to transfer 100 leads from an Excel data source in SQL to Snowflake. The data will then be transformed by a Python project, offering a detailed, event-by-event snapshot of each lead's evolution. This improved representation attempts to increase the depth and clarity of the analysis.

## Project Details

### 1. **Data Extraction & Migration:**
- **Azure Data Factory** is used to extract 100 leads from an Excel data source stored in SQL.
- These leads are then migrated to Snowflake for further processing.

### 2. **Data Transformation with Python:**
- A dedicated Python project is set up to transform the fetched data.
- The transformation offers a granular view, recording each significant event in the lead's journey.

### 3. **Final Storage:**
- The transformed data is saved into the 'LeadEvents' table in Snowflake.

## Getting Started

### Pre-requisites

- Python 3.8 or later
- Snowflake account credentials
- Azure Data Factory configured for the data source
- To create the same architecture, use queries from Queries folder

### Documentation
Complete A to Z documentation about how to build the pipeline and how to deploy are elaborately ecplained in the file name 
"Setting Up an Azure Data Factory Pipeline.pdf"


### Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [repository-url]
   cd [repository-directory]
   
2. **Set up a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

### Python Project Structure
    ´´
    BIT/
    |-- requirements.txt
    |-- config/
    |   `-- settings.py
    |-- connectors/
    |   `-- snowflake_connector.py
    |-- transformations/
    |   `-- data_transform.py
    `-- main.py




### Usage

1. Update the `config/settings.py` with the appropriate Snowflake credentials and configurations.
   ```bash
    SNOWFLAKE_ACCOUNT = 'YourAccountID: e.g, {nm123456}.{us-east}.azure'
    SNOWFLAKE_USER = 'YourSnowflakeUserName'
    SNOWFLAKE_PASSWORD = 'YourPassword'
    SNOWFLAKE_DATABASE = 'NameOfYourDB'
    SNOWFLAKE_SCHEMA = 'YourSchemaName'
    SNOWFLAKE_WAREHOUSE = 'YourWarehouseName'


3. Run the main Python script to initiate the data transformation process:

```bash
   python main.py






