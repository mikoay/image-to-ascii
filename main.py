import sys
from PIL import Image

image = sys.argv[1].strip()

def imgToAscii(file):
    img = Image.open(file)
    name = file[:file.find(".")]
    width, height = img.size
    px = img.load()
    ascii = []
    for _ in range(height):
        ascii.append(["X"] * width)
    for y in range(height):
        for x in range(width):
            if sum(px[x, y]) == 0:
                ascii[y][x] = "#"
            elif sum(px[x, y]) in range(1, 100):
                ascii[y][x] = "X"
            elif sum(px[x, y]) in range(100, 200):
                ascii[y][x] = "%"
            elif sum(px[x, y]) in range(200, 300):
                ascii[y][x] = "&"
            elif sum(px[x, y]) in range(300, 400):
                ascii[y][x] = "*"
            elif sum(px[x, y]) in range(400, 500):
                ascii[y][x] = "+"
            elif sum(px[x, y]) in range(500, 600):
                ascii[y][x] = "/"
            elif sum(px[x, y]) in range(600, 700):
                ascii[y][x] = "("
            elif sum(px[x, y]) in range(700, 750):
                ascii[y][x] = "'"
            else:
                ascii[y][x] = " "
    final = open(f"{name}.txt", "w")
    for row in ascii:
        final.write("".join(row)+"\n")
    final.close()
    img.close()

if __name__ == "__main__":
    imgToAscii(image)