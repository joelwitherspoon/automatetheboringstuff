def commacode(commalist):
    try:
        if commalist is None:
            print("There is nothing in this list")
        else:
            for idx in range(len(commalist)-1):
                print(commalist[idx],end=',')
            print('and ' + commalist[-1])
    except IndexError:
        print("IndexError: Can't process this list")

cclist = ['andy','buzz', 'slinky dog', 'bo', 'mr. potato head']
commacode(cclist)
