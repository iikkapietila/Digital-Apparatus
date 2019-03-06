import tut.arduino_led_matrix as led_matrix
import math
import time
from random import randint

led_matrix.init()




def intro_text(c1, c2, c3, speed, iteration):
    string = "PLK 2018 ! PLIVE FT NISUAL ULTIMATE EMBED DED DEMO" \
             " FULL REAL TIME ON PYNQ 8 X 8 HD ! DIGITAL AP PARATUS"
    i = 0
    for kirjain in string:
        led_matrix.display_char(kirjain, c1, c2, c3, 0, 0, 0)
        time.sleep(1)
        i = i + 1
        print("Character", i, "done")

    led_matrix.clear()
    time.sleep(2)

    enjoy = "E N J O Y  Y O U  K O O K S"
    for kirjain in enjoy:
        led_matrix.display_char(kirjain, 255, 0, 255, 0, 0, 0)
        time.sleep(0.1)

        i = i + 1
        print("Character", i, "done")

    led_matrix.clear()

    print("intro_text done at ", time.time(), " - iteration: ", i,
          " / ", iteration)

    led_matrix.clear()
    time.sleep(2)
    return




def intro_lines(c1, c2, c3, speed, iteration):

    loopcounter = 0
    TIME = 0.075
    while loopcounter <= 2:

        lottery = randint(1, 2)

        if lottery == 1:

            i = 0
            while i <= 1:
                y = 7
                x = randint(0,7)
                for y in range(0,8):
                    led_matrix.set_led_color(x, y, c1, c2, c3)
                    time.sleep(TIME)
                    y = y - 1

                y = 7
                for y in range(0,8):
                    led_matrix.set_led_color(x, y, 0, 0, 0)
                    time.sleep(TIME)
                    y = y - 1

                i = i + 1

        elif lottery == 2:

            i = 0
            while i <= 1:
                y = 7
                x = randint(0, 7)
                for y in range(0, 8):
                    led_matrix.set_led_color(y, x, c1, c2, c3)
                    time.sleep(TIME)
                    y = y - 1

                y = 7
                for y in range(0, 8):
                    led_matrix.set_led_color(y, x, 0, 0, 0)
                    time.sleep(TIME)
                    y = y - 1

                i = i + 1

        loopcounter = loopcounter + 1




def crossingLines(c1, c2, c3, speed, iteration):
    i = 0
    while i <= iteration:
        a = 7
        b = 0
        while a >= 3 and b <= 4:
            led_matrix.set_led_color(4, a, c1, c2, c3)
            led_matrix.set_led_color(3, b, c1, c2, c3)
            a = a - 1
            b = b + 1
            time.sleep(speed)

        a = 2
        b = 5
        while a >= 0 and b <= 7:
            led_matrix.set_led_color(a, 4, c1, c2, c3)
            led_matrix.set_led_color(b, 3, c1, c2, c3)
            a = a - 1
            b = b + 1
            time.sleep(speed)


        print("Crossing Lines done at ", time.time(), " - iteration: ", i,
              " / ", iteration)

        i = i + 1




