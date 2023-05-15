from django.test import TestCase


class TestURLs(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Ran once before any test methods"""
        pass

    def setUp(self) -> None:
        """Ran prior to every test method"""
        pass

    def tearDown(self) -> None:
        """Ran following every test method"""
        pass

    def test_true(self):
        return self.assertTrue(True)

    def test_false(self):
        return self.assertFalse(False)

    def test_equal(self):
        return self.assertEquals(1, 1)
