---
layout: default
title: Home
full_bleed: true
---

<!-- ===== HERO ===== -->
<section class="hero">
  <div class="wrap">
    <div class="hero-inner">
      <div>
        <span class="eyebrow">{{ site.hero.eyebrow }}</span>

        <h1 class="hero-title">
          {{ site.hero.headline_lead }}
          <span class="accent">{{ site.hero.headline_accent }}</span>
        </h1>

        <p class="hero-name">{{ site.author.name }} <span>— {{ site.hero.affiliations }}</span></p>

        <p class="hero-blurb">{{ site.hero.blurb }}</p>

        <div class="hero-actions">
          <a class="btn btn--primary" href="{{ '/projects/' | relative_url }}">
            See the work <svg aria-hidden="true"><use href="#i-arrow"/></svg>
          </a>
          {% include social-links.html %}
        </div>
      </div>

      <div class="hero-portrait">
        {% if site.author.avatar %}
        <img src="{{ site.author.avatar | relative_url }}" alt="{{ site.author.name }}" />
        {% else %}
        <div class="portrait-fallback">🧑‍💻</div>
        {% endif %}
      </div>
    </div>

    <div class="hero-stats">
      <div class="stat">
        <div class="stat-num">{{ site.stats.years_experience }}+</div>
        <div class="stat-label">Years in production ML</div>
      </div>
      <div class="stat">
        <div class="stat-num">3</div>
        <div class="stat-label">Domains: credit, fraud, risk</div>
      </div>
      <div class="stat">
        <div class="stat-num">54</div>
        <div class="stat-label">Topics in the open ML guide</div>
      </div>
    </div>
  </div>
</section>

<!-- ===== FOCUS ===== -->
{% if site.focus_areas.size > 0 %}
<section class="section">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-index">01</span>
      <h2>What I work on</h2>
      <span class="sec-line"></span>
    </div>

    <div class="focus-grid reveal">
      {% for area in site.focus_areas %}
      <div class="focus-card">
        <div class="focus-index">{{ area.index }}</div>
        <h3>{{ area.title }}</h3>
        <p>{{ area.body }}</p>
        {% if area.tags %}
        <div class="chip-row">
          {% for t in area.tags %}<span class="chip">{{ t }}</span>{% endfor %}
        </div>
        {% endif %}
      </div>
      {% endfor %}
    </div>
  </div>
</section>
{% endif %}

<!-- ===== SELECTED WORK ===== -->
{% if site.projects.size > 0 %}
<section class="section">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-index">02</span>
      <h2>Selected work</h2>
      <span class="sec-line"></span>
      <a class="sec-more" href="{{ '/projects/' | relative_url }}">All work →</a>
    </div>

    <div class="card-list">
      {% assign sorted_projects = site.projects | sort: "date" | reverse %}
      {% for project in sorted_projects limit:3 %}
        <div class="reveal">{% include project-card.html project=project %}</div>
      {% endfor %}
    </div>
  </div>
</section>
{% endif %}

<!-- ===== OPEN RESOURCE ===== -->
<section class="section">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-index">03</span>
      <h2>Open resource</h2>
      <span class="sec-line"></span>
    </div>

    <div class="feature-band reveal">
      <div class="band-text">
        <span class="eyebrow">Free · Always open</span>
        <h3>ML / DS Master Study Guide</h3>
        <p>
          54 topics spanning linear algebra, classical ML, neural networks, deep learning
          architectures and the LLM era — written as the reference I wanted while preparing
          for system design and modelling interviews, and kept as an everyday revision deck.
        </p>
        <div class="chip-row">
          <span class="chip">Machine Learning</span>
          <span class="chip">Deep Learning</span>
          <span class="chip">NLP &amp; LLMs</span>
          <span class="chip">MLOps</span>
          <span class="chip">System Design</span>
        </div>
      </div>
      <a class="btn btn--primary" href="https://yaksh-patel.github.io/ml-guide" target="_blank" rel="noopener">
        <svg aria-hidden="true"><use href="#i-book"/></svg> Open the guide
      </a>
    </div>
  </div>
</section>

<!-- ===== WRITING ===== -->
{% if site.posts.size > 0 %}
<section class="section">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="sec-index">04</span>
      <h2>Writing</h2>
      <span class="sec-line"></span>
      <a class="sec-more" href="{{ '/blog/' | relative_url }}">All posts →</a>
    </div>

    <div class="card-list">
      {% for post in site.posts limit:3 %}
        <div class="reveal">{% include post-card.html post=post %}</div>
      {% endfor %}
    </div>
  </div>
</section>
{% endif %}

<!-- ===== CONTACT ===== -->
<section class="section section--tight">
  <div class="wrap">
    <div class="contact-band reveal">
      <span class="eyebrow">Get in touch</span>
      <h2>Building something that has to work in production?</h2>
      <p>I'm always happy to talk through ML systems, decision modelling, or where AI tooling actually helps.</p>
      <div class="hero-actions">
        {% include social-links.html %}
      </div>
    </div>
  </div>
</section>
