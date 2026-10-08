import demo1
print(f"UsitName={__name__}")
def add():
    print(f"Addition={12+13}")
def add1():
    print(f"Addition1={12+13}")
def main():
    print("Demo=",__name__)
    add()
    add1()
main()
if __name__=="__main__":
    print("DEmo=",__name__)
    add()
    add1()