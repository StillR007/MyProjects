def find_screen_height(width, ratio):
    num = ratio.replace(':', ' ').split(" ")
    return f'{width}x{int(width / int(num[0]) * int(num[1]))}'


find_screen_height(1024, "4:3")
find_screen_height(1280, "16:9")
find_screen_height(3840, "32:9")