def squareOutwards (c1, c2, c3, speed, iteration):
    """
    This is the square out effect function
    :param c1: 0 - 255 for red
    :param c2: 0 - 255 for green
    :param c3: 0 - 255 for blue
    :param speed: value for time.sleep (wait)
    :param iteration: number of loops
    :return:
    """
    i = 0
    while i <= iteration:
        x = 0
        y = 0

        #first round
        led_matrix.set_led_color(3, 3, c1, c2, c3)
        led_matrix.set_led_color(3, 4, c1, c2, c3)
        led_matrix.set_led_color(4, 3, c1, c2, c3)
        led_matrix.set_led_color(4, 4, c1, c2, c3)

        time.sleep(speed)
        led_matrix.clear()

        led_matrix.set_led_color(2, 2, c1, c2, c3)
        led_matrix.set_led_color(2, 3, c1, c2, c3)
        led_matrix.set_led_color(2, 4, c1, c2, c3)
        led_matrix.set_led_color(2, 5, c1, c2, c3)

        led_matrix.set_led_color(3, 2, c1, c2, c3)
        led_matrix.set_led_color(4, 2, c1, c2, c3)

        led_matrix.set_led_color(3, 5, c1, c2, c3)
        led_matrix.set_led_color(4, 5, c1, c2, c3)

        led_matrix.set_led_color(5, 2, c1, c2, c3)
        led_matrix.set_led_color(5, 3, c1, c2, c3)
        led_matrix.set_led_color(5, 4, c1, c2, c3)
        led_matrix.set_led_color(5, 5, c1, c2, c3)

        time.sleep(speed)
        led_matrix.clear()

        led_matrix.set_led_color(1, 1, c1, c2, c3)
        led_matrix.set_led_color(2, 1, c1, c2, c3)
        led_matrix.set_led_color(3, 1, c1, c2, c3)
        led_matrix.set_led_color(4, 1, c1, c2, c3)
        led_matrix.set_led_color(5, 1, c1, c2, c3)
        led_matrix.set_led_color(6, 1, c1, c2, c3)

        led_matrix.set_led_color(1, 2, c1, c2, c3)
        led_matrix.set_led_color(1, 3, c1, c2, c3)
        led_matrix.set_led_color(1, 4, c1, c2, c3)
        led_matrix.set_led_color(1, 5, c1, c2, c3)
        led_matrix.set_led_color(1, 6, c1, c2, c3)

        led_matrix.set_led_color(2, 6, c1, c2, c3)
        led_matrix.set_led_color(3, 6, c1, c2, c3)
        led_matrix.set_led_color(4, 6, c1, c2, c3)
        led_matrix.set_led_color(5, 6, c1, c2, c3)

        led_matrix.set_led_color(6, 1, c1, c2, c3)
        led_matrix.set_led_color(6, 2, c1, c2, c3)
        led_matrix.set_led_color(6, 3, c1, c2, c3)
        led_matrix.set_led_color(6, 4, c1, c2, c3)
        led_matrix.set_led_color(6, 5, c1, c2, c3)
        led_matrix.set_led_color(6, 6, c1, c2, c3)

        time.sleep(speed)
        led_matrix.clear()

        looper = 0
        while looper <= 1:

            x = 0
            while x <= 7:
                led_matrix.set_led_color(x, 0, c1, c2, c3)
                x = x + 1

            x = 0
            while x <= 7:
                led_matrix.set_led_color(x, 7, c1, c2, c3)
                x = x + 1

            y = 0
            while y <= 7:
                led_matrix.set_led_color(0, y, c1, c2, c3)
                y = y + 1

            y = 0
            while y <= 7:
                led_matrix.set_led_color(7, y, c1, c2, c3)
                y = y + 1

            looper = looper + 1

        print("Square outwards done at ", time.time(), " - iteration: ", i,
              " / ", iteration)
        i = i + 1




def plk(c1, c2, c3, speed, iteration):
    string = "PLK"
    i = 0
    for kirjain in string:
        led_matrix.display_char(kirjain, c1, c2, c3, 20, 0, 20)
        time.sleep(speed)

        i = i + 1

    print("PLK done at ", time.time(), " - iteration: ", i,
          " / ", iteration)

    led_matrix.clear()




def x(c1, c2, c3, speed, iteration):
    i = 0
    x = 3
    y = 4
    while i <= 3:
        led_matrix.set_led_color(x, y, c1, c2, c3)
        led_matrix.set_led_color(y, x, c1, c2, c3)
        led_matrix.set_led_color(x, x, c1, c2, c3)
        led_matrix.set_led_color(y, y, c1, c2, c3)
        i = i + 1
        y = y + 1
        x = x - 1
        time.sleep(speed)

    print("X done at", time.time(), " - iteration: ", i, " / ", iteration)




