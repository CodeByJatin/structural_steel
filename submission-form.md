# SUBMISSION FORM: TASK 3 (CLIENT B — STRUCTURAL STEEL)
**Role:** Forward Deployed Engineer (FDE)  
**Candidate Name / ID:** FDE Candidate  
**Client:** Client B — Structural Steel Fabricator (80,000 Tonnes / Year)  

---

### Question 1: In two sentences: what is the client's real problem, and how is it different from what they asked for?*

The client asked for AI across five scattered operations (nesting, drawing revisions, yard storage, trailer loading, and vehicle utilization) under the assumption that AI software would automatically eliminate operational friction. In reality, their core problem is an unmeasured workflow with organizational bottlenecks: manual nesting continues because staff claims remain unverified, usable steel remnants sit stranded because project accounting prevents material sharing between jobs, and hundreds of tonnes of steel scrap are absorbed without billing clients due to missing revision governance.

---

### Question 2: Who are the people in this deal, and what does each of them need to hear from you?*

* **Cost Control Engineer (Our Contact):** Needs defensible, verified numbers on material scrap and an objective audit of manual vs. automated nesting, giving them credible data for management without causing conflict with factory floor teams.
* **Executive Management:** Needs a low-risk, milestone-based pilot with a fast payback (under 60 days) that addresses their primary cash drain ($76M raw steel spend) without requiring an expensive multi-year software overhaul.
* **Nesting Team (Absent from calls):** Needs to hear that the software is not replacing their craft or threatening their jobs; it is an assistant that finds yard offcuts and calculates layouts, while they retain 100% sign-off authority and manual override on every cut.
* **Engineering / Detailing Team (Absent from calls):** Needs to hear that drawing tracking is designed to back-charge client design modifications and protect project margins, not to penalize internal drafting errors.
* **Yard & Sizing Shop Floor (Absent from calls):** Needs to hear that remnant tracking uses simple barcode stickers and physical racks, not complex computer vision cameras or rigid digital stacking rules that fail in heavy rain and dust.

---

### Question 3: The five questions you would ask on the next call, ranked.** For each one: why it matters, and what you assumed while you wait for the answer.*

1. **Rank 1: Can your IT team export cutting files (DXF/NC1), plate purchases, and scrap weight records from Strumis for 20 completed jobs?**
   * *Why it matters:* We must calculate the real historical baseline before writing code. We cannot improve what we have not measured.
   * *Working Assumption:* Strumis contains CAD part lists and plate invoices, but offcut dimensions and actual CNC scrap weights are unstandardized.
2. **Rank 2: Can the Lead Nesting Engineer join our next technical working session?**
   * *Why it matters:* If the nesting team does not trust the software, they will refuse to cut algorithmic layouts on the shop floor.
   * *Working Assumption:* Nesting staff are defensive about their manual routine and will reject any tool that removes their control.
3. **Rank 3: Will company finance allow a standard salvage credit (e.g., 80% of prime steel price) when Project B consumes an offcut bought by Project A?**
   * *Why it matters:* If accounting locks every steel plate to a single project budget, cross-project remnant reuse is blocked.
   * *Working Assumption:* Finance will approve a standard internal transfer rate if total company steel expenditure drops.
4. **Rank 4: Where and in what format are drawing revisions and client change requests stored?**
   * *Why it matters:* We need to know whether change reasons exist in structured database tables, PDF drawing title blocks, or unstructured email threads.
   * *Working Assumption:* Most revision reasons exist only as text notes inside PDF blueprints and email chains.
5. **Rank 5: What is the primary cause of low trailer utilization: loading delays, missing parts at coating, or dispatch scheduling?**
   * *Why it matters:* Management is unhappy about hiring outside trailers, but adding software will fail if the true bottleneck is painting or fabrication delays.
   * *Working Assumption:* Fleet idle time is caused by shop-floor production bottlenecks, not vehicle packing geometry.

---

### Question 4: Which options did you consider, and why did you pick the one you did?** What did you rule out, and why?*

* **Option 1: Complete Operations AI (The Client Wishlist).**  
  * *Why ruled out:* Attempting to optimize five departments at the same time dilutes engineering focus and creates severe operational friction.
* **Option 2: Computer Vision Yard System.**  
  * *Why ruled out:* Industrial steel yards are exposed to rain, dust, grease, and crane shadows. Optical systems fail frequently in this environment and cannot achieve millimeter cutting precision.
