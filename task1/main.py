# coding: utf-8


# I use sqlalchemy and ORM to insert the data
# I will use sqlite as a RDBMS 


import operator
from data_loader import load_data_to_dictionary
from sqlalchemy import create_engine


def reset_tables(engine):
    engine.execute("""drop table if exists measurements""")
    engine.execute("""drop table if exists measures""")
    engine.execute("""drop table if exists counties""")
    engine.execute("""drop table if exists units""")

    # I keep created/updated data as integers for simplicity
    engine.execute("""
    CREATE TABLE IF NOT EXISTS measurements (
    sid INTEGER NOT NULL,
    "created_at" INTEGER NOT NULL,
    "created_meta" INTEGER NOT NULL,
    "updated_at" INTEGER NOT NULL,
    "updated_meta" INTEGER NOT NULL,


    "MeasureId" INTEGER NOT NULL, 
    "ReportYear" INTEGER NOT NULL, 
    "Value" FLOAT NOT NULL, 
    "CountyFips" INTEGER NOT NULL, 
    "Unit" VARCHAR NOT NULL,
    "DataOrigin" VARCHAR NOT NULL,

    PRIMARY KEY(sid), 
    FOREIGN KEY("MeasureId") REFERENCES measures ("MeasureId"),
    FOREIGN KEY("CountyFips") REFERENCES counties ("CountyFips")
    FOREIGN KEY("Unit") REFERENCES units ("Unit")
    )
    """)

    engine.execute("""
    CREATE TABLE IF NOT EXISTS measures (
    "MeasureId" INTEGER NOT NULL, 
    "MeasureName" VARCHAR NOT NULL, 
    "MeasureType" CARCHAR NOT NULL, 
    PRIMARY KEY (MeasureId)
    )
    """)

    # Assuming each county maps to exactly one state.
    # We could create a separate ralation to the state, but don't do it to save time.
    # let's assume we rarely query anything by state. Data on the highest resolution (per county) is more interesting
    engine.execute("""
    CREATE TABLE IF NOT EXISTS counties (
    "CountyFips" INTEGER NOT NULL, 
    "CountyName" VARCHAR NOT NULL, 
    "StateFips" INTEGER NOT NULL, 
    "StateName" VARCHAR NOT NULL, 
    PRIMARY KEY (CountyFips)
    )
    """)

    # It might be better to introduce an integer ID.
    engine.execute("""
    CREATE TABLE IF NOT EXISTS units (
    "Unit" Varchar NOT NULL, 
    "UnitName" VARCHAR NOT NULL, 
    PRIMARY KEY (Unit)
    )
    """)


def select_columns(dict_data, list_col_names):
    return tuple(dict_data[k] for k in list_col_names)


def insert_if_not_exists(connection, measurement, table, columns, id_column):
    r = connection.execute("select {columns} from {table} where {id_column}='{value}'".format(
        columns=','.join(columns),
        table=table,
        id_column=id_column,
        value=measurement[id_column]))
    # assuming input data is correct in terms of measureIds
    existing = r.first()
    if existing is None:
        insert(connection, measurement, table, columns)
    else:
        # here could be a check for inconsistent data
        pass


def insert(connection, measurement, table, columns):
    connection.execute("INSERT INTO '{table}' {columns} values {values}".format(
        table=table,
        columns=columns,
        values=select_columns(measurement, columns)))


def insert_data(data, engine, column_names, limit=None):
    reset_tables(engine)
    cols_measure = ("MeasureId", "MeasureName", "MeasureType")
    cols_measurement = ("sid", "MeasureId", "ReportYear", "Value", "CountyFips", "Unit",
                        "DataOrigin",
                        'created_at', 'created_meta', 'updated_at', 'updated_meta'
                        )
    cols_county = ("CountyFips", "CountyName", "StateFips", "StateName")
    cols_unit = ("Unit", "UnitName")

    for row in data[:limit]:
        with engine.begin() as connection:
            measurement = dict(zip(column_names, row))
            insert_if_not_exists(connection, measurement, 'measures', cols_measure, 'MeasureId')
            insert_if_not_exists(connection, measurement, 'counties', cols_county, 'CountyFips')
            insert_if_not_exists(connection, measurement, 'units', cols_unit, 'Unit')
            insert(connection, measurement, 'measurements', cols_measurement)


def test_missing_data():
    engine = create_engine('sqlite:///:memory:', echo=False)
    insert_data(data, engine, column_names, 1000)


def main():
    data_and_meta = load_data_to_dictionary()

    data, meta = data_and_meta['data'], data_and_meta['meta']
    assert all(type(x) == list for x in data)

    column_names = list(map(operator.itemgetter('name'), meta['view']['columns']))
    engine = create_engine('sqlite:///local_db2.sqlite', echo=False)
    # engine = create_engine('postgres://postgres:postgres@localhost:5432/postgres', echo=False)
    insert_data(data, engine, column_names, 1000)


if __name__ == '__main__':
    main()
