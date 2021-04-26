#!/usr/bin/python3

import json
import sys

from codestream_parser import caifile


def main():
    with open(sys.argv[1], 'rb') as f:
        cai_json = caifile.get_cai_json_from_f(f)
        print(json.dumps(cai_json, indent=4))


if __name__ == '__main__':
    main()