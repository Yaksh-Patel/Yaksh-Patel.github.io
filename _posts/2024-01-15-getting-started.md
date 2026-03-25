---
layout: post
title: "Getting Started: Your First Post"
date: 2024-01-15
categories: [machine-learning]
tags: [python, scikit-learn, tutorial]
read_time: 5
excerpt: "A template post showing all the features available when writing on this site — headings, code blocks, math, tables, and more."
---

This is a template post. Replace or delete this file and add your own.
File location: `_posts/2024-01-15-getting-started.md`

## Writing Posts

To create a new post, add a file to the `_posts/` folder with the naming format:

```
YYYY-MM-DD-your-post-title.md
```

Every post needs this **front matter** block at the top:

```yaml
---
layout: post
title: "Your Post Title"
date: 2024-01-15
categories: [machine-learning]   # one category recommended
tags: [python, statistics]        # as many tags as you like
read_time: 8                      # estimated minutes
excerpt: "One-sentence summary shown on the blog listing page."
---
```

## Code Blocks

Python code with syntax highlighting:

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

model = GradientBoostingClassifier(
    n_estimators=200,
    max_depth=4,
    learning_rate=0.05
)
model.fit(X_train, y_train)
print(f"AUC-ROC: {roc_auc_score(y_test, model.predict_proba(X_test)[:,1]):.4f}")
```

## Math Equations

Inline math: $\text{Gini} = 2 \cdot \text{AUC} - 1$

Display equations:

$$
\text{LogLoss} = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \log(\hat{p}_i) + (1-y_i)\log(1-\hat{p}_i) \right]
$$

## Tables

| Metric | Logistic Regression | XGBoost | LightGBM |
|--------|--------------------:|--------:|---------:|
| AUC-ROC | 0.782 | 0.831 | 0.835 |
| Gini   | 0.564 | 0.662 | 0.670 |
| KS Stat | 0.43 | 0.51 | 0.52 |

## Blockquotes

> A model is not good because it is complex, but because it captures the right structure in the data.

## Images

Add images to `/assets/images/` and reference like:

```markdown
![Alt text](/assets/images/your-chart.png)
```
