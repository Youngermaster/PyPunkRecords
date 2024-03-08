# High-Level Architecture Overview

1. **Peer Structure**: Each peer in the network will have two main components:

   - **Server Module (PServidor)**: Handles incoming requests from other peers.
   - **Client Module (PCliente)**: Sends requests to other peers.

2. **Microservices Breakdown**:

   - **File Listing Service**: Manages the indexing and retrieval of file listings from a peer.
   - **File Information Service**: Provides detailed information about files, such as metadata, size, and URI/URL.
   - **Dummy File Transfer Service**: Simulates file upload and download processes.

3. **Communication Protocols**:

   - **REST API**: Used for stateless requests like retrieving file listings.
   - **gRPC**: Facilitates efficient, low-latency communication for operations like requesting file information.
   - **MOM (Message-Oriented Middleware)**: Handles asynchronous messaging between peers, enhancing decoupling and scalability.

4. **Peer Discovery and Management**:

   - Implement a dynamic discovery mechanism for peers to find and connect with each other using the peer friend URLs in their configuration files.
   - Manage peer connections and maintain an updated list of active/inactive peers.

5. **Configuration Management**:
   - Each peer should dynamically read its configuration at startup (Bootstrap), which includes IP, port, directory for file listings, and URLs of peer friends.

## Additional Considerations

- **Scalability**: Design the architecture to easily add new peers and scale horizontally.
- **Fault Tolerance**: Implement strategies to handle peer failures, ensuring the network remains robust.
- **Security**: Consider security aspects like authentication and secure communication channels.
- **Data Synchronization**: Plan for future implementation of actual file transfer and synchronization.

## Visual Representation

Creating a visual diagram of the architecture can be very helpful. It should include:

- The internal structure of each peer showing the server and client modules.
- Microservices within each peer and their responsibilities.
- How peers communicate with each other using different protocols.
- Peer discovery and dynamic network formation.
