# Day 8: Async Web Crawler

## Challenge
Build an asynchronous web crawler that can efficiently fetch and process multiple web pages concurrently.

## Requirements
- Use `aiohttp` for making asynchronous HTTP requests
- Implement concurrent fetching with `asyncio`
- Handle errors gracefully (timeouts, invalid URLs, etc.)
- Respect robots.txt and implement rate limiting
- Extract and store relevant data from web pages

## Advanced Twist
Add rate limiting and error retry logic:
- Implement adaptive rate limiting based on server response
- Add exponential backoff for failed requests
- Retry failed requests up to a maximum number of attempts
- Log retry attempts and failures for monitoring

## Implementation Tips
1. Use `aiohttp.ClientSession` for efficient connection pooling
2. Implement a semaphore to limit concurrent requests
3. Use `asyncio.gather()` or `asyncio.as_completed()` for managing concurrent tasks
4. Parse HTML content using `BeautifulSoup` or similar libraries
5. Store results in a structured format (JSON, database, etc.)

## Testing
Create test cases for:
- Single URL fetching
- Multiple concurrent URL fetching
- Error handling (invalid URLs, timeouts)
- Rate limiting behavior
- Retry logic with mock failures