# AUGMANITAI AG-UI Event Types

User-agent interaction events for AUGMANITAI terminology explorer.

## Event Categories

### Discovery Events

#### `term_search_initiated`
User submits a search query.

```json
{
  "type": "term_search_initiated",
  "timestamp": "2026-04-10T12:34:56Z",
  "data": {
    "query": "semantic drift",
    "filters": {
      "domains": ["systemic_effects", "cognitive_processes"],
      "languages": ["en"]
    },
    "resultLimit": 10
  }
}
```

#### `term_search_results`
Agent returns search results.

```json
{
  "type": "term_search_results",
  "timestamp": "2026-04-10T12:34:57Z",
  "data": {
    "query": "semantic drift",
    "resultCount": 3,
    "results": [
      { "id": "sg-001", "name": "Semantic Gravity" },
      { "id": "da-001", "name": "Definitional Authority" },
      { "id": "sat-001", "name": "Silent Authority Transfer" }
    ],
    "processingTime": 42
  }
}
```

### Interaction Events

#### `term_hover`
User hovers over a term (for UI animations).

```json
{
  "type": "term_hover",
  "timestamp": "2026-04-10T12:35:01Z",
  "data": {
    "termId": "sg-001",
    "component": "search_result_card",
    "durationMs": 250
  }
}
```

#### `term_click`
User clicks on a term card or reference.

```json
{
  "type": "term_click",
  "timestamp": "2026-04-10T12:35:05Z",
  "data": {
    "termId": "sg-001",
    "action": "view_details",
    "source": "search_results",
    "targetState": "viewing_term"
  }
}
```

#### `term_selection`
User selects a term for further action.

```json
{
  "type": "term_selection",
  "timestamp": "2026-04-10T12:35:10Z",
  "data": {
    "termId": "sg-001",
    "selectedAction": "find_related",
    "handoffToAgent": true
  }
}
```

### Navigation Events

#### `domain_browse_initiated`
User browses semantic domains.

```json
{
  "type": "domain_browse_initiated",
  "timestamp": "2026-04-10T12:36:00Z",
  "data": {
    "domain": "systemic_effects",
    "expandLevel": 1,
    "viewLayout": "tree"
  }
}
```

#### `domain_expand`
User expands a domain to see constituent terms.

```json
{
  "type": "domain_expand",
  "timestamp": "2026-04-10T12:36:05Z",
  "data": {
    "domain": "systemic_effects",
    "termCount": 5,
    "animated": true
  }
}
```

#### `relation_graph_view`
User opens a term relationship visualization.

```json
{
  "type": "relation_graph_view",
  "timestamp": "2026-04-10T12:36:10Z",
  "data": {
    "primaryTermId": "sg-001",
    "graphLayout": "force-directed",
    "nodeCount": 6,
    "edgeCount": 5
  }
}
```

#### `graph_node_click`
User clicks a node in relationship graph.

```json
{
  "type": "graph_node_click",
  "timestamp": "2026-04-10T12:36:15Z",
  "data": {
    "nodeId": "da-001",
    "relationshipType": "same_domain",
    "targetState": "viewing_term"
  }
}
```

### Analysis Events

#### `drift_validation_initiated`
User initiates semantic drift checking.

```json
{
  "type": "drift_validation_initiated",
  "timestamp": "2026-04-10T12:37:00Z",
  "data": {
    "termId": "sle-001",
    "usageContext": "The system learned to evolve linguistically...",
    "threshold": 0.8
  }
}
```

#### `drift_detected`
Agent detects semantic drift from canonical definition.

```json
{
  "type": "drift_detected",
  "timestamp": "2026-04-10T12:37:02Z",
  "data": {
    "termId": "sle-001",
    "canonicalDef": "The process by which human language and AI-generated language patterns...",
    "usageContext": "The system learned to evolve linguistically...",
    "similarity": 0.72,
    "driftLevel": "moderate",
    "recommendations": [
      "Consider using original definition",
      "Check if new usage represents term evolution"
    ]
  }
}
```

#### `drift_not_detected`
Agent confirms usage aligns with canonical definition.

```json
{
  "type": "drift_not_detected",
  "timestamp": "2026-04-10T12:37:02Z",
  "data": {
    "termId": "sle-001",
    "similarity": 0.94,
    "confidence": 0.95,
    "message": "Usage aligns well with canonical definition"
  }
}
```

### Collaboration Events

#### `comparison_initiated`
User starts comparing multiple terms.

```json
{
  "type": "comparison_initiated",
  "timestamp": "2026-04-10T12:38:00Z",
  "data": {
    "termIds": ["sle-001", "rke-001", "ssp-001"],
    "comparisonType": "definitions",
    "layout": "side_by_side"
  }
}
```

#### `comparison_attribute_select`
User selects attributes to compare.

```json
{
  "type": "comparison_attribute_select",
  "timestamp": "2026-04-10T12:38:05Z",
  "data": {
    "attributes": [
      "name_en",
      "definition_en",
      "domain",
      "examples"
    ]
  }
}
```

#### `export_initiated`
User exports term data.

```json
{
  "type": "export_initiated",
  "timestamp": "2026-04-10T12:39:00Z",
  "data": {
    "termIds": ["sg-001", "da-001"],
    "format": "json",
    "includeExamples": true,
    "includeRelations": true
  }
}
```

