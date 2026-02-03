# Standard User Stories and Acceptance Criteria
Customer Support Chatbot

---

## USER STORIES

### Billing & Payments

#### US‑001 — Double Charge Resolution
As a customer, I want to understand why I was charged twice so that I can resolve the issue without contacting support.

#### US‑002 — Invoice Explanation
As a customer, I want to know why my invoice amount changed so that I can verify billing accuracy.

#### US‑003 — Payment Failure Troubleshooting
As a customer, I want help resolving failed payments so that I can complete my transaction.

---

### Account Management

#### US‑004 — Password Reset
As a customer, I want clear instructions to reset my password so that I can regain access to my account.

#### US‑005 — Update Email Address
As a customer, I want to update my email address so that my account information stays current.

#### US‑006 — Cancel Account
As a customer, I want to cancel my account so that I can stop using the service.

---

### Troubleshooting

#### US‑007 — App Crash Diagnosis
As a customer, I want the bot to ask clarifying questions so that I receive accurate troubleshooting steps.

#### US‑008 — Avoid Repetition
As a customer, I want the bot to avoid repeating steps I already tried so that I don’t get stuck in a loop.

---

### Escalation

#### US‑009 — Human Agent Escalation
As a customer, I want to escalate to a human agent so that I can resolve complex issues.

---

### General Experience

#### US‑010 — Fast Response
As a customer, I want quick responses so that I don’t feel frustrated or ignored.

#### US‑011 — Polite & Empathetic Tone
As a customer, I want the bot to communicate politely so that I feel respected and supported.

---

# ACCEPTANCE CRITERIA

### AC‑001 — Double Charge Resolution
- Bot asks for account ID.
- Bot explains possible causes of double charges.
- Bot proposes next steps (refund, verification, escalation).
- Response meets relevance, correctness, and tone thresholds.

### AC‑002 — Invoice Explanation
- Bot requests relevant billing details.
- Bot provides clear explanation of invoice changes.
- Bot avoids generic or repetitive responses.

### AC‑003 — Payment Failure Troubleshooting
- Bot asks clarifying questions (payment method, error message).
- Bot provides targeted troubleshooting steps.
- Bot offers escalation if unresolved.

---

### AC‑004 — Password Reset
- Bot provides step‑by‑step reset instructions.
- Instructions match documented workflow.
- Bot confirms completion or next steps.

### AC‑005 — Update Email Address
- Bot verifies identity or account ownership.
- Bot provides accurate update instructions.
- Bot handles invalid email cases.

### AC‑006 — Cancel Account
- Bot confirms intent.
- Bot outlines cancellation steps.
- Bot provides link or action path.
- Bot warns about irreversible actions.

---

### AC‑007 — App Crash Diagnosis
- Bot asks clarifying questions (device, OS, error message).
- Bot provides targeted troubleshooting steps.
- Bot avoids premature suggestions.

### AC‑008 — Avoid Repetition
- Bot checks what steps the user already tried.
- Bot avoids repeating instructions.
- Bot adapts troubleshooting path.

---

### AC‑009 — Human Agent Escalation
- Bot recognizes escalation intent.
- Bot escalates gracefully.
- Bot provides confirmation message.

---

### AC‑010 — Fast Response
- Response time meets SLA threshold.

### AC‑011 — Polite & Empathetic Tone
- Bot uses polite, supportive language.
- Bot acknowledges frustration when appropriate.
