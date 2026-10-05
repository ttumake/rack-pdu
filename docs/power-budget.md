# Preliminary power budget

## Fixed source rating

The RSP-320-24 data sheet rates its 24 V output at 13.4 A / **321.6 W**. The specified AC efficiency is 89% typical. Do not use the listing's 40 A making/inrush current as operating input consumption; the data sheet defines it as inrush at 230 VAC.

## Four-port calculation

Assumptions below are explicit planning values, not measured performance.

| Quantity | Formula | 94% per-port buck | 90% per-port buck |
| --- | --- | ---:| ---:|
| One PC output | 20 V × 3.25 A | 65.0 W | 65.0 W |
| Four PC outputs | 4 × 65 W | 260.0 W | 260.0 W |
| Four converter input demand | 260 W / efficiency | 276.6 W | 288.9 W |
| Margin to 321.6 W PSU rating | 321.6 W − input demand | 45.0 W (14.0%) | 32.7 W (10.2%) |
| Approx. 24 V rail current | input demand / 24 V | 11.53 A | 12.04 A |

This leaves no basis for a fifth simultaneous 65 W port: five outputs are 325 W before any conversion loss, exceeding the PSU rating.

## System limits and required measurements

- The PSU's built-in fan, the PD-controller rails, LEDs, bleeders and any external cooling are not separately budgeted in the table. Their real consumption and the converter losses are measured at full load.
- `65 W` is a load target. Dell actual requirements may be 65 W, 90 W or other values; final ratings follow the actual adapter labels.
- A 20 V/3.25 A contract is greater than 3 A. The complete port path — controller policy, VCONN/e-marker behavior, USB-C receptacle, PCB copper/connectors, cable and AK-ND-C10 — needs a validated 5 A rating.
- The design must characterize simultaneous attach, converter enable sequencing and PSU hiccup/restart behavior. A 10–14% steady-state margin is not a transient budget.
- At 115 VAC, use the data-sheet derating curve when determining field use. Do not assume the 321.6 W nameplate rating at every line voltage/ambient.

## Design allocation before test

| Rail/item | Preliminary allocation | Status |
| --- | ---:| --- |
| Four PD loads | 260 W | Target only |
| Per-port converter loss | ≤7.22 W total at 90% | Must be measured per channel |
| Logic, protection, indicators | ≤4 W total | To be measured |
| System PSU headroom | ≥25 W after measured auxiliaries at representative ambient | Acceptance gate |

The prototype passes its power-budget gate only if the worst normal simultaneous load, auxiliaries, and measured converter losses remain below the derated PSU rating with at least 25 W of margin. Fault/startup behavior has a separate validation gate.
