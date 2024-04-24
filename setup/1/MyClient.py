import Pyro4

def main():
    try:
        uri = "PYRONAME:MyRemoteClass"
        obj = Pyro4.Proxy(uri)
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("The Addition is:", obj.addition(a, b))
        print("The Multiplication is:", obj.mult(a, b))
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
