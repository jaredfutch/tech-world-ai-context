# Launch Kit

Use this file as a public promotion starter for the Tech-World AI Context Framework. Keep claims tied to the repository and avoid implying endorsement by AI vendors.

## One-line description

An open-source continuity and project-state framework for long-running work with ChatGPT, Codex, and AI coding agents.

## Short pitch

AI assistants are good at individual conversations, but substantial projects accumulate decisions, corrections, repositories, migrations, deployments, and changing facts. The Tech-World AI Context Framework separates remembered intent from current project truth and verification evidence so AI-assisted work can continue without repeatedly rebuilding context.

## Core message

The framework is built around a simple distinction:

```text
Conversation history tells us what the project is supposed to be.
Current artifacts tell us what the project actually is.
Verification tells us what actually works.
```

## LinkedIn launch post

I kept running into the same problem with long-running AI-assisted projects: the conversation remembered the goal, but that did not always mean it knew the current state of the repository, database, deployment, or prior corrections.

So I built the Tech-World AI Context Framework, an open-source approach to controlled continuity across ChatGPT, Codex, repositories, project files, decisions, corrections, migrations, tests, deployments, and handoffs.

The core idea is simple:

Conversation history tells us what the project is supposed to be.
Current artifacts tell us what the project actually is.
Verification tells us what actually works.

It also uses a strict software state model:

Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted

The goal is not infinite AI memory. It is a reliable source-of-truth hierarchy for work that lasts longer than one chat.

The framework is MIT licensed and available on GitHub. Feedback from developers, operators, AI power users, and people managing long-running agent workflows is welcome.

## Short social post

I open-sourced the Tech-World AI Context Framework: a continuity and project-state architecture for long-running ChatGPT, Codex, and AI-agent work.

Instead of treating chat memory as truth, it separates:

Intent → Current artifacts → Verification → Deployment → Acceptance

The goal is controlled continuity, not infinite memory.

## Hacker News / developer-community introduction

Title suggestion:

**Show HN: A framework for keeping long-running AI projects grounded in repository truth**

Post body:

I built this after repeatedly seeing a gap between what an AI assistant remembered about a project and what actually existed in the current repository or runtime.

The framework uses layered context: a stable bootstrap, repository-level instructions, private project records, current source/schema/configuration, and verification evidence. Corrections explicitly supersede rejected older guidance, and software state is tracked as Requested → Implemented → Code-Verified → Runtime-Tested → Deployed → User-Accepted.

The project is less about prompt engineering and more about source-of-truth control for work that spans many conversations and releases.

I would be interested in criticism from people running coding agents or long-lived AI workflows: where does this model break, and what state do you think belongs closest to the repository?

## Discussion prompts

- How do you prevent an AI coding agent from trusting stale conversational context over the repository?
- Where do you store durable project corrections and rejected decisions?
- Do you distinguish implemented, tested, deployed, and accepted states in AI-assisted work?
- How do you recover context when a project spans months and multiple tools?
- What should an AI agent treat as authoritative when memory and runtime evidence disagree?

## Suggested GitHub topics

These must be added through GitHub repository settings if the connected API does not expose topic writes.

```text
ai
chatgpt
codex
ai-agents
coding-agents
context-engineering
prompt-engineering
developer-tools
knowledge-management
project-management
ai-workflow
llm
open-source
```

Prefer the most accurate subset rather than using every possible topic.

## Social preview copy

**Tech-World AI Context Framework**

Controlled continuity for ChatGPT, Codex & AI coding agents

**Intent → Evidence → Implementation → Verification**

## Promotion checklist

- Confirm latest release is current.
- Add GitHub repository topics.
- Add a GitHub social preview image.
- Pin the repository on the maintainer profile.
- Share the one-minute demo rather than only the repository root.
- Publish the LinkedIn launch post.
- Post a discussion-oriented Show HN / developer-community introduction.
- Watch GitHub Insights → Traffic for referral and clone changes.
- Use feedback to improve examples before expanding the specification.
