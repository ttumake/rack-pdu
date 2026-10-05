# USB-C PD source architecture review

## Constraint that drives the architecture

The target per-port output is 65 W. At 20 V that is 3.25 A. A standard 3 A C-to-C cable is not sufficient; a 5 A electronically marked cable and source behavior that handles its capability are required throughout the PD cable path. The Dell barrel adapter is downstream and must also be rated for the negotiated power.

The controller does not replace the power converter. With a 24 V source, each port needs a regulated buck stage that follows the negotiated PDO, a controlled VBUS path, overcurrent/fault management, discharge and connector protection.

## Compared options

| Architecture | Advantages | Blocking risk | Result |
| --- | --- | --- | --- |
| **STUSB4710A + external buck/path** | Standalone source controller; source PDOs through 20 V/5 A; ST evaluation design is useful reference | Controller availability observed as restricted/obsolete at one distributor; reference converter/path not proven for 65 W; cable/e-marker behavior must not be assumed from the PDO field | Reference only; not selected |
| **TPS25750D + external 24 V buck** | PD 3.0, VCONN, integrated 5–20 V 7 A high-voltage path, PD policy engine, no external MCU needed; pre-configured firmware/GUI | Device procurement not confirmed; configuration/cable-current behavior and thermal loss must be demonstrated; separate buck still required | **Preliminary one-port architecture** |
| **PD PHY/controller + MCU + external power path** | Firmware can implement and log policy, cable rules, current/thermal coordination and system sequencing | Firmware, USB-PD compliance, test burden and long-term maintenance are substantially higher | Fallback if the standalone controller cannot prove/meet the 5 A source requirement |

Primary sources: [TPS25750 datasheet](https://www.ti.com/lit/ds/symlink/tps25750.pdf), [STUSB4710 datasheet](https://www.st.com/resource/en/datasheet/stusb4710.pdf), [STEVAL-ISC004V1](https://www.st.com/en/evaluation-tools/steval-isc004v1.html).

## Preliminary one-port functional chain

```text
24 V protected input
  -> per-port fuse / reverse-fault isolation / input transient suppression
  -> adjustable synchronous buck, 5/9/12/15/20 V selected only under PD policy
  -> controlled, current-limited VBUS path
  -> USB-C receptacle + CC/ESD protection
  -> qualified 5 A e-marked C-C cable
  -> AK-ND-C10 candidate (external; not Dell-ID qualified)
  -> actual Dell DC input

TPS25750D: CC/VCONN/PD policy, PDO control, VBUS monitoring and fault interface
```

### Required preliminary design rules

1. Default VBUS behavior and any 5 V source path must follow the controller's reference configuration. Do not backfeed a 20 V buck output into a 5 V-only path.
2. The buck output may change only when the PD policy has removed/disabled VBUS or the selected reference design explicitly supports the transition. The architecture must prevent a voltage step on an attached sink.
3. Configure no PDO above 3 A until cable discovery/authorization is demonstrated with a PD analyzer and known 3 A/5 A e-marked cables.
4. Protection is layered: input fuse/isolation, converter current limit, controlled VBUS OCP, connector TVS/ESD protection, and active VBUS discharge.
5. Keep all initial testing low-voltage, current-limited and into electronic loads. Mains integration and Dell tests are later gates.

## Why a four-layer PCB is the starting point

A 65 W/5 A PD power path needs short high-current loops, continuous low-impedance return, controlled switching-current geometry, thermal copper and a clean CC/PD region. A 4-layer board allows a solid internal ground plane plus dedicated 24 V/VBUS copper without routing power return through the controller area. This is a starting constraint, not a fabrication release: the eventual stack-up, copper weight, via/current capacity and thermal performance must be quoted and verified with the chosen assembler.

## Assembly and procurement risk

TPS25750D is a 4 × 6 mm QFN and typical synchronous-buck/USB-C parts are fine-pitch or bottom-terminated packages. Professional assembly is recommended for the prototype; request an assembly quote for one 4-layer board and confirm placement, X-ray/AOI availability, stencil policy, component consignment and private-consumer ordering. Public availability checks during bootstrap did not establish stock for TPS25750DRJKR, so do not order the rest of the BOM around it yet.
