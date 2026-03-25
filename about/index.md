---
layout: default
title: About
permalink: /about/
---

<article class="about-layout">
  <!--
    EDIT THIS FILE: /about/index.md
    Replace all placeholder text with your own content.
    Add your photo to /assets/images/avatar-large.jpg
  -->

  <h1>About Me</h1>

  <!-- Replace with your photo:
  <img src="/assets/images/avatar-large.jpg" alt="Yaksh Patel" class="about-photo" />
  -->

  <h2>Who am I</h2>

  <p>
    My name is <strong>Yaksh Patel</strong>, and I am a Senior Data Scientist specialising in
    credit risk modelling and machine learning for fintech. <!-- Edit this intro paragraph -->
  </p>

  <p>
    <!-- EDIT: Add your background, story, what drives you -->
    My work involves building end-to-end ML models: from exploratory data analysis and feature
    engineering through to model training, validation, monitoring, and deployment in production
    environments. I care deeply about interpretable models and making data-driven decisions
    robust enough for high-stakes financial applications.
  </p>

  <p>
    <!-- EDIT: Add personal philosophy, motivations -->
    I believe in writing about what I learn. This site is a record of technical explorations,
    project write-ups, and ideas I want to think through carefully.
  </p>

  <h2>Experience</h2>

  <div class="timeline">
    <!--
      EDIT: Add/remove/change timeline items below.
      Each item is a <div class="timeline-item">
    -->
    <div class="timeline-item">
      <div class="tl-period">Oct '24 – Present</div>
      <div class="tl-title">Senior Data Scientist</div>
      <div class="tl-org">PayZen · San Francisco (Remote)</div>
      <div class="tl-desc">Built Walkaway, Collections and Credit Risk models.</div>
    </div>

    <div class="timeline-item">
      <div class="tl-period">Jun '22 - Oct '24</div>
      <div class="tl-title">Associate</div>
      <div class="tl-org">Goldman Sachs · Bengaluru</div>
      <div class="tl-desc">Responsible for credit and fraud underwriting models for Apple Card, GM Card and Personal Loans.</div>
    </div>

    <div class="timeline-item">
      <div class="tl-period">May '21 – Aug '21</div>
      <div class="tl-title">Data Science Intern</div>
      <div class="tl-org">Simpl (One Sigma Tech. Pvt. Ltd.) · Bengaluru (Remote)</div>
      <div class="tl-desc">Devised rules for fraud detection using HDBSCAN algorithm and detected fraud rings for various merchants.</div>
    </div>
  </div>

  <h2>Education</h2>

  <div class="timeline">
    <div class="timeline-item">
      <div class="tl-period">2017 – 2022</div>
      <div class="tl-title">Dual Degree: B.Tech. (Mechanical Engineering) + M.Tech. (Financial Engineering)</div>
      <div class="tl-org">Indian Institute of Technology Kharagpur · Kharagpur, West Bengal</div>
      <div class="tl-desc">CGPA: 8.41/10</div>
    </div>
  </div>

  <h2>Technical Skills</h2>

  <!--
    EDIT: Adjust skill names and proficiency levels (0-100 for the width).
    Add or remove .skill-box entries as needed.
  -->
  <div class="skills-grid">
    <div class="skill-box">
      <div class="skill-name">Python</div>
      <div class="skill-bar"><div class="skill-fill" style="width:95%"></div></div>
    </div>
    <div class="skill-box">
      <div class="skill-name">SQL</div>
      <div class="skill-bar"><div class="skill-fill" style="width:90%"></div></div>
    </div>
    <div class="skill-box">
      <div class="skill-name">Machine Learning</div>
      <div class="skill-bar"><div class="skill-fill" style="width:88%"></div></div>
    </div>
    <div class="skill-box">
      <div class="skill-name">Credit Risk Modelling</div>
      <div class="skill-bar"><div class="skill-fill" style="width:85%"></div></div>
    </div>
    <div class="skill-box">
      <div class="skill-name">Feature Engineering</div>
      <div class="skill-bar"><div class="skill-fill" style="width:90%"></div></div>
    </div>
    <div class="skill-box">
      <div class="skill-name">Statistics</div>
      <div class="skill-bar"><div class="skill-fill" style="width:82%"></div></div>
    </div>
    <div class="skill-box">
      <div class="skill-name">XGBoost / LightGBM</div>
      <div class="skill-bar"><div class="skill-fill" style="width:88%"></div></div>
    </div>
    <div class="skill-box">
      <div class="skill-name">MLflow / Experiment Tracking</div>
      <div class="skill-bar"><div class="skill-fill" style="width:75%"></div></div>
    </div>
    <div class="skill-box">
      <div class="skill-name">PySpark / Big Data</div>
      <div class="skill-bar"><div class="skill-fill" style="width:70%"></div></div>
    </div>
    <div class="skill-box">
      <div class="skill-name">Docker / Cloud (AWS/GCP)</div>
      <div class="skill-bar"><div class="skill-fill" style="width:65%"></div></div>
    </div>
  </div>

  <h2>Contact</h2>

  <p>
    If you have questions about my posts or projects, feel free to open an issue on the relevant
    GitHub repository. For private enquiries, reach me at
    <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>.
  </p>
</article>
