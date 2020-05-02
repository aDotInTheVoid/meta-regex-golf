#![type_length_limit="12373190"]

use itertools::Itertools;
use regex::Regex;

use std::collections::HashSet;
use std::hash::{Hash, Hasher};

type Set<'a> = HashSet<&'a str>;

const WINNERS: &str = "washington adams jefferson jefferson madison madison monroe \
     monroe adams jackson jackson van-buren harrison polk taylor \
     pierce buchanan lincoln lincoln grant grapartnt hayes garfield \
     cleveland harrison cleveland mckinley mckinley roosevelt taft \
     wilson wilson harding coolidge hoover roosevelt roosevelt \
     roosevelt roosevelt truman eisenhower eisenhower kennedy \
     johnson nixon nixon carter reagan reagan bush clinton clinton \
     bush bush obama obama trump";

const LOSERS: &str = "clinton jefferson adams pinckney pinckney clinton king adams \
     jackson adams clay van-buren van-buren clay cass scott fremont \
     breckinridge mcclellan seymour greeley tilden hancock blaine \
     cleveland harrison bryan bryan parker bryan roosevelt hughes \
     cox davis smith hoover landon willkie dewey dewey stevenson \
     stevenson nixon goldwater humphrey mcgovern ford carter \
     mondale dukakis bush dole gore kerry mccain romney clinton";

const START: u8 = '^' as u8;
const DOT: u8 = '.' as u8;
const END: u8 = '$' as u8;

#[derive(Clone)]
struct Part {
    string: String,
    reg: Regex,
}

impl Hash for Part {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.string.hash(state);
    }
}
impl PartialEq for Part {
    fn eq(&self, other: &Self) -> bool {
        self.string == other.string
    }
}
impl Eq for Part {}

impl Part {
    fn new(string: String) -> Self {
        let reg = Regex::new(&string).unwrap();
        Self { reg, string }
    }
}

pub fn main() {
    let mut winners: HashSet<_> = WINNERS.split_whitespace().collect();
    let mut losers: HashSet<_> = LOSERS
        .split_whitespace()
        .collect::<Set>()
        .difference(&winners)
        .map(|x| *x)
        .collect::<HashSet<_>>();

    losers.insert("fillmore");
    losers.remove("fremont");

    println!("{}", find_regex(&mut winners, &losers));
}

fn find_regex(winners: &mut Set, losers: &Set) -> String {
    let mut pool: HashSet<_> = regex_parts(&winners, &losers).collect();
    let mut solutions: Vec<Part> = vec![];
    // Iterate until we match all winners
    while winners.len() != 0 {
        // Select best candidate from pool
        let best = pool.iter().max_by_key(|pat| {
            4 * matches(pat, winners.iter().map(|&x| x)).count() as i64 - pat.string.len() as i64
        });
        // Candidate may be none, so we need to handle that
        if let Some(best_part) = best {
            // Add to solutions
            solutions.push(best_part.clone());
            // Remove entries matched by new regex
            winners.retain(|entry| !best_part.reg.is_match(entry));
            // Remove regex's that no longer match anything
            pool.retain(|patern| matches(patern, winners.iter().map(|&x| x)).next().is_some());
        } else {
            eprintln!("I don't think it can be done");
        }
    }
    solutions.into_iter().map(|x| x.string).join("|")
}

fn regex_parts<'a>(winners: &'a Set<'a>, losers: &'a Set<'a>) -> impl Iterator<Item = Part> + 'a {
    let whole = winners.iter().map(|x| format!("^{}$", x));
    let parts = whole
        .clone()
        .flat_map(subparts)
        .flat_map(dotify)
        .map(Part::new)
        .filter(move |part| losers.iter().all(|loser| !part.reg.is_match(loser)));
    whole.map(Part::new).chain(parts)
}

fn dotify(word: String) -> impl Iterator<Item = String> {
    let has_front = (word.as_bytes()[0] == START) as usize;
    let has_end = (word.as_bytes()[word.len() - 1] == END) as usize;
    let len = word.len() - has_front - has_end;
    (0..2_usize.pow(len as u32))
        .map(move |x| x << has_front)
        .map(move |n| get_dots(&word, n))
}

fn get_dots(word: &str, n: usize) -> String {
    let mut tmp = word.to_string();
    set_dots(&mut tmp, n);
    tmp
}

fn set_dots(word: &mut str, n: usize) {
    assert!(word.is_ascii(), "Not ascii, cant do dots");
    for i in 0..word.len() {
        if ((n >> i) & 1) != 0 {
            // Safety: The thing is all ascii, so we
            //         will maintain utf-8 invariance
            unsafe {
                word.as_bytes_mut()[i] = DOT;
            }
        }
    }
}

fn subparts(word: String) -> impl Iterator<Item = String> {
    let len = word.len();
    (0..=len)
        .cartesian_product(1..5)
        .map(|(start, offset)| (start, start + offset))
        .filter(move |(_, end)| *end <= len)
        .map(move |(start, end)| word[start..end].to_owned())
}

fn matches<'a>(
    r: &'a Part,
    strs: impl Iterator<Item = &'a str> + 'a,
) -> impl Iterator<Item = &'a str> + 'a {
    strs.filter(move |s| r.reg.is_match(s))
}
