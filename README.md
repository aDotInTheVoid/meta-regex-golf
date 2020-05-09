# Metaregex benchmarks

Each version is a separate project as they have different options

To run the benchmarks
```
./build.sh
./bench.sh
```
You may want to change `$runs` in `bench.sh` to something lower.

# History
The numbering isn't continuous, as the following projects were removed

- `v2_regex_feats`: Regex crate features
- `v4_inline_never`: Never inline for better flamegraphs
- `v6_regex_feats`: Also regex crate features.

They were just too much, and were slightly slower.|  | Real | User | Sys |

|  | Real | User | Sys |
|--|------|------|-----|
| python3 norvig_nocache.py | 1.181500 | 1.175260 | 0.000000 |
| python3 norvig_with_cache.py | 0.790220 | 0.784960 | 0.000000 |
| out/v1_naive | 2.395320 | 2.388920 | 0.000000 |
| out/v3_cheep_tricks | 2.289380 | 2.283400 | 0.000000 |
| out/v5_cache_regex | 0.190640 | 0.179840 | 0.005660 |
| out/v7_jemalloc | 0.163220 | 0.153220 | 0.006380 |
