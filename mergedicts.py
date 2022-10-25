def merge_max_mappings(dict1, dict2):
    new_dict = dict2.copy()
    for k in dict1.keys():
        if k in dict2.keys():
            new_dict[k] = max(dict1[k], dict2[k])
        else:
            new_dict[k] = dict1[k]
    return new_dict


def test_bananas():
    dict1 = {'bananas': 7, 'apples': 3, 'pears': 14}
    dict2 = {'bananas': 3, 'apples': 6, 'grapes': 9}
    res = merge_max_mappings(dict1, dict2)
    answer = {'bananas': 7, 'apples': 6, 'grapes': 9, 'pears': 14}
    if res == answer:
        print("Test passed!")
    else:
        print("Oh no :(")

test_bananas()