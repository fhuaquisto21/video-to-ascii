import cv2
import json
import time
from sty import fg

#brightness = [" ", ".", "+", "*", "G", "H", "M", "#", "&", "%"]
brightness = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
#brightness = ["%", "&", "#", "M", "H", "G", "*", "+", ".", " "]

title = "Friday_Night_Funkin"
data = { "frames": [], "fps": 30 }

def main():
    # url = input('URL: ');
    url = "/home/fhuaquisto/Downloads/friday_night_finkin.avi"
    cap = cv2.VideoCapture(url)

    while True:
        #cap.set(cv2.CAP_PROP_FPS, 30)
        ret, frame = cap.read()
        iframe = []
        if ret == True:
            xframe = cv2.resize(frame, (80, 45), fx = 0, fy = 0, interpolation = cv2.INTER_CUBIC)
            for i in range(len(xframe)):
                irow = []
                for j in range(len(xframe[0])):
                    level = int(((sum(xframe[i, j]) / 3) / 255) * 69)
                    if level == 69:
                        level = 68
                    character = fg(xframe[i, j][2], xframe[i, j][1], xframe[i, j][0]) + brightness[level] + fg.rs
                    irow.append(character)
                    irow.append(character)
                iframe.append(irow)
            data["frames"].append(iframe)
        else:
            break
    with open(f'./videos/{title}.txt', 'w') as file:
        json.dump(data, file)
        
        

def play():
    with open(f"./videos/{title}.txt", 'r') as file:
        data = json.load(file)
    delta = 1 / data["fps"]
    for frame in data["frames"]:
        start = time.time()
        for row in frame:
            for char in row:
                print(char, end="")
            print()

        if (delta - (time.time() - start) > 0):
            time.sleep(delta - (time.time() - start))
        print("\033c", end="")

if __name__ == '__main__':
    print("\033c", end="")
    #main()
    play()
