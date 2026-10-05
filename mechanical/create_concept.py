"""Generate the native FreeCAD enclosure concept.

The spreadsheet inside rack-pdu-concept.FCStd is the editable dimensional source.
This generator is retained for reproducibility; it is not a fabrication drawing.
"""

import FreeCAD as App
import Part

OUT = "rack-pdu-concept.FCStd"

doc = App.newDocument("rack_pdu_concept")
params = doc.addObject("Spreadsheet::Sheet", "Parameters")
params.Label = "Parameters — edit values/status before modeling release"

rows = [
    ("Parameter", "Value", "Unit", "Status / source"),
    ("RackPanelWidth", "254 mm", "mm", "Concept only — measure actual rack"),
    ("RackUnitHeight", "44.45 mm", "mm", "1U nominal — measure rail pattern"),
    ("RackRailClearWidth", "222.25 mm", "mm", "Placeholder de-facto 10-in convention"),
    ("MaterialThickness", "1.2 mm", "mm", "Concept sheet thickness"),
    ("BendRadius", "1.2 mm", "mm", "Concept only; obtain fabricator bend data"),
    ("TrayDepth", "270 mm", "mm", "Placeholder; rack/depth clearance unmeasured"),
    ("TrayInternalWidth", "=RackRailClearWidth - 2 * MaterialThickness", "mm", "Derived"),
    ("PSULength", "215 mm", "mm", "Confirmed RSP-320 data sheet envelope"),
    ("PSUWidth", "115 mm", "mm", "Confirmed RSP-320 data sheet envelope"),
    ("PSUHeight", "30 mm", "mm", "Confirmed RSP-320 data sheet envelope"),
    ("PSUPositionX", "4 mm", "mm", "Concept side clearance"),
    ("PSUFrontOffset", "32.5 mm", "mm", "Concept; terminal/wire envelope unmeasured"),
    ("PSUMountPitch", "150 mm", "mm", "Data-sheet drawing; transcription review required"),
    ("PSUMountDatum", "32.5 mm", "mm", "Data-sheet drawing; transcription review required"),
    ("PCBWidth", "90 mm", "mm", "Concept envelope only"),
    ("PCBDepth", "150 mm", "mm", "Concept envelope only"),
    ("PCBPositionX", "128 mm", "mm", "Concept; must follow KiCad board"),
    ("PCBFrontOffset", "65 mm", "mm", "Concept; must follow connector placement"),
    ("PCBStandoffHeight", "6 mm", "mm", "Concept only"),
    ("ConnectorCutoutWidth", "10 mm", "mm", "Placeholder; use connector drawing"),
    ("ConnectorCutoutHeight", "4 mm", "mm", "Placeholder; use connector drawing"),
    ("PortPitch", "16 mm", "mm", "Placeholder; use connector drawing"),
    ("PortStartX", "132 mm", "mm", "Placeholder; use connector drawing"),
    ("VentSlotWidth", "3 mm", "mm", "Concept only; airflow gate unresolved"),
    ("VentSlotLength", "35 mm", "mm", "Concept only; airflow gate unresolved"),
]

for index, (name, value, unit, status) in enumerate(rows, 1):
    params.set("A%d" % index, name)
    params.set("B%d" % index, value)
    params.set("C%d" % index, unit)
    params.set("D%d" % index, status)
    if index > 1:
        params.setAlias("B%d" % index, name)

for column, width in (("A", 190), ("B", 150), ("C", 55), ("D", 360)):
    params.setColumnWidth(column, width)
params.setStyle("A1:D1", "bold", "add")
params.setBackground("A1:D1", (0.20, 0.20, 0.20))
params.setStyle("A1:D1", "underline", "add")
params.setBackground("A2:D26", (0.93, 0.93, 0.93))
params.set("A28", "DO NOT FABRICATE")
params.set("B28", "Update M-001 / M-002 measurements first")
params.setStyle("A28:B28", "bold", "add")
params.setBackground("A28:B28", (1.0, 0.60, 0.30))

# Geometry uses spreadsheet expressions. X is rack width, Y is front-to-back depth, Z is height.
def make_box(name, label, length, width, height, color, transparency=0):
    obj = doc.addObject("Part::Box", name)
    obj.Label = label
    obj.Length = length
    obj.Width = width
    obj.Height = height
    return obj

bottom = make_box("TrayBottom", "Tray bottom — 1.2 mm concept sheet", 1, 1, 1, (0.08, 0.08, 0.08))
bottom.setExpression("Length", "Parameters.TrayInternalWidth")
bottom.setExpression("Width", "Parameters.TrayDepth")
bottom.setExpression("Height", "Parameters.MaterialThickness")

left = make_box("TrayLeftWall", "Tray left wall — concept fold", 1, 1, 1, (0.08, 0.08, 0.08))
left.setExpression("Length", "Parameters.MaterialThickness")
left.setExpression("Width", "Parameters.TrayDepth")
left.setExpression("Height", "Parameters.RackUnitHeight")

right = make_box("TrayRightWall", "Tray right wall — concept fold", 1, 1, 1, (0.08, 0.08, 0.08))
right.setExpression("Length", "Parameters.MaterialThickness")
right.setExpression("Width", "Parameters.TrayDepth")
right.setExpression("Height", "Parameters.RackUnitHeight")
right.setExpression("Placement.Base.x", "Parameters.TrayInternalWidth - Parameters.MaterialThickness")

