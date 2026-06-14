import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# ─── Matrix pins from schematic ───────────────────────────────────────────────
# COL0–COL16 → IO0–IO16
# ROW0–ROW5  → IO38, IO39, IO40, IO42, IO45, IO48

COL_PINS = (
    board.IO0,  board.IO1,  board.IO2,  board.IO3,
    board.IO4,  board.IO5,  board.IO6,  board.IO7,
    board.IO8,  board.IO9,  board.IO10, board.IO11,
    board.IO12, board.IO13, board.IO14, board.IO15,
    board.IO16,
)

ROW_PINS = (
    board.IO38,
    board.IO39,
    board.IO40,
    board.IO42,
    board.IO45,
    board.IO48,
)

keyboard.matrix = MatrixScanner(
    column_pins=COL_PINS,
    row_pins=ROW_PINS,
    columns_to_anodes=True,   # diodes point col→row (cathode on row side)
)

# ─── Modules ──────────────────────────────────────────────────────────────────
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
