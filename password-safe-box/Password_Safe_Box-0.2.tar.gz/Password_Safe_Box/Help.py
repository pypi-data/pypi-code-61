def Help(func=""):
    if func=="Password_Most_Secured":
        print('Password_Most_Secured:\n\nDescription:\nThe most secure way to store a string,\nthis function calculates 6 hashes\nand returns them combined in 1 string\nunless the "Hash" argument is specified (A lot better security than a normal hash)\n\nrequired arguments:\n"password"(The password you want to convert)\n\noptional arguments:\n"salt"(A word or number to make the password more secure)\n"hash"(The hash you want to get for output [Leave blank for custom output])\n')
        return ""
    elif func=="Password_Fastest":
        print('Password_Fastest:\n\nDescription:\nThe Fastest way to store a string (slightly better security than a normal hash)\nrequired arguments:\n"password"(The password you want to convert)\n\noptional arguments:\n"salt"(A word or number to make the password more secure)\n"hash"(The hash you want to get for output [Leave blank for custom output])\n')
        return ""
    else:
        print("Password_Most_Secured\nPassword_Fastest")
        return ""
