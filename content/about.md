---
title: About
---
## Intro

Welcome! We are a few open source sanskrit programmers, and this is our centralized repository of data pertaining to the ashtadhyayi and its commentaries. We welcome you to contribute corrections to the content or improvements to the UI.

### Motivation
This data is presented in many places on the internet (wikisource, sanskritdocuments.org, avg-sanskrit, ashtadhyayi.com etc..), but there was no centralized place where corrections and curations could happen in a crowdsourced yet controlled fashion. Hence this repository.

## Content
The content is located in various directories in the content folder. Each file is devanagari encoded markdown text with yaml frontmatter.

## UI
We use the Hugo static site generator to generate webpages.

### Updating the UI with the latest content
- Install [Hugo](gohugo.io)
- Run `hugo` (Takes ~ 16s as of 20181216.)
- Check in and push the changed files to github.

### Technical considerations
- github.io is a convenient place to present the data (no money needed for server resources).
- The Jekyll static site generator is just too slow for data of this magnitude.
- Using javascript to dynamically include content from github.com runs into CORS problems.