rear = make_box("TrayRearWall", "Rear wall — IEC cutout pending", 1, 1, 1, (0.08, 0.08, 0.08))
rear.setExpression("Length", "Parameters.TrayInternalWidth")
rear.setExpression("Width", "Parameters.MaterialThickness")
rear.setExpression("Height", "Parameters.RackUnitHeight")
rear.setExpression("Placement.Base.y", "Parameters.TrayDepth - Parameters.MaterialThickness")

front = make_box("RackFrontPanel", "Front panel — rack hole pattern pending", 1, 1, 1, (0.08, 0.08, 0.08))
front.setExpression("Length", "Parameters.RackPanelWidth")
front.setExpression("Width", "Parameters.MaterialThickness")
front.setExpression("Height", "Parameters.RackUnitHeight")
front.setExpression("Placement.Base.x", "(Parameters.TrayInternalWidth - Parameters.RackPanelWidth) / 2")

lid = make_box("RemovableLid", "Removable ventilated lid — vents conceptual", 1, 1, 1, (0.12, 0.12, 0.12), 20)
lid.setExpression("Length", "Parameters.TrayInternalWidth")
lid.setExpression("Width", "Parameters.TrayDepth")
lid.setExpression("Height", "Parameters.MaterialThickness")
lid.setExpression("Placement.Base.z", "Parameters.RackUnitHeight - Parameters.MaterialThickness")

psu = make_box("RSP320Envelope", "Mean Well RSP-320-24 — confirmed exterior envelope", 1, 1, 1, (0.72, 0.72, 0.75), 25)
psu.setExpression("Length", "Parameters.PSUWidth")
psu.setExpression("Width", "Parameters.PSULength")
psu.setExpression("Height", "Parameters.PSUHeight")
psu.setExpression("Placement.Base.x", "Parameters.PSUPositionX")
psu.setExpression("Placement.Base.y", "Parameters.PSUFrontOffset")
psu.setExpression("Placement.Base.z", "Parameters.MaterialThickness")

pcb = make_box("PCBEnvelope", "PD PCB envelope — not a real board", 1, 1, 1, (0.10, 0.55, 0.18), 30)
pcb.setExpression("Length", "Parameters.PCBWidth")
pcb.setExpression("Width", "Parameters.PCBDepth")
pcb.setExpression("Height", "1.6 mm")
pcb.setExpression("Placement.Base.x", "Parameters.PCBPositionX")
pcb.setExpression("Placement.Base.y", "Parameters.PCBFrontOffset")
pcb.setExpression("Placement.Base.z", "Parameters.MaterialThickness + Parameters.PCBStandoffHeight")

# Display-only front connector envelopes, not panel cuts.
for port in range(4):
    keepout = make_box("Port%dKeepout" % (port + 1), "USB-C port %d keepout — placeholder" % (port + 1), 1, 1, 1, (0.90, 0.15, 0.12), 20)
    keepout.setExpression("Length", "Parameters.ConnectorCutoutWidth")
    keepout.setExpression("Width", "Parameters.MaterialThickness * 2")
    keepout.setExpression("Height", "Parameters.ConnectorCutoutHeight")
    keepout.setExpression("Placement.Base.x", "Parameters.PortStartX + %d * Parameters.PortPitch" % port)
    keepout.setExpression("Placement.Base.y", "-Parameters.MaterialThickness / 2")
    keepout.setExpression("Placement.Base.z", "(Parameters.RackUnitHeight - Parameters.ConnectorCutoutHeight) / 2")

# Display-only vent envelopes. They deliberately do not cut the lid before airflow is verified.
for slot in range(4):
    vent = make_box("ConceptVent%d" % (slot + 1), "Vent %d — conceptual, airflow unverified" % (slot + 1), 1, 1, 1, (0.20, 0.55, 0.80), 45)
    vent.setExpression("Length", "Parameters.VentSlotLength")
    vent.setExpression("Width", "Parameters.VentSlotWidth")
    vent.setExpression("Height", "0.2 mm")
    vent.setExpression("Placement.Base.x", "Parameters.PSUPositionX + 15 mm")
    vent.setExpression("Placement.Base.y", "Parameters.PSUFrontOffset + 20 mm + %d * 12 mm" % slot)
    vent.setExpression("Placement.Base.z", "Parameters.RackUnitHeight")

mount_data = doc.addObject("App::FeaturePython", "PSUMountingData")
mount_data.Label = "RSP-320 mounting limits — data only, do not drill from this model"
mount_data.addProperty("App::PropertyLength", "MountPitch", "Data sheet")
mount_data.MountPitch = 150
mount_data.addProperty("App::PropertyLength", "LongDatum", "Data sheet")
mount_data.LongDatum = 32.5
mount_data.addProperty("App::PropertyString", "BaseThread", "Data sheet")
mount_data.BaseThread = "4 × M4; maximum penetration L = 3 mm"
mount_data.addProperty("App::PropertyString", "SideThread", "Data sheet")
mount_data.SideThread = "4 × M4 each side; maximum penetration L = 5 mm"
mount_data.addProperty("App::PropertyString", "TerminalAndAirflow", "Verification gate")
mount_data.TerminalAndAirflow = "Exact terminal/wire envelope and airflow interface must be inspected on actual PSU."

notes = doc.addObject("App::FeaturePython", "ReleaseGate")
notes.Label = "NOT FABRICATION-READY — measurements M-001 / M-002 open"
notes.addProperty("App::PropertyString", "Purpose", "Release gate")
notes.Purpose = "Fit concept only. Do not derive cut, vent, fastener or mains wiring dimensions from placeholders."
notes.addProperty("App::PropertyString", "Source", "Release gate")
notes.Source = "Mean Well RSP-320 datasheet p. 4; docs/requirements.md"

doc.recompute()
doc.saveAs(OUT)
