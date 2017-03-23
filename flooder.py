import sys

from flooder.menti_flooder import MentiFlooder

if __name__ == "__main__":
    if len(sys.argv) == 2:
        flooder = MentiFlooder(sys.argv[1])
        flooder.retrieve_questions()
        flooder.send_responses()
