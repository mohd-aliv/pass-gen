import random
import string

def gen_pass(length):
    char=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(char) for _ in range(length))
    return password

def main():
    print("="*40)
    print("  Password generator")
    print("="*40)
    length=int(input("Password kitna lanba chaiye? (8-32): "))
    if length<8 or length > 32:
        print("8 se 32 ke bitch rakho!")
        return
    count=int(input("Kitne password chiye? (1-10):"))
    print("-"*40)
    print("\n App ke password :\n")
    print("-"*40)
    for i in range(count):
        pwd=gen_pass(length)
        print(f"    {i+1}.{pwd}")
    print("\n" + "=" *40)
if __name__=="__main__":
    main()

