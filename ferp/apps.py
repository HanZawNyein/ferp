import os
from ferp.core.config import settings
from itertools import chain
import sys

# Define the directory to start searching
APPS = [
    # ('/groups', groups_app)
]


def find_apps_py_files(directory):
    apps_py_files = []

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename == 'main.py':
                apps_py_files.append([root.split('/')[-1], os.path.join(root, filename)])
    return apps_py_files


sys.path.extend(settings.addons_path)
flattened_list = list(chain.from_iterable([find_apps_py_files(addons_path) for addons_path in settings.addons_path]))
for APP_NAME, flattened in flattened_list:
    app = __import__(APP_NAME)
    try:
        APPS.append(
            (f'/{APP_NAME}', app.main.app)
        )
    except AttributeError as e:
        continue

if __name__ == "__main__":
    print(APPS)
