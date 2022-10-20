from collections import deque


def check_gift():
    pass


materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))



while materials and magic_level:
    current_material = materials[-1]
    current_magic = magic_level[0]
    result_to_check = current_magic + current_material

    if result_to_check < 100:
        pass

    elif result_to_check > 499:
        pass


    else:
        pass
