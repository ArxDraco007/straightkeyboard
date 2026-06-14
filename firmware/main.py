import board
from kb import keyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

# ─── Layout reference (your plate, left to right, top to bottom) ──────────────
#
# ROW0 (17 keys): Esc F1  F2  F3  F4  F5  F6  F7  F8  F9  F10 F11 F12 PrtSc ScLk Paus Del
# ROW1 (17 keys): `   1   2   3   4   5   6   7   8   9   0   -   =   BSPC       Ins  Home PgUp
# ROW2 (17 keys): Tab  Q   W   E   R   T   Y   U   I   O   P   [   ]   \        Del  End  PgDn
# ROW3 (17 keys): Caps  A   S   D   F   G   H   J   K   L   ;   '   ENTER           Up
# ROW4 (17 keys): LSFT   Z   X   C   V   B   N   M   ,   .   /  RSFT               Up (dup)
# ROW5 (17 keys): LCTL LGUI LALT         SPC              RALT RFUN RCTL  Lft  Dn   Rgt
#
# NOTE: Wide keys (BSPC, Enter, Shift, Space) occupy multiple columns in the
# matrix — the "extra" column position maps to KC.NO (empty/transparent).
# Adjust the TRNS/NO positions below to match your actual wiring.
# ─────────────────────────────────────────────────────────────────────────────

# Layer index
BASE = 0
FN   = 1

keyboard.keymap = [
    # ── BASE layer ────────────────────────────────────────────────────────────
    [
        # ROW0 — Function row (17 keys)
        KC.ESC,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,
        KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,
        KC.PSCR, KC.SLCK, KC.PAUS, KC.DEL,

        # ROW1 — Number row (17 keys)
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,
        KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,
        KC.BSPC, KC.NO,                               # BSPC is 2u → NO for extra col
        KC.INS,  KC.HOME, KC.PGUP,

        # ROW2 — QWERTY row (17 keys)
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,
        KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
        KC.DEL,  KC.END,  KC.PGDN,

        # ROW3 — Home row (17 keys)
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,
        KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.ENT,  KC.NO,   KC.NO,   KC.NO,   KC.UP,   # Enter 2.25u + nav cluster

        # ROW4 — Shift row (17 keys)
        KC.LSFT, KC.NO,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,
        KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH,
        KC.RSFT, KC.NO,   KC.NO,   KC.NO,   KC.NO,

        # ROW5 — Bottom row (17 keys)
        KC.LCTL, KC.LGUI, KC.LALT,
        KC.NO,   KC.NO,   KC.SPC,  KC.NO,   KC.NO,   KC.NO,   # 6.25u space
        KC.RALT, KC.MO(FN), KC.RCTL,
        KC.LEFT, KC.DOWN, KC.RGHT,
    ],

    # ── FN layer ──────────────────────────────────────────────────────────────
    [
        # ROW0
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

        # ROW1
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS,

        # ROW2
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS,

        # ROW3
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.TRNS,

        # ROW4
        KC.TRNS, KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.NO,   KC.NO,   KC.NO,   KC.NO,

        # ROW5
        KC.TRNS, KC.TRNS, KC.TRNS,
        KC.NO,   KC.NO,   KC.TRNS, KC.NO,   KC.NO,   KC.NO,
        KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS,
    ],
]

if __name__ == '__main__':
    keyboard.go()
