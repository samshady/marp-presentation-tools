---
marp: true
theme: cargobeamer
paginate: true
footer: "CargoBeamer — KI & Automatisierung | 2026"
---

<style>
/* Color icons with cargobeamer primary blue */
.icon-blue {
  text-align: center;
  margin-bottom: 10px;
}
.icon-blue svg,
.icon-blue img {
  width: 64px;
  height: 64px;
  fill: none;
  stroke: #6EC8FF;
  stroke-width: 2;
}
.icon-blue svg *[fill] {
  fill: #6EC8FF;
}
</style>

<!-- _class: title -->

# KI & Robotik

## Automatisierung der Zukunft

---

## KI in der Industrie

<div class="icon-blue">

![](icons/carbon_ai.svg)

</div>

- **Machine Learning** — Mustererkennung in Produktionsdaten
- **Computer Vision** — Qualitätskontrolle via Bildverarbeitung
- **Predictive Maintenance** — Vorhersage von Wartungsbedarf

---

## Robotik

<div class="icon-blue">

![](icons/tabler_robot.svg)

</div>

| Typ | Einsatzbereich | Vorteil |
|---|---|---|
| Industrieroboter | Fertigung | Präzision, 24/7 Betrieb |
| Kollaborative Roboter | Montage | Mensch-Roboter-Interaktion |
| Autonome Roboter | Logistik | Flexible Navigation |

---

## Moderne Computerarchitektur

<div class="icon-blue">

![](icons/mdi_computer.svg)

</div>

- **Edge Computing** — Verarbeitung direkt am Sensor
- **Cloud-Plattformen** — Skalierbare KI-Infrastruktur
- **GPU-Beschleunigung** — Training komplexer Modelle

---

> Künstliche Intelligenz ist der Schlüssel zur nächsten Generation industrieller Automatisierung.

```python
def predict_failure(sensor_data):
    model = load_model("maintenance_v2.pt")
    return model.predict(sensor_data)
```
