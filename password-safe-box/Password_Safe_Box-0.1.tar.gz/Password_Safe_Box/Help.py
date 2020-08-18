def Help(func="allfuncs"):
    if func=="Password":
        print('Password arguments\nrequired:\n"password"(The password you want to convert)\n\noptional:\n"salt"(A word or number to make the password more secure)\n"method"(The number or string of the method you wish to use)\n"hash"(The hash you want to get for output [Leave blank for custom normal secured output])\n')
    else:
        print("Password")
