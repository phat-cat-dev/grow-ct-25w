# HESA source CSVs

None of the five CSVs the vocabulary stores record as their sources were found anywhere under `/home/abbottdev/workspace-26u`, excluding `archive/`, searched twice by two independent methods (`find -iname` per file, and a Python `os.walk`) on 30 September 2026 (adp-0204). None is committed here. Abbott must supply them.

| File | SHA-256 the stores record | Found |
|---|---|---|
| `CAH_Groupings.csv` | `f113839534b8f18696059feeaed78fe0f2e1211003171c3e4e05d3a373bd3d94` | No |
| `hecos_vocab.csv` | `38af934ed6ddfe7a914938d189d8f9d3b6c9d6f526d576602f652ead7e9fe6cc` | No |
| `HECoS_CAH_Mappings.csv` | `26a047b119e5617ae8827b1fd03bad471c6fd1408317f99ecfe749eaf51c5ee0` | No |
| `hecos_preferred.csv` | `12c4de65b628fed7ff3527753ea69a2f885b50f7cddd07847af95a08f6bbe872` | No |
| `hecos_related.csv` | `ee9c60532d67b7bc5fe8d39521c8d2924b5bec4b4e374ae5ba98bcc7bec4efb5` | No |

HESA's version and date for each file, as the stores record: CAH v1.3.4 (`core/vocab/cah.json`'s `source.version`), HECoS with no version or release date HESA's own pages give (`core/vocab/hecos.json`'s `source.release`, `null`).

Once supplied, place each file here unedited, confirm its SHA-256 against this table, and rewrite this file to record its size and where it was found.
