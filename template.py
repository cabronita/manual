#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input', help='Input parameter')
parser.add_argument('-s', '--some_integer', default=0, help='some optional parameter', metavar='SOME_INT', type=int)
parser.add_argument('-v', '--verbosity', action='count', default=0,
                    help='increase output verbosity (-vv for debug)')
args = parser.parse_args()
