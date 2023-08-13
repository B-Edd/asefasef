from ai import create_board, get_best_move
import pyautogui
import time
import sys
import getpixelcolor


time.sleep(2)

screen_tl = (540, 384)
screen_br = (940, 684)

screen_row = ((screen_tl[1] - screen_br[1]) // 6) - 10
screen_col = ((screen_br[0] - screen_tl[0]) // 7) + 4

board_pos = []

for row in range(7):
    for col in range(6):
        x = screen_tl[0] + screen_col * row
        y = screen_br[1] + screen_row * col
        board_pos.append((x, y))
        pyautogui.moveTo(x, y)
        x, y = pyautogui.position()

        # Get the RGB color values of the pixel at the mouse position
        width = 5
        height = 5
        print(getpixelcolor.average(x, y, width, height))
        time.sleep(0.3)


board = create_board()
print(pyautogui.position())

