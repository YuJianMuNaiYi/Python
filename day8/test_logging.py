import logging
import  pdb
# logging.basicConfig(level=logging.info)

def foo(s):
    pdb.set_trace()
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('End ...')
