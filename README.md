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

They were just too much, and were slightly slower.