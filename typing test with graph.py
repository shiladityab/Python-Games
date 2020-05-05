import matplotlib.pyplot as plt
import time as t
times = []
mistakes = 0

print("-------------------------------------------------------------------------------------------------")
print("This Program will help you to type faster. Type the word 'programming' as fast as you can for five times.")
print("-------------------------------------------------------------------------------------------------")

input("Press ENTER to continue")

while len(times) < 5 :
    start = t.time()
    word = input("Type the word :  ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)
    if (word.lower() != "programming") :
        mistakes += 1

print("You have made " + str(mistakes) + " mistake(s)")
print("Now see your evolution :  ")
t.sleep(3)

x = [1,2,3,4,5]
y = times

plt.plot(x,y)

legend = ['1', '2', '3', '4', '5']
plt.xticks(x, legend)

plt.ylabel("Time in Seconds")
plt.xlabel("Attempts")
plt.title("Your typing Evolution")

plt.show()

print("-------------------------------------------------------------------------------------------------")