### Agent Handoff Events

#### `suggestion_presented`
Agent suggests related term or action.

```json
{
  "type": "suggestion_presented",
  "timestamp": "2026-04-10T12:40:00Z",
  "data": {
    "suggestionType": "related_term",
    "sourceTermId": "sg-001",
    "suggestedTermId": "lfma-001",
    "reason": "Both relate to terminology dominance in discourse",
    "confidence": 0.87
  }
}
```

#### `suggestion_accepted`
User accepts agent's suggestion.

```json
{
  "type": "suggestion_accepted",
  "timestamp": "2026-04-10T12:40:05Z",
  "data": {
    "suggestionId": "sug-12345",
    "suggestionType": "related_term",
    "actionTaken": "navigate_to_term",
    "targetTermId": "lfma-001"
  }
}
```

#### `suggestion_rejected`
User rejects agent's suggestion.

```json
{
  "type": "suggestion_rejected",
  "timestamp": "2026-04-10T12:40:10Z",
  "data": {
    "suggestionId": "sug-12345",
    "suggestionType": "related_term",
    "userFeedback": "Not relevant to current search"
  }
}
```

#### `task_delegated`
User hands off analysis task to agent.

```json
{
  "type": "task_delegated",
  "timestamp": "2026-04-10T12:41:00Z",
  "data": {
    "taskType": "comprehensive_domain_analysis",
    "domain": "systemic_effects",
    "parameters": {
      "depth": "full",
      "includeHistory": true
    },
    "expectedDuration": 5000
  }
}
```

#### `agent_task_completed`
Agent completes delegated task.

```json
{
  "type": "agent_task_completed",
  "timestamp": "2026-04-10T12:41:15Z",
  "data": {
    "taskId": "task-9999",
    "taskType": "comprehensive_domain_analysis",
    "resultCount": 5,
    "processingTime": 14200,
    "status": "success",
    "results": [...]
  }
}
```

### State Management Events

#### `session_started`
User begins AUGMANITAI session.

```json
{
  "type": "session_started",
  "timestamp": "2026-04-10T12:00:00Z",
  "data": {
    "sessionId": "sess-abc123",
    "userId": "user-anon",
    "language": "en",
    "initialState": "idle"
  }
}
```

#### `state_transition`
UI state changes due to user action or agent response.

```json
{
  "type": "state_transition",
  "timestamp": "2026-04-10T12:35:05Z",
  "data": {
    "from": "searching",
    "to": "viewing_term",
    "trigger": "term_click",
    "context": {
      "termId": "sg-001"
    }
  }
}
```

#### `session_ended`
User closes session.

```json
{
  "type": "session_ended",
  "timestamp": "2026-04-10T13:00:00Z",
  "data": {
    "sessionId": "sess-abc123",
    "duration": 3600000,
    "eventCount": 47,
    "finalState": "idle"
  }
}
```

### Error Events

#### `error_occurred`
An error happens during interaction.

```json
{
  "type": "error_occurred",
  "timestamp": "2026-04-10T12:45:00Z",
  "data": {
    "errorCode": "TERM_NOT_FOUND",
    "errorMessage": "Term 'xyz-999' does not exist",
    "userContext": "search",
    "recoveryAction": "return_to_search",
    "severity": "warning"
  }
}
```

#### `error_recovered`
User or system recovers from error.

```json
{
  "type": "error_recovered",
  "timestamp": "2026-04-10T12:45:05Z",
  "data": {
    "errorCode": "TERM_NOT_FOUND",
    "recoveryMethod": "user_retry_search",
    "newState": "searching"
  }
}
```

## Event Characteristics

### Common Properties

All events include:

```json
{
  "type": "event_type",
  "timestamp": "ISO 8601",
  "data": {
    "...event-specific fields..."
  }
}
```

### Optional Properties

```json
{
  "sessionId": "sess-abc123",
  "userId": "user-id",
  "clientId": "client-device-id",
  "traceId": "distributed-trace-id",
  "correlationId": "related-events-group-id"
}
```

## Event Flow Example

```
user_query → term_search_initiated
              ↓
         agent processes
              ↓
         term_search_results
              ↓
         user examines results
              ↓
         term_click (sg-001)
              ↓
         state_transition (viewing_term)
              ↓
         suggestion_presented (related term)
              ↓
         suggestion_accepted
              ↓
         term_click (lfma-001)
              ↓
         state_transition (viewing_term)
              ↓
         task_delegated (drift validation)
              ↓
         agent_task_completed
              ↓
         suggestion_presented (validation results)
              ↓
         state_transition (idle)
              ↓
         session_ended
```

## Event Listener Registration

Components can register for specific event types:

```typescript
addEventListener('term_click', (event) => {
  console.log(`Term ${event.data.termId} clicked`);
  navigateToTerm(event.data.termId);
});

addEventListener('drift_detected', (event) => {
  showDriftWarning(event.data.driftLevel, event.data.recommendations);
});
```

## Analytics & Telemetry

Events are captured for:
- User behavior analysis
- Agent performance monitoring
- Interaction pattern discovery
- UX optimization
- Error rate tracking
