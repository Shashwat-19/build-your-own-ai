# Contributing

Thanks for helping make this list better. One rule sits above all others:

> **It must be free, and it must teach you to _build_ the thing, not just _use_ it.**

## What gets accepted

A resource should meet **all** of these:

- **Free.** No paywall, no "free chapter then pay". Free books, courses, blog posts, videos and repositories are all fine. Companion code for a paid book is fine if the repo itself is complete and runnable.
- **Builds something.** It walks you through implementing a system (a tokenizer, an agent loop, a vector index), or it is a small, readable codebase meant for learning. Pure API usage guides ("call `openai.chat.completions.create`") do not qualify.
- **Explainers are the exception.** A conceptual write-up can be listed as **Explainer** if it is widely used as the companion to building that thing (e.g. _The Illustrated Transformer_).
- **Works today.** The link resolves, the code runs on a currently supported version of its framework, or the author notes how to adapt it.
- **Not a duplicate.** Check the section first.

## What does not get accepted

- Paywalled or sign-up-walled content
- Product marketing, listicles or SEO roundups
- Affiliate or referral links
- Your own resource submitted with no explanation of what it teaches (self-submissions are welcome, but say what makes it worth a learner's time)

## How to add a resource

1. Find the right `### Build your own …` section. If none fits, add a new one and an entry in **Contents**.
2. Add one line, matching this format exactly:

   ```markdown
   * [**Language**: _Title of the tutorial_](https://link)
   ```

   - Use the language the reader will write (`Python`, `TypeScript`, `C++`, `Rust`, `Go`, `C/CUDA`…), or `Explainer` for conceptual write-ups.
   - Append `` `[video]` `` for video content.
   - Keep the title close to the original; add a short clarifier after a colon if the title alone is vague.
3. Within a section, keep **Explainer** entries first, then code entries roughly in the order a learner should tackle them (easiest first).
4. Open a pull request using the template.

## Reporting a dead or outdated link

Open an issue with the **Broken link** template, or send a PR that fixes or removes it. A link-checker workflow also runs weekly and opens an issue automatically when links break.

## Code of conduct

Be kind, be specific, assume good intent. Maintainers may close contributions or issues that are hostile or spammy.
