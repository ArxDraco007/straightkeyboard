import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
COL_PINS = (board.IO0,  board.IO1,  board.IO2,  board.IO3, board.IO4,  board.IO5,  board.IO6,  board.IO7,
board.IO8,  board.IO9,  board.IO10, board.IO11, board.IO12, board.IO13, board.IO14, board.IO15,
board.IO16,)
ROW_PINS = (board.IO38, board.IO39, board.IO40, board.IO42, board.IO45, board.IO48,)
keyboard.matrix = MatrixScanner(column_pins=COL_PINS,row_pins=ROW_PINS,columns_to_anodes=True,)
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
from kmk.keys import KC

keyboard.keymap = [[
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,
        KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.PSCR, KC.SLCK, KC.PAUS, KC.NO,
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,
        KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.INS,  KC.HOME, KC.PGUP,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,
        KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.ENT,  KC.DEL,  KC.END,  KC.PGDN,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,
        KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.NUHS, KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.LSFT, KC.NUBS, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,
        KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.NO,   KC.NO,   KC.UP,   KC.NO,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC,  KC.NO,   KC.NO,   KC.NO,   KC.NO,
        KC.RALT, KC.RGUI, KC.APP,  KC.RCTL, KC.NO,   KC.NO,   KC.LEFT, KC.DOWN, KC.RGHT,
    ],]

if __name__ == '__main__':
    keyboard.go()