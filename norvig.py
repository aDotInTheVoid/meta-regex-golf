from __future__ import division, print_function
import re
import itertools

def words(text): return set(text.split())

winners = words('''washington adams jefferson jefferson madison madison monroe 
    monroe adams jackson jackson van-buren harrison polk taylor pierce buchanan 
    lincoln lincoln grant grapartnt hayes garfield cleveland harrison cleveland mckinley
    mckinley roosevelt taft wilson wilson harding coolidge hoover roosevelt 
    roosevelt roosevelt roosevelt truman eisenhower eisenhower kennedy johnson nixon 
    nixon carter reagan reagan bush clinton clinton bush bush obama obama''')

losers = words('''clinton jefferson adams pinckney pinckney clinton king adams 
    jackson adams clay van-buren van-buren clay cass scott fremont breckinridge 
    mcclellan seymour greeley tilden hancock blaine cleveland harrison bryan bryan 
    parker bryan roosevelt hughes cox davis smith hoover landon willkie dewey dewey 
    stevenson stevenson nixon goldwater humphrey mcgovern ford carter mondale 
    dukakis bush dole gore kerry mccain romney''')

losers = losers - winners
def mistakes(regex, winners, losers):
    "The set of mistakes made by this regex in classifying winners and losers."
    return ({"Should have matched: " + W 
             for W in winners if not re.search(regex, W)} |
            {"Should not have matched: " + L 
             for L in losers if re.search(regex, L)})

def verify(regex, winners, losers): 
    assert not mistakes(regex, winners, losers)
    return True

losers = {'fillmore'} | losers - {'fremont'}

def findregex(winners, losers, k=4):
    "Find a regex that matches all winners but no losers (sets of strings)."
    # Make a pool of regex parts, then pick from them to cover winners.
    # On each iteration, add the 'best' part to 'solution',
    # remove winners covered by best, and keep in 'pool' only parts
    # that still match some winner.
    pool = regex_parts(winners, losers)
    solution = []
    def score(part): return k * len(matches(part, winners)) - len(part)
    while winners:
        best = max(pool, key=score)
        solution.append(best)
        winners = winners - matches(best, winners)
        pool = {r for r in pool if matches(r, winners)}
    return OR(solution)

def matches(regex, strings):
    "Return a set of all the strings that are matched by regex."
    return {s for s in strings if re.search(regex, s)}

OR = '|'.join # Join a sequence of strings with '|' between them

def regex_parts(winners, losers):
    "Return parts that match at least one winner, but no loser."
    wholes = {'^' + w + '$'  for w in winners}
    parts = {d for w in wholes for p in subparts(w) for d in dotify(p)}
    return wholes | {p for p in parts if not matches(p, losers)}

def subparts(word, N=4):
    "Return a set of subparts of word: consecutive characters up to length N (default 4)."
    return set(word[i:i+n+1] for i in range(len(word)) for n in range(N)) 
    
def dotify(part):
    "Return all ways to replace a subset of chars in part with '.'."
    choices = map(replacements, part)
    return {cat(chars) for chars in itertools.product(*choices)}

def replacements(c): return c if c in '^$' else c + '.'

cat = ''.join

solution = findregex(winners, losers)
verify(solution, winners, losers)

print(len(solution), solution)
