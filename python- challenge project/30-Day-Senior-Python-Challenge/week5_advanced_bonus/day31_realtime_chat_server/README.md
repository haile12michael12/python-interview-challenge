# Day 31: Realtime Chat Server (FastAPI + WebSockets)

## Challenge
Build a realtime chat server using FastAPI and WebSockets that supports multiple rooms and users.

## Requirements
- Use FastAPI for the web framework
- Implement WebSocket connections for realtime communication
- Support multiple chat rooms
- Handle user connections/disconnections
- Broadcast messages to room participants
- Store chat history (in-memory or database)

## What It Tests
- Concurrency with WebSockets
- Publish/Subscribe patterns
- Session handling
- Realtime data streaming
- Connection management

## Implementation Tips
1. Use FastAPI's WebSocket support for handling connections
2. Implement a message broker or in-memory store for chat history
3. Handle connection lifecycle events (connect, disconnect, reconnect)
4. Implement room management and user presence
5. Add authentication for users (optional but recommended)
6. Consider using Redis for scaling across multiple server instances

## Testing
Create test cases for:
- User connection and disconnection
- Message broadcasting within rooms
- Multiple rooms isolation
- Error handling for invalid connections
- Concurrent users and messages
- Message history retrieval