import os
import sys
import time


class TestMixin:
    def start_test(self):
        self.start_time = time.monotonic()
        print("\033[91mStarting test......................................................................\033[0m")
        time.sleep(0.2)
        total_width = 70  # Set the total width of the progress bar
        for i in range(8):
            percent_complete = (i + 1) * 12.5
            num_hashes = round(percent_complete * total_width / 100)
            progress_bar = "#" * num_hashes + "." * (total_width - num_hashes)
            sys.stdout.write(f"\rTesting {progress_bar} {percent_complete:>3} %")
            sys.stdout.flush()
            time.sleep(0.1)
        os.environ.pop('FLASK_ENV', None)

        if self._outcome.success:
            print(
                f"\nRunning test: {self.test_name} - "
                f"{self._testMethodName} - \033[32mPASSED\033[0m")

        else:
            print(
                f"\nRunning test: {self.test_name} - "
                f"{self._testMethodName} - \033[31mFAILED\033[0m")

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