def spiral(c1, c2, c3, speed, iteration):

    f = 0
    x = 0
    y = 0

    while f <= 3:

        while x < 7 - f:
            led_matrix.set_led_color(x, y, c1, c2, c3)
            x = x + 1
            time.sleep(speed)

        while y < 7 - f:
            led_matrix.set_led_color(x, y, c1, c2, c3)
            y = y + 1
            time.sleep(speed)

        while x > 0 + f:
            led_matrix.set_led_color(x, y, c1, c2, c3)
            x = x - 1
            time.sleep(speed)

        while y > 1 + f:
            led_matrix.set_led_color(x, y, c1, c2, c3)
            y = y - 1
            time.sleep(speed)

        f = f + 1

    led_matrix.set_led_color(3, 4, c1, c2, c3)





def greetz(c1, c2, c3, speed, iteration):
    string = "GREETZ GO TO  MAT TCUR RENT  X  ASD  X  CONSPIRACY" \
             "  X  FAIRLIGHT  X  CNCD  X  FARBRAUSCH  X  FUTURE CREW  X  KEWLERS" \
             "  X  IVORY LABS  X  INSTANS SI  X  AS SEMBLY  X"

    for kirjain in string:
        led_matrix.display_char(kirjain, c1, c2, c3, 0, 0, 0)
        time.sleep(0.3)
        print("character", kirjain, "done at", time.time())

    spiral(255, 0, 255, 0.02, 1)

    stringb = "ALSO TO MANY OTHERS"
    for kirjain in stringb:
        led_matrix.display_char(kirjain, c1, c2, c3, 0, 0 ,0)
        time.sleep(0.4)

    led_matrix.clear()

    return




def random_dots(c1, c2, c3, speed, iteration):

    x = randint(0, 7)
    y = randint(0, 7)

    b1 = 0
    b2 = 0
    b3 = 0

    while b1 <= 255:
        led_matrix.set_led_color(x, y, b1, c1, c2)
        b1 = b1 + 10
        time.sleep(speed)

    x = randint(0, 7)
    y = randint(0, 7)

    while b2 <= 255:
        led_matrix.set_led_color(x, y, b2, c1, c2)
        b2 = b2 + 10
        time.sleep(speed)

    x = randint(0, 7)
    y = randint(0, 7)

    while b2 <= 255:
        led_matrix.set_led_color(x, y, b3, c1, c2)
        b2 = b2 + 10
        time.sleep(speed)

    x = randint(0, 7)
    y = randint(0, 7)

    b1 = 0

    while b1 <= 255:
        led_matrix.set_led_color(x, y, b1, c1, c2)
        b1 = b1 + 10
        time.sleep(speed)

    return




def plasma_function():
    PIXEL_WIDTH = 8
    PIXEL_HEIGHT = 8
    x = 0
    y = 0
    counter = 0
    beginning = time.time()

    while True:
        for x in range(PIXEL_WIDTH):
            current = time.time()
            current = int(current * 9)
            vy = math.sin(x * 3.0 + current)
            vy = (vy + 1) / 2
            vy = int(vy * 8)
            y = vy

            for y in range(PIXEL_HEIGHT):
                current = time.time()
                current = int(current*9)

                v = math.sin(x * 10.0 + current)
                v = (v+1) / 2
                v = int(v * 8)

                x = v
                c1 = randint(0, 254)
                c2 = randint(0, 254)
                c3 = randint(0, 254)
                led_matrix.set_led_color(x, y, c1, c2, c2)

                time.sleep(0.01)
                now = time.time()
                passed = now-beginning

                print(passed)
                if passed > 10:
                    return




