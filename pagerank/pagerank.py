import os
import random
import re
import sys
import pandas as pd

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    #TO-DO 
    ProbDist = {}
    if len(corpus[page]) != 0:
        for link in corpus[page]:
            PageProb = (damping_factor/len(corpus[page])) + ((1-damping_factor)/len(corpus))
            ProbDist[link] = PageProb
        for page in corpus:
            if page not in ProbDist:
                ProbDist[page] = (1-damping_factor)/len(corpus)
    else:
        for link in corpus:
            ProbDist[link] = 1/len(corpus)
    return ProbDist
    #TO-DO
    #raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # TO-DO
    sample = []
    pages = list(corpus.keys())
    Sample = random.choice(pages)
    sample.append(Sample)
    for _ in range(n-1):
        ProbDist = transition_model(corpus,Sample, damping_factor)
        Sample = random.choices(list(ProbDist.keys()), list(ProbDist.values()))[0]
        sample.append(Sample)
    PageRank = {page : sample.count(page)/n for page in pages}
    return PageRank
    # TO-DO
    #raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #To-Do
    num_links = []
    for links in corpus.values():
        num_links.append(len(links))
    df = pd.DataFrame({'page': corpus.keys(),
                       'links': corpus.values(),
                       'num_links': num_links
                       })
    N =len(df)
    tolerance = 0.001
    pages = corpus.keys()
    connecting_matrix = pd.DataFrame(0, index = pages, columns = pages, dtype = float)
    for index, row in df.iterrows():
        for link in row['links']:
            connecting_matrix.at[link,row['page']] = 1/row['num_links']
    pr = pd.Series(1.0/N, index = pages)

    while True:
        previous_pr = pr.copy()
        pr = (1-damping_factor)/N + damping_factor*connecting_matrix.dot(pr)
        if (pr-previous_pr).abs().sum() < tolerance:
            break
    pr = pr/pr.sum()
    pr = pr.to_dict()
    return pr
    #To-Do
    #raise NotImplementedError


if __name__ == "__main__":
    main()
