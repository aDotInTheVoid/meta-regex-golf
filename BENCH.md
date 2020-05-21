Benchmarked with 
`hyperfine -w 3 -m 500 --export-markdown BENCH.md "python3 norvig_nocache.py" "python3 norvig_with_cache.py" out/*`

## System Details
- rustc 1.43.1 (8d69840ab 2020-05-04)
- Python 3.7.7
- hyperfine 1.6.0
- Fedora 31 (Workstation Edition) x86_64
- Linux 5.6.13-200.fc31.x86_64
- glibc-2.30-11.fc31.x86_64
- Intel i7-2700K (8) @ 3.900GHz, 7922MiB Ram (as reported by neofetch)

All packages up to date as of Thu 21 May 2020 12:03:04 BST

| Command | Mean [s] | Min [s] | Max [s] | Relative |
|:---|---:|---:|---:|---:|
| `python3 norvig_nocache.py` | 1.192 ± 0.014 | 1.166 | 1.231 | 7.0 |
| `python3 norvig_with_cache.py` | 0.792 ± 0.011 | 0.775 | 0.826 | 4.6 |
| `out/v1_naive` | 2.397 ± 0.068 | 2.214 | 2.616 | 14.0 |
| `out/v3_cheep_tricks` | 2.332 ± 0.061 | 2.145 | 2.567 | 13.6 |
| `out/v5_cache_regex` | 0.196 ± 0.002 | 0.192 | 0.209 | 1.1 |
| `out/v7_jemalloc` | 0.171 ± 0.001 | 0.168 | 0.182 | 1.0 |
