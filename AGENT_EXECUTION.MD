# Agent Execution Design Patterns

## 1. ReAct: Synergizing Reasoning and Acting in Language Models
ReAct is a prompting method for large language models that combines reasoning (e.g., chain-of-thought prompting) and acting (e.g., interacting with external tools like search engines) to enable more robust problem-solving and task completion.

## 2. ReWOO: Decoupling Reasoning from Observations for Efficient Augmented Language Models

ReWOO is a framework that improves augmented language models by **decoupling the reasoning process from external observations**, allowing the model to plan and strategize before engaging with tools, leading to more efficient and effective problem-solving.

ReWOO significantly improves upon ReAct by **decoupling reasoning from observation**, enabling **upfront, comprehensive planning** and leading to **greater efficiency (fewer LLM calls, lower token usage), faster execution, and enhanced robustness against tool failures.**

## 3. Plan and Execute (Plan-and-Act)
