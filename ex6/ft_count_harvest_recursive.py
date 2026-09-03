def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def ft_helper(day):
        if day == days + 1:
            return
        print(f"Day {day}")
        ft_helper(day + 1)

    ft_helper(1)
    print("Harvest time!")
