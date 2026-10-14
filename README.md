# Structural Steel Remnant and Revision Management (SMROE)

### Forward Deployed Engineer (FDE) Case Study — Client B
**Client:** Structural Steel Fabricator (80,000 Tonnes / Year, 10–15 Concurrent Projects)  
**Annual Steel Spend:** ~$76,000,000 | **Realistic Target Savings:** $950,000 / Year  

---

## 📁 Repository Structure

```
structural_steel/
├── case-study.md                        # Deliverable 1: 6-Page Technical & Commercial Proposal
├── client-note.md                       # Deliverable 2: 1-Page Executive Management Memorandum
├── submission-form.md                   # Deliverable 3: 10 Graded Questions Answered
├── prototype/
│   └── nesting_benchmark.py             # Deliverable 4: Executable Python Benchmark Script
├── 06c9f684-fdb5-47e5-ab38-fc1720b3ab9d-discovery-call-notes.txt  # Raw Discovery Notes
└── README.md                            # Repository Documentation & Overview
```

---

## 🚀 Practical Overview of the Solution

The client requested artificial intelligence across five operational areas: nesting, drawing revisions, yard storage, trailer loading, and vehicle utilization.

As Forward Deployed Engineers, we **narrowed the scope and eliminated unrealistic software additions**:
1. **Rejected Trailer Loading AI & Yard Stacking AI:** Trailer idle time is caused by shop-floor fabrication delays, not 3D packing geometry. Existing vehicle GPS data is already unread. Yard stacking algorithms fail when project dates shift daily.
2. **Deterministic Mathematics for Cutting:** We do not use neural networks for physical steel cutting. We use standard 2D cutting-stock heuristics to guarantee zero torch collisions.
3. **Cross-Project Remnant Management:** We solve the accounting barrier where Project A cannot share offcuts with Project B, tracking usable yard remnants through an automated internal salvage ledger.
4. **Document Text Processing for Revisions:** We use text processing to extract revision notes from incoming drawings, drafting commercial claims so clients pay for scrap caused by late design changes.

---

## 💻 Running the Benchmark Script

The prototype proves the business logic using synthetic data calibrated to the client's volume:

### Requirements:
* Python 3.8+ (Uses standard built-in libraries; no `pip install` required).

### Command:
```bash
python prototype/nesting_benchmark.py
```

### Script Output Summary:
* **Current As-Is Process:** Independent single-project nesting on new plates yields **32.6% plate scrap** (calibrated to the client's 20–25% manual baseline).
* **SMROE Optimized Process:** Remnant-first matching + multi-project pooling drops scrap to **19.5%** on the test batch.
* **Cost Clearinghouse:** Credits donating project (+$626.43) and debits consuming project, saving $2,237.25 on a single cutting batch.
* **Revision Claim Calculator:** Identifies client-driven design changes and drafts a $1,377.50 change-order claim.
* **Annual Projection:** A realistic 1.0% waste reduction (\$760,000) + recovered client revision scrap (\$190,000) = **\$950,000 / year total value**.

---

## 📑 Core Deliverables

* [**Case Study Proposal (`case-study.md`)**](case-study.md) — 6-page comprehensive proposal covering problem analysis, ranked unknowns, solution architecture, pilot protocols, timelines, and practical unit economics.
* [**Executive Management Memo (`client-note.md`)**](client-note.md) — 1-page non-technical memo written for the Cost Control engineer to forward to executive management.
* [**Submission Form Answers (`submission-form.md`)**](submission-form.md) — Answers to all 10 evaluation questions with clear pushback, risk analysis, and AI disclosure.
