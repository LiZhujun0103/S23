
import os,sys

Basedir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(Basedir)

from lib import show

if __name__ == '__main__':
    show.show()