import unittest
from unittest.mock import MagicMock, patch
from pyspark.sql import DataFrame
from app.app import Incremental 

class TestSparkDataFrame(unittest.TestCase):
    @patch("pyspark.sql.session.SparkSession")
    def test_dataframe_count(self, mock_spark_session):

        mock_spark_session._instantiatedSession.createDataFrame. \
        return_value.select. \
        return_value.distinct. \
        return_value.count.return_value = 1

        incremental_service = Incremental()

        try:
            incremental_service.execute_service()
        except:
            self.fail()
        
