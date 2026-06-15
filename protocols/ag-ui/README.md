# AUGMANITAI AG-UI Implementation

**Agent-User Interaction Protocol** for AUGMANITAI terminology explorer UI.

## Overview

This AG-UI implementation defines the user-agent interaction patterns for AUGMANITAI, including UI component specifications, user-to-agent handover protocols, and event-driven architecture for seamless terminology exploration.

## Core Files

### ui-schema.json
**UI Component Specifications** following CopilotKit and modern agent-UI conventions.

**Components**:
1. **Term Card** — Display term definitions with configurable fields, theming, and interactions
2. **Search Widget** — Full-text search with suggestions, filters, and result display modes
3. **Relation Graph** — Force-directed network visualization of term relationships
4. **Domain Browser** — Semantic domain hierarchy with lazy/eager expansion
5. **Term Timeline** — Version history and change tracking

**Features**:
- Multi-theme support (light/dark)
- Responsive layouts (grid/list/compact)
- Animation system (entry, expansion)
- Color coding by domain
- Accessibility considerations

### handover-protocol.json
**User-Agent State Machine** for interaction control and data exchange.

**States**:
- `idle` — Awaiting user input
- `searching` — User searching for terms
- `browsing` — Exploring domains/relationships
- `viewing_term` — Displaying term details
- `comparing_terms` — Side-by-side term comparison
- `validating_drift` — Checking semantic drift
- `delegating_task` — User hands off analysis to agent
- `awaiting_response` — Waiting for agent completion
- `presenting_results` — Displaying agent results
- `error` — Error state with recovery options

**Transitions**:
- User triggers: query, selection, navigation, handoff
- Agent triggers: ready, error, completion
- System triggers: timeout

**Data Exchange**:
- User → Agent: queries, selections, preferences
- Agent → User: results, suggestions, metadata

### event-types.md
**Event Catalog** for all user-agent interactions.

**Categories**:
1. **Discovery** — Searching, browsing
2. **Interaction** — Clicking, hovering, selecting
3. **Navigation** — Domain browsing, graph navigation
4. **Analysis** — Drift validation, comparison
5. **Collaboration** — Multi-term comparison, export
6. **Handoff** — Suggestions, delegation
7. **State Management** — Session lifecycle
8. **Error Handling** — Error occurrence and recovery

**Example Events**:
```json
{
  "type": "term_click",
  "timestamp": "2026-04-10T12:35:05Z",
  "data": {
    "termId": "sg-001",
    "action": "view_details",
    "source": "search_results"
  }
}
```

## UI Architecture

```
┌──────────────────────────────────────┐
│         User Interface Layer         │
├──────────────────────────────────────┤
│  Search Bar  │  Domain Browser  │    │
│  ┌────────┐  │  ┌──────────┐    │    │
│  │ Input  │  │  │ Taxonomy │    │    │
│  │        │  │  └──────────┘    │    │
│  └────────┘  │                   │    │
├──────────────────────────────────────┤
│      Term Card Display              │
│  ┌──────────────────────────────┐   │
│  │ Name EN / DE                  │   │
│  │ Definition EN / DE            │   │
│  │ Domain Badge | Examples       │   │
│  │ Related Terms Link            │   │
│  └──────────────────────────────┘   │
├──────────────────────────────────────┤
│      Relation Graph Viewport        │
│  ┌──────────────────────────────┐   │
│  │   [Primary]                  │   │
│  │      / | \                   │   │
│  │   [A] [B] [C]               │   │
│  └──────────────────────────────┘   │
├──────────────────────────────────────┤
│         Event System Layer           │
│  term_click → state_transition      │
│  suggestion_accepted → task_delegate│
└──────────────────────────────────────┘
```

## Interaction Flows

### Basic Search and View

```
1. User types in search widget
2. Emits: term_search_initiated
3. Agent: executes search
4. Emits: term_search_results
5. UI renders result cards
6. User clicks card
7. Emits: term_click
8. UI transitions to viewing_term state
9. Renders full term details
```

### Domain Exploration

```
1. User clicks domain in browser
2. Emits: domain_browse_initiated
3. UI loads domain hierarchy
4. User expands domain node
5. Emits: domain_expand
6. UI reveals child terms with animation
7. User clicks term
8. Emits: term_click
9. Transitions to viewing_term
```

### Semantic Drift Validation

```
1. User enters usage context
2. Selects term and "validate drift"
3. Emits: drift_validation_initiated
4. Delegates to agent
5. Emits: task_delegated
6. Agent analyzes usage vs. canonical
7. Emits: drift_detected (or not_detected)
8. UI displays results with confidence score
9. Shows recommendations if drift found
```

