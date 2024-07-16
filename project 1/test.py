username = input("enter your name")
with open (f"{username}.txt") as f:
    f.write(f"{username}hiiii")