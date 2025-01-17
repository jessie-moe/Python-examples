def computepay(h, r):
    r = float(rate)
    h= float(hrs)
    total = (r * min(h,40)) + (1.5*r*((abs(h-40)+(h-40))/2))
    return total

hrs = input("Enter Hours:")
rate = input("Enter Hourly Rate:")


print("Pay", computepay(hrs, rate))