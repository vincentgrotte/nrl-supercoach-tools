CURL_TO_FETCH_TEAM_FIXTURES = \
"""
curl 'https://www.supercoach.com.au/2025/api/nrl/classic/v1/players/20/upcoming_fixture' \
  -H 'accept: application/json' \
  -H 'accept-language: en-GB,en;q=0.8' \
  -H 'authorization: Bearer INSERT_BEARER_TOKEN' \
  -b 'INSERT_COOKIE' \
  -H 'priority: u=1, i' \
  -H 'referer: https://www.supercoach.com.au/nrl/classic/team/field(playerProfile:player-profile/20)' \
  -H 'sec-ch-ua: "Not(A:Brand";v="99", "Brave";v="133", "Chromium";v="133"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
"""