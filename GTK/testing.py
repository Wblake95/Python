def signCheck(text):
    check = ["*", "/", "+","-"]
    if text[-1] in check:
        print("text[-1] in check")
        return False
