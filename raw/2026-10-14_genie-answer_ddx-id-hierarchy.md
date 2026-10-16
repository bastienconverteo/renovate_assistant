Source: Databricks Genie answer, pasted by Bastien in the project thread on 2026-10-14 21:07 UTC.
Bastien's question (in French): "Quelle est la différence entre les différents IDs dans DDX? brand_mdm_id, global_mdm_id, brand_customer_id, global_customer_id etc.?"
Genie's answer below is unchanged.

---

Voici la hiérarchie des IDs, du plus granulaire au plus global:
1. `source_customer_id` — L'ID tel qu'il arrive du système source (Salesforce/Demandware, MARS, CEGID). Chaque système source a son propre schéma d'ID. Un même client peut avoir plusieurs `source_customer_id` s'il a été enregistré dans plusieurs systèmes.
2. `brand_customer_id` = `brand_mdm_id` — L'ID unifié au niveau de la marque. C'est le résultat de la résolution d'identité au sein d'une marque (ex: tous les clients Kiehl's fusionnés via email/phone/address matching, quel que soit le système source). Ces deux noms désignent le même concept (ratio 1:1, ~10.5M au Canada):

* `brand_customer_id` → nom utilisé dans SuperGold / `crm_reporting`
* `brand_mdm_id` → nom utilisé dans DDX actuel / Liveramp / `crm_base`

3. `global_mdm_id` = `global_customer_id` — L'ID cross-brand. Représente une personne physique identifiée à travers plusieurs marques (ex: quelqu'un qui achète chez Kiehl's ET Lancôme a 2 `brand_mdm_id` distincts mais 1 seul `global_mdm_id`). Ratio ~1.32:1 (10.5M brand_mdm → 8.0M global_mdm). Même renommage SuperGold:

* `global_mdm_id` → nom DDX actuel
* `global_customer_id` → nom SuperGold

Le point critique à retenir: tous ces IDs sont hashed en MD5 avec le suffixe `_222` quand ils passent de `crm_base` (PII, unhashed) vers `crm_reporting` / `crm_analytics` (analytique, hashed). La formule: `md5(concat(original_id, '_222'))`. Et, les IDs ne sont uniques que par `brand_code` — toujours filtrer sur la marque à chaque étape de join.
