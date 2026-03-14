import polars as pl

from eco2doe import batch_report


def test_read_metadata():
    data = batch_report.read_metadata()
    assert isinstance(data, pl.DataFrame)


def test_batchreport():
    report = batch_report.BatchReport('tests/data/batchreport.tab')
    assert isinstance(report.wide_data, pl.DataFrame)
    assert isinstance(report.long_data, pl.DataFrame)
