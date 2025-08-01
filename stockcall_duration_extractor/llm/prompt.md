Analyze the following lines extracted from a financial report. These lines contain various time durations, but not all of them specify the duration for a stock price target or recommendation. The objective is to identify the single line that provides the target duration to act on the stock.

**Input Sentences:**
1. "While management continues to aim for 10-20% net area additions annually (~14% YoY in FY25), acceleration of store additions is the utmost priority and seen as the best way to tackle the rising competition from Quick Commerce (QC)."
2. "We raise our FY26-28E EBITDA and PAT by ~2-4% as the increase in CoR (primarily related to staff costs to improve service levels) normalizes."
3. "DMart Ready: Looking to reduce delivery timelines to ~6 hours  Overall, management remains content with the progress of the DMart Ready business (revenue up ~20% YoY in FY25)."
4. "DMart added 50 stores in FY25 (~14% YoY) and aims to add 10–20% area annually."
5. "QC impact on LFL growth: Management had indicated ~1.0-1.5% impact on LFL growth due to Quick Commerce earlier and believes the impact is largely reflected in FY25."
6. "DMart Ready’s losses increased in FY25 owing to a shift to a more home delivery-based model and general inflation in delivery costs due to higher competitive intensity from QC."
7. "Exhibit 3: Bill cuts grew ~17% YoY in FY25…"

**Instructions:**
- Find the single sentence that provides the most direct or implied duration for a stock price or recommendation.
- Ignore lines that contain time durations but are not related to the stock's recommendation or price target.
- Do not make a guess if the duration is not explicit.
- If a sentence is found, provide the output in JSON format.
- The `duration_in_months` should be a normalized integer value (e.g., 20 months from July 2025 to the end of FY2027).
- Include a new key, `duration_source`, which should be "provided" if the duration is explicitly stated (e.g., "next 3 years") or "inferred" if it is derived from a fiscal year (e.g., "FY2027").
- If no sentence clearly refers to the expected target duration, the output must be a JSON object with a single key: `message` with the value "No clear duration found.".
- Do not include any text outside the JSON object.

**Sample Output (Match Found):**
```json
{
  "matched_sentence": "After the strong performance in this quarter, we factor in a revenue/ profit growth of 17%/ 17% and maintain our Buy rating with PT of Rs. 445 based on 44x of FY2027 EPS.",
  "duration_in_months": 20,
  "unit": "months",
  "confidence_score": "high",
  "duration_source": "inferred"
}

(If Match not found)
{
  "message": "No clear duration found."
}