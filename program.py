import sys

def default():
    print("Hello")

def cat():
    print("Mnau")

def dog():
    print("Haf")

def main():
    if sys.argv[1] == "cat":
        cat()
    elif sys.argv[1] == "dog":
        dog()
    else:
        default()

if __name__ == "__main__":
    main()
