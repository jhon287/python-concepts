"""Python Concepts I Wish I Knew Way Earlier"""
from unittest import TestCase
from typing import Any
from multiprocessing import Pool
from dog import Dog


# See multiprocessing below 👇😉
def your_funtion(number: int) -> int:
    """Your Function"""
    return number**2


# pylint: disable=unnecessary-lambda-assignment
square = lambda number: number**2


class Test(TestCase):
    """Python Concepts Tests"""

    # Tuple Unpacking
    def test_tuple_unpacking(self):
        """Tuple Unpacking"""
        person = ["bob", 30, "male"]
        name, age, gender = person

        self.assertEqual(first=name, second="bob")
        self.assertEqual(first=age, second=30)
        self.assertEqual(first=gender, second="male")

    # Tuple Unpacking With *
    def test_tuple_unpacking_everything_else(self):
        """Tuple Unpacking Everything Else"""
        fruits = ["apple", "orange", "pear", "pineapple", "durian", "banana"]
        first, second, *others = fruits

        self.assertEqual(first=first, second="apple")
        self.assertEqual(first=second, second="orange")
        self.assertEqual(first=others, second=["pear", "pineapple", "durian", "banana"])

    # List Comprehension
    def test_list_comprehension(self):
        """List Comprehension"""
        # pylint: disable=unnecessary-comprehension
        list_1 = [i for i in range(1, 4)]
        list_2 = [i * 2 for i in range(1, 4)]
        list_3 = [i**2 for i in range(1, 4)]
        list_4 = [i for i in range(1, 4) if i % 2 == 1]

        self.assertEqual(first=list_1, second=[1, 2, 3])
        self.assertEqual(first=list_2, second=[2, 4, 6])
        self.assertEqual(first=list_3, second=[1, 4, 9])
        self.assertEqual(first=list_4, second=[1, 3])

    # Set Comprehension
    def test_set_comprehension(self):
        """Set Comprehension"""
        # pylint: disable=unnecessary-comprehension
        set_1 = {i for i in range(1, 4)}

        self.assertEqual(first=set_1, second={1, 2, 3})

    # Dict Comprehension
    def test_dict_comprehension(self):
        """Dictonary Comprehension"""
        dict_1 = {i: i**2 for i in range(1, 4)}

        self.assertEqual(first=dict_1, second={1: 1, 2: 4, 3: 9})

    # Ternary operator
    def test_ternary_operator(self):
        """Ternary Operator"""
        score: int = 57
        grade: str = "A*" if score > 90 else "pass" if score > 50 else "fail"

        self.assertEqual(first=grade, second="pass")

    # Magic Methods In Python Classes
    def test_magic_class_methods(self):
        """Magic Methods In Python Classes"""
        dog_1: Dog = Dog("rocky", 4)
        dog_2: Dog = Dog("fifi", 2)

        self.assertEqual(first=str(dog_1), second="Dog(name=rocky, age=4)")
        self.assertTrue(expr=dog_1 > dog_2)

    # *args
    def test_args(self):
        """Args (*args)"""

        def function_args(var_a: int, var_b: int, *args: int):
            self.assertEqual(first=var_a, second=1)
            self.assertEqual(first=var_b, second=2)
            self.assertEqual(first=args, second=(3, 4, 5))

        function_args(1, 2, 3, 4, 5)

    # **kwargs
    def test_kwargs(self):
        """Kwargs (**kwargs)"""

        def function_kwargs(var_a: int, var_b: int, **kwargs: int):
            self.assertEqual(first=var_a, second=1)
            self.assertEqual(first=var_b, second=2)
            self.assertEqual(first=kwargs, second={"c": 3, "d": 4})

        function_kwargs(var_a=1, var_b=2, c=3, d=4)

    # Truthy values
    def test_truthy_values(self):
        """Truthy Values"""
        truthy_values: list[Any] = [
            1,
            2,
            100,
            -1,
            3.14,
            "a",
            [1],
            {2: 3},
            {1, 2},
            Dog(name="rocky", age=4),
        ]
        for value in truthy_values:
            self.assertTrue(expr=value)

    # Falsy values
    def test_falsy_values(self):
        """Falsy Values"""
        falsy_values: list[Any] = [0, "", [], {}, set(), None]
        for value in falsy_values:
            self.assertFalse(expr=value)

    # Break vs continue vs pass
    def test_break_continue_pass(self):
        """Break vs continue vs pass"""

        def my_break(digits: list[int]) -> list[int]:
            """Break"""
            my_results: list[int] = []
            for digit in digits:
                if digit == 3:
                    break
                my_results.append(digit)
            return my_results

        def my_continue(digits: list[int]) -> list[int]:
            """Continue"""
            my_results: list[int] = []
            for digit in digits:
                if digit == 3:
                    continue
                my_results.append(digit)
            return my_results

        def my_pass(digits: list[int]) -> list[int]:
            """Pass"""
            my_results: list[int] = []
            for digit in digits:
                if digit == 3:
                    pass
                my_results.append(digit)
            return my_results

        my_digits: list[int] = range(1, 6)

        self.assertEqual(first=my_break(digits=my_digits), second=[1, 2])
        self.assertEqual(first=my_continue(digits=my_digits), second=[1, 2, 4, 5])
        self.assertEqual(first=my_pass(digits=my_digits), second=list(my_digits))

    # Try, except and finally blocks
    def test_try_expect_finally(self):
        """Try, except and finally blocks"""

        def my_try_expect(digit: int) -> float | str:
            """Try, Except"""
            try:
                my_result: float = 1 / digit
                return my_result
            except ZeroDivisionError:
                return "Zero Division Error !"

        def my_try_expect_finally(digit: int) -> float | str:
            """Try, Except and Finally"""
            try:
                my_result: float = 1 / digit
                return my_result
            except ZeroDivisionError:
                return "Error"
            finally:
                return "Finally Pouet..."  # pylint: disable=lost-exception

        self.assertEqual(first=my_try_expect(digit=2), second=1 / 2)
        self.assertEqual(first=my_try_expect(digit=0), second="Zero Division Error !")
        self.assertEqual(
            first=my_try_expect_finally(digit=0), second="Finally Pouet..."
        )

    # Decorators
    def test_decorators(self):
        """Decorators"""

        def add_exclamation_mark(your_function):
            """Add Exclamation Mark"""

            def inner(*args, **kwargs):
                return f"{your_function(*args, **kwargs)}!"

            return inner

        name: str = "Tim"

        @add_exclamation_mark
        def greet(name: str) -> str:
            return f"Hello {name}"

        self.assertEqual(first=greet(name=name), second=f"Hello {name}!")

    # Generators + the ‘yield’ Keyword
    def test_generators_the_yeild_keyword(self):
        """Generators + the ‘yield’ Keyword"""

        def simple_generator():
            yield "apple"
            yield "orange"
            yield "pear"

        self.assertEqual(
            first=list(simple_generator()),
            second=["apple", "orange", "pear"],
        )

    # Method chaining
    def test_method_chaining(self):
        """Method chaining"""
        sentence: str = " APPLE ORANGE PEAR "
        self.assertEqual(
            first=sentence.strip().lower().split(), second=["apple", "orange", "pear"]
        )

    # Lambda functions
    def test_lambda_functions(self):
        """Lambda functions"""

        def add(int_1: int, int_2: int):
            return int_1 + int_2

        def hello(name: str):
            return f"Hello {name}"

        def test(int_1: int, int_2: int, int_3: int, int_4: int):
            return (int_1 + int_2) / (int_3 - int_4)

        add_lambda = lambda int_1, int_2: int_1 + int_2
        hello_lambda = lambda name: f"Hello {name}"
        test_lambda = lambda int_1, int_2, int_3, int_4: (int_1 + int_2) / (
            int_3 - int_4
        )

        self.assertEqual(
            first=add(int_1=1, int_2=2), second=add_lambda(int_1=1, int_2=2)
        )
        self.assertEqual(first=hello(name="Tim"), second=hello_lambda(name="Tim"))
        self.assertEqual(
            first=test(int_1=1, int_2=2, int_3=3, int_4=4),
            second=test_lambda(int_1=1, int_2=2, int_3=3, int_4=4),
        )

    # Raise and custom exceptions
    def test_raise_custom_exceptions(self):
        """Raise and custom exceptions"""

        class ScoreException(Exception):
            """ScoreException Class"""

            def __init__(self):
                super().__init__("score cannot be higher than 100")

        score: int = 150
        with self.assertRaises(expected_exception=Exception):
            if score > 100:
                # pylint: disable=broad-exception-raised
                raise Exception("Score cannot be higher than 100!")
        with self.assertRaises(expected_exception=ScoreException):
            if score > 100:
                raise ScoreException()

    # Multiprocessing
    def test_multiprocessing(self):
        """Multiprocessing"""

        def run_pool(my_list=list[int]) -> list[int]:
            with Pool(processes=10) as pool:
                return pool.map(func=your_funtion, iterable=my_list)

        self.assertEqual(
            first=run_pool(list(range(50))), second=list(map(square, list(range(50))))
        )
