def outer():
    print("Entering outer")

    def inner():
        print("Entering inner")
        print("Processing")
        print("Leaving inner")

    print("Calling Inner") 
    inner()
outer()
print("Program Ended")       