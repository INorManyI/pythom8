import unittest
from unittest.mock import patch
from io import StringIO

def binary_search(arr, key):
    print(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return -1

def main():
    try:
        n = int(input("Введите размер массива: "))
        if n > 10 or n < 1:
            print("Размер массива вне диапазона!")
            return
        
        print("Теперь вводите элементы массива!")
        array = []
        for i in range(n):
            element = int(input(f"Введите {i+1}-й элемент: "))
            array.append(element)
        
        array.sort() 
        
        key = int(input("Введите ключ: "))
        
        result = binary_search(array, key)
        if result != -1:
            print(f"Элемент {key} найден по индексу {result}.")
        else:
            print(f"Элемент {key} не найден в массиве.")
        
    except Exception:
        print("Некорректные данные")

class test_correct_input(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO) 
    def test_correct_array_size_1(self, mock_stdout):
        with patch('builtins.input', side_effect=['1', '5', '5']):
            main()
            self.assertIn("Элемент 5 найден по индексу 0.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_correct_array_size_10(self, mock_stdout):
        with patch('builtins.input', side_effect=['10', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '5']):
            main()
            self.assertIn("Элемент 5 найден по индексу 4.", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_correct_array_size(self, mock_stdout):
        with patch('builtins.input', side_effect=['4', '2', '4', '6', '8', '6']):
            main()
            self.assertIn("Элемент 6 найден по индексу 2.", mock_stdout.getvalue())
            
class test_incorrect_input(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_array_size_0(self, mock_stdout):
        with patch('builtins.input', side_effect=['0']):
            main()
            self.assertIn("Размер массива вне диапазона!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_array111(self, mock_stdout):
        with patch('builtins.input', side_effect=['1', 'dsfngk' , '1']):
            main()
            self.assertIn("Некорректные данные", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_array222(self, mock_stdout):
        with patch('builtins.input', side_effect=['1', '?', '1']):
            main()
            self.assertIn("Некорректные данные", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_array333(self, mock_stdout):
        with patch('builtins.input', side_effect=['1', '1', 'ваьдлпавл']):
            main()
            self.assertIn("Некорректные данные", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_array444(self, mock_stdout):
        with patch('builtins.input', side_effect=['1', '1', '?']):
            main()
            self.assertIn("Некорректные данные", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_array_size_11(self, mock_stdout):
        with patch('builtins.input', side_effect=['11']):
            main()
            self.assertIn("Размер массива вне диапазона!", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_array_size_srt(self, mock_stdout):
        with patch('builtins.input', side_effect=['вапвчыр']):
            main()
            self.assertIn("Некорректные данные", mock_stdout.getvalue())


                   
    @patch('sys.stdout', new_callable=StringIO)
    def test_incorrect_array_size_float(self, mock_stdout):
        with patch('builtins.input', side_effect=['3.5']):
            main()
            self.assertIn("Некорректные данные", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()