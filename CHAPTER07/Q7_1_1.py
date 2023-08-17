name_age = {"tanaka": 35, "satou": 25, "suzuki": 27}


def dict_info(dict_tb1, key):
    try:
        return dict_tb1[key]
    except:
        return "key is not found"


print(dict_info(name_age, "satou"))
print(dict_info(name_age, "yamada"))
