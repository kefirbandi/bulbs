import unittest
from bulbs.tests import BulbsTestCase, suite
from bulbs.config import Config
from bulbs.neo4jserver import Neo4jResource, ExactIndex, NEO4J_URI
from index_tests import IndexTestCase

config = Config(NEO4J_URI)
BulbsTestCase.resource = Neo4jResource(config)
BulbsTestCase.index_class = ExactIndex

if __name__ == '__main__':
    suite = suite()
    suite.addTest(unittest.makeSuite(IndexTestCase))
    unittest.main(defaultTest='suite')