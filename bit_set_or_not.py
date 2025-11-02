n=13
i=1
if n & 1<<i:
    print(f"Yes {i}th bit set bit")
else:
    print("Not set")


if 1 & n>>i:
    print(f"Yes {i}th bit set bit")
else:
    print("Not set")
