from sqlalchemy import create_engine

from main import insert_data

column_names = ['sid', 'id', 'position', 'created_at', 'created_meta', 'updated_at', 'updated_meta', 'meta',
                'MeasureId', 'MeasureName', 'MeasureType', 'StratificationLevel', 'StateFips', 'StateName',
                'CountyFips', 'CountyName', 'ReportYear', 'Value', 'Unit', 'UnitName', 'DataOrigin', 'MonitorOnly']


def test_correct_data():
    engine = create_engine('sqlite:///:memory:', echo=False)
    data = [
        [2, '0CEF0EA4-44D1-43F9-B7A3-BA8760697583', 2, 1439356237, '925122', 1439356237, '925122', None, '83',
         'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard',
         'Counts', 'State x County', '1', 'Alabama', '1051', 'Elmore', '1999', '5', 'No Units', 'No Units',
         'Monitor Only', '1'],
        [3, 'CA5C8F9E-7EC2-4E85-A30E-5A35FCFAACFB', 3, 1439356237, '925122', 1439356237, '925122', None, '83',
         'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard',
         'Counts', 'State x County', '1', 'Alabama', '1073', 'Jefferson', '1999', '39', 'No Units', 'No Units',
         'Monitor Only', '1']]
    num = insert_data(data, engine, column_names, None)

    measurements = engine.execute("SELECT * FROM measurements;").fetchall()
    assert measurements == [
        (2, 1439356237, 925122, 1439356237, 925122, 83, 1999, 5.0, 1051, 'No Units', 'Monitor Only'),
        (3, 1439356237, 925122, 1439356237, 925122, 83, 1999, 39.0, 1073, 'No Units', 'Monitor Only')
    ]

    measures = engine.execute("SELECT * FROM measures;").fetchall()
    assert measures == [
        (83, 'Number of days with maximum 8-hour average ozone concentration over '
             'the National Ambient Air Quality Standard', 'Counts')]

    assert num == 2


def test_empty_data():
    engine = create_engine('sqlite:///:memory:', echo=False)
    data = [
        [2, '0CEF0EA4-44D1-43F9-B7A3-BA8760697583', 2, 1439356237, '925122', 1439356237, '925122', None, '83',
         'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard',
         'Counts', 'State x County', '1', 'Alabama', '1051', 'Elmore', '1999', '5', 'No Units', 'No Units',
         'Monitor Only', '1'],
        [3, 'CA5C8F9E-7EC2-4E85-A30E-5A35FCFAACFB', 3, 1439356237, '925122', 1439356237, '925122', None, '83',
         'Number of days with maximum 8-hour average ozone concentration over the National Ambient Air Quality Standard',
         'Counts', 'State x County', '1', 'Alabama', '1073', 'Jefferson', None, '39', 'No Units', 'No Units',
         'Monitor Only', '1']]
    num = insert_data(data, engine, column_names, None)

    measurements = engine.execute("SELECT * FROM measurements;").fetchall()
    assert measurements == [
        (2, 1439356237, 925122, 1439356237, 925122, 83, 1999, 5.0, 1051, 'No Units', 'Monitor Only'),
    ]

    measures = engine.execute("SELECT * FROM measures;").fetchall()
    assert measures == [
        (83, 'Number of days with maximum 8-hour average ozone concentration over '
             'the National Ambient Air Quality Standard', 'Counts')]
    assert num == 1