* **Option 3: Replacing Strumis ERP.**  
  * *Why ruled out:* Takes 2 to 3 years, costs millions, and creates massive operational risk for the factory.
* **Option 4 (SELECTED): Strumis Remnant & Revision Intelligence Layer.**  
  * *Why picked:* Focuses strictly on high-dollar cash recovery: reusing leftover steel plates and billing clients for revision scrap. It uses standard 2D cutting heuristics integrated into Strumis, delivering ~$950k/year in practical savings with zero factory disruption.

---

### Question 5: How will the client know the pilot worked?** Metric, baseline, threshold, how many runs, who measures, and what result would make you stop.*

* **Core Metric:** Total Steel Scrap Percentage ($\% \text{ Scrap} = \frac{\text{Purchased Steel Mass} - \text{Finished Part Mass}}{\text{Purchased Steel Mass}} \times 100$).
* **Baseline:** Established across 20 historical jobs extracted from Strumis (currently estimated at 7–10% total, 20–25% for plates).
* **Success Threshold:** A conservative **1.0% absolute reduction in total steel waste** (saving ~800 tonnes / $760k annually), plus at least **25% of plate remnants reused** within 30 days.
* **Secondary Metric:** Billed Revision Scrap: At least **60% of client-driven design scrap** successfully back-charged to clients.
* **Test Protocol:** 
  * Phase 1: Retrospective benchmark on 20 historical jobs.
  * Phase 2: Controlled live run on 15 consecutive shop floor cutting batches.
* **Who Measures:** Jointly measured by the Client Cost Control Lead and the FDE, reconciled against certified scrap weigh-scale receipts.
* **Kill Criteria (What makes us stop):**
  1. The algorithm fails to beat manual layouts by at least **1.0% absolute yield** across the 20 historical test jobs.
  2. The Lead Nesting Engineer demonstrates that algorithmic cut paths increase machine torch collisions or thermal plate warping.
  3. Client IT fails to provide database exports within 21 days.

---

### Question 6: What does this cost the client, and what does it cost us to deliver?** Show the arithmetic and name the pricing structure. What value does the client get, in their money?*

#### 1. Practical Client Value Arithmetic:
* **Annual Throughput:** 80,000 Tonnes.
* **Average Steel Cost:** \$950 / Tonne.
* **Total Annual Raw Material Spend:** $80,000 \times \$950 = \mathbf{\$76,000,000}$.
* **1.0% Absolute Waste Reduction:**  
  $$80,000 \text{ Tonnes} \times 0.01 \times \$950/\text{Tonne} = \mathbf{\$760,000 / \text{year in direct steel savings}}.$$
* **Recovered Client Revision Scrap (Conservative):**  
  $$\approx 200 \text{ Tonnes unbilled client design changes} \times \$950 = \mathbf{\$190,000 / \text{year}}.$$
* **Total Realistic Annual Value to Client:** **\$950,000 / year.**

#### 2. Cost to Deliver (12-Week Pilot):
* **Team:** 1 Lead FDE (1.0 FTE) + 1 Optimization Engineer (1.0 FTE) for 12 weeks.
* **Internal Loaded Cost:** 2 FTEs $\times$ \$20,000/month $\times$ 3 months = \$120,000.
* **Travel and Software Tools:** \$10,000.
* **Total Delivery Cost to Us:** **\$130,000**.

#### 3. Pricing Structure to Client:
* **Fixed Pilot Fee:** **\$95,000** billed in three milestone payments (\$35k kickoff, \$30k audit delivery, \$30k pilot completion).
* **Success Incentive:** **10% of verified direct steel savings** during months 4 through 12 (capped at \$80,000).
* **Annual License Post-Pilot:** **\$75,000 / year** (maintenance, cloud hosting, and integration updates).
* **Payback Period:** **Under 2 months** of operational deployment.

---

### Question 7: Timeline.** What is the first result the client sees, and when? Which steps depend on the client rather than on us?*

#### Timeline Schedule:
* **Weeks 1 to 3 (Audit Phase):** Extract Strumis data and run 2D optimization on 20 historical jobs.
* **Weeks 4 to 7 (Integration Phase):** Connect Strumis read replica, build remnant barcode generator, and set up the cost ledger.
* **Weeks 8 to 11 (Shadow Run Phase):** Run 15 live production cutting batches on CNC machines with nesting engineer sign-off.
* **Week 12 (Review Phase):** Reconcile weighed scrap receipts and finalize the rollout plan.

