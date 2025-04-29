import os
import sys

if 'AUTH_KEY' not in os.environ:
    print("You do not have AUTH_KEY set in your environment",file=sys.stderr)
    sys.exit(1)
else:
    AUTH_KEY = os.environ['AUTH_KEY']
