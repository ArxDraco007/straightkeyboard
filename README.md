# ArxKeyboard - A Custom Keyboard
## Building a custom mechanical keyboard from scratch.

## Why did I make this project?
Keyboards are a crucial part and parcel of your everyday life and efficiency, and it is crucial for you to have the very best.
Customize your keyboard to make sure you enjoy your work. You can also type very fast. It is also a very fun project to make, and it is also very cool to have your own custom keyboard.

## Pictures - 
The Schematic
<img width="1061" height="730" alt="image" src="https://github.com/user-attachments/assets/f8df278e-c3b5-4529-8906-ba8469c8658e" />

The PCB
<img width="1175" height="521" alt="image" src="https://github.com/user-attachments/assets/67d0b8d9-f7cd-48d6-b6cc-034c6d859405" />

The CAD Model
<img width="1920" height="1080" alt="keeb" src="https://github.com/user-attachments/assets/af03148c-1585-4285-886d-65fe6a421191" />

## Zine
<img width="1304" height="2000" alt="zine (1)" src="https://github.com/user-attachments/assets/5fa10383-74f4-461d-a10f-634892cacf32" />


## BOM

# Bill of Materials

| Ref | Value | Footprint | Qty | Supplier | Link | Notes |
|-----|-------|-----------|-----|----------|------|-------|
| C1 | 100nF | 0603 | 1 | Robu.in | [100nF 0603 (pack of 40)](https://robu.in/product/100nf-0603-surface-mount-multilayer-ceramic-capacitor-pack-of-40) | X7R 50V |
| C2 | 22nF | 0603 | 1 | Robu.in | [22nF 0603 (pack of 50)](https://robu.in/product/22nf-0603-surface-mount-multilayer-ceramic-capacitor-pack-of-50/) | 0603 MLCC |
| C11 | 10uF | EIA-3216-18 (Case A) | 1 | Robu.in | [Vishay 10uF 16V Tantalum 3216-18](https://robu.in/product/293d106x0016a2te3-vishay-tantalum-capacitor-10uf-16v-3-ohm-0-2-3216-18) | Vishay 10uF 16V Tantalum; check stock |
| C12 | 22uF | EIA-3216-18 (Case A) | 1 | element14 India | [22uF 3216 Tantalum — element14 India](https://in.element14.com/search?st=22uF+3216+tantalum) | No confirmed listing on Robu/Evelta; source from element14 India |
| R1 | 5.1kΩ | 0603 | 1 | Robu.in | [YAGEO RC0603JR-075K1L — 5.1kΩ 5% 0603](https://robu.in/product/rc0603jr-075k1l-yageo-res-thick-film-0603-5-1k-ohm-5-0-1w1-10w-%C2%B1100ppm-c-pad-smd-t-r/) | USB-C CC pull-down |
| R2 | 5.1kΩ | 0603 | 1 | Robu.in | [YAGEO RC0603JR-075K1L — 5.1kΩ 5% 0603](https://robu.in/product/rc0603jr-075k1l-yageo-res-thick-film-0603-5-1k-ohm-5-0-1w1-10w-%C2%B1100ppm-c-pad-smd-t-r/) | USB-C CC pull-down |
| R4 | 10kΩ | 0603 | 1 | Robu.in | [10kΩ 0603 SMD (pack of 100)](https://robu.in/product/10k-ohm-1-4w-0603-surface-mount-chip-resistor-pack-of-100/) | 10k 1/4W 0603 SMD |
| D1–D88 | 1N4148W-7-F | SOD-123 | 88 | Evelta.com | [1N4148W-7-F — Diodes Inc](https://evelta.com/1n4148w-7-f-100v-300ma-fast-switching-diode-2pin-smt-sod123/) | Diodes Inc; 100V 300mA; genuine |
| U1 | ESP32-S3-WROOM-1-N16R8 | Module | 1 | Robu.in | [ESP32-S3-WROOM-1-N16R8](https://robu.in/product/espressif-esp32-s3-wroom-1-n16r8-module/) | 16MB Flash 8MB PSRAM |
| U2 | AMS1117-3.3 | SOT-223 | 1 | Evelta.com | [AMS1117-3.3 — Advanced Monolithic Systems](https://evelta.com/ams1117-3-3-advanced-monolithic-systems-3-3v-1a-ldo-voltage-regulator/) | AMS original; 1A LDO; ~₹12 |
| J1 | GCT USB4105-GF-A | 16P Top Mount SMD | 1 | element14 India | [USB4105-GF-A-060](https://in.element14.com/gct-global-connector-technology/usb4105-gf-a-060/usb-conn-2-0-type-c-r-a-rcpt-16pos/dp/3777659) | USB-C 16P top mount SMD |
| SW1–SW88 | Cherry MX2A | PCB Mount | 88 | Meckeys.com | [Cherry MX2A (10/pack)](https://meckeys.com/shop/accessories/keyboard-accessories/key-switches/cherry-mx2a-switch/) | ₹350/10 pack → ~₹3080 total |
|Total| | | | | |50$|

## Assembly instructions - 
Flash ESP32 first — caught from the schematic that U1 is the brains, better to test firmware before burying it in solder
Tantalum polarity warning — C11 and C12 are the ones that'll pop if reversed, called that out hard
USB-C CC pins — your schematic clearly shows R1/R2 as the CC pull-downs for USB 2.0 negotiation, mentioned explicitly
Diode orientation — 88 diodes, all SOD-123, all need to face the right way for the matrix to work
Mounting holes H1–H8 — visible in your PCB layout, referenced in the case assembly step
Two-layer case — pulled from your 3D render, red top + blue bottom sandwich
