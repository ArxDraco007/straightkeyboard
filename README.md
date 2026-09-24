# ArxKeyboard - A Custom Keyboard
## Building a custom mechanical keyboard from scratch.

## Why did I make this project?
Keyboards are a crucial part and parcel of your everyday life and efficiency, and it is crucial for you to have the very best.
It is also a very fun project to make, and it is also very cool to have your own custom keyboard.

## Description
This keyboard is a full-size mechanical keyboard. This has a custom PCB built around an ESP32-S3 WROOM. It contains a 6x17 switch matrix. It is a  two-piece case, red top shell over a blue base, designed in Fusion 360 and printed to match hole-for-hole with the PCB mounting points. It is running KMK on the firmware side.

## Pictures - 
The Schematic
<img width="1018" height="687" alt="image" src="https://github.com/user-attachments/assets/450f9e94-2e35-4df6-bc14-1ba40f85e5f0" />

The PCB
<img width="1171" height="593" alt="image" src="https://github.com/user-attachments/assets/5d8aa79d-ff13-42a5-92b9-0c2aea6cc852" />

The CAD Model
<img width="1920" height="1080" alt="keeb" src="https://github.com/user-attachments/assets/af03148c-1585-4285-886d-65fe6a421191" />

## Zine
<img width="1304" height="2000" alt="zine (7)" src="https://github.com/user-attachments/assets/21761cac-657a-44d6-b18f-49df1bce9ef4" />


# Bill of Materials (BOM)

| Ref. | Value / Part Number | Footprint | Qty. | Supplier | Link | Notes |
|:---|:---|:---|---:|:---|:---|:---|
| C1 | 100 nF | 0603 | 1 | Robu.in | [100 nF 0603 — Pack of 40](https://robu.in/product/100nf-0603-surface-mount-multilayer-ceramic-capacitor-pack-of-40) | X7R, 50 V |
| C2 | 22 nF | 0603 | 1 | Robu.in | [22 nF 0603 — Pack of 50](https://robu.in/product/22nf-0603-surface-mount-multilayer-ceramic-capacitor-pack-of-50/) | 0603 MLCC |
| C11 | 10 µF | EIA-3216-18 (Case A) | 1 | Robu.in | [Vishay 10 µF 16 V Tantalum](https://robu.in/product/293d106x0016a2te3-vishay-tantalum-capacitor-10uf-16v-3-ohm-0-2-3216-18) | Vishay, 10 µF, 16 V; check stock |
| C12 | 22 µF | EIA-3216-18 (Case A) | 1 | element14 India | [22 µF 3216 Tantalum](https://in.element14.com/search?st=22uF+3216+tantalum) | Source from element14 India |
| R1 | 5.1 kΩ | 0603 | 1 | Robu.in | [YAGEO RC0603JR-075K1L](https://robu.in/product/rc0603jr-075k1l-yageo-res-thick-film-0603-5-1k-ohm-5-0-1w1-10w-%C2%B1100ppm-c-pad-smd-t-r/) | USB-C CC pull-down |
| R2 | 5.1 kΩ | 0603 | 1 | Robu.in | [YAGEO RC0603JR-075K1L](https://robu.in/product/rc0603jr-075k1l-yageo-res-thick-film-0603-5-1k-ohm-5-0-1w1-10w-%C2%B1100ppm-c-pad-smd-t-r/) | USB-C CC pull-down |
| R4 | 10 kΩ | 0603 | 1 | Robu.in | [10 kΩ 0603 SMD — Pack of 100](https://robu.in/product/10k-ohm-1-4w-0603-surface-mount-chip-resistor-pack-of-100/) | 1/4 W SMD resistor |
| D1–D88 | 1N4148W-7-F | SOD-123 | 88 | Evelta.com | [1N4148W-7-F — Diodes Inc.](https://evelta.com/1n4148w-7-f-100v-300ma-fast-switching-diode-2pin-smt-sod123/) | 100 V, 300 mA; genuine Diodes Inc. |
| U1 | ESP32-S3-WROOM-1-N16R8 | Module | 1 | Robu.in | [ESP32-S3-WROOM-1-N16R8](https://robu.in/product/espressif-esp32-s3-wroom-1-n16r8-module/) | 16 MB Flash, 8 MB PSRAM |
| U2 | AMS1117-3.3 | SOT-223 | 1 | Evelta.com | [AMS1117-3.3](https://evelta.com/ams1117-3-3-advanced-monolithic-systems-3-3v-1a-ldo-voltage-regulator/) | 3.3 V, 1 A LDO |
| J1 | GCT USB4105-GF-A-060 | 16P Top-Mount SMD | 1 | element14 India | [USB4105-GF-A-060](https://in.element14.com/gct-global-connector-technology/usb4105-gf-a-060/usb-conn-2-0-type-c-r-a-rcpt-16pos/dp/3777659) | USB-C, 16-pin, top-mount SMD |
| SW1–SW88 | Cherry MX2A | PCB Mount | 88 | Meckeys.com | [Cherry MX2A — 10 Pack](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/cherry-mx2a-switch/) | ₹350 / 10-pack; ≈ ₹3,080 total |
| PCB | ArxKey, 2-Layer, 280 × 130 mm | — | 5 | JLCPCB | [JLCPCB](https://jlcpcb.com/) | Manufacturing cost: $7 |

---

## Cost Summary

| Item | Estimated Cost |
|:---|---:|
| Components | Included above |
| Cherry MX2A switches | ≈ ₹3,080 |
| PCB manufacturing — 5 boards | $7 |
| **Estimated Total** | **≈ $57** |

## Stuff You Need to Remember When Making This!!! - 
- Make sure U1 is in the keepout zone.
- Flash the ESP32 before assembly for testing.
- Don't reverse Tantalum capacitors, they pop (Electroboom reference(if you get it)).
- One SOD-123 per key in the matrix facing right.
- Mount in mounting holes!
- Look at the zine and sandwich the PCB.
- Do everything right or else you're cooked.
