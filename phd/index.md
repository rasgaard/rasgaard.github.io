---
layout: default
title: PhD Status
---
## Status Updates
Once a month I try to sit down and think about what has happened.

{% assign posts = site.phd_status | sort: 'date' | reverse %}
{% for status in posts %}
   - {{status.date | date: '%Y'}}, **{{status.date | date: '%B'}}** - <a href="{{status.url}}">{{status.title}}</a>
{% endfor %}
## About the project
It is titled *"Edge deployment of deep neural networks via Model Compression for Healthcare Applications"* and is a collaboration between [Laerdal Medical](https://laerdal.com/) and the [Technical University of Denmark](https://www.dtu.dk/). It's a 3-year PhD going from October 1st 2025 to September 31st 2028.

Here are a few key statements that motivates me about the project: 
- We'd like to see how much performance we can squeeze onto devices with limited compute.
- Huge amounts of resources have already one into training models. Let's make sure that they're put to use by making them applicable on a wide range of devices.
- Centralizing AI inference is the standard but it's not always clear winner. *Distributing* inference compute to the client-side can be beneficial, perhaps even necessary, due to privacy, latency or cost at scale.

## Advice I keep returning to
- Andrej Karpathy: A Survival Guide to a PhD
    - [https://karpathy.github.io/2016/09/07/phd/](https://karpathy.github.io/2016/09/07/phd/)
- Tim Dettmers: Lessons Learned from Successful PhD Students
    - [https://mlsys.org/virtual/2025/invited-talk/3298](https://mlsys.org/virtual/2025/invited-talk/3298)
- John Schulman: An Opinionated Guide to ML Research
    - [http://joschu.net/blog/opinionated-guide-ml-research.html](http://joschu.net/blog/opinionated-guide-ml-research.html)
- Eugene Vinitsky
    - [https://www.eugenevinitsky.com/blogs/](https://www.eugenevinitsky.com/blogs/)
- Richard Hamming: You and Your Research
    - [https://www.cs.virginia.edu/~robins/YouAndYourResearch.html](https://www.cs.virginia.edu/~robins/YouAndYourResearch.html)
- Michael Nielsen: Principles of Effective Research
    - [https://michaelnielsen.org/blog/principles-of-effective-research/](https://michaelnielsen.org/blog/principles-of-effective-research/)
- Sam Altman: How to be successful
    - [https://blog.samaltman.com/how-to-be-successful](https://blog.samaltman.com/how-to-be-successful)
- Maxwell Forbes: The PhD metagame
    - [https://maxwellforbes.com/posts/your-paper-is-an-ad/](https://maxwellforbes.com/posts/your-paper-is-an-ad/)