#### First Result Delivered:
* **Day 21 (End of Week 3):** The **Historical Benchmark Audit Report**. For the first time, management sees hard numbers comparing their manual nesting yield against mathematical algorithms on 20 past jobs.

#### Client-Dependent Steps:
1. **Week 1:** Client IT granting read-only database export from Strumis.
2. **Week 2:** Scheduling two 1-hour calibration meetings with the Lead Nesting Engineer.
3. **Week 4:** Finance approval of the inter-project salvage credit rate.
4. **Week 7:** Providing 2 standard barcode label printers in the cutting bay.

---

### Question 8: Where did you push back on the client, narrow their ask, or tell them not to do something?** [can only raise your score]*

1. **Pushed back on Trailer Loading AI:** The client wanted AI to optimize trailer loading and equipment scheduling. We said **NO**. The client purchased CarTrack GPS and an internal vehicle booking system 6 months ago, but nobody reads the data. Low utilization is caused by shop-floor fabrication delays, not packing math. Adding software to an unused booking tool will not fix idle trailers.
2. **Pushed back on Yard Stacking AI:** The client wanted an algorithm to sequence plate stacks in the yard. We said **NO**. In a busy steel yard, crane operators under production pressure will ignore computer instructions when project priorities change daily. Remnant consumption removes the clutter naturally.
3. **Pushed back on Replacing Strumis:** The client asked if they should switch to a different software system. We said **NO**. Strumis is an established ERP. Replacing it would risk stopping factory production.
4. **Pushed back on Deep Learning for Cutting Geometry:** The client asked for AI to optimize cutting. We pushed back on neural networks. In steel cutting, geometry must be exact to the millimeter. We used deterministic Operations Research algorithms that guarantee collision-free cutting paths.

---

### Question 9: What is most likely to go wrong with your plan, and what in these notes did you not trust?** [can only raise your score]*

#### What is Most Likely to Go Wrong:
1. **Nesting Team Resistance:** Nesting programmers might intentionally find edge cases where the software fails or claim that algorithmic layouts cause machine torch collisions, refusing to sign off.  
   * *Mitigation:* Involve them early; let them set safety parameters; keep 100% human sign-off so the tool acts as an assistant.
2. **Accounting Inflexibility:** Project managers may refuse to let their projects use remnants or give credits, insisting on buying new prime steel to protect their individual budgets.  
   * *Mitigation:* Require senior finance leadership to mandate standard salvage rates before live cutting begins.

#### What We Did NOT Trust in These Notes:
1. **We did NOT trust the reported waste numbers (20–25% plate, 5–10% profile, 7–10% overall):** The client contact explicitly admitted: *"We don't have enough data to analyze how much steel is being wasted... the manual data shows about 20 to 25%."* These numbers are manual estimates, not weighed data. The Phase 1 audit must measure true historical waste before we accept these figures.
2. **We did NOT trust the nesting team's claim that automatic nesting wastes more steel than manual nesting:** This is a common defensive reaction by manual workers protecting their daily routine. It has never been tested with verified data.
3. **We did NOT trust that equipment idle time is a software problem:** The client has 13 trailers and low utilization, yet hires outside trucks. They already have CarTrack GPS and a booking system that are completely ignored. The problem is operational discipline, not a missing algorithm.

---

### Question 10: What did you use AI for?** Which tools, where they helped, where they misled you, and what you threw away.*

* **Where AI Was Used (Language Models / NLP):**  
  We used language models exclusively for **unstructured document text processing**: reading revision title blocks on incoming PDF drawings and architect change emails to determine whether steel scrap was caused by client design changes or internal drafting errors.
* **Where AI Helped:**  
  AI was very effective at extracting text from messy drawing notes and drafting pre-filled commercial change-order claims.
* **Where AI Misled Us:**  
  Initial generic AI tools suggested using deep reinforcement learning for 2D nesting and computer vision cameras for yard tracking. In an industrial steel yard, cameras fail due to dust, rain, and shadows, while neural networks cannot guarantee zero collision on a physical CNC cutting machine.
* **What We Threw Away:**  
  We threw away all computer vision proposals for the yard. We threw away all deep learning for cutting geometry (using standard 2D bin-packing math instead). We threw away all 3D trailer loading optimization models.

---

### Github Repo URL:
`https://github.com/CodeByJatin/structural_steel`
