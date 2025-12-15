import subprocess
import sys


def run_tests():
    print("запуск тестов...")

    result = subprocess.run([
        sys.executable, "-m", "pytest",
        "-v",
        "--tb=short",
        "tests/"
    ])

    if result.returncode == 0:
        print("\n✅ все тесты прошли успешно!")
    else:
        print("\n❌ есть ошибки в тестах")

    return result.returncode


if __name__ == '__main__':
    sys.exit(run_tests())