pytest loads conftest.py files hierarchically from root to leaf directories, starting from the root conftest.py and proceeding to subdirectories.

Don't redefine fixtures from parent conftest.py.