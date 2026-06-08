---
marp: true
theme: cargobeamer
paginate: true
footer: "CargoBeamer — KI & Automatisierung | 2026"
---

<!-- _class: title -->

<style scoped>
.deco-icon {
  position: absolute;
  opacity: 0.3;
  pointer-events: none;
}
.deco-tr { top: 30px; right: 40px; width: 80px; }
.deco-bl { bottom: 80px; left: 40px; width: 60px; }
</style>

<img src="icons/carbon_ai.svg" class="deco-icon deco-tr">
<img src="icons/tabler_robot.svg" class="deco-icon deco-bl">

# KI & Robotik

## Automatisierung der Zukunft

---

<style scoped>
.deco-icon {
  position: absolute;
  opacity: 0.12;
  pointer-events: none;
}
.deco-tr { top: 20px; right: 20px; width: 60px; }
.deco-tl { top: 30px; left: 30px; width: 50px; }
.deco-mr { top: 50%; right: 30px; width: 40px; transform: translateY(-50%); }
</style>

<img src="icons/carbon_ai.svg" class="deco-icon deco-tl">
<img src="icons/mdi_computer.svg" class="deco-icon deco-mr">

## KI in der Industrie

- **Machine Learning** — Mustererkennung in Produktionsdaten
- **Computer Vision** — Qualitätskontrolle via Bildverarbeitung
- **Predictive Maintenance** — Vorhersage von Wartungsbedarf

---

<style scoped>
.deco-icon {
  position: absolute;
  opacity: 0.12;
  pointer-events: none;
}
.deco-tr { top: 20px; right: 20px; width: 50px; }
.deco-tl { top: 30px; left: 30px; width: 60px; }
.deco-ml { top: 40%; left: 20px; width: 45px; }
</style>

<img src="icons/tabler_robot.svg" class="deco-icon deco-tl">
<img src="icons/carbon_ai.svg" class="deco-icon deco-ml">

## Robotik

| Typ | Einsatzbereich | Vorteil |
|---|---|---|
| Industrieroboter | Fertigung | Präzision, 24/7 Betrieb |
| Kollaborative Roboter | Montage | Mensch-Roboter-Interaktion |
| Autonome Roboter | Logistik | Flexible Navigation |

---

<style scoped>
.deco-icon {
  position: absolute;
  opacity: 0.12;
  pointer-events: none;
}
.deco-tr { top: 20px; right: 20px; width: 60px; }
.deco-tl { top: 30px; left: 30px; width: 50px; }
.deco-mr { top: 45%; right: 25px; width: 40px; }
</style>

<img src="icons/mdi_computer.svg" class="deco-icon deco-tl">
<img src="icons/tabler_robot.svg" class="deco-icon deco-mr">

## Moderne Computerarchitektur

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
