import re

with open("Seminar_E-Business/Seminar_E-Business.md", "r") as f:
    text = f.read()

old_block = text.split("## Literaturverzeichnis")[1]

new_block = """

### 1. Wissenschaftliche Literatur (ca. 12)

- Akerlof, G. A. (1970). The Market for "Lemons": Quality Uncertainty and the Market Mechanism. *The Quarterly Journal of Economics*, *84*(3), 488–501.
- Ba, S., & Pavlou, P. A. (2002). Evidence of the Effect of Trust Building Technology in Electronic Markets: Price Premiums and Buyer Behavior1. *MIS Quarterly*, *26*(3), 243–268.
- Babić Rosario, A., Sotgiu, F., De Valck, K., & Bijmolt, T. H. A. (2016). The Effect of Electronic Word of Mouth on Sales: A Meta-Analytic Review of Platform, Product, and Metric Factors. *Journal of Marketing Research*, *53*(3), 297–318.
- Banerjee, S., Dellarocas, C., & Zervas, G. (2021). Interacting User-Generated Content Technologies: How Questions and Answers Affect Consumer Reviews. *Journal of Marketing Research*, *58*(4), 742–761.
- Bolton, G. E., Katok, E., & Ockenfels, A. (2004). How Effective Are Electronic Reputation Mechanisms? An Experimental Investigation. *Management Science*, *50*(11), 1587–1602.
- Chevalier, J. A., & Mayzlin, D. (2006). The Effect of Word of Mouth on Sales: Online Book Reviews. *Journal of Marketing Research*, *43*(3), 345–354.
- Dellarocas, C. (2003). The Digitization of Word of Mouth: Promise and Challenges of Online Feedback Mechanisms. *Management Science*, *49*(10), 1407–1424.
- Forman, C., Ghose, A., & Wiesenfeld, B. (2008). Examining the Relationship between Reviews and Sales: The Role of Reviewer Identity Disclosure in Electronic Markets. *Information Systems Research*, *19*(3), 291–313.
- Hu, N., Zhang, J., & Pavlou, P. A. (2009). Overcoming the J-shaped Distribution of Product Reviews. *Communications of the ACM*, *52*(10), 144–147.
- Resnick, P., Kuwabara, K., Zeckhauser, R., & Friedman, E. (2000). Reputation Systems. *Communications of the ACM*, *43*(12), 45–48.

### 2. Primärquellen Idealo.de (ca. 3)

<!-- - idealo. (2026). *Über idealo*. Abgerufen am 12.05.2026, von https://www.idealo.de/unternehmen/ueber-idealo -->

- idealo internet GmbH. (o. D.). *Die AGB Der Idealo Internet GmbH*. Abgerufen am 12.05.2026, von https://www.idealo.de/legal/agb
- idealo internet GmbH. (o. D.). *https://www.idealo.de/aktion/ranking*. Abgerufen am 12.05.2026, von https://www.idealo.de/aktion/ranking
  <!-- - idealo internet GmbH. (o. D.). *Digital Services Act*. Abgerufen am 12.05.2026, von https://www.idealo.de/unternehmen/digital-services-act -->

### 3. Marktdaten und Statistiken (ca. 3)

- EHI Retail Institute. (2022). *E-Commerce 2021: Zeit Des Wachstums - EHI Retail Institute*. Abgerufen am 12.05.2026, von https://www.ehi.org/presse/e-commerce-2021-zeit-des-wachstums/
- Statista. (o. D.). *Trust in Product Research Results Germany 2024*. Abgerufen am 12.05.2026, von https://www.statista.com/statistics/1460541/trust-product-research-results-germany/
<!-- - Statista. (o. D.). *eCommerce - Worldwide | Statista Market Forecast*. Abgerufen am 12.05.2026, von https://www.statista.com/outlook/emo/ecommerce/worldwide -->

### 4. Fachpresse (ca. 2)

- heise online. (2025). *Wettbewerbszentrale Erhebt Vorwürfe Gegen Trustpilot*. Abgerufen am 12.05.2026, von https://www.heise.de/news/Wettbewerbszentrale-erhebt-Vorwuerfe-gegen-Trustpilot-10417863.html
  <!-- - heise online. (2020). *Yelps Bewertungssystem Rechtmäßig: BGH Hebt Urteil Des OLG Auf*. Abgerufen am 12.05.2026, von https://www.heise.de/news/Yelps-Bewertungssystem-rechtmaessig-BGH-hebt-Urteil-des-OLG-auf-4637314.html -->
  <!-- - heise online. (2019). *Amazon Verhindert 13 Millionen Fake-Bewertungen*. Abgerufen am 12.05.2026, von https://www.heise.de/news/Amazon-verhindert-13-Millionen-Fake-Bewertungen-4551032.html -->
"""

new_text = text.replace(old_block, new_block)

with open("Seminar_E-Business/Seminar_E-Business.md", "w") as f:
    f.write(new_text)

print("done")
