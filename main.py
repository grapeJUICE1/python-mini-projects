def Trip ():
    km = float (input ("Type the distance in km: "))
    lpkm = float (input ("Type the liters per kilometer usage by the car: "))
    ppl = float (input ("Type the price per liter: "))

    total_cost = km * lpkm * ppl
    print (total_cost)



def main():
    Trip()

if __name__ == '__main__':
    main()