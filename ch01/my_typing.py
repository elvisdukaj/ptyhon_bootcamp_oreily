from typing import Union, Optional


def bar(a: int) -> int:
    return a


ret_val = bar(0)
print(ret_val)


def nonreturnfunc(a: str) -> None:
    print(a)


nonreturnfunc("test")


def division(a: int, b: int) -> Optional[float]:
    if b != 0:
        return a / b

    return None


print(division(1, 2))
print(division(1, 0))


def division2(a: int, b: Union[int, float, None]) -> Optional[float]:
    if b is None:
        return None

    if b is 0:
        return None

    return a / b


print(division2(1, 2))
print(division2(1, None))


def my_test_unpack(input_val: dict[str, int], key: str) -> int:
    return input_val[key]


print(my_test_unpack({"key": 3}, "key"))


def returns_tuple(input_val: list[str], index: int) -> tuple[str, int]:
    return input_val[index], index


res = returns_tuple(["elem"], 0)
print(res)
