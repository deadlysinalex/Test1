speed = int(input("please insert the speed limit: "))
driver = int(input("Please insert the speed of the driver: "))

if (speed<driver):
    amountover1 = driver-speed
    print("They were going " + str(amountover1) + " mph over the limit")

    amountover2 = amountover1 * 5
    if amountover1 >= 90:
        print("200 dollars extra as their speed exceeds 90 mph")
        total = amountover2 + 200
        print("The total amount they have to pay for their ticket is $" + str(total)+".")
    else:
        total = amountover2
        print("The total amount they have to pay for their ticket is $" + str(total)+".")
else:
    print("Inside the speed limit")