def plasma_function2():
    PIXEL_WIDTH = 8
    PIXEL_HEIGHT = 8

    x = 0
    y = 0
    counter = 0
    beginning = time.time()

    while True:

        for x in range(PIXEL_WIDTH):

            current = time.time()
            current = int(current * 9)

            vy = math.sin(x * 3.0 + current)
            vy = (vy + 1) / 2
            vy = int(vy * 8)

            y = vy

            for y in range(PIXEL_HEIGHT):
                current = time.time()
                current = int(current*9)

                v = math.sin(x * 10.0 + current)
                v = (v+1) / 2
                v = int(v * 8)

                x = v
                c1 = randint(0, 254)
                c2 = randint(0, 254)
                c3 = randint(0, 254)
                led_matrix.set_led_color(x, y, c1, c2, c2)

                crossingLines(c1, c2, 255, 0.01, 1)

                time.sleep(0.01)

                now = time.time()

                passed = now-beginning

                print(passed)
                if passed > 10:
                    return




def shutdown():
    b = 255
    while b > 0:
        b = b - 5
        for x in range(8):
            for y in range(8):
                led_matrix.set_led_color(x, y, b, b, b)
                time.sleep = 0.05
    return





def rand_red():
    value = randint(0, 255)
    return value

def rand_green():
    value = randint(0, 255)
    return value

def rand_blue():
    value = randint(0, 255)
    return value





def main():

    time.sleep(2)

    i = 0
    while i == 0:
        intro_text(rand_blue(), rand_blue(), rand_red(), 0.5, 1)
        i = i + 1
        time.sleep(5)

    i = 0
    while i <= 1:
        intro_lines(rand_red(), rand_green(), rand_blue(), 0.5, 1)
        i = i + 1

    i = 0
    while i <= 8:
        crossingLines(rand_blue(), rand_green(), rand_red(), 0.05, 1)
        crossingLines(0, 0, 0, 0.05, 1)
        i = i + 1

    i = 0
    while i <= 1:
        plk(rand_red(), rand_green(), rand_blue(), 1, 1)
        i = i + 1

    i = 0
    while i <= 2:
        plk(rand_red(), rand_green(), rand_blue(), 0.5, 1)
        i = i + 1


    i = 0
    while i <= 4:
        plk(rand_red(), rand_green(), rand_blue(), 0.2, 1)
        i = i + 1

    i = 0
    while i <= 19:
        squareOutwards(rand_red(), rand_green(), rand_blue(), 0.1, 1)
        i = i + 1

    led_matrix.clear()

    i = 0
    while i <= 35:
        x(rand_red(), rand_green(), rand_blue(), 0.1, 1)
        i = i + 1

    led_matrix.clear()

    i = 0
    while i <= 15:
        x(rand_red(), rand_green(), rand_blue(), 0.1, 1)
        squareOutwards(rand_red(), rand_green(), rand_blue(), 0.1, 1)
        i = i + 1

    i = 0
    while i <= 6:
        x(rand_red(), rand_green(), rand_blue(), 0.1, 1)
        squareOutwards(rand_red(), rand_green(), rand_blue(), 0.1, 1)
        crossingLines(255, 255, 255, 0.02, 1)
        i = i + 1

    i = 0
    while i <= 20:
        spiral(rand_red(), rand_green(), rand_blue(), 0.01, 1)
        i = i + 1

    led_matrix.clear()

    i = 0
    while i == 0:
        greetz(255, 200, 40, 1, 1)
        i = i + 1

    i = 0
    while i <= 3:
        spiral(255, 0, 255, 0.01, 1)
        crossingLines(255, 0, 255, 0.02, 1)
        squareOutwards(255, 0, 255, 0.1, 1)
        i = i + 1

    i = 0
    while i <= 5:
        random_dots(rand_red(), rand_green(), rand_blue(), 0.05, 1)
        i = i + 1

    i = 0
    while i <= 1:
        plasma_function()
        i = i + 1

    i = 0
    while i <= 1:
        plasma_function2()
        i = i + 1

    i = 0
    while i <= 1:
        plasma_function2()
        spiral(255, 0, 255, 0.01, 1)
        i = i + 1

    i = 0
    while i <= 3:
        spiral(rand_red(), rand_green(), rand_blue() , 0.03, 1)
        i = i + 1

    shutdown()

main()
