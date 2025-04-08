import time
import threading

print("Hello World!!")
print("I am Carbine C")
print("NO! I am Carbine C")
print("No, I am Melt The Sun")

print("""Piss poop 
shit fart
and other bodily fluids""")

print("I am Carbine C\nNo I'M Carbine C\nDang nabbit, I'm Melt the Sun\n")

def melt_the_sun():
    for _ in range(1000):  # Start small for testing
        print("MELT THE SUN\nWIGGER")
        time.sleep(0.1)

def say_bitch():
    for _ in range(1000):
        print("Bitch\n")
        time.sleep(0.3)

# Start threads (make sure threading is imported above!)
thread1 = threading.Thread(target=melt_the_sun)
thread2 = threading.Thread(target=say_bitch)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("🔥 Both loops finished!")