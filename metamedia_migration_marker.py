# Enhanced Cross Domain Media Artwork Migration Script

from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.orm import sessionmaker

# Define your database connection strings
source_db_url = 'postgresql://user:password@host:port/source_db'
destination_db_url = 'mysql+pymysql://user:password@host:port/destination_db'

# Create database engines
source_engine = create_engine(source_db_url)
dest_engine = create_engine(destination_db_url)

# Create session makers
SourceSession = sessionmaker(bind=source_engine)
DestSession = sessionmaker(bind=dest_engine)

# Initialize sessions
source_session = SourceSession()
dest_session = DestSession()

# Reflect tables from source and destination databases
metadata_source = MetaData(bind=source_engine)
metadata_dest = MetaData(bind=dest_engine)

# Replace 'did_table' with your actual table name
table_name = 'did_klib'
source_table = Table(table_name, metadata_source, autoload_with=source_engine)
dest_table = Table(table_name, metadata_dest, autoload_with=dest_engine)

try:
    # Fetch data from source
    source_data = source_session.execute(select([source_table])).fetchall()

    # Insert data into destination
    for row in source_data:
        insert_stmt = dest_table.insert().values(**dict(row))
        dest_session.execute(insert_stmt)

    # Commit the transaction
    dest_session.commit()
    print(f"Data migration of table '{table_name}' completed successfully.")
except Exception as e:
    print(f"Error during migration: {e}")
    dest_session.rollback()
finally:
    # Close sessions
    source_session.close()
    dest_session.close()
