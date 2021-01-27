from socket import *
import time
startTime = time.time()

if __name__ == "__main__":
    target = input('enter host for scanning:')
    t_IP = gethostbyname(target)
    print('Starting scan on host: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()
print("time taken:", time.time() - startTime)
