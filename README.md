# rack-pdu

Custom 10-inch rack USB-C PD distribution unit for four Dell OptiPlex Micro PCs, powered by one 24 V Mean Well RSP-320-24.

> **Safety/status — conceptual prototype.** Nothing in this repository is fabrication-ready or approved for connection to mains equipment or a Dell PC. The electronics are not yet a validated schematic or PCB. Use suitably rated electronic loads during validation before connecting equipment.

## Status

| Area | State |
| --- | --- |
| Repository, requirements, safety gates | Started |
| 24 V power budget | Preliminary; four 65 W ports appear feasible only after measured conversion/thermal validation |
| PD architecture | Preliminary selection: TI TPS25750D reference-based source architecture; supply and cable-discovery behaviour are procurement/bench gates |
| Dell compatibility | Blocked on exact OptiPlex service tags/models and an AK-ND-C10 compatibility test |
| Single-port KiCad project | Native project and architectural design sheet created; no circuit released for fabrication |
| Enclosure | Parametric FreeCAD concept created; rack and PSU terminal/airflow fit still require physical verification |
| Multi-port design | Not started |

## Toolchain

- KiCad 10: `electronics/`
- FreeCAD: `mechanical/`
- Git: native sources and decisions

The supplied workstation has `kicad` and `FreeCAD` available. Generated manufacturing and preview artifacts belong in `exports/` and are intentionally not source of truth.

## Layout

- `docs/` — requirements, decisions, power budget, architecture rationale, validation plan
- `electronics/port-prototype/` — one-port KiCad project and design gates
- `electronics/distribution/` — reserved for the replicated multi-port design
- `mechanical/` — FreeCAD enclosure concept; dimensions live in its spreadsheet
- `bom/` — preliminary BOM and sourcing-risk notes
- `exports/` — generated-only fabrication or preview files; do not edit as source

## Start here

1. Read [requirements](docs/requirements.md), [decisions](docs/decisions.md), and the [validation plan](docs/validation-plan.md).
2. Enter the **four exact Dell models/service tags**, their OEM-adapter labels, and rack rail measurements in `docs/requirements.md`.
3. Open `mechanical/rack-pdu-concept.FCStd` in FreeCAD. Edit the `Parameters` spreadsheet; do not edit generated geometry dimensions directly.
4. Open `electronics/port-prototype/port-prototype.kicad_pro` in KiCad. Complete controller availability and the controller/cable capability review before adding a power circuit.
5. Validate one channel into an electronic load before replicating it.

## Repository placement

Created at `projects/rack-pdu`. The workspace already has `projects/` for independent projects, so a second top-level hardware-project folder would duplicate the existing organization.

## Source references

- Mean Well RSP-320 datasheet: <https://www.meanwell.com/Upload/PDF/RSP-320/RSP-320-SPEC.PDF>
- TI TPS25750 datasheet: <https://www.ti.com/lit/ds/symlink/tps25750.pdf>
- ST STUSB4710 reference: <https://www.st.com/en/evaluation-tools/steval-isc004v1.html>
- Akyga AK-ND-C10: <https://www.akyga.com/products/1221-laptop-adapter-ak-nd-c10-usb-c-4-5-x-3-0-mm-20-v.html>
