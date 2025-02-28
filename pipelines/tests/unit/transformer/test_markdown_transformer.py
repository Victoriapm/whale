import logging
import unittest

from pyhocon import ConfigFactory
from typing import Dict, Iterable, Any, Callable  # noqa: F401

from whale.models.table_metadata import TableMetadata, ColumnMetadata
from whale.transformer.markdown_transformer import MarkdownTransformer


DATABASE = 'mock_database'
CLUSTER = 'mock_cluster'
SCHEMA = 'mock_schema'
TABLE = 'mock_table'
COLUMN = 'mock_column'
COLUMN_DESCRIPTION = 'mock_column_description'


class TestMarkdownTransformer(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self._conf = ConfigFactory.from_dict({
            'base_directory': './.test_artifacts',
            })

    def test_transformed_record_contains_components(self):
        """
        """
        column = ColumnMetadata(
            name=COLUMN,
            col_type="Integer",
            sort_order=0,
            description=COLUMN_DESCRIPTION,
        )
        record = TableMetadata(
            database=DATABASE,
            cluster=CLUSTER,
            schema=SCHEMA,
            name=TABLE,
            columns=[column]
        )
        components = [
            DATABASE,
            CLUSTER,
            SCHEMA,
            TABLE,
            COLUMN,
            COLUMN_DESCRIPTION,
        ]
        transformer = MarkdownTransformer()
        transformer.init(self._conf)
        transformed_record = transformer.transform(record)
        markdown_blob = transformed_record.markdown_blob
        transformer.close()

        has_components = \
            all(x in markdown_blob for x in components)

        self.assertEqual(has_components, True)
