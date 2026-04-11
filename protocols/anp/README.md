# AUGMANITAI ANP Implementation

**W3C Agent Network Protocol** (ANP) implementation for decentralized agent-to-agent networking with AUGMANITAI.

## Overview

This ANP implementation enables AUGMANITAI to operate as a decentralized agent node in peer-to-peer agent networks, using W3C Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs) for authentication and authorization.

## Core Components

### 1. DID Document (`did-schema.json`)

**Decentralized Identifier** following W3C DID specification:

- **DID Format**: `did:web:augmanitai.local`
- **Type**: Agent
- **Verification Methods**: Ed25519, ECDSA cryptographic keys
- **Service Endpoints**: Query, P2P, HTTP
- **Authentication**: Public key cryptography

### 2. Verifiable Credentials

#### Term Credential Template (`term-credential-template.json`)

W3C Verifiable Credential v2.0 format for issuing cryptographically-signed term definitions:

**Subject Properties**:
- Term ID, abbreviation, multilingual names
- Full definitions (EN/DE)
- Semantic domain
- Usage examples
- Status (active/deprecated/archived)

**Proof Types**:
- DataIntegrityProof with Ed25519 or ECDSA

#### Issuer Credential (`issuer-credential.json`)

Self-issued credential asserting AUGMANITAI's authority as terminology issuer:

- Framework version and term count
- License (CC BY-NC-ND 4.0)
- ISO standard compliance
- Data policy (non-commercial, no derivatives)
- Authorization for credential issuance

#### Proof Schema (`proof-schema.json`)

JSON Schema for cryptographic proofs:
- DataIntegrityProof format
- Cryptosuites: Ed25519-RDFC-2022, ECDSA-2019
- Verification methods and proof purposes
- Optional domain and challenge for additional security

### 3. P2P Manifest (`p2p-manifest.json`)

Agent node manifest for ANP network participation:

**Capabilities**:
- Core: term operations (lookup, search, relate, validate_drift)
- Network: peer discovery, message routing, capability delegation
- Storage: read-only distributed, indexing, replication

**Endpoints**:
- P2P (libp2p, IPFS)
- HTTP
- Query (ANP-native)

**Network Configuration**:
- DHT-based peer discovery
- Max 100 peers
- Open trust model with DID verification
- Factor-3 replication

## DID Document Flow

```
┌─────────────────────────────────────────┐
│ DID Resolution (did:web:augmanitai)     │
├─────────────────────────────────────────┤
│ ├─ Verification Methods (Ed25519 key)   │
│ ├─ Service Endpoints:                   │
│ │  ├─ TermLookupService                 │
│ │  ├─ TermSearchService                 │
│ │  ├─ TermRelateService                 │
│ │  ├─ DriftValidationService            │
│ │  └─ PeerToPeerService                 │
│ ├─ Authentication Methods               │
│ ├─ Assertion Methods (for VCs)          │
│ └─ Proof (signature)                    │
└─────────────────────────────────────────┘
```

## Verifiable Credential Lifecycle

```
1. ISSUANCE
   ├─ Issuer creates Term VC
   ├─ Signs with private key
   └─ Publishes VC

2. DISTRIBUTION
   ├─ VC transmitted to requesting agents
   ├─ Embedded in responses
   └─ Published to VC registries

3. VERIFICATION
   ├─ Agent verifies issuer DID
   ├─ Checks signature against public key
   ├─ Validates credential status
   └─ Confirms proof cryptosuite

4. USAGE
   ├─ Agent can present VC to peers
   ├─ Use in authorization decisions
   └─ Reference in discourse/attribution
```

## Integration with Other Protocols

### MCP Bridge
MCP tool calls → ANP TaskRequest → DID-signed VC

### A2A Bridge
A2A TaskRequest → ANP P2P message → Verifiable Credential

### AG-UI Integration
UI events → ANP capability delegation → VC-protected actions

## Security Model

### Authentication
- **Method**: Public key cryptography (Ed25519, ECDSA)
- **Storage**: DID Document
- **Verification**: Against public key in DID

### Authorization
- **Method**: Verifiable Credentials
- **Issuance**: Self-issued by AUGMANITAI authority
- **Delegation**: Capability delegation via signed VCs

### Data Integrity
- **Proof Type**: DataIntegrityProof
- **Cryptosuite**: Ed25519-RDFC-2022
- **Signature**: Base64-encoded proof value

### Trust Chain
```
did:web:augmanitai.local
    ↓ contains verificationMethod
    ed25519 public key
    ↓ verifies signatures on
    Issuer Credential
    ↓ authorizes issuance of
    Term Credentials
    ↓ signed by private key, verified via
    Public key in DID document
```

## Example ANP Request/Response

### Agent Discovery

1. **Find AUGMANITAI**: `resolve(did:web:augmanitai.local)`
2. **Inspect DID Document**: Extract service endpoints
3. **Connect to P2P endpoint**: `local://augmanitai/p2p`

### Capability Query

```json
{
  "type": "CapabilityQuery",
  "did": "did:web:augmanitai.local",
  "requestedCapabilities": [
    "term_lookup",
    "term_validate_drift"
  ]
}
```

### VC Presentation

```json
{
  "type": "VerifiablePresentationRequest",
  "challenge": "nonce-12345",
  "domain": "augmanitai.local"
}
```

Agent responds with signed presentation of Issuer Credential.

## Key Interoperability

| Component | MCP | A2A | ANP | AG-UI |
|-----------|-----|-----|-----|-------|
| Agent Discovery | DX | Card | DID | Config |
| Authentication | OAuth | API Key | DID | Session |
| Authorization | Tools | Skills | VCs | Permissions |
| Message Format | JSON | JSON-LD | Linked Data | Events |

## Compliance & Standards

- **W3C DID Core**: v1.0
- **W3C VC Data Model**: v2.0
- **Cryptography**: RFC 8037 (CFRG ECDH and Signatures)
- **JSON-LD**: W3C Recommendation
- **RDF**: W3C RDF 1.1

## License & Attribution

- **License**: CC BY-NC-ND 4.0
- **Author**: Andreas Ehstand
- **ORCID**: 0009-0006-3773-7796
- **DOI**: 10.5281/zenodo.19481331

## Related Documentation

- MCP: `../mcp/`
- A2A: `../a2a/`
- AG-UI: `../ag-ui/`
- Bridges: `../bridges/`
