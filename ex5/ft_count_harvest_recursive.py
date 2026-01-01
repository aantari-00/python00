def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_count(days)


def ft_count(day):
    if day == 0:
        print("Harvest time!")
        return
    ft_count(day - 1)
    print("Day", day)
