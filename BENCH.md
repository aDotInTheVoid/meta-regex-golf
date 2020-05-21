Benchmarked with 
`hyperfine -w 15 -m 500 --export-markdown BENCH.md "python3 norvig_nocache.py" "python3 norvig_with_cache.py" out/*`

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
| `python3 norvig_nocache.py` | 1.186 ± 0.013 | 1.161 | 1.252 | 7.0 |
| `python3 norvig_with_cache.py` | 0.789 ± 0.010 | 0.771 | 0.821 | 4.7 |
| `out/v1_naive` | 2.426 ± 0.070 | 2.227 | 2.692 | 14.3 |
| `out/v3_cheep_tricks` | 2.317 ± 0.068 | 2.148 | 2.587 | 13.7 |
| `out/v5_cache_regex` | 0.194 ± 0.002 | 0.191 | 0.206 | 1.1 |
| `out/v7_jemalloc` | 0.169 ± 0.002 | 0.166 | 0.180 | 1.0 |

```
Benchmark #1: python3 norvig_nocache.py
  Time (mean ± σ):      1.186 s ±  0.013 s    [User: 1.179 s, System: 0.003 s]
  Range (min … max):    1.161 s …  1.252 s    500 runs

Benchmark #2: python3 norvig_with_cache.py
  Time (mean ± σ):     788.8 ms ±  10.2 ms    [User: 783.9 ms, System: 2.9 ms]
  Range (min … max):   770.8 ms … 821.4 ms    500 runs

Benchmark #3: out/v1_naive
  Time (mean ± σ):      2.426 s ±  0.070 s    [User: 2.420 s, System: 0.001 s]
  Range (min … max):    2.227 s …  2.692 s    500 runs

Benchmark #4: out/v3_cheep_tricks
  Time (mean ± σ):      2.317 s ±  0.068 s    [User: 2.311 s, System: 0.001 s]
  Range (min … max):    2.148 s …  2.587 s    500 runs

Benchmark #5: out/v5_cache_regex
  Time (mean ± σ):     194.0 ms ±   1.6 ms    [User: 182.9 ms, System: 10.4 ms]
  Range (min … max):   190.8 ms … 206.0 ms    500 runs

Benchmark #6: out/v7_jemalloc
  Time (mean ± σ):     169.2 ms ±   1.5 ms    [User: 158.2 ms, System: 10.5 ms]
  Range (min … max):   166.4 ms … 179.6 ms    500 runs

Summary
  'out/v7_jemalloc' ran
    1.15 ± 0.01 times faster than 'out/v5_cache_regex'
    4.66 ± 0.07 times faster than 'python3 norvig_with_cache.py'
    7.01 ± 0.10 times faster than 'python3 norvig_nocache.py'
   13.70 ± 0.42 times faster than 'out/v3_cheep_tricks'
   14.34 ± 0.43 times faster than 'out/v1_naive'
```
