# Extract: LiveRamp weekly file schema ("LR for RENOVATE.xlsx")

- Type: sample of the file Canada sends to LiveRamp weekly, with Damien's two added fields; provided by Bastien in inbox/ on 2026-10-08 after Damien's reply
- Original: inbox/LR for RENOVATE.xlsx (git-ignored). Column list only: raw/2026-10-08_schema_liveramp-weekly-file-columns.md
- Ingested: 2026-10-08
- Content: one sheet "LR Values", 51 columns, 3 sample rows. The rows contain real-looking personal data; none is copied into this repo.

## What the file shows
- 49 columns are the current weekly file; columns 50 and 51 (`subcategories`, `Is_Churn_12M_36M`) are the two fields Damien added. Both are empty in the sample rows, so no value format is known.
- Identifiers: `brand_mdm_id`, `global_mdm_id` (MDM naming, see DEC-0003). Brand and division columns: `division`, `brand`.
- Churn and engagement flags already in the current file: `active_buyer_l12m`, `lapsed_buyer_l12m_plus`, `buyer_l14_d`, `new_buyer`, `engaged_prospects_l12m`, `inactive_prospects_l12m`, `inactive_buyers_12m`, `engaged_prospect_6m`, `inactive_prospect_6m`, `active_buyers_6m`, `inactive_prospects_l24m`, `engaged_prospects_l24m`, `churn_12_24_flag`, `churn_24plus_flag`, `global_control_group_flag`. Also `loyalty_status`, `loyalty_tier`.
- Model output: `segment_type` and `segment_value` (sample values seen in rows: a "Likely to Convert 3 months" segment with value 1).
- Profile and preference columns: `skin_concerns`, `hair_concerns`, `retail_channel_preference`, `gender`, `category`, `franchise`.
- Contact and address columns: `first_name`, `last_name`, `date_of_birth`, `email1` to `email4`, `phone_num`, `mobile_num`, `address_line1`, `address_line2`, `state_code`, `city`, `postal_code`, `country_code`, `zip4`, `zip5`. Spending: `lifetime_net_sales`, `12_months_net_sales`. Technical: `last_modified_dt`.

## Consequences
1. The Genie-suggested attributes (`churn_12_24_flag`, `churn_24plus_flag`, `engaged_prospects_l12m`, `segment_type`) are not only Genie predictions: they are columns of the current Canada LiveRamp file (documented). They are existing business usage. What is still open is whether Gold has to carry them as such or derive them (REQ-0007, REQ-0008, DEC-0007).
2. Is_Churn_12M_36M is one flag for the 12-36 month window (Bastien, 2026-10-08). Next to `churn_12_24_flag` and `churn_24plus_flag` the file would hold three overlapping churn windows. Bastien raised the options: one standardised definition, configurable windows, or multiple flags (DEC-0018).
3. Name match against the 479 SuperGold rows (exact name only): `first_name` (DP-0006), `last_name` (DP-0007), `gender` (DP-0009), `last_modified_dt` (DP-0122), `segment_value` (DP-0252), `address_line1` (DP-0271), `address_line2` (DP-0272), `zip4` (DP-0275), `zip5` (DP-0276), `postal_code` (DP-0277). The other columns have no exact-name equivalent; several have probable equivalents (for example `new_buyer` and DP-0143 `new_buyer_status_key`, `loyalty_status` and DP-0047). A field-by-field mapping is Bastien's gap analysis in progress and Databricks Prompt B. These are name matches only, not verified equivalents. [inferred]

## Open questions
- Value formats of the flags (Y / N in the sample) and whether `subcategories` is free text or a coded list.
- Whether the weekly file stays as is once Gold exists, or Gold becomes its source.
