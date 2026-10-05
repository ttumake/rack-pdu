# Validation plan

## Safety boundary

This plan is for an experienced builder with an isolated, fused mains setup, appropriate probes and electronic loads. It does not make the design safe by itself. Perform low-voltage port work from a current-limited 24 V bench supply first. Connect the RSP-320 to mains only after enclosure PE, IEC inlet fuse, terminal cover, strain relief and clearances have been inspected.

No Dell PC is connected until all one-port electrical acceptance items pass with loads.

## Stage 0 — Inputs and mechanical fit

| Test | Method | Pass condition |
| --- | --- | --- |
| Rack fit | Measure rail clear width, hole pattern/thread, usable depth and rail offsets; enter values in FreeCAD spreadsheet | Tray/ears fit the actual rack without forcing rails |
| PSU geometry | Inspect purchased RSP-320-24 against manufacturer drawing; verify bottom/side mount pattern, terminal cover, wire bend and all airflow openings | FreeCAD model updated from actual specimen; no screw exceeds data-sheet penetration limit |
| Clearance | Assemble tray, PSU, board mock, lid and representative USB-C/IEC wiring | No contact; serviceable screws/connectors; lid closes without loading terminals |
| PE bond | Measure earth stud-to-exposed-metal continuity and inspect hardware/washer/marking | Low-resistance permanent protective-earth path; no PE used as signal return |

## Stage 1 — One-port, bench-supply electrical bring-up

| Test | Method | Pass condition |
| --- | --- | --- |
| Pre-power inspection | Schematic/ERC and PCB/DRC once circuit/layout exist; check component orientation and resistance to GND | No unresolved errors; no short before power |
| Controlled 24 V enable | Current-limited bench supply, no sink | No uncontrolled VBUS; controller starts without excess input current |
| USB-C attach | Test with known compliant sink and PD analyzer | Correct attach/detach and orientation behavior; no source voltage before negotiation policy permits it |
| PDO matrix | Request every advertised PDO using PD analyzer/e-load | Voltage is within negotiated tolerance and no non-advertised voltage occurs |
| 65 W path | Use known 5 A e-marked C-C cable, PD analyzer and 20 V/3.25 A electronic load | Cable capability is observed/handled as required by controller; stable 65 W operation; no connector/path overheating |
| 3 A cable boundary | Use a compliant 3 A cable or cable emulator | Controller never creates an unsafe over-3-A path; behavior documented |
| Current limit / short | Step load above limit and apply controlled VBUS short through rated fixture | Per-port protection operates; no damaged part; recovery matches design policy |
| VBUS discharge | Disconnect/disable and log VBUS with scope | Meets chosen USB-C discharge policy; no hazardous retained VBUS |
| ESD/surge protection review | Verify chosen protection device ratings/layout; perform only with suitable qualified equipment | No claim of IEC compliance without formal test |

## Stage 2 — Thermal and dynamic validation

| Test | Method | Pass condition |
| --- | --- | --- |
| Full-load soak | 20 V/3.25 A load for minimum 60 min at expected ambient with lid fitted | All measured component and connector temperatures remain within derated limits; no oscillation or thermal shutdown |
| Connect/disconnect cycling | Repeated attach/detach under zero, nominal and near-limit load | One channel recovers cleanly; no reset or VBUS disturbance on an independently powered reference channel |
| Input disturbance | Step 24 V input within allowed range and cycle source supply | Controlled start and recovery; no unsafe output |
| Fan/vent flow | Measure/observe flow and temperatures with lid installed | No blocked PSU opening; the enclosure does not reverse or starve intended cooling |

## Stage 3 — Multi-port integration

| Test | Method | Pass condition |
| --- | --- | --- |
| Four-port simultaneous load | Four electronic loads at 20 V/3.25 A, then representative startup profiles | Input stays below derated PSU capacity; ≥25 W measured normal-operation margin |
| Per-port fault isolation | Short/overload one port while three ports have nominal loads | Faulted port contains/retries per policy; other ports retain negotiated output |
| Aggregate startup | Cold start with loads/PD analyzers attached | No uncontrolled cycling; no PSU hiccup under intended startup policy |
| Mains thermal soak | Enclosed, bonded unit at intended line voltage and ambient | PSU and port temperatures pass; no odor, discoloration or abnormal noise |

## Stage 4 — Dell integration

Record each actual model, OEM adapter label, BIOS messages and sustained load result. Test AK-ND-C10 only after Stages 0–3 pass.

| Test | Pass condition |
| --- | --- |
| Adapter recognition | No Dell unknown/undersized-adapter warning, or documented explicit acceptance decision |
| Boot and stress load | PC boots and sustains a representative workload without power/thermal event |
| Four-PC coexistence | Individual attach/detach or PC fault does not interrupt another PC |

## Release gates

Fabrication release requires recorded pass evidence for ratings, ERC/DRC, protection behavior, thermal data, mechanical fit, PE/mains integration review and the exact Dell/adapter setup. A conceptual model, an unloaded PD negotiation, or a clean ERC alone is not release evidence.
