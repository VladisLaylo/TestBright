import sys

print(sys.version_info)
print(sys.version)


hy_dig = int(input("Guess the number: "))

if hy_dig > 100:
    print(f"{'Integer'} {hy_dig} {'more then 100'}")
elif hy_dig < 100:
    print(f"{'Integer'} {hy_dig} {'less then 100'}")
elif hy_dig == 100:
    print(f"{'Integer'} {hy_dig} {'= 100'}")
else:
    print("Who knows?")