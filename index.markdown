---
layout: default
---

<!-- Hero Section -->
<section class="hero">
  <div class="hero-content">
    <div class="hero-symbol">
      <span class="code-bracket">&lt;</span>
      <span class="hero-title">{{ site.name }}</span>
      <span class="code-bracket">/&gt;</span>
    </div>
    <div class="hero-tagline">
      <span class="typing-text">Code • Create • Innovate</span>
    </div>
    <div class="hero-cta">
      <a href="/archive.html" class="cta-primary">Explore Posts</a>
      <a href="/about.html" class="cta-secondary">About</a>
    </div>
  </div>
  <div class="hero-particles">
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
  </div>
</section>

<!-- Recent Posts Section -->
<section class="recent-posts">
  <h2 class="section-title">Recent Posts</h2>
  <div class="posts-grid">
    {% for post in site.posts limit: 3 %}
    <article class="post-card">
      <div class="post-card-content">
        <div class="post-meta">
          <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%B %d, %Y" }}</time>
          {% if post.tags %}
            <div class="post-tags">
              {% for tag in post.tags limit: 2 %}
                <span class="tag">{{ tag }}</span>
              {% endfor %}
            </div>
          {% endif %}
        </div>
        <h3 class="post-title">
          <a href="{{ post.url }}">{{ post.title }}</a>
        </h3>
        <p class="post-excerpt">
          {% if post.excerpt %}
            {{ post.excerpt | strip_html | truncatewords: 25 }}
          {% else %}
            {{ post.content | strip_html | truncatewords: 25 }}
          {% endif %}
        </p>
        <div class="post-footer">
          <span class="read-time">5 min read</span>
          <a href="{{ post.url }}" class="read-more">Read More →</a>
        </div>
      </div>
    </article>
    {% endfor %}
  </div>

  <div class="archive-link">
    <a href="/archive.html" class="view-all-posts">
      <i class="fa fa-archive"></i>
      View All Posts in Archive
    </a>
  </div>
</section>
