# Agent Design Pattern

## 1. Sequential
**Alias**: Sequential Workflow, Sequential pipeline Pattern

### Pattern
```mermaid
graph LR;
    In(("In")):::input-->A
    A-->B;
    B-->C;
    C-->Out(("Out")):::output;
    
    classDef input fill:#93c5fd;
    classDef output fill:#86efac;
```

### Goal
Implement a multi-step process where the output of one step feeds into the next.

## 2. Parallel
**Alias**: Fan-Out/Gather

### Pattern
```mermaid
graph LR;
    In(("In")):::input-->A;
    A-->B;
    A-->C;
    A-->D;
    B-->E;
    C-->E;
    D-->E;
    E-->Out(("Out")):::output;
    
    classDef input fill:#93c5fd;
    classDef output fill:#86efac;
```

### Goal
 Execute independent tasks simultaneously to reduce **latency**, then combine their outputs.

## 3. Coordinator
**Alias**: Coordinator/Dispatcher Pattern, Group Chat

### Pattern
```mermaid
graph LR;
    In(("In")):::input-->Coordinator;
    Coordinator-->AgentA;
    Coordinator-->AgentB;
    Coordinator-->AgentC;
    AgentA-->Coordinator;
    AgentB-->Coordinator;
    AgentC-->Coordinator;
    Coordinator-->Out(("Out")):::output;
    
    classDef input fill:#93c5fd;
    classDef output fill:#86efac;
```

### Goal
Route incoming requests to the appropriate specialist agent.

## 4. Reflection
**Alias**: Review/Critique Pattern , Generator-Critic, Evaluator-optimizer

### Pattern
```mermaid
graph LR;
    In(("In")):::input-->Generator;
    Generator-->|Output|Critic;
    Critic-->Decision{Acceptable?};
    Decision-->|Yes|Out(("Out")):::output;
    Decision-->|No|Generator;
    
    classDef input fill:#93c5fd;
    classDef output fill:#86efac;
```

### Goal
Improve the quality or validity of generated output by having a dedicated agent review it.

## 5. Handoffs
**Alias**: Swarm

### Pattern
```mermaid
graph LR;
    In(("In")):::input-->AgentA;
    AgentA-->|"handoff"|AgentB;
    AgentA-->|"handoff"|AgentC;
    AgentA-->|"handoff"|Human;
    AgentB-->|"handoff"|AgentA;
    AgentB-->|"handoff"|AgentC;
    AgentC-->|"handoff"|AgentA;
    AgentC-->|"handoff"|AgentB;
    AgentC-->|"handoff"|Human;
    Human-->Out(("Out")):::output;
    
    classDef input fill:#93c5fd;
    classDef output fill:#86efac;
```

### Goal
Let agent delegate tasks to other agents using a special tool call.
