import os
import time


class TestMixin:
    def start_test(self):
        self.start_time = time.monotonic()
        print("Starting test...............................................")
        time.sleep(0.2)  # wait for 1 second
        os.environ.pop('FLASK_ENV', None)

    def setUp(self):
        super().setUp()
        self.start_test()

        print(
            f"Running test: {self.test_name} - "
            f"{self._testMethodName} - {time.monotonic() - self.start_time:.3f} seconds")
        print(f"{self._testMethodName} - completed.\n\n")
