# Requirements and evidence

## Confirmed design basis

| ID | Requirement / fact | State | Evidence |
| --- | --- | --- | --- |
| R-001 | Design basis PSU is Mean Well **RSP-320-24**. Purchase remains unconfirmed. | Confirmed basis | [Mean Well datasheet](https://www.meanwell.com/Upload/PDF/RSP-320/RSP-320-SPEC.PDF) |
| R-002 | PSU output is 24 V, 13.4 A, 321.6 W. Adjustable output range is 20–26.4 V. | Confirmed | Mean Well datasheet, p. 3 |
| R-003 | PSU AC input is 88–264 VAC, 47–63 Hz. Its listed 40 A at 230 VAC is inrush, not continuous input current. | Confirmed | Mean Well datasheet, pp. 2–3 |
| R-004 | PSU envelope is 215 × 115 × 30 mm. It has M4 base holes with 3 mm maximum screw penetration and M4 side holes with 5 mm maximum penetration. | Confirmed | Mean Well datasheet, p. 4 |
| R-005 | Target is four independently regulated USB-C PD source ports. The fifth port is excluded unless the aggregate budget is re-qualified. | Confirmed | Project goal |
| R-006 | Per-port target is 65 W. At 20 V this is 3.25 A; the cable path therefore requires a 5 A electronically marked USB-C cable if a 65 W/20 V contract is used. | Confirmed | Arithmetic; USB-C current rules must be validated in controller/cable test |
| R-007 | Do not apply the 24 V rail directly to USB-C VBUS or a Dell DC input. | Confirmed safety requirement | Project goal |
| R-008 | Enclosure target is 10-inch, 1U, folded metal tray and removable ventilated lid. 1U and 10-inch dimensions are **not** accepted as rail-fit evidence. | Confirmed intent; dimensions unconfirmed | Project goal |
| R-009 | Mains integration requires rear fused IEC inlet, covered live terminals, and protective-earth bond to exposed conductive enclosure. | Confirmed safety requirement | Project goal |
| R-010 | Native source of truth is KiCad and FreeCAD. `exports/` contains generated artifacts only. | Confirmed | Project goal |

## Dell compatibility gate

A Dell OptiPlex 3080 Micro example specifies a 65 W, 19.5 V, 3.34 A, 4.5 mm adapter ([Dell specification](https://www.dell.com/support/manuals/en-pg/optiplex-3080-micro/optiplex3080_micro_specs/power-adapter?guid=guid-0ac35263-1ccc-4d6b-b667-55bf6f3aa185&lang=en-us)). This is **not evidence for the four actual PCs**.

The actual models, their OEM adapter labels, and their DC-input arrangements must be recorded before finalising a PDO set or buying adapters:

| Port | OptiPlex model / service tag | OEM label V/A/W | Power input | Test result |
| --- | --- | --- | --- | --- |
| 1 | Unknown | Unknown | Unknown | Not tested |
| 2 | Unknown | Unknown | Unknown | Not tested |
| 3 | Unknown | Unknown | Unknown | Not tested |
| 4 | Unknown | Unknown | Unknown | Not tested |

Many barrel-input Dell systems use a centre identification pin. The Akyga AK-ND-C10 advertises a 4.5 × 3.0 mm + pin connector, 18.5–20 V, 5 A maximum, and 100 W maximum ([Akyga product page](https://www.akyga.com/products/1221-laptop-adapter-ak-nd-c10-usb-c-4-5-x-3-0-mm-20-v.html)). Its page does **not** establish successful adapter-ID behavior with the actual PCs. AK-ND-C10 is only a test candidate.

## Measurements still required

| ID | Measurement / verification | Why it gates hardware |
| --- | --- | --- |
| M-001 | Rack manufacturer/drawing; rail-to-rail clear width, hole size/thread, horizontal and vertical hole centres, usable depth, rail front/back offsets | Final tray width/depth, ears, mounting pattern |
| M-002 | Actual RSP-320-24 specimen terminal cover envelope, terminal-wire bend envelope, fan intake/exhaust direction, and required unobstructed faces | Lid/vent geometry and PSU location |
| M-003 | Actual Dell models and OEM adapter labels | Required output voltage, wattage, connector and ID compatibility |
| M-004 | AK-ND-C10 at 20 V PD with each actual Dell, including BIOS adapter recognition | Prevents a connector-only false positive |
| M-005 | PD controller stock, lifecycle, assembly capability, and documented 5 A/e-marked-cable behaviour | Component selection and 65 W contract compliance |
| M-006 | Connector vendor drawing, through-panel geometry, retention, VBUS/CC ESD ratings | PCB outline and front-panel cutouts |
| M-007 | PCB assembler stack-up, copper, via capability and price for one 4-layer board | Layout rules and realistic prototype cost |

## Non-negotiable verification gates

- No mains wiring or powered test in an unbonded metal enclosure.
- No live mains terminals without an insulating terminal cover.
- No Dell PC test before USB-C PD contracts, voltage accuracy, current limit, discharge, fault response and full-load temperature are proven with loads.
- No 65 W source advertisement until the selected PD controller and full cable/adapter path have passed 5 A e-marker/cable capability validation.
- No fabrication release until schematic ERC, PCB DRC, component ratings, creepage/clearance, thermal behavior, connector retention/alignment and enclosure clearances have all been reviewed.
