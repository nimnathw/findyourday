import unittest

import mock

import findyourday.functions


class TestFunctions(unittest.TestCase):


    @mock.patch('findyourday.functions.user_input', return_value = '29/12/1974')
    def test_gooddata(self, mocked_input):
        self.assertEqual(findyourday.functions.find_day(), 'Sunday')


    @mock.patch('findyourday.functions.user_input', return_value = 'asd12/12')
    @mock.patch('findyourday.functions.find_day', return_value = 'IncludesStringError')
    def test_withstrings(self, mocked_function, mocked_input):
        findyourday.functions.find_day()
        self.assertIsNotNone(mocked_function)
        mocked_function.assert_called_with()
        mocked_function.assert_called_once_with()

        mocked_function.reset_mock()
        mocked_function.assert_not_called()
        

    @mock.patch('findyourday.functions.user_input', return_value = '12\12\1222')
    @mock.patch('findyourday.functions.find_day', return_value = 'IncludesBackslash Error')
    def test_withbackslashes(self, mocked_function, mocked_input):
        mocked_function()
        self.assertIsNotNone(mocked_function)
        assert mocked_function.called
        mocked_function.assert_called_with()
        mocked_function.assert_called_once_with()

        mocked_function.reset_mock()
        mocked_function.assert_not_called()


    @mock.patch('findyourday.functions.user_input', return_value = '1234124')
    @mock.patch('findyourday.functions.find_day', return_value = 'Value Error')
    def test_allnumbers(self, mocked_function, mocked_input):
        find_day_called = mocked_function()
        self.assertIsNotNone(mocked_function)
        assert mocked_function.called
        mocked_function.assert_called_with()
        mocked_function.assert_called_once_with()

        mocked_function.reset_mock()
        mocked_function.assert_not_called()


if __name__ == '__main__':
    unittest.main()
