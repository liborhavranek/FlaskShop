import os
import time


class TestMixin:
    def start_test(self):
        self.start_time = time.monotonic()
        print("\033[91mStarting test...............................................\033[0m")
#        time.sleep(0.1)
        os.environ.pop('FLASK_ENV', None)

        print(
            f"Running test: {self.test_name} - "
            f"{self._testMethodName} - TESTED")
        time.sleep(0.1)
        if self._outcome.success:
            print("\033[32m" + f"{self._testMethodName} - passed." + "\033[0m")
            print("\033[32m" + f"{self._testMethodName} - completed.\n\n" + "\033[0m")

        else:
            print("\033[31m" + f"{self._testMethodName} - failed." + "\033[0m")
            print("\033[31m" + f"{self._testMethodName} - completed.\n\n" + "\033[0m")

        time.sleep(0.8)


    def setUp(self):
        super().setUp()
        self.start_test()

    def subTest(self, **params):
        self.start_test()
        return super().subTest(**params)

