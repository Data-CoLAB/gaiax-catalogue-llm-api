API to access enhanced search and information from SQL database:

- "POST /search HTTP/1.1"
      - String "query" needed
      - Returns \{id_url: similarity_score\}

- "GET /get_all_resources HTTP/1.1"
      - Returns \[\{id_url, title, tags\}\]
  
Execute with docker for execution
