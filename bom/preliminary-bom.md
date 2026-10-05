# Preliminary BOM and sourcing notes

> **Not an order list.** References and costs are planning estimates, not quotes. No substitute is authorized without datasheet, lifecycle, package, thermal and cable-capability review.

## One-port PD prototype

| Ref/function | Preliminary part / specification | Qty | Estimated EUR, single unit | Sourcing / qualification note |
| --- | --- | ---:| ---:| --- |
| PD source controller | TI TPS25750DRJKR, 4 × 6 mm QFN | 1 | 7–15 | Preliminary architecture. Public availability check did not establish stock; verify lifecycle/lead time before schematic capture. |
| PD configuration/programming | TI-supported configuration storage/programming path per selected reference | 1 | 2–8 | Exact parts/programming workflow TBD from the selected controller reference design. |
| 24 V → PDO buck | 4-layer, ≥36 V input, ≥5 A output synchronous buck architecture | 1 | 15–35 | Choose only after transient, control-transition and thermal design review. This is a function, not an approved part number. |
| Controlled VBUS/OCP/discharge | ≥28 V, ≥5 A path with controllable current limit, reverse blocking and discharge | 1 | 5–15 | Must coordinate with TPS25750D and remain safe during PDO changes/faults. |
| USB-C receptacle | Mid-mount/through-hole hybrid, 5 A VBUS contacts; vendor mechanical drawing required | 1 | 1–4 | Verify panel access, retention, CC pinout and assembly process. |
| CC/VBUS ESD and VBUS TVS | USB-C-rated low-capacitance CC protection and VBUS transient part | 1 set | 2–8 | Select after receptacle/controller reference and surge environment are fixed. |
| Input fuse/isolation | Per-port DC fuse and reverse-fault protection | 1 set | 2–7 | Current rating follows measured worst case; do not use a fuse as the only semiconductor protection. |
| Inductor, MOSFETs, capacitors, resistors | Rated for converter ripple, voltage and temperature | 1 set | 10–25 | Values/package/ratings TBD from final buck design. |
| 4-layer PCB | Approx. 90 × 150 mm initial envelope | 1 | 25–70 | Private consumer cost varies strongly with fab, finish, panel/minimum order and assembly. Quote after layout. |
| Professional assembly/stencil | One or small batch | 1 | 50–150 | Confirm QFN capability and private-customer terms; often dominates a one-off. |

**Planning subtotal, one one-port board:** **€119–337**, excluding shipping, VAT/import, PD analyzer, electronic load, bench supply, enclosure, cable and Dell adapter. This range is an estimate inferred from low-quantity prototype economics; it is not supplier pricing.

## System items (four-port target)

| Item | Qty | Estimated EUR | Note |
| --- | ---:| ---:| --- |
| Mean Well RSP-320-24 | 1 | Quote required | Selected design basis; purchase not confirmed. [Retail listing](https://www.reichelt.com/de/en/shop/product/switching_power_supply_pfc_322_w_24_v_13_4_a-147896) serves only as source/product reference. |
| Fused IEC inlet, switch, PE hardware, terminal cover/wiring | 1 set | 30–80 | Select safety-rated, appropriately approved components. |
| Folded steel/aluminium tray and lid, coating | 1 | 80–250 | Depends on one-off sheet-metal service and final drawings. |
| AK-ND-C10 candidate adapters | 4 | Quote required | Candidate is rated 100 W/5 A by Akyga but Dell recognition remains untested. |
| 5 A e-marked C-C cables | 4 | 40–100 total | Require explicit 5 A/e-marker rating and test evidence. |

## Supplier constraints

- Treat a distributor's web stock as time-sensitive. Capture date, supplier, MOQ, lead time, package and price when placing an order.
- Check whether the chosen PCB assembler accepts private consumers, supplied parts, LCSC/distributor part numbers and QFN assembly at the required pitch.
- Do not use marketplace adapters/cables with only a connector-size claim; require an explicit current/power rating and test them.
- The source architecture and cost estimate are deliberately provisional until controller stock and the final converter are selected.
