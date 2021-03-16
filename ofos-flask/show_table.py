import sys
from mysql_module_lib import *

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("required parameter: [table_name]")
        exit()

    show_table(sys.argv[1])