from matplotlib import pyplot as plt
import numpy as np

while True:
    lower_limit=int(input("Oppgi nedre grense for x: "))
    upper_limit=int(input("Oppgi øvre grense for x: "))
    step=float(input("Oppgi steg: "))
    f=input("Skriv inn funksjonen f(x): ")

    if lower_limit>=upper_limit:
        print("Øvre grense må være større enn nedre grense!")
    else:
        break


x=np.arange(lower_limit,upper_limit,step)
y=eval(f)

plt.title('f(x)='+f)
plt.ylabel('Y akse')
plt.xlabel('X akse')

plt.plot(x,y)

plt.show()
