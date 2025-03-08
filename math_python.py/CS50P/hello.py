#first function

def main():

    name = input("whats your name?").strip().title()
    hello(name)


def hello(to):

	print(f"hello,", to) 

    # say hello to use
main()