# Metaregex benchmarks

Code for [this blog post](https://adotinthevoid.github.io/posts/2020/05/metaregex-python-can-be-fast-too/)

Each version is a separate project as they have different options

To run the benchmarks with [hyperfine](https://github.com/sharkdp/hyperfine)
```
./build.sh
hyperfine "python3 norvig_nocache.py" "python3 norvig_with_cache.py" out/*
```


## History
The numbering isn't continuous, as the following projects were removed

- `v2_regex_feats`: Regex crate features
- `v4_inline_never`: Never inline for better flamegraphs
- `v6_regex_feats`: Also regex crate features.

They were just too much, and were slightly slower.


## Results

For detailed results see [BENCH.md](./BENCH.md)

| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `python3 norvig_nocache.py` | 1.186 ± 0.013 | 1.161 | 1.252 | 7.0 |
| `python3 norvig_with_cache.py` | 0.789 ± 0.010 | 0.771 | 0.821 | 4.7 |
| `out/v1_naive` | 2.426 ± 0.070 | 2.227 | 2.692 | 14.3 |
| `out/v3_cheep_tricks` | 2.317 ± 0.068 | 2.148 | 2.587 | 13.7 |
| `out/v5_cache_regex` | 0.194 ± 0.002 | 0.191 | 0.206 | 1.1 |
| `out/v7_jemalloc` | 0.169 ± 0.002 | 0.166 | 0.180 | 1.0 |
