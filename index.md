---
layout: default
title: Home
---

<!-- ===== HOME HERO ===== -->
<div class="home-hero">
  <!--
    EDIT: Replace the emoji placeholder below with your actual photo.
    Add your photo to /assets/images/avatar-large.jpg and
    change <div class="hero-photo-placeholder"> to:
    <img src="/assets/images/avatar-large.jpg" alt="Yaksh Patel" class="hero-photo" />
  -->
  <div class="hero-photo-placeholder">🧑‍💻</div>

  <h1>Yaksh Patel</h1>
  <p class="hero-subtitle">Senior Data Scientist · Machine Learning · Credit Risk · Fintech</p>

  <p>
    Passionate about building and deploying machine learning systems across domains. I’ve worked on credit, fraud, and risk modeling in fintech, and am particularly interested in deep learning and real-world ML applications.
  </p>

  <p>
    <!-- EDIT: Replace this paragraph with your own background / story -->
    PayZen · Ex-Goldman Sachs · IIT Kharagpur
  </p>
</div>

<!-- ===== ML/DS STUDY GUIDE CALLOUT ===== -->
<div class="guide-callout">
  <div class="guide-callout-inner">
    <div class="guide-callout-text">
      <div class="guide-callout-label">📖 Open Resource</div>
      <h3 class="guide-callout-title">ML/DS Master Study Guide</h3>
      <p class="guide-callout-desc">
        51 topics from linear algebra to LLMs — with SVG animations, runnable Python code,
        and ideal interview answers. Built for interview prep and everyday revision.
        Covers credit risk, MLOps, transformers, XGBoost, backprop and more.
      </p>
      <div class="guide-callout-tags">
        <span class="tag">Machine Learning</span>
        <span class="tag">Deep Learning</span>
        <span class="tag">NLP</span>
        <span class="tag">Credit Risk</span>
        <span class="tag">MLOps</span>
        <span class="tag">Interview Prep</span>
      </div>
    </div>
    <a href="https://yaksh-patel.github.io/ml-guide" target="_blank" rel="noopener" class="guide-callout-btn">
      Open Guide ↗
    </a>
  </div>
</div>

<!-- ===== RECENT POSTS ===== -->
{% if site.posts.size > 0 %}
<div class="section-header">
  <h2>Recent Posts</h2>
  <span class="section-line"></span>
  <a href="/blog/">See all →</a>
</div>

<div class="card-list">
  {% for post in site.posts limit:4 %}
  <article class="post-card">
    <div class="post-meta">
      <span class="post-date">{{ post.date | date: "%Y-%m-%d" }}</span>
      {% if post.categories.first %}
      <span class="post-category">{{ post.categories.first }}</span>
      {% endif %}
    </div>
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    {% if post.excerpt %}
    <p class="post-excerpt">{{ post.excerpt | strip_html | truncate: 160 }}</p>
    {% endif %}
    {% if post.tags.size > 0 %}
    <div class="post-tags">
      {% for tag in post.tags limit:4 %}
      <span class="tag">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </article>
  {% endfor %}
</div>
{% else %}
<div class="section-header">
  <h2>Recent Posts</h2>
  <span class="section-line"></span>
</div>
<div class="post-card" style="text-align:center; color:var(--text-muted); padding:32px;">
  No posts yet — add Markdown files to <code>_posts/</code> to get started.
</div>
{% endif %}

<!-- ===== RECENT PROJECTS ===== -->
{% if site.collections.projects.docs.size > 0 %}
<div class="section-header">
  <h2>Selected Projects</h2>
  <span class="section-line"></span>
  <a href="/projects/">See all →</a>
</div>

<div class="card-list">
  {% assign sorted_projects = site.projects | sort: "date" | reverse %}
  {% for project in sorted_projects limit:3 %}
  <div class="project-card">
    <div class="project-header">
      <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
      <div class="project-links">
        {% if project.github %}
        <a href="{{ project.github }}" class="project-link" target="_blank">GitHub</a>
        {% endif %}
        {% if project.demo %}
        <a href="{{ project.demo }}" class="project-link" target="_blank">Demo</a>
        {% endif %}
      </div>
    </div>
    {% if project.description %}
    <p class="project-desc">{{ project.description }}</p>
    {% endif %}
    {% if project.tags %}
    <div class="project-tech">
      {% for tag in project.tags %}
      <span class="tag">{{ tag }}</span>
      {% endfor %}
    </div>
    {% endif %}
  </div>
  {% endfor %}
</div>
{% else %}
<div class="section-header">
  <h2>Selected Projects</h2>
  <span class="section-line"></span>
</div>
<div class="project-card" style="text-align:center; color:var(--text-muted); padding:32px;">
  No projects yet — add Markdown files to <code>_projects/</code> to get started.
</div>
{% endif %}
