while True:
    lis = [1,34,99,-23]
    
    num = int(input("ur num : "))
    
    # if num in lis:
    #     for i in lis:
    #         print("found")
    #         print(i)
    #         break

    # else:
    #     print("not found")
    if num in lis:
        for i,item in enumerate(lis):
            if item == num:
                print("Found",num,"at position",i+1)

