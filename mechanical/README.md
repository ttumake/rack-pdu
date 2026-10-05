# Parametric enclosure concept

`rack-pdu-concept.FCStd` is a native FreeCAD **concept**. The `Parameters` spreadsheet is the source of all editable dimensions. The visible tray/lid, PSU envelope, PCB envelope and front connector keep-outs are derived from those values.

## Model status

- **Accurate from RSP-320 data sheet:** outer envelope 215 × 115 × 30 mm; base/side M4 limitations; 150 mm mounting-hole pitch and 32.5 mm datum shown in the manufacturer drawing.
- **Deliberate placeholders:** rack rail geometry; tray depth; PSU terminal cover/wire bend envelope; exact terminal locations; USB-C receptacle and IEC inlet cuts; final vent opening location; PCB dimensions/standoffs.
- **Not fabrication-ready:** the tray uses simple solids representing 1.2 mm folded sheet, not a released bend allowance/K-factor drawing. The lid vent rectangles are an explicitly marked concept region and must not dictate final airflow.

## Update sequence

1. Measure the actual rack and update `RackRailClearWidth`, `RackPanelWidth`, `RackUnitHeight`, hole pattern and `TrayDepth`.
2. Inspect the actual PSU before modifying any mount/terminal/vent geometry. Never exceed 3 mm base or 5 mm side screw penetration stated in the data sheet.
3. Replace the PCB envelope/connector keep-outs only after the KiCad board and connector 3D models exist.
4. Determine inlet/outlet vent placement from the actual PSU fan opening/flow direction and an assembled thermal test; update/remove the conceptual vent group.
5. Export STEP only as a generated fit-check artifact after native model review.

## Orientation

The PSU model uses 115 mm across the tray width and 215 mm front-to-back. The 90 mm-wide preliminary PCB envelope is alongside it. That arrangement needs approximately 209 mm before side clearances, so it may fit a measured ~222 mm rail opening, but it is not a claim that the target rack accepts it.
