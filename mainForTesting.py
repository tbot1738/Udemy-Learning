from multiprocessing.sharedctypes import Value


def do_smth(num):
    try:
        return int(num)+5
    except ValueError as err:
        return err
