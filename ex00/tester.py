from S1E9 import Character, Stark


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)

    print("---")

    lyanna = Stark("Lyanna", False)
    print(lyanna.__dict__)

    print("---")

    try:
        hodor = Character("Hodor")
        hodor.die() #just to skip flake8 error (unused variable)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
