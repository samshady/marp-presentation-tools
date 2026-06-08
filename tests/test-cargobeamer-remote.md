---
marp: true
theme: cargobeamer
paginate: true
footer: "CargoBeamer — KI & Automatisierung | 2026"
---

<!-- _class: title -->

# KI & Robotik

## Automatisierung der Zukunft

---

<style scoped>
section {
  background-image: url("icons/carbon_ai.svg");
  background-repeat: no-repeat;
  background-position: calc(100% - 60px) 50%;
  background-size: 80px;
}
</style>

## KI in der Industrie

- **Machine Learning** — Mustererkennung in Produktionsdaten
- **Computer Vision** — Qualitätskontrolle via Bildverarbeitung
- **Predictive Maintenance** — Vorhersage von Wartungsbedarf

---

<style scoped>
section {
  background-image: url("icons/tabler_robot.svg"), url("icons/carbon_ai.svg");
  background-repeat: no-repeat;
  background-position: calc(100% - 60px) 30%, 60px 60%;
  background-size: 80px, 70px;
}
</style>

## Robotik

| Typ | Einsatzbereich | Vorteil |
|---|---|---|
| Industrieroboter | Fertigung | Präzision, 24/7 Betrieb |
| Kollaborative Roboter | Montage | Mensch-Roboter-Interaktion |
| Autonome Roboter | Logistik | Flexible Navigation |

---

<style scoped>
section {
  background-image: url("icons/mdi_computer.svg");
  background-repeat: no-repeat;
  background-position: calc(100% - 60px) 50%;
  background-size: 80px;
}
</style>

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
