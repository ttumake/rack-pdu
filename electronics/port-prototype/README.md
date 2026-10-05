# One-port 65 W PD prototype

`port-prototype.kicad_sch` is an **architectural design-gate sheet**, not a completed power schematic. It records the selected preliminary TPS25750D architecture and constraints while component sourcing and 5 A/e-marker behavior are unresolved.

## Deliberate omissions

No power circuit, footprint association, netlist, PCB or STEP export exists yet. Adding a plausible buck circuit before choosing a controller configuration, converter topology, VBUS protection, USB-C receptacle and components would be unsafe and misleading.

## Start capture only after these gates close

1. TPS25750DRJKR procurement/lifecycle and configuration process verified.
2. TI reference design reviewed for 24 V source operation and PDO transition behavior.
3. A 65 W/5 A contract tested with known compliant 3 A and 5 A e-marked cables and a PD analyzer.
4. USB-C receptacle drawing, ESD/TVS strategy and enclosure connector alignment chosen.
5. Converter and VBUS path components selected with voltage/current/thermal margins.

Then capture named functional blocks in this order: protected input, bias rails, buck, VBUS path/discharge/OCP, TPS25750D configuration and CC/VCONN, receptacle/ESD, test points. Run ERC before PCB placement.

PCB STEP is intentionally absent: generate it only from a reviewed board outline and 3D-footprint assignment, then place it under `exports/preview/` as a generated fit-check artifact.

See [PD architecture review](../../docs/pd-architecture.md) and [validation plan](../../docs/validation-plan.md).