### Term Comparison

```
1. User selects multiple terms
2. Emits: comparison_initiated
3. UI opens comparison view
4. User selects attributes to compare
5. Emits: comparison_attribute_select
6. UI renders side-by-side comparison
7. Highlights similarities/differences
8. Optional export
9. Emits: export_initiated
```

## Component States

### Term Card Component

```
States:
- collapsed: Summary only
- expanded: Full definition + examples
- highlighted: Emphasis for search match
- selected: User selected for action
- loading: Awaiting data
- error: Failed to load

Transitions:
hover → highlighted
click → expanded/selected
dismiss error → normal
```

### Search Widget Component

```
States:
- empty: No query entered
- typing: User entering query
- suggesting: Showing suggestions
- loading: Executing search
- results: Displaying results
- error: Search failed

Interactions:
- Type in input → typing state
- Wait 300ms → suggesting state
- Submit → loading state
- Got results → results state
- User clears → empty state
```

### Relation Graph Component

```
States:
- loading: Fetching graph data
- initial: First render, zoomed to fit
- interactive: User can pan/zoom
- selecting: User hovering/selecting nodes
- expanded: Show additional details
- error: Failed to load graph

Interactions:
- Scroll → zoom
- Drag → pan
- Click node → selecting/expand
- Double-click → focus on node
```

## Event Streaming

Events flow through the system:

```
User Action
    ↓
DOM Event Handler
    ↓
EMIT Custom Event
    ↓
Event Bus
    ├→ Analytics Logger
    ├→ State Machine
    ├→ UI Renderer
    ├→ Agent (if needed)
    └→ Session Storage
    ↓
UI Update
    ↓
Visual Feedback
```

## Accessibility

All components support:
- ARIA labels and roles
- Keyboard navigation
- Screen reader compatibility
- High contrast mode
- Reduced motion preferences

## Performance Optimizations

- **Virtual Scrolling**: For large term lists
- **Lazy Loading**: Domain expansion on demand
- **Caching**: Search results, graph data
- **Debouncing**: Search input (300ms)
- **Progressive Rendering**: Gradual result display

## Error Handling

**Error Types**:
- `TERM_NOT_FOUND` — Recovery: return to search
- `NETWORK_ERROR` — Recovery: retry with backoff
- `INVALID_QUERY` — Recovery: suggest corrected query
- `TIMEOUT` — Recovery: cancel operation, offer retry

**UI States**:
- Error banner with recoverable message
- Disable relevant controls
- Offer clear recovery action
- Log error for analytics

## Localization

UI supports multilingual display:
- English (en) ↔ German (de)
- Language selector in header
- Dynamically loads translations
- Applies to all term content

## Session Management

```
Session Lifecycle:
1. session_started — User opens app
   ├─ Initialize state machine to idle
   ├─ Load user preferences
   └─ Restore previous session if available

2. [Interactive Phase] — Multiple state transitions
   └─ Each event logged with timestamp, context

3. session_ended — User closes app
   ├─ Persist session history
   ├─ Record analytics
   └─ Clean up resources
```

## Integration with Other Protocols

### MCP Bridge
```
AG-UI Click Event
    ↓
Convert to MCP Tool Call
    ↓
MCP Server executes
    ↓
Return to UI
    ↓
Render via UI Schema
```

### A2A Bridge
```
task_delegated Event
    ↓
Convert to A2A TaskRequest
    ↓
Send to AUGMANITAI Agent
    ↓
Receive TaskResponse
    ↓
agent_task_completed Event
```

### ANP Bridge
```
External Agent Suggestion
    ↓
Wrap in DID-signed message
    ↓
Verify credential
    ↓
suggestion_presented Event
```

## Testing

**Component Testing**:
- Render with mock data
- Verify state transitions
- Test event emissions
- Check accessibility

**Integration Testing**:
- Test handover flows
- Verify agent communication
- Check error recovery
- Validate state consistency

**E2E Testing**:
- Full user journeys
- Multi-step workflows
- Cross-browser compatibility
- Performance benchmarks

## License & Attribution

- **License**: CC BY-NC-ND 4.0
- **Author**: Andreas Ehstand
- **ORCID**: 0009-0006-3773-7796
- **DOI**: 10.5281/zenodo.20161494

## Related Documentation

- MCP: `../mcp/`
- A2A: `../a2a/`
- ANP: `../anp/`
- Bridges: `../bridges/`


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../../IMPRESSUM.md).*
