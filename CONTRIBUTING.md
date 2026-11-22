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
4. Check your change locally (needs only Python 3):

   ```bash
   python3 scripts/validate_readme.py README.md
   ```

   It checks entry format, duplicate URLs and that every Contents anchor resolves. CI runs the same script on every pull request, plus a link checker.
5. Open a pull request using the template. Keep one topic per PR so it is quick to review.

## Reporting a dead or outdated link

Open an issue with the **Broken link** template, or send a PR that fixes or removes it. A link-checker workflow also runs weekly and opens an issue automatically when links break.

## Review

PRs are normally reviewed within a week. A maintainer may ask you to adjust the section, wording or ordering. If a PR sits without a reply for two weeks, feel free to comment on it.

## Licence of your contribution

This list is released under [CC0 1.0](LICENSE). By submitting a pull request you agree your contribution to the list (the entry text, not the linked resource) is released under the same terms. Linked resources keep their own licences.

## Code of conduct

Everyone taking part is expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md). Maintainers may close contributions or issues that are hostile or spammy.
