#!/usr/bin/env python3

# Created by: Peter Gemmell
# Created on: April 2022
# This program is the constants file for "Space Aliens" program on the PyBadge

SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
TOTAL_NUMBER_OF_LASERS
SHIP_SPEED = 1
ALIEN_SPEED = 1
LASER_SPEED = 2
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SCREEN_SIZE
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# Using for button state
button_state = {
  "button_up": "up",
  "button_just_pressed": "just pressed",
  "button_still_pressed": "still pressed",
  "button_released": "released"
}
# new pallet for filled text
RED_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
                b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
