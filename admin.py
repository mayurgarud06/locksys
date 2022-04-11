def auth(name):
    n = input(f"System is being accessed by {name}\nDo you want approve it?(Y/N)")
    if n.lower()=="y":
        return True
    else:
        return False