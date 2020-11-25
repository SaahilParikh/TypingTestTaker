import random
def ipv4Gen():
        ip = str(random.randint(0, 256))
        for i in range (3):
            ip = str(random.randint(0, 256)) + '.' + ip

        return ip
