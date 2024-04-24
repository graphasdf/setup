# 1. Implement multi-threaded client/server Process communication
# using RMI.

# pip install pyro4

# pyro4-ns  ---> tarminal command to run sever 

import Pyro4

@Pyro4.expose
class MyRemoteClass(object):
    def addition(self, x, y):
        return x + y

    def mult(self, x, y):
        return x * y

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(MyRemoteClass)
    ns.register("MyRemoteClass", uri)
    print("Server is ready.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
