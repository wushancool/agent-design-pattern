# Multi-Agent Design Pattern

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
Process data through a series of dependent steps where each step builds on the previous one.

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
Distribute tasks across multiple agents simultaneously and consolidate results to improve efficiency.

## 3. Coordinator
**Alias**: Coordinator/Dispatcher Pattern, Group Chat, Supervisor-Worker pattern

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
Manage workflow between specialist agents to leverage their unique capabilities effectively.

## 4. Reflection
**Alias**: Review/Critique Pattern, Generator-Critic, Evaluator-optimizer

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
Enhance output quality through iterative feedback and refinement cycles.

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
Enable dynamic task delegation between agents based on expertise and availability.

## 6. Human in the loop
### Pattern
```mermaid
graph LR;
In(("In")):::input-->AgentA;
AgentA-->Human;
Human-->|Option 1|AgentB;
Human-->|Option 2|AgentC;
AgentB-->Out1(("Out 1")):::output;
AgentC-->Out2(("Out 2")):::output;

classDef input fill:#93c5fd;
classDef output fill:#86efac;
```

### Goal
Integrate human expertise and judgment at critical decision points in automated workflows.