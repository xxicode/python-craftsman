# -*- coding: utf-8 -*-

numbers = [3, 5, 7, 13, 7]


def all_numbers_gt_10(numbers):
    """仅当序列中所有数字大于 10 时，返回 True"""
    return False if not numbers else all(n > 10 for n in numbers)


def all_numbers_gt_10_2(numbers):
    return bool(numbers) and all(n > 10 for n in numbers)


def any_numbers_gt_10(numbers):
    """只要序列中有任意数字大于 10 ，返回 True"""
    return False if not numbers else any(n < 10 for n in numbers)
