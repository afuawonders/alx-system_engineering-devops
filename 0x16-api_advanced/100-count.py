import requests

def count_words(subreddit, word_list, after=None, results=None):
    if results is None:
        results = {}

    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json", headers=headers, params=params, allow_redirects=False)
        data = response.json().get("data", {})
        children = data.get("children", [])

        for child in children:
            title = child.get("data", {}).get("title", "").lower()

            for keyword in word_list:
                keyword_lower = keyword.lower()
                if keyword_lower in title:
                    results[keyword_lower] = results.get(keyword_lower, 0) + title.count(keyword_lower)

        if data.get("after") is not None:
            count_words(subreddit, word_list, after=data["after"], results=results)
        else:
            sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))

            for keyword, count in sorted_results:
                print(f"{keyword}: {count}")

    except Exception as e:
        pass  # Handle exceptions if needed (e.g., invalid subreddit)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])

