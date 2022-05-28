
import app
import unittest

class MyTestCase(unittest.TestCase):
	def setUp(self):
		app.app.testing = True
		self.app = app.app.test_client()

	def test_home(self):
		result = result = self.app.get('/')
		self.assertTrue(result, True)

if __name__ == "__main__":
	unittest.main()