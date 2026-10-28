print("Hello from Adri")
print("Code shared using GitHub")

# decorator ex:
def check(mm):
    def kit():
        print("Starting")
        mm()
        mm()
        print("Ending")
    return kit    
@check
def oii():
    print("Calling")
oii()   


# Generator
