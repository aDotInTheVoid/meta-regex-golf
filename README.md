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
|--|------|------|-----|
| python3 norvig_nocache.py | 1.177380 | 1.171280 | 0.000000 |
| python3 norvig_with_cache.py | 0.785040 | 0.779820 | 0.000000 |
| out/v1_naive | 2.407900 | 2.401880 | 0.000000 |
| out/v2_regex_feats | 2.428660 | 2.422040 | 0.000000 |
| out/v3_cheep_tricks | 2.288340 | 2.282500 | 0.000000 |
| out/v4_inline_never | 2.281600 | 2.275380 | 0.000020 |
| out/v5_cache_regex | 0.190940 | 0.181220 | 0.006680 |
| out/v6_regex_feats | 0.221020 | 0.213860 | 0.001540 |
| out/v7_jemalloc | 0.169620 | 0.155900 | 0.006220 |
