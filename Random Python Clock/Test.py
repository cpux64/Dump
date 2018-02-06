from datetime import datetime


def main():
    potato = now.date()
    carrot = datetime.now().time()
    year = str(potato)[0] + str(potato)[1] + str(potato)[2] + str(potato)[3]
    year0 = str(year)[0]
    year1 = str(year)[1]
    year2 = str(year)[2]
    cent = int(year0) * 10 + int(year1) + 1
    mill = int(year0)
    dec = int(year0) * 100 + int(year1) * 10 + int(year2) + 1
    month_str = str(potato)[5]
    month_str1 = str(potato)[6]
    month = int(month_str) * 10 + int(month_str1)
    day_str = str(potato)[8]
    day_str1 = str(potato)[9]
    day = int(day_str) * 10 + int(day_str1)
    hour_str = str(carrot)[0]
    hour_str1 = str(carrot)[1]
    hour = int(hour_str) * 10 + int(hour_str1)
    min_str = str(carrot)[3]
    min_str1 = str(carrot)[4]
    minute = int(min_str) * 10 + int(min_str1)
    sec_str = str(carrot)[6]
    sec_str1 = str(carrot)[7]
    second = int(sec_str) * 10 + int(sec_str1)
    msec_str = str(carrot)[9]
    msec_str1 = str(carrot)[10]
    msec_str2 = str(carrot)[11]
    msec = int(msec_str) * 100 + int(msec_str1) * 10 + int(msec_str2)
    print("Millennium: " + str(mill))
    print("Century: " + str(cent))
    print("Decade: " + str(dec))
    print("Year: " + str(year))
    print("Month: " + str(month))
    print("Day: " + str(day))
    print("Hour: " + str(hour))
    print("Minute: " + str(minute))
    print("Second: " + str(second))
    print("Millisecond: " + str(msec))
    choice = input("Press Enter to repeat, or any other key to exit.")
    while True:
        if choice == "":
            main()
        else:
            return


main()
