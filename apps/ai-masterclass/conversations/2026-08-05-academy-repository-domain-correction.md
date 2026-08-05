# Academy repository and domain correction

**Date:** 2026-08-05

## Hardeep Anand direction

> I don't understand the staging where you are going to dev, because dev is a completely different
> repository where you're building software for commercial real estate and Section 8 housing and
> that kind of stuff, right? It is a product of Apple's build, not for anything else. How do you do
> this? Because it's not making sense. Fix it!

Hardeep also established that the internal Academy must use a completely separate GitHub repository.
The Academy may sit within the APAS.ai company architecture, while One Water AI and One Water
Foundation remain distinct product, sales, licensing, and delivery concerns.

## Governed correction

- APAS.dev is the separate APAS commercial real-estate and housing product.
- APAS.dev will not name or host the Academy, its staging environment, its repository, or its brand.
- The internal application identity is APAS.ai Academy.
- The production hostname target is `academy.apas.ai`.
- The application will have a dedicated private repository named `apas-academy-studio`.
- Preview deployments are temporary, access-controlled branch builds from that same repository.
- `owos-learning-content` remains the only authority for approved curriculum.
- The current Academy code in `onewater-os-platform` is transitional and must be extracted once,
  verified for parity, and removed from that platform after cutover.

This correction does not authorize production deployment, public curriculum release, credentialing,
or publication to any learner platform.
