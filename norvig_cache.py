import re
import itertools
re.purge()
Set = frozenset # Data will be frozensets, so they can't be mutated.

def words(text):
    "All space-separated words in text."
    return Set(text.split())

def phrases(text, sep='/'): 
    "All sep-separated phrases in text, uppercased and stripped."
    return Set(p.upper().strip() for p in text.split(sep))

def mistakes(regex, winners, losers):
    "The set of mistakes made by this regex in classifying winners and losers."
    return ({"Should have matched: " + W 
             for W in winners if not re.search(regex, W)} |
            {"Should not have matched: " + L 
             for L in losers if re.search(regex, L)})

def findregex(winners, losers, k=4):
    "Find a regex that matches all winners but no losers (sets of strings)."
    # Make a pool of regex parts, then pick from them to cover winners.
    # On each iteration, add the 'best' part to 'solution',
    # remove winners covered by best, and keep in 'pool' only parts
    # that still match some winner.
    pool = regex_parts(winners, losers)
    solution = []
    def score(p): return k * len(matches(p, winners)) - len(p)
    while winners:
        best = max(pool, key=score)
        solution.append(best)
        winners = winners - matches(best, winners)
        pool = {p for p in pool if matches(p, winners)}
    return OR(solution)

def matches(regex, strings):
    "Return a set of all the strings that are matched by regex."
    searcher = re.compile(regex).search
    return set(filter(searcher, strings))

OR  = '|'.join # Join a sequence of strings with '|' between them
cat = ''.join  # Join a sequence of strings with nothing between them

def regex_parts(winners, losers):
    "Return parts that match at least one winner, but no loser."
    wholes = {'^' + w + '$' for w in winners}
    parts = {d for w in wholes for p in subparts(w) for d in dotify(p)}
    return wholes | {p for p in parts if not matches(p, losers)}

def subparts(word):
    "Return a set of subparts of word: consecutive characters up to length 4."
    return set(word[i:i+n] for i in range(len(word)) for n in (1, 2, 3, 4)) 
    
def dotify(part):
    "Return all ways to replace a subset of chars in part with '.'."
    choices = map(replacements, part)
    return {cat(chars) for chars in itertools.product(*choices)}

def replacements(c): 
    "All ways to replace character c with something interesting: for now, 'c' or '.'."
    return c if c in '^$' else c + '.'

def report(winners, losers):
    "Find a regex to match A but not B, and vice-versa.  Print summary."
    solution = findregex(winners, losers)
    assert not mistakes(solution, winners, losers)
    print('Chars: {}, ratio: {:.1f}, inputs: {}:{}'.format(
          len(solution), len(trivial(winners)) / len(solution) , len(winners), len(losers)))
    return solution

def trivial(winners): return '^(' + OR(winners) + ')$'

winners = words('''washington adams jefferson jefferson madison madison monroe 
    monroe adams jackson jackson van-buren harrison polk taylor pierce buchanan 
    lincoln lincoln grant grant hayes garfield cleveland harrison cleveland mckinley
    mckinley roosevelt taft wilson wilson harding coolidge hoover roosevelt 
    roosevelt roosevelt roosevelt truman eisenhower eisenhower kennedy johnson nixon 
    nixon carter reagan reagan bush clinton clinton bush bush obama obama''')
losers = words('''clinton jefferson adams pinckney pinckney clinton king adams 
    jackson adams clay van-buren van-buren clay cass scott fremont breckinridge 
    mcclellan seymour greeley tilden hancock blaine cleveland harrison bryan bryan 
    parker bryan roosevelt hughes cox davis smith hoover landon wilkie dewey dewey 
    stevenson stevenson nixon goldwater humphrey mcgovern ford carter mondale 
    dukakis bush dole gore kerry mccain romney''') - winners

solution = findregex(winners, losers)
print(solution)