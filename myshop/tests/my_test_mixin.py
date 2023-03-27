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
            f"{self._testMethodName} - {time.monotonic() - self.start_time:.3f} seconds")
 #       time.sleep(0.1)
        print("\033[32m" + f"{self._testMethodName} - completed.\n\n" + "\033[0m")
        time.sleep(0.1)

    def setUp(self):
        super().setUp()
        self.start_test()


