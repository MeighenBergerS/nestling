# Lesson 02: LLMs for Code

LLMs have become genuinely useful coding assistants.
Used well, they compress the time from "I need a function that does X" to working,
tested code. Used poorly, they introduce subtle bugs that pass casual inspection and
fail only under the conditions that matter most.

This lesson covers how to pair-program with an LLM while keeping you in control of
correctness.

---

## The pair-programming model

Think of the LLM as a very fast, knowledgeable junior colleague.
It knows a lot of syntax, patterns, and library APIs.
It can produce a first draft quickly.
But it can be confidently wrong, it does not know your codebase, and it has no skin in the game
when the analysis produces the wrong result.

Your role is:

1. **Specify clearly.** You define what the code must do and what constraints apply.
2. **Review critically.** You read the output as you would any code submission.
3. **Test rigorously.** You write or demand tests; you do not accept "it looks right".
4. **Understand before using.** You do not merge code you cannot explain.

The LLM accelerates step 1 to draft; you own steps 2–4 entirely.

---

## Effective prompts for code

The quality of LLM-generated code is strongly correlated with the quality of your prompt.
Vague prompts produce vague code. Specific prompts produce specific code.

### What to include

- **Language and version.** "Python 3.11", "C++17", "JavaScript ESNext".
- **What the function should do.** One sentence in plain English.
- **Input types and shapes.** "Takes a numpy array of shape (N, 3)".
- **Output format.** "Returns a dict mapping strings to floats".
- **Constraints.** "Must handle empty input", "Must be vectorised", "No external dependencies".
- **Style.** "Follow NumPy docstring conventions", "Use type hints".

### Example: vague prompt

> "Write a function to process the data."

The model will produce something. It will not be what you want.

### Example: specific prompt

> "Write a Python 3.11 function `bin_energies(events, edges)` that takes a 1-D NumPy
> array `events` of floats and a 1-D NumPy array `edges` of bin edges (length N+1 for N bins),
> and returns a 1-D NumPy array of length N containing the count of events in each bin.
> Use `numpy.digitize`. Handle empty `events` by returning an array of zeros.
> Include a NumPy-style docstring and type hints."

This prompt will produce usable, testable code.

---

## Reviewing LLM-generated code

Never merge LLM-generated code without reading every line.
The model can produce code that:

- **Looks correct but has off-by-one errors.** Bin edges, array slicing, loop bounds.
- **Uses the wrong API.** Deprecated functions, arguments in the wrong order,
  misunderstood return types.
- **Handles only the happy path.** Empty arrays, NaN values, edge cases at domain
  boundaries are commonly omitted.
- **Has security issues.** Shell injection via `subprocess`, SQL injection via string
  formatting, unsafe deserialisation. These patterns appear in training data and the model
  reproduces them.
- **Is subtly non-reproducible.** Unset random seeds, floating-point operations that
  differ across platforms, silent type coercions.

Read code from an LLM as you would read code from a student, with respect but with
attention to every assumption.

---

## Testing LLM-generated code

A key industrial discipline is: **do not trust code you have not tested**.
For LLM-generated code this discipline is especially important.

### What to test

- **Expected inputs.** Does the function produce the correct output on a case you can
  verify by hand?
- **Edge cases.** Empty input, single-element input, extreme values, NaN, inf.
- **Type behaviour.** What happens if an integer is passed where a float is expected?
- **Error handling.** Does the function raise, return None, or silently return garbage
  on bad input?

### Asking the LLM to write tests

You can ask the model to write tests for the code it produced.
This is useful, as it reveals the model's assumptions about what the code is supposed to do.
But the model may write tests that pass trivially or that test only the happy path.
You must still review the tests.

> "Write pytest unit tests for the function above. Include tests for an empty array,
> an array with one element, an array where all values fall outside the bin range,
> and an array with NaN values."

---

## Common workflows

### Workflow 1: Draft and review

1. Write a clear specification (docstring or comment).
2. Ask the model to implement it.
3. Read every line. Flag anything you do not understand.
4. Run the tests. Fix failures yourself or ask the model to explain and fix them.
5. Commit only code you understand.

### Workflow 2: Explain and debug

1. Paste the code and the error message.
2. Ask the model to explain what the error means and where it originates.
3. Evaluate the explanation: is it plausible? Does it match what you know about the code?
4. Apply the fix. Understand why it works before moving on.

### Workflow 3: Code review

1. Paste a function or module.
2. Ask the model to identify potential bugs, edge cases, and style issues.
3. Treat the output as a checklist, not a verdict. Investigate each flagged item.

---

## Security considerations

LLM-generated code reproduces patterns from training data, including insecure patterns.

| Risk | Example | Mitigation |
|------|---------|------------|
| Shell injection | `subprocess.run(f"ls {user_input}", shell=True)` | Use argument lists, not shell strings |
| SQL injection | `cursor.execute(f"SELECT * FROM t WHERE id={val}")` | Use parameterised queries |
| Unsafe deserialisation | `pickle.loads(user_data)` | Use safe formats (JSON) for untrusted data |
| Hardcoded credentials | `API_KEY = "sk-..."` in source | Use environment variables or secrets managers |
| Arbitrary code execution | `eval(user_input)` | Never eval untrusted strings |

If you are generating code for a service that handles external input, security review
is essential regardless of whether the code was LLM-generated or human-written.

---

## Industrial context: how the field approaches LLM-assisted development

**Copilot and code review gates.** Organisations using GitHub Copilot or similar tools
typically require the same code review process for AI-assisted code as for human-written
code. The origin of the code does not change the review obligation.

**Prompt injection in code.** When LLMs are embedded in automated pipelines that
process user-supplied text, adversarial inputs can manipulate the model's output.
If you are building a pipeline that feeds external data to an LLM, treat that data
as untrusted and constrain the model's output format.

**Test generation at scale.** Industry teams use LLMs to generate test suites for
existing code. The limiting factor is always the quality of the specification. Tests
generated from an underspecified function test the implementation, not the intended
behaviour.

**Reproducibility in research pipelines.** Code generated for a paper must produce
the same results from the same data regardless of who runs it and when.
LLM-generated code often omits seeds, version pins, and determinism flags.
Add these explicitly before treating any output as final.

---

## Checklist

- [ ] My prompts specify language, input/output types, and constraints.
- [ ] I read every line of LLM-generated code before using it.
- [ ] I have tests covering expected inputs and edge cases.
- [ ] I understand every function I commit. I can explain what it does and why.
- [ ] I have checked for security issues if the code handles external input.
- [ ] Random seeds and version pins are set for any code that produces results.

---

## What to read next

[Lesson 03](lesson-03.md) covers LLMs for writing: when drafting assistance is appropriate
and how to maintain authorship of your own work.
