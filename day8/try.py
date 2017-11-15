def Test():
    try:
        print('try...')
        r=10/int('2')
        print('result:',r)
    except ValueError as e:    # 捕获多个异常
        print('ValueError:',e)
    except ZeroDivisionError as  e:
        print('except:',e)
    else:                  # 没有错误发生时,可以这样写
        print('no Error..')
    finally:
        print('finally ...')
    print('End')

def Test1():
    try:
        print('try ...')
    except ValueError as e:
        print('ValueError...')
    except UnicodeEncodeError as  e:    # 此异常永远也捕获不到,按照Python异常的继承关系
        print('UnicodeError...')
    

Test()

