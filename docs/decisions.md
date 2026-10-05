# Decisions

## D-001 — Place the project in `projects/rack-pdu`

**Decision:** Use the existing `projects/` group rather than create a second top-level hardware-project group.

**Why:** The workspace already stores unrelated project repositories under `projects/`. `rack-pdu` is independent of the active `pvg-character-loader` repository.

## D-002 — Keep a one-port validation architecture

**Decision:** Validate one independently regulated 65 W source channel, then replicate only the validated channel.

**Why:** A fault or PD renegotiation on one PC must not interrupt the other ports. A shared output converter creates coupling and fault-containment risk.

**Consequences:** Every port needs a converter, controlled VBUS path/current limit, VBUS discharge, CC/connector protection, and its own PD policy/control path. The four-port board must have input aggregation and startup management.

## D-003 — Do not select STUSB4710A for the 65 W prototype

**Decision:** Treat STUSB4710A/STEVAL-ISC004V1 as an architectural reference, not a released BOM choice.

**Evidence:** STUSB4710 supports stand-alone source PDOs up to 20 V/5 A, but the documented implementation needs a separate external converter and source path. Public distributor results observed during repository bootstrap report availability risk for STUSB4710AQTR. The evaluation design cannot be assumed to meet 65 W without a converter/path thermal review.

**Why:** A 20 V, 3.25 A (65 W) contract exceeds 3 A. The source must only provide that contract after compliant 5 A e-marked-cable behavior is demonstrated. Do not infer it from a configurable PDO-current field.

References: [STUSB4710 datasheet](https://www.st.com/resource/en/datasheet/stusb4710.pdf), [STEVAL-ISC004V1](https://www.st.com/en/evaluation-tools/steval-isc004v1.html).

## D-004 — Preliminary controller architecture is TPS25750D + external 24 V buck

**Decision:** Use a TI TPS25750D reference-based standalone PD 3.0 source architecture as the preliminary single-port design target, **pending procurement and cable tests**.

**Evidence:** TPS25750D is PD 3.0 compliant, includes VCONN switching, has a 5–20 V/high-voltage path rated to 7 A continuous, and is packaged in 4 × 6 mm QFN ([datasheet](https://www.ti.com/lit/ds/symlink/tps25750.pdf)). It does not replace the adjustable 24 V input buck converter: its integrated paths are a negotiated VBUS path, not a 24 V-to-PDO regulator.

**Why:** It removes custom firmware from the first proof-of-concept while providing an explicit VCONN/PD controller. This is lower risk than attempting a 65 W standalone design around the ST reference before verifying e-mark behavior.

**Risks/gates:** Observed distributor/TI availability information did not establish purchasable stock for TPS25750DRJKR. The design remains blocked until actual availability, supported configuration, 5 A cable discovery/contract behavior, source OCP coordination and TPS25750D thermal dissipation are proven. If unavailable or unsuitable, use a PD-3.0 controller/MCU architecture with documented cable discovery rather than silently downgrading the 65 W requirement.

## D-005 — USB-C-to-Dell adapter remains external and unqualified

**Decision:** Retain AK-ND-C10 as a candidate external adapter; do not integrate a Dell barrel/ID circuit in revision 0.

**Why:** The Akyga page claims 4.5 × 3.0 mm + pin, 18.5–20 V, 5 A and 100 W, but does not prove its Dell ID behavior with the four specific PCs. External adapters preserve a standard USB-C output while compatibility is tested.

## D-006 — Four 65 W ports are conditionally within the PSU rating

**Decision:** Do not add a fifth 65 W port. Four 65 W ports proceed only with measured converter efficiency and thermal/startup validation.

**Why:** The nominal 260 W output load leaves 61.6 W at the PSU output. At preliminary 90–94% converter efficiency, the four-channel 24 V input demand is 288.9–276.6 W; see [power budget](power-budget.md). That is not enough margin to assume simultaneous startup/fault behavior without test.

## D-007 — Enclosure is a parametric concept, not a production drawing

**Decision:** Model a 1U 10-inch tray/lid with a conservatively limited internal width and a RSP-320 envelope in FreeCAD. Delay fabrication dimensions, final vents and cuts until physical measurements are recorded.

**Why:** 10-inch rail geometry is a de facto convention. The PSU data sheet confirms envelope and screw penetration limits, but terminal wire bend, terminal cover and airflow interface must be checked on the actual purchased unit.

## D-008 — No reuse of HomeLab-PDU-V1 files

**Decision:** Study but do not copy the Shrike-Lab design, CAD, PCB, drawings, or BOM.

**Why:** It targets a different HRP-300-24 PSU. It is licensed CERN-OHL-S v2, whose reciprocal obligations would apply to derivatives. This repository has no derived source files. Reference: [HomeLab-PDU-V1 README](https://github.com/Shrike-Lab/HomeLab-PDU-V1).
