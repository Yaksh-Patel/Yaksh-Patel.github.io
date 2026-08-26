---
layout: default
title: About
permalink: /about/
narrow: true
---

<div class="page-header">
  <span class="eyebrow">About</span>
  <h1>Yaksh Patel</h1>
  <p>{{ site.author.role }} · {{ site.author.location }}</p>
</div>

<div class="post-content">

<p class="prose-lead">
  I build machine learning systems that make consequential decisions — and I care most
  about the part everyone skips: what happens after the model ships.
</p>

<p>
  My work has been in credit, fraud and risk at fintechs and a bank, which is a useful place
  to learn ML engineering because the feedback is unforgiving. A model that leaks future
  information scores beautifully offline and loses money in production. A pipeline that
  silently drifts costs real portfolio performance before anyone notices. So I've spent my
  career on the full path — ingestion, feature engineering, training with validation that
  respects temporal ordering, deployment, and the monitoring that catches problems before a
  business metric does.
</p>

<p>
  That's pushed my interest steadily toward the systems layer: how ML services are
  architected, where state should live, what has to be synchronous, how you validate
  something whose correctness is statistical rather than binary, and how you keep a model
  explainable to the people accountable for its decisions. Increasingly that includes
  building with the current generation of models and treating them as engineering problems
  — architecture, failure modes, evaluation, and where a human still has to hold the wheel.
</p>

<p>
  I write things down here, and I keep an open
  <a href="https://yaksh-patel.github.io/ml-guide" target="_blank" rel="noopener">54-topic ML/DS
  study guide</a> that covers everything from linear algebra to the LLM era.
</p>

<h2>Experience</h2>

<div class="timeline">
  <div class="timeline-item">
    <div class="tl-period">Oct 2024 — Present</div>
    <div class="tl-title">Senior Data Scientist</div>
    <div class="tl-org"><strong>PayZen</strong> · San Francisco (Remote)</div>
    <div class="tl-desc">
      <ul>
        <li>Build and deploy the ML systems behind credit decisioning and collections strategy</li>
        <li>Own models end to end — feature pipelines through production deployment — with measurable gains in operational efficiency and portfolio performance</li>
        <li>Automated portfolio monitoring and reporting pipelines so risk shifts surface early rather than at review time</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="tl-period">Jun 2022 — Oct 2024</div>
    <div class="tl-title">Associate</div>
    <div class="tl-org"><strong>Goldman Sachs</strong> · Bengaluru</div>
    <div class="tl-desc">
      <ul>
        <li>Worked on credit and fraud decision systems for Apple Card, GM Card and Personal Loans</li>
        <li>Built graph-based approaches for fraud-ring detection and improved underwriting strategy</li>
        <li>Contributed to model monitoring, validation, and the integration of alternative data sources</li>
      </ul>
    </div>
  </div>

  <div class="timeline-item">
    <div class="tl-period">May 2021 — Aug 2021</div>
    <div class="tl-title">Data Science Intern</div>
    <div class="tl-org"><strong>Simpl</strong> (One Sigma Technologies) · Bengaluru (Remote)</div>
    <div class="tl-desc">
      <ul>
        <li>Built fraud detection using clustering and graph-based techniques</li>
        <li>Contributed to onboarding risk policy and scoring systems</li>
      </ul>
    </div>
  </div>
</div>

<h2>Education</h2>

<div class="timeline">
  <div class="timeline-item">
    <div class="tl-period">2017 — 2022</div>
    <div class="tl-title">B.Tech. Mechanical Engineering + M.Tech. Financial Engineering</div>
    <div class="tl-org">Indian Institute of Technology Kharagpur</div>
    <div class="tl-desc">Dual degree · CGPA 8.41/10</div>
  </div>
</div>

<h2>Toolkit</h2>

<div class="skill-groups">
  <div class="skill-group">
    <div class="skill-group-name">Modelling</div>
    <div class="chip-row">
      <span class="chip">XGBoost</span>
      <span class="chip">LightGBM</span>
      <span class="chip">Graph methods</span>
      <span class="chip">Feature engineering</span>
      <span class="chip">WoE encoding</span>
      <span class="chip">Statistics &amp; probability</span>
      <span class="chip">Interpretability</span>
    </div>
  </div>

  <div class="skill-group">
    <div class="skill-group-name">ML systems</div>
    <div class="chip-row">
      <span class="chip">Feature pipelines</span>
      <span class="chip">Walk-forward validation</span>
      <span class="chip">MLflow</span>
      <span class="chip">Optuna</span>
      <span class="chip">Batch scoring</span>
      <span class="chip">Drift &amp; PSI monitoring</span>
      <span class="chip">Model validation</span>
    </div>
  </div>

  <div class="skill-group">
    <div class="skill-group-name">Deep learning &amp; AI</div>
    <div class="chip-row">
      <span class="chip">PyTorch</span>
      <span class="chip">TensorFlow</span>
      <span class="chip">NLP</span>
      <span class="chip">LLM applications</span>
      <span class="chip">AI-assisted development</span>
    </div>
  </div>

  <div class="skill-group">
    <div class="skill-group-name">Data &amp; languages</div>
    <div class="chip-row">
      <span class="chip">Python</span>
      <span class="chip">SQL</span>
      <span class="chip">PySpark</span>
      <span class="chip">Large-scale tabular data</span>
      <span class="chip">Matplotlib</span>
      <span class="chip">Seaborn</span>
    </div>
  </div>
</div>

<h2>Contact</h2>

<p>
  Reach me at <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>, or on
  <a href="https://linkedin.com/in/{{ site.author.linkedin }}" target="_blank" rel="noopener">LinkedIn</a>
  and <a href="https://github.com/{{ site.author.github }}" target="_blank" rel="noopener">GitHub</a>.
</p>

</div>
