def explode(arr):
    if type(arr[0]) != int and type(arr[1]) != int:
        return 'Void!'
    if type(arr[0]) == int and type(arr[1]) == int:
        count_of_lists = sum(arr)
        final_list = []
        __i = 1
        while __i <= count_of_lists:
            final_list.append(arr)
            __i += 1
        return final_list
    else:
        for _i in arr:
            if type(_i) == int:
                count_of_lists = _i
                final_list = []
                __i = 1
                while __i <= count_of_lists:
                    final_list.append(arr)
                    __i += 1
                return final_list
            else:
                pass


explode([9, 3])
explode(['a', 3])
explode([6, 'c'])
explode(['a', 'b'])
explode([1, 0])
