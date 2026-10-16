Source: Databricks Genie answer, pasted by Bastien in the project thread on 2026-10-14 21:12 UTC.
Question asked (suggested by Claude): "In customer360, is brand_customer_id equal to brand_mdm_id on every row? Give the share of rows where they match."
Genie's answer below is unchanged.

---

0% des lignes — brand_customer_id et brand_mdm_id ne sont jamais égaux dans customer360 (0 sur 14.2M lignes).

Cependant, c'est une relation 1:1 parfaite: les 11.65M brand_customer_id distincts mappent chacun vers exactement 1 brand_mdm_id (et inversement). Ce sont donc deux systèmes d'identifiants distincts — deux valeurs MD5 différentes — avec une correspondance biunivoque, et non deux noms pour la même valeur.

Pour rejoindre l'un à l'autre, il faut passer par dim_customer_bridge (qui contient le mapping brand_customer_id → brand_mdm_id → global_mdm_id). Ils ne sont pas interchangeable directement dans un join.

Je corrige au passage ce que j'avais dit plus tôt: quand l'appendix note "two names for the same concept", ça veut dire qu'ils représentent le même niveau d'identité (la marque), pas que les valeurs sont identiques.
