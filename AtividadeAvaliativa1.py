import math
import threading


def thread_func(num, ini, fim):
    global end
    #print('Thread', threading.get_ident(), 'verificando numero {} no intervalo {} a {}'.format(num, ini, fim-1))
    num_float = float(num)
    for i in range(int(ini), int(fim)):
        #print (i)
        if end: return False
        if (num_float / i).is_integer():
            #print (i, " - False \n")
            end = True
            return False
        #print(i, " - True\n")
    return True


def check_prime(num):
    global end
    end = False
    sqrt_num = math.sqrt(num)
    meio_num = int(sqrt_num / 2)

    if meio_num <= 2:
        meio_num = 3

    #Thread 1 com primeiro grupo de verificação
    t1 = threading.Thread(target=thread_func, args=(num, 2, meio_num))
    t1.start()
    #Tread 2 com segundo grupo de verificação
    t2 = threading.Thread(target=thread_func, args=(num, meio_num, int(sqrt_num)+1))
    t2.start()

    t1.join()
    t2.join()

    if end:
        #print("O número {} não é primo.".format(num))
        return False
    else:
        #print("O número {} é primo.".format(num))
        return True


if __name__ == "__main__":
    print(check_prime(10